import re

with open(r'frontend\src\components\Dashboard.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Import SearchableSelect
if "SearchableSelect" not in content:
    content = content.replace("import { cn } from '@/lib/utils'", "import { cn } from '@/lib/utils'\nimport { SearchableSelect } from './ReportFilters'")

# 2. Replace states
state_old = """  const [dateFrom, setDateFrom] = useState(new Date().getFullYear() + '-01-01')
  const [dateTo, setDateTo] = useState(new Date().getFullYear() + '-12-31')"""
state_new = """  const [yearVal, setYearVal] = useState(new Date().getFullYear().toString())
  const [periodType, setPeriodType] = useState('monthly')
  const [periodVal, setPeriodVal] = useState('all')

  const periodOptions = useMemo(() => {
    if (periodType === 'monthly') return [['all','كل الأشهر'],['01','يناير'],['02','فبراير'],['03','مارس'],['04','أبريل'],['05','مايو'],['06','يونيو'],['07','يوليو'],['08','أغسطس'],['09','سبتمبر'],['10','أكتوبر'],['11','نوفمبر'],['12','ديسمبر']];
    if (periodType === 'quarterly') return [['all','كل الأرباع'],['1','الربع الأول'],['2','الربع الثاني'],['3','الربع الثالث'],['4','الربع الرابع']];
    if (periodType === 'semi_annual') return [['all','كل الفترات'],['1','النصف الأول'],['2','النصف الثاني']];
    return [['all','كامل السنة']];
  }, [periodType])"""
content = content.replace(state_old, state_new)

# 3. Replace fetch
fetch_old = "fetch(`/api/dashboard?date_from=${dateFrom}&date_to=${dateTo}&force_refresh=${forceRefresh ? '1' : '0'}`)"
fetch_new = "fetch(`/api/dashboard?year_val=${yearVal}&period_type=${periodType}&period_val=${periodVal}&force_refresh=${forceRefresh ? '1' : '0'}`)"
content = content.replace(fetch_old, fetch_new)

# 4. Replace inputs
inputs_old = """          <div className="flex items-center gap-2 bg-slate-100/80 p-1.5 rounded-xl border border-slate-200/60 shadow-inner w-full sm:w-auto">
            <span className="text-xs font-bold text-slate-500 px-2">من</span>
            <Input 
              type="date" 
              className="h-8 w-full sm:w-auto border-none bg-white rounded-lg shadow-sm focus-visible:ring-1 focus-visible:ring-primary/30 text-xs font-semibold" 
              value={dateFrom} 
              onChange={e => setDateFrom(e.target.value)} 
            />
            <span className="text-xs font-bold text-slate-500 px-2">إلى</span>
            <Input 
              type="date" 
              className="h-8 w-full sm:w-auto border-none bg-white rounded-lg shadow-sm focus-visible:ring-1 focus-visible:ring-primary/30 text-xs font-semibold" 
              value={dateTo} 
              onChange={e => setDateTo(e.target.value)} 
            />
          </div>"""
inputs_new = """          <div className="flex items-center gap-2 bg-slate-100/80 p-1.5 rounded-xl border border-slate-200/60 shadow-inner w-full sm:w-auto">
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
          </div>"""
content = content.replace(inputs_old, inputs_new)

with open(r'frontend\src\components\Dashboard.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("Dashboard.tsx patched successfully!")
