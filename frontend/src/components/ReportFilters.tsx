import { useState, useEffect, useRef } from 'react'
import { Filter, ChevronDown, Search } from 'lucide-react'
import { cn } from "@/lib/utils"

export interface ReportParam {
  name: string
  label: string
  type: string
  default?: string
  options?: [string, string][]
  hidden?: boolean
  _list?: string[]
}

export function SearchableSelect({ 
  options, 
  value, 
  onChange, 
  placeholder = "اختر..." 
}: { 
  options: [string, string][], 
  value: string, 
  onChange: (val: string) => void,
  placeholder?: string
}) {
  const [isOpen, setIsOpen] = useState(false)
  const [search, setSearch] = useState("")
  const dropdownRef = useRef<HTMLDivElement>(null)
  
  const selectedLabel = options.find(o => o[0] === value)?.[1] || placeholder
  const filteredOptions = options.filter(o => o[1].toLowerCase().includes(search.toLowerCase()) || o[0].includes(search))

  // Handle clicking outside to close
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsOpen(false)
      }
    }
    document.addEventListener("mousedown", handleClickOutside)
    return () => document.removeEventListener("mousedown", handleClickOutside)
  }, [])

  return (
    <div className="relative" ref={dropdownRef}>
      <div 
        className={cn(
          "flex h-11 w-full cursor-pointer items-center justify-between whitespace-nowrap rounded-xl bg-slate-100/50 px-4 py-2 text-sm shadow-inner transition-all hover:bg-slate-100",
          isOpen && "ring-2 ring-primary/20 bg-white"
        )}
        onClick={() => setIsOpen(!isOpen)}
      >
        <span className="truncate text-black font-medium">{selectedLabel}</span>
        <ChevronDown className={cn("w-4 h-4 text-slate-400 transition-transform", isOpen && "rotate-180 text-primary")} />
      </div>
      
      {isOpen && (
        <div className="absolute z-50 mt-2 w-full rounded-2xl border-none bg-white/90 backdrop-blur-xl shadow-[0_12px_40px_rgba(0,0,0,0.12)] overflow-hidden">
          <div className="relative p-2 border-b border-slate-100/50">
            <Search className="absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
            <input
              type="text"
              className="w-full bg-slate-50 rounded-lg pl-3 pr-9 py-2 text-sm outline-none focus:ring-2 focus:ring-primary/20 transition-all"
              placeholder="بحث..."
              value={search}
              onChange={e => setSearch(e.target.value)}
              autoFocus
            />
          </div>
          <div className="max-h-60 overflow-auto p-1">
            {filteredOptions.length > 0 ? (
              filteredOptions.map(opt => {
                const isSelected = value === opt[0]
                return (
                  <div 
                    key={opt[0]} 
                    className={cn(
                      "cursor-pointer px-4 py-2.5 text-sm rounded-lg transition-all duration-200 mb-1 last:mb-0",
                      isSelected 
                        ? "bg-primary/10 font-bold text-primary" 
                        : "hover:bg-slate-50 text-slate-600 hover:text-slate-900"
                    )}
                    onClick={() => {
                      onChange(opt[0])
                      setIsOpen(false)
                      setSearch("")
                    }}
                  >
                    {opt[1]}
                  </div>
                )
              })
            ) : (
              <div className="p-4 text-center text-sm font-medium text-slate-400">لا توجد نتائج</div>
            )}
          </div>
        </div>
      )}
    </div>
  )
}

