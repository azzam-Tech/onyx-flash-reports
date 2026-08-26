import { useState, useEffect, useMemo } from 'react'
import { Input } from './ui/input'
import { Button } from './ui/button'
import {
  BarChart, Bar, LineChart, Line, PieChart, Pie, Cell,
  XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer
} from 'recharts'
import { 
  TrendingUp, TrendingDown, DollarSign, ShoppingCart, 
  Wallet, Package, Receipt, BarChart3, Activity 
} from 'lucide-react'
import { cn } from '@/lib/utils'
import { SearchableSelect } from './ReportFilters'

function formatNumber(num: number) {
  if (num === null || num === undefined) return '0'
  return new Intl.NumberFormat('en-US', { maximumFractionDigits: 0 }).format(num)
}

function KPICard({ title, value, icon: Icon, color, trend }: { title: string, value: number, icon: any, color: "blue" | "green" | "orange" | "purple" | "red" | "teal", trend?: "up" | "down" }) {
  const colorMap = {
    blue: "text-blue-600 bg-blue-100/50 ring-blue-500/20",
    green: "text-emerald-600 bg-emerald-100/50 ring-emerald-500/20",
    orange: "text-orange-600 bg-orange-100/50 ring-orange-500/20",
    purple: "text-purple-600 bg-purple-100/50 ring-purple-500/20",
    red: "text-rose-600 bg-rose-100/50 ring-rose-500/20",
    teal: "text-teal-600 bg-teal-100/50 ring-teal-500/20"
  }
  
  return (
    <div className="soft-card p-6 flex flex-col justify-between relative overflow-hidden group">
      {/* Decorative background glow */}
      <div className={cn(
        "absolute -right-6 -top-6 w-24 h-24 rounded-full blur-2xl opacity-20 group-hover:opacity-40 transition-opacity duration-500",
        color === 'blue' && "bg-blue-500",
        color === 'green' && "bg-emerald-500",
        color === 'orange' && "bg-orange-500",
        color === 'purple' && "bg-purple-500",
        color === 'red' && "bg-rose-500",
        color === 'teal' && "bg-teal-500"
      )} />
      
      <div className="flex justify-between items-start mb-4 relative z-10">
        <div className={cn("p-3 rounded-2xl ring-1", colorMap[color])}>
          <Icon className="w-5 h-5" />
        </div>
        {trend && (
          <div className={cn(
            "flex items-center gap-1 text-xs font-bold px-2 py-1 rounded-full",
            trend === 'up' ? "text-emerald-600 bg-emerald-50" : "text-rose-600 bg-rose-50"
          )}>
            {trend === 'up' ? <TrendingUp className="w-3 h-3" /> : <TrendingDown className="w-3 h-3" />}
          </div>
        )}
      </div>
      
      <div className="relative z-10">
        <div className="text-slate-500 text-sm font-semibold mb-1">{title}</div>
        <div className="text-2xl font-extrabold text-slate-800 tracking-tight">
          {formatNumber(value)}
        </div>
      </div>
    </div>
  )
}

