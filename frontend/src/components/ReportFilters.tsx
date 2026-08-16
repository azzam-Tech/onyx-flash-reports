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
}

function SearchableSelect({ 
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
        <span className="truncate text-slate-700 font-medium">{selectedLabel}</span>
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
  onApply 
}: { 
  params: ReportParam[]
  initialBinds: Record<string, string>
  onApply: (binds: Record<string, string>) => void 
}) {
  const [binds, setBinds] = useState<Record<string, string>>(initialBinds)

  useEffect(() => {
    setBinds(initialBinds)
  }, [initialBinds])

  if (!params || params.length === 0) return null

  const handleChange = (name: string, value: string) => {
    setBinds(prev => ({ ...prev, [name]: value }))
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    onApply(binds)
  }

  return (
    <form onSubmit={handleSubmit} className="soft-card relative z-20 p-6 flex flex-wrap gap-5 items-end print:hidden">
      {params.filter(p => !p.hidden).map(p => (
        <div key={p.name} className="flex flex-col gap-2 min-w-[180px] flex-1 max-w-[280px]">
          <label className="text-[13px] font-bold text-slate-500 uppercase tracking-wide px-1">{p.label}</label>
          
          {p.type === 'select' ? (
            <SearchableSelect 
              options={p.options || []}
              value={binds[p.name] ?? p.default ?? (p.options?.[0]?.[0] || '')}
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
            <input
              type={p.type === 'date' ? 'date' : 'text'}
              className="h-11 w-full rounded-xl border-none bg-slate-100/50 px-4 text-sm shadow-inner outline-none focus:bg-white focus:ring-2 focus:ring-primary/20 transition-all text-slate-700 font-medium"
              value={binds[p.name] ?? p.default ?? ''}
              onChange={e => handleChange(p.name, e.target.value)}
            />
          )}
        </div>
      ))}
      <button 
        type="submit" 
        className="soft-button gradient-primary h-11 px-8 rounded-xl flex items-center justify-center gap-2 font-bold text-white hover:-translate-y-0.5"
      >
        <Filter className="w-4 h-4" /> عرض التقرير
      </button>
    </form>
  )
}