export function ReportFilters({ 
  params, 
  initialBinds, 
  onApply,
  children
}: { 
  params: ReportParam[]
  initialBinds: Record<string, string>
  onApply: (binds: Record<string, string>) => void 
  children?: React.ReactNode
}) {
  const [binds, setBinds] = useState<Record<string, string>>(initialBinds)
  const [activeQuickDate, setActiveQuickDate] = useState<string | null>(null)

  useEffect(() => {
    setBinds(initialBinds)
  }, [initialBinds])

  if (!params || params.length === 0) return null

  const hasDateFilters = params.some(p => p.type === 'date')

  const setQuickDate = (type: string) => {
    setActiveQuickDate(type)
    const date1 = params.find(p => p.type === 'date' && (p.name.includes('from') || p.name.includes('1')))?.name
    const date2 = params.find(p => p.type === 'date' && (p.name.includes('to') || p.name.includes('2')))?.name

    if (!date1 || !date2) return

    const today = new Date()
    let d1 = new Date()
    let d2 = new Date()

    switch (type) {
      case 'today':
        break
      case 'yesterday':
        d1.setDate(today.getDate() - 1)
        d2.setDate(today.getDate() - 1)
        break
      case 'this_week':
        d1.setDate(today.getDate() - today.getDay())
        d2 = new Date(d1)
        d2.setDate(d1.getDate() + 6)
        break
      case 'last_week':
        d1.setDate(today.getDate() - today.getDay() - 7)
        d2 = new Date(d1)
        d2.setDate(d1.getDate() + 6)
        break
      case 'this_month':
        d1.setDate(1)
        d2 = new Date(today.getFullYear(), today.getMonth() + 1, 0)
        break
      case 'last_month':
        d1 = new Date(today.getFullYear(), today.getMonth() - 1, 1)
        d2 = new Date(today.getFullYear(), today.getMonth(), 0)
        break
      case 'this_year':
        d1 = new Date(today.getFullYear(), 0, 1)
        d2 = new Date(today.getFullYear(), 11, 31)
        break
      case 'last_year':
        d1 = new Date(today.getFullYear() - 1, 0, 1)
        d2 = new Date(today.getFullYear() - 1, 11, 31)
        break
    }

    const formatDate = (d: Date) => {
      const pad = (n: number) => String(n).padStart(2, '0');
      return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
    };

    setBinds(prev => ({
      ...prev,
      [date1]: formatDate(d1),
      [date2]: formatDate(d2)
    }))
  }

  const handleChange = (name: string, value: string) => {
    setBinds(prev => ({ ...prev, [name]: value }))
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    onApply(binds)
  }

  return (
    <div className="flex flex-col gap-4 print:hidden">
      <form onSubmit={handleSubmit} className="soft-card relative z-20 p-6 flex flex-wrap gap-5 items-end">

      {params.filter(p => {
        if (p.hidden) return false
        // Hide rep_code if grp_by is 1
        if (p.name === 'rep_code' && binds['grp_by'] === '1') return false
        return true
      }).map(p => {
        // Linked Dropdowns Logic for period_val
        let options = p.options || []
        if (p.name === 'period_val' && binds['period_type']) {
          const pt = binds['period_type']
          options = options.map(o => {
            if (o[0] === 'all') return o
            const valNum = parseInt(o[0])
            const parts = o[1].split(' / ')
            let txt = o[1]
            if (pt === 'monthly' && valNum >= 1 && valNum <= 12) txt = parts[0]
            else if (pt === 'quarterly' && valNum >= 1 && valNum <= 4) txt = parts[1] || txt
            else if (pt === 'semi_annual' && valNum >= 1 && valNum <= 2) txt = parts[2] || txt
            return [o[0], txt] as [string, string]
          }).filter(o => {
            if (o[0] === 'all') return true
            const valNum = parseInt(o[0])
            if (pt === 'monthly' && valNum >= 1 && valNum <= 12) return true
            if (pt === 'quarterly' && valNum >= 1 && valNum <= 4) return true
            if (pt === 'semi_annual' && valNum >= 1 && valNum <= 2) return true
            return false
          })
        }

        return (
          <div key={p.name} className="flex flex-col gap-2 min-w-[180px] flex-1 max-w-[280px]">
            <label className="text-[13px] font-bold text-black uppercase tracking-wide px-1">{p.label}</label>
            
            {p.type === 'select' ? (
              <SearchableSelect 
                options={options}
                value={binds[p.name] ?? p.default ?? (options[0]?.[0] || '')}
                onChange={val => handleChange(p.name, val)}
              />
            ) : p.type === 'checkbox' ? (
               <div className="flex items-center h-11 px-2">
                 <label className="relative inline-flex items-center cursor-pointer">
                   <input 
                     type="checkbox" 
                     checked={binds[p.name] === '1'}
                     onChange={e => handleChange(p.name, e.target.checked ? '1' : '0')}
                     className="sr-only peer"
                   />
                   <div className="w-11 h-6 bg-slate-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] rtl:after:right-[2px] rtl:after:left-auto after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary shadow-inner"></div>
                 </label>
               </div>
            ) : (
              <>
                <input
                  type={p.type === 'date' ? 'date' : 'text'}
                  className="h-11 w-full rounded-xl border-none bg-slate-100/50 px-4 text-sm shadow-inner outline-none focus:bg-white focus:ring-2 focus:ring-primary/20 transition-all text-slate-700 font-medium"
                  value={binds[p.name] ?? p.default ?? ''}
                  onChange={e => handleChange(p.name, e.target.value)}
                  list={p._list ? `list-${p.name}` : undefined}
                />
                {p._list && p._list.length > 0 && (
                  <datalist id={`list-${p.name}`}>
                    {p._list.map(item => (
                      <option key={item} value={item} />
                    ))}
                  </datalist>
                )}
              </>
            )}
          </div>
        )
      })}
      <button 
        type="submit" 
        className="soft-button gradient-primary h-11 px-8 rounded-xl flex items-center justify-center gap-2 font-bold text-white hover:-translate-y-0.5"
      >
        <Filter className="w-4 h-4" /> عرض التقرير
      </button>
      </form>

      {/* Auxiliary Actions Card (Quick Dates & Buttons) */}
      <div className="bg-white/80 backdrop-blur-xl border border-white/60 shadow-[0_2px_10px_rgba(0,0,0,0.02)] rounded-2xl flex flex-col sm:flex-row items-center justify-between p-3 px-5 gap-4">
        {hasDateFilters ? (
          <div className="flex flex-wrap items-center bg-slate-100/80 p-1.5 rounded-xl shadow-inner border border-slate-200/50 gap-1">
            <button type="button" onClick={() => setQuickDate('today')} className={cn("px-4 py-1.5 text-[13px] font-bold rounded-lg transition-all duration-300", activeQuickDate === 'today' ? "bg-white text-primary shadow-sm ring-1 ring-slate-200/50" : "text-slate-500 hover:text-slate-800 hover:bg-slate-200/50")}>اليوم</button>
            <button type="button" onClick={() => setQuickDate('this_week')} className={cn("px-4 py-1.5 text-[13px] font-bold rounded-lg transition-all duration-300", activeQuickDate === 'this_week' ? "bg-white text-primary shadow-sm ring-1 ring-slate-200/50" : "text-slate-500 hover:text-slate-800 hover:bg-slate-200/50")}>هذا الأسبوع</button>
            <button type="button" onClick={() => setQuickDate('this_month')} className={cn("px-4 py-1.5 text-[13px] font-bold rounded-lg transition-all duration-300", activeQuickDate === 'this_month' ? "bg-white text-primary shadow-sm ring-1 ring-slate-200/50" : "text-slate-500 hover:text-slate-800 hover:bg-slate-200/50")}>هذا الشهر</button>
            <button type="button" onClick={() => setQuickDate('last_month')} className={cn("px-4 py-1.5 text-[13px] font-bold rounded-lg transition-all duration-300", activeQuickDate === 'last_month' ? "bg-white text-primary shadow-sm ring-1 ring-slate-200/50" : "text-slate-500 hover:text-slate-800 hover:bg-slate-200/50")}>الشهر السابق</button>
            <button type="button" onClick={() => setQuickDate('this_year')} className={cn("px-4 py-1.5 text-[13px] font-bold rounded-lg transition-all duration-300", activeQuickDate === 'this_year' ? "bg-white text-primary shadow-sm ring-1 ring-slate-200/50" : "text-slate-500 hover:text-slate-800 hover:bg-slate-200/50")}>هذه السنة</button>
            <button type="button" onClick={() => setQuickDate('last_year')} className={cn("px-4 py-1.5 text-[13px] font-bold rounded-lg transition-all duration-300", activeQuickDate === 'last_year' ? "bg-white text-primary shadow-sm ring-1 ring-slate-200/50" : "text-slate-500 hover:text-slate-800 hover:bg-slate-200/50")}>السنة السابقة</button>
          </div>
        ) : <div />}
        
        {children && (
          <div className="flex flex-col sm:flex-row items-center gap-2.5 w-full sm:w-auto">
            {children}
          </div>
        )}
      </div>
    </div>
  )
}