export function Dashboard() {
  const [data, setData] = useState<any>(null)
  const [hideProfit, setHideProfit] = useState(false)
  const [yearVal, setYearVal] = useState(new Date().getFullYear().toString())
  const [periodType, setPeriodType] = useState('monthly')
  const [periodVal, setPeriodVal] = useState('all')

  const periodOptions = useMemo(() => {
    if (periodType === 'monthly') return [['all','كل الأشهر'],['01','يناير'],['02','فبراير'],['03','مارس'],['04','أبريل'],['05','مايو'],['06','يونيو'],['07','يوليو'],['08','أغسطس'],['09','سبتمبر'],['10','أكتوبر'],['11','نوفمبر'],['12','ديسمبر']];
    if (periodType === 'quarterly') return [['all','كل الأرباع'],['1','الربع الأول'],['2','الربع الثاني'],['3','الربع الثالث'],['4','الربع الرابع']];
    if (periodType === 'semi_annual') return [['all','كل الفترات'],['1','النصف الأول'],['2','النصف الثاني']];
    return [['all','كامل السنة']];
  }, [periodType])
  const [isLoading, setIsLoading] = useState(true)

  const fetchData = (forceRefresh = false) => {
    setIsLoading(true)
    fetch(`/api/dashboard?year_val=${yearVal}&period_type=${periodType}&period_val=${periodVal}&force_refresh=${forceRefresh ? '1' : '0'}`)
      .then(res => res.json())
      .then(resData => {
        setData(resData.data)
        setHideProfit(resData.hide_profit)
        setIsLoading(false)
      })
      .catch(err => {
        console.error(err)
        setIsLoading(false)
      })
  }

  useEffect(() => {
    fetchData()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  // Format Recharts data
  const monthlyData = useMemo(() => {
    if (!data) return []
    return data.months.map((m: string, i: number) => ({
      name: m,
      sales: data.msales[i] || 0,
      collect: data.mcollect[i] || 0,
      purch: data.mpurch[i] || 0,
    }))
  }, [data])

  const repData = useMemo(() => {
    if (!data) return []
    return data.rep_labels.slice(0, 5).map((l: string, i: number) => ({
      name: l,
      value: data.rep_vals[i] || 0
    }))
  }, [data])

  const itmData = useMemo(() => {
    if (!data) return []
    return data.itm_labels.slice(0, 5).map((l: string, i: number) => ({
      name: l,
      value: data.itm_vals[i] || 0
    }))
  }, [data])

  const PIE_COLORS_1 = ['#4f46e5', '#38bdf8', '#10b981', '#f59e0b', '#8b5cf6']
  const PIE_COLORS_2 = ['#f43f5e', '#d946ef', '#0ea5e9', '#14b8a6', '#eab308']

  if (isLoading && !data) {
    return (
      <div className="flex-1 flex items-center justify-center bg-transparent">
        <div className="flex flex-col items-center gap-4">
          <div className="w-10 h-10 rounded-full border-4 border-primary/20 border-t-primary animate-spin shadow-lg"></div>
          <div className="text-sm font-bold text-slate-500 animate-pulse">جاري بناء لوحة القيادة...</div>
        </div>
      </div>
    )
  }

  return (
    <div className="flex-1 flex flex-col h-full bg-transparent overflow-auto p-4 md:p-6 gap-6">
      {/* Top Header Card */}
      <div className="soft-card flex flex-col sm:flex-row items-start sm:items-center justify-between p-6 gap-4 print:hidden relative overflow-hidden shrink-0">
        <div className="absolute -left-10 -top-10 w-40 h-40 bg-primary/5 rounded-full blur-3xl"></div>
        
        <div className="relative z-10">
          <h2 className="text-2xl font-extrabold text-slate-800 flex items-center gap-2">
            <Activity className="w-6 h-6 text-primary" />
            لوحة القيادة
          </h2>
          <p className="text-sm text-slate-500 mt-1 font-medium">نظرة شاملة وتحليلية لأداء المؤسسة</p>
        </div>
        
        <div className="flex flex-col sm:flex-row items-center gap-3 relative z-10 w-full sm:w-auto">
          <div className="flex items-center gap-2 bg-slate-100/80 p-1.5 rounded-xl border border-slate-200/60 shadow-inner w-full sm:w-auto">
            <div className="w-[100px]">
              <SearchableSelect 
                options={[['2023','2023'],['2024','2024'],['2025','2025'],['2026','2026'],['2027','2027'],['2028','2028']]} 
                value={yearVal} 
                onChange={setYearVal} 
              />
            </div>
            <div className="w-[130px]">
              <SearchableSelect 
                options={[['monthly','شهري'],['quarterly','ربعي'],['semi_annual','نصفي'],['annual','سنوي']]} 
                value={periodType} 
                onChange={(val) => { setPeriodType(val); setPeriodVal('all'); }} 
              />
            </div>
            <div className="w-[130px]">
              <SearchableSelect 
                options={periodOptions as [string, string][]} 
                value={periodVal} 
                onChange={setPeriodVal} 
              />
            </div>
          </div>
          <button 
            onClick={() => fetchData(true)} 
            className="w-full sm:w-auto gradient-primary text-white px-5 py-2.5 rounded-xl font-bold text-sm shadow-md shadow-primary/20 hover:shadow-lg hover:-translate-y-0.5 transition-all duration-300"
          >
            تحديث البيانات
          </button>
        </div>
      </div>

      {data && (
        <div className="space-y-6 pb-6">
          {/* KPI Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 lg:gap-6">
            <KPICard title="إجمالي المبيعات" value={data.sales} icon={BarChart3} color="blue" trend="up" />
            <KPICard title="إجمالي التحصيل" value={data.collect} icon={Wallet} color="green" trend="up" />
            <KPICard title="إجمالي المشتريات" value={data.purch} icon={ShoppingCart} color="orange" trend="down" />
            {!hideProfit && <KPICard title="مجمل الربح" value={data.gross} icon={DollarSign} color="purple" trend="up" />}
            
            {!hideProfit && <KPICard title="صافي الربح" value={data.netprofit} icon={TrendingUp} color="green" trend="up" />}
            <KPICard title="الذمم المدينة" value={data.recv} icon={Receipt} color="red" trend="down" />
            <KPICard title="قيمة المخزون" value={data.invval} icon={Package} color="teal" />
            <KPICard title="صافي الضريبة" value={data.vat} icon={Activity} color="orange" />
          </div>

          {/* Charts Grid */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div className="soft-card p-6">
              <h3 className="text-base font-extrabold text-slate-700 mb-6 flex items-center gap-2">
                <div className="w-2 h-2 rounded-full bg-blue-500"></div>
                المبيعات والتحصيل شهرياً
              </h3>
              <div className="h-72" dir="ltr">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={monthlyData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                    <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f1f5f9" />
                    <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{fill: '#94a3b8', fontSize: 12}} dy={10} />
                    <YAxis axisLine={false} tickLine={false} tick={{fill: '#94a3b8', fontSize: 12}} tickFormatter={(value) => value.toLocaleString()} />
                    <Tooltip 
                      formatter={(value: number) => formatNumber(value)} 
                      cursor={{fill: '#f8fafc'}}
                      contentStyle={{borderRadius: '12px', border: 'none', boxShadow: '0 4px 20px rgba(0,0,0,0.08)', fontWeight: 'bold'}}
                    />
                    <Legend iconType="circle" wrapperStyle={{paddingTop: '20px', fontSize: '12px', fontWeight: 'bold'}} />
                    <Bar dataKey="sales" name="مبيعات" fill="#4f46e5" radius={[6, 6, 0, 0]} maxBarSize={40} />
                    <Bar dataKey="collect" name="تحصيل" fill="#10b981" radius={[6, 6, 0, 0]} maxBarSize={40} />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>

            <div className="soft-card p-6">
              <h3 className="text-base font-extrabold text-slate-700 mb-6 flex items-center gap-2">
                <div className="w-2 h-2 rounded-full bg-orange-500"></div>
                المشتريات شهرياً
              </h3>
              <div className="h-72" dir="ltr">
                <ResponsiveContainer width="100%" height="100%">
                  <LineChart data={monthlyData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                    <defs>
                      <linearGradient id="colorPurch" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#f59e0b" stopOpacity={0.3}/>
                        <stop offset="95%" stopColor="#f59e0b" stopOpacity={0}/>
                      </linearGradient>
                    </defs>
                    <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f1f5f9" />
                    <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{fill: '#94a3b8', fontSize: 12}} dy={10} />
                    <YAxis axisLine={false} tickLine={false} tick={{fill: '#94a3b8', fontSize: 12}} tickFormatter={(value) => value.toLocaleString()} />
                    <Tooltip 
                      formatter={(value: number) => formatNumber(value)}
                      contentStyle={{borderRadius: '12px', border: 'none', boxShadow: '0 4px 20px rgba(0,0,0,0.08)', fontWeight: 'bold'}}
                    />
                    <Legend iconType="circle" wrapperStyle={{paddingTop: '20px', fontSize: '12px', fontWeight: 'bold'}} />
                    <Line type="monotone" dataKey="purch" name="مشتريات" stroke="#f59e0b" strokeWidth={4} dot={{r: 5, strokeWidth: 2, fill: '#fff'}} activeDot={{r: 8, strokeWidth: 0, fill: '#f59e0b'}} />
                  </LineChart>
                </ResponsiveContainer>
              </div>
            </div>

            <div className="soft-card p-6">
              <h3 className="text-base font-extrabold text-slate-700 mb-6 flex items-center gap-2">
                <div className="w-2 h-2 rounded-full bg-purple-500"></div>
                أفضل 5 مناديب (مبيعات)
              </h3>
              <div className="h-72" dir="ltr">
                <ResponsiveContainer width="100%" height="100%">
                  <PieChart>
                    <Pie data={repData} dataKey="value" nameKey="name" cx="50%" cy="50%" innerRadius={70} outerRadius={90} paddingAngle={3} stroke="none">
                      {repData.map((_, index) => (
                        <Cell key={`cell-${index}`} fill={PIE_COLORS_1[index % PIE_COLORS_1.length]} />
                      ))}
                    </Pie>
                    <Tooltip 
                      formatter={(value: number) => formatNumber(value)}
                      contentStyle={{borderRadius: '12px', border: 'none', boxShadow: '0 4px 20px rgba(0,0,0,0.08)', fontWeight: 'bold'}}
                    />
                    <Legend layout="vertical" verticalAlign="middle" align="right" wrapperStyle={{fontSize: '14px', fontWeight: 'bold', lineHeight: '28px'}} />
                  </PieChart>
                </ResponsiveContainer>
              </div>
            </div>

            <div className="soft-card p-6">
              <h3 className="text-base font-extrabold text-slate-700 mb-6 flex items-center gap-2">
                <div className="w-2 h-2 rounded-full bg-rose-500"></div>
                أفضل 5 أصناف (مبيعات)
              </h3>
              <div className="h-72" dir="ltr">
                <ResponsiveContainer width="100%" height="100%">
                  <PieChart>
                    <Pie data={itmData} dataKey="value" nameKey="name" cx="50%" cy="50%" innerRadius={70} outerRadius={90} paddingAngle={3} stroke="none">
                      {itmData.map((_, index) => (
                        <Cell key={`cell-${index}`} fill={PIE_COLORS_2[index % PIE_COLORS_2.length]} />
                      ))}
                    </Pie>
                    <Tooltip 
                      formatter={(value: number) => formatNumber(value)}
                      contentStyle={{borderRadius: '12px', border: 'none', boxShadow: '0 4px 20px rgba(0,0,0,0.08)', fontWeight: 'bold'}}
                    />
                    <Legend layout="vertical" verticalAlign="middle" align="right" wrapperStyle={{fontSize: '14px', fontWeight: 'bold', lineHeight: '28px'}} />
                  </PieChart>
                </ResponsiveContainer>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
