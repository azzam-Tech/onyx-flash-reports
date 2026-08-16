import { useState, useEffect } from "react"
import { Settings, Save, Target, EyeOff } from "lucide-react"

export function SettingsManagement() {
  const [reps, setReps] = useState<{code: string, name: string}[]>([])
  const [targets, setTargets] = useState<any>({})
  const [hideProfit, setHideProfit] = useState(false)
  const [isLoading, setIsLoading] = useState(true)
  const [activeTab, setActiveTab] = useState<'targets' | 'other'>('targets')
  const [isSaving, setIsSaving] = useState(false)

  // We fetch hidden configs to pass them back untouched so we don't accidentally overwrite them
  const [hiddenTabs, setHiddenTabs] = useState<string[]>([])
  const [hiddenReports, setHiddenReports] = useState<string[]>([])

  useEffect(() => {
    fetchData()
  }, [])

  const fetchData = async () => {
    try {
      const res = await fetch("/api/settings_manage")
      const data = await res.json()
      if (data.reps) setReps(data.reps)
      if (data.targets) setTargets(data.targets)
      if (data.hide_profit !== undefined) setHideProfit(data.hide_profit)
      if (data.hidden_tabs) setHiddenTabs(data.hidden_tabs)
      if (data.hidden_reports) setHiddenReports(data.hidden_reports)
    } catch (e) {
      console.error(e)
    } finally {
      setIsLoading(false)
    }
  }

  const handleTargetChange = (repCode: string, month: number, value: string) => {
    const numericValue = parseFloat(value) || 0
    setTargets((prev: any) => ({
      ...prev,
      [repCode]: {
        ...(prev[repCode] || {}),
        [month.toString()]: numericValue
      }
    }))
  }

  const handleSave = async () => {
    setIsSaving(true)
    try {
      const res = await fetch("/api/settings_manage", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          hide_profit: hideProfit,
          targets: targets,
          hidden_tabs: hiddenTabs,
          hidden_reports: hiddenReports
        })
      })
      if (res.ok) {
        alert("تم حفظ الإعدادات والمتغيرات بنجاح!")
      } else {
        alert("حدث خطأ أثناء الحفظ. تأكد من أنك تملك صلاحيات المدير.")
      }
    } catch (e) {
      console.error(e)
    } finally {
      setIsSaving(false)
    }
  }

  if (isLoading) {
    return <div className="flex h-full items-center justify-center text-slate-500">جاري التحميل...</div>
  }

  return (
    <div className="min-h-full bg-slate-50 flex flex-col p-8 overflow-y-auto" dir="rtl">
      
      <div className="flex items-center justify-between mb-8">
        <div className="flex items-center gap-4">
          <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center shadow-lg shadow-purple-600/20">
            <Settings className="w-6 h-6 text-white" />
          </div>
          <div>
            <h1 className="text-2xl font-bold text-slate-900 tracking-tight">الإعدادات والمتغيرات العامة</h1>
            <p className="text-sm text-slate-500 mt-1">تحديد المستهدفات المالية وإعدادات عرض النظام.</p>
          </div>
        </div>
        <button 
          onClick={handleSave}
          disabled={isSaving}
          className="flex items-center gap-2 px-8 py-3 rounded-xl font-bold text-white bg-indigo-600 hover:bg-indigo-700 shadow-md shadow-indigo-600/20 transition-all disabled:opacity-50"
        >
          <Save className="w-5 h-5" />
          {isSaving ? 'جاري الحفظ...' : 'حفظ الإعدادات والمتغيرات'}
        </button>
      </div>

      <div className="bg-white rounded-3xl p-2 shadow-sm border border-slate-100 flex flex-col mb-8">
        <div className="flex gap-2 p-2 border-b border-slate-100">
          <button 
            onClick={() => setActiveTab('targets')}
            className={`flex-1 flex items-center justify-center gap-2 py-3 px-6 rounded-2xl font-bold text-sm transition-all ${activeTab === 'targets' ? 'bg-indigo-50 text-indigo-700' : 'text-slate-500 hover:bg-slate-50 hover:text-slate-700'}`}
          >
            <Target className="w-4 h-4" />
            المتغيرات (أهداف المناديب)
          </button>
          <button 
            onClick={() => setActiveTab('other')}
            className={`flex-1 flex items-center justify-center gap-2 py-3 px-6 rounded-2xl font-bold text-sm transition-all ${activeTab === 'other' ? 'bg-indigo-50 text-indigo-700' : 'text-slate-500 hover:bg-slate-50 hover:text-slate-700'}`}
          >
            <EyeOff className="w-4 h-4" />
            إعدادات العرض
          </button>
        </div>

        <div className="p-6">
          {activeTab === 'targets' && (
            <div className="overflow-x-auto rounded-2xl border border-slate-200">
              <table className="w-full text-sm text-right">
                <thead className="bg-slate-50 text-slate-700 font-bold">
                  <tr>
                    <th className="px-6 py-4 whitespace-nowrap border-b border-slate-200 sticky right-0 bg-slate-50 z-10 shadow-[1px_0_0_0_#e2e8f0]">اسم المندوب</th>
                    {[...Array(12)].map((_, i) => (
                      <th key={i} className="px-4 py-4 whitespace-nowrap border-b border-slate-200 text-center">
                        شهر {i + 1}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-200 bg-white">
                  {reps.map((rep) => (
                    <tr key={rep.code} className="hover:bg-slate-50 transition-colors">
                      <td className="px-6 py-4 font-bold text-slate-900 whitespace-nowrap sticky right-0 bg-white shadow-[1px_0_0_0_#e2e8f0]">
                        {rep.name}
                      </td>
                      {[...Array(12)].map((_, i) => {
                        const month = i + 1
                        const val = targets[rep.code]?.[month.toString()] ?? 1000000
                        return (
                          <td key={month} className="px-2 py-2">
                            <input 
                              type="number"
                              value={val}
                              onChange={(e) => handleTargetChange(rep.code, month, e.target.value)}
                              className="w-full min-w-[90px] px-3 py-2 bg-slate-50 border border-slate-200 rounded-lg text-center font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:bg-white transition-all"
                            />
                          </td>
                        )
                      })}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}

          {activeTab === 'other' && (
            <div className="max-w-3xl mx-auto space-y-6">
              <div className="bg-white border-2 border-slate-100 rounded-3xl p-6 flex flex-col gap-6">
                <h3 className="font-bold text-lg text-slate-900">إعدادات العرض العامة</h3>
                
                <label className={`flex items-center gap-4 cursor-pointer p-4 rounded-2xl border-2 transition-all ${hideProfit ? 'border-red-500 bg-red-50/50' : 'border-slate-100 hover:border-slate-200 bg-slate-50'}`}>
                  <input 
                    type="checkbox" 
                    checked={hideProfit}
                    onChange={(e) => setHideProfit(e.target.checked)}
                    className="w-5 h-5 accent-red-500 rounded text-red-500 focus:ring-red-500"
                  />
                  <div>
                    <div className={`font-bold ${hideProfit ? 'text-red-700' : 'text-slate-900'}`}>
                      إخفاء الأرباح بالكامل
                    </div>
                    <div className="text-sm text-slate-500 mt-1">
                      تفعيل هذا الخيار سيؤدي إلى إخفاء مجمل وصافي الربح من جميع التقارير ولوحة القيادة لجميع المستخدمين بدون استثناء.
                    </div>
                  </div>
                </label>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
