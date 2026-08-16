import { ScrollArea } from "./ui/scroll-area"
import { cn } from "@/lib/utils"
import type { Tab } from "../App"
import { LayoutDashboard, FileText, Settings, Activity, ChevronDown, LogOut } from "lucide-react"
import { useState, useEffect } from "react"

export function Sidebar({ user, tabs, activeTab, activeReport, onSelectReport, onLogout }: { 
  user: any,
  tabs: Tab[], 
  activeTab: string, 
  activeReport: string,
  onSelectReport: (tabId: string, reportId: string) => void,
  onLogout: () => void
}) {
  const [expandedTabs, setExpandedTabs] = useState<string[]>([activeTab])

  useEffect(() => {
    if (activeTab && !expandedTabs.includes(activeTab)) {
      setExpandedTabs(prev => [...prev, activeTab])
    }
  }, [activeTab])

  const toggleTab = (tabId: string) => {
    setExpandedTabs(prev => 
      prev.includes(tabId) ? prev.filter(id => id !== tabId) : [...prev, tabId]
    )
  }

  return (
    <div className="w-72 h-full py-6 pr-6 flex flex-col z-10 print:hidden">
      {/* Floating Soft Card Container */}
      <div className="bg-card flex flex-col h-full rounded-3xl shadow-[0_8px_30px_rgba(0,0,0,0.04)] border border-white/60 overflow-hidden">
        
        {/* Logo Area */}
        <div className="p-8 pb-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl gradient-primary flex items-center justify-center shadow-lg shadow-primary/30">
              <Activity className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1 className="text-xl font-extrabold text-foreground tracking-tight">SREEN<span className="text-primary">Pro</span></h1>
              <p className="text-xs text-muted-foreground font-medium">لوحة التحكم والتقارير</p>
            </div>
          </div>
        </div>

        {/* Navigation Area */}
        <ScrollArea className="flex-1 px-4 py-4" dir="rtl">
          <div className="space-y-4">
            {tabs.map((tab) => {
              const isExpanded = expandedTabs.includes(tab.id)
              return (
                <div key={tab.id} className="flex flex-col">
                  <button 
                    onClick={() => toggleTab(tab.id)}
                    className={cn(
                      "flex items-center justify-between w-full px-4 py-3 rounded-xl transition-all duration-200",
                      isExpanded ? "bg-slate-50/80 text-primary" : "text-slate-500 hover:bg-slate-50 hover:text-slate-800"
                    )}
                  >
                    <div className="flex items-center gap-2 text-[12px] font-bold uppercase tracking-wider">
                      <LayoutDashboard className="w-4 h-4" />
                      {tab.title}
                    </div>
                    <ChevronDown className={cn("w-4 h-4 transition-transform duration-300", isExpanded && "rotate-180")} />
                  </button>
                  
                  <div className={cn(
                    "flex flex-col space-y-1 overflow-hidden transition-all duration-300 ease-in-out px-2",
                    isExpanded ? "max-h-[1000px] opacity-100 mt-2" : "max-h-0 opacity-0 mt-0"
                  )}>
                    {tab.reports.map((report) => {
                      const isActive = activeTab === tab.id && activeReport === report.id
                      return (
                        <button
                          key={report.id}
                          onClick={() => onSelectReport(tab.id, report.id)}
                          className={cn(
                            "w-full flex items-center gap-3 text-right pr-11 pl-4 py-2.5 text-sm font-semibold rounded-xl transition-all duration-200",
                            isActive 
                              ? "gradient-primary hover:-translate-y-0.5 shadow-sm shadow-primary/20" 
                              : "text-slate-500 hover:bg-white hover:text-slate-900 hover:shadow-sm"
                          )}
                        >
                          <FileText className={cn("w-4 h-4 shrink-0", isActive ? "text-white" : "text-slate-400")} />
                          <span className="leading-snug">{report.title}</span>
                        </button>
                      )
                    })}
                  </div>
                </div>
              )
            })}
          </div>
        </ScrollArea>

        {/* Footer Area */}
        <div className="p-6 pt-4 mt-auto border-t border-slate-100/50">
          <div className="text-xs font-bold text-slate-400 mb-3 px-2">أدوات</div>
          <div className="space-y-2">
            {user?.role === 'admin' && (
              <>
                <button 
                  onClick={() => onSelectReport('tools', 'settings')}
                  className={cn("flex items-center gap-3 text-sm text-slate-600 font-semibold px-4 py-3 w-full rounded-xl hover:bg-slate-50 hover:text-slate-900 hover:shadow-sm transition-all duration-300",
                    activeTab === 'tools' && activeReport === 'settings' ? "bg-slate-50 text-slate-900 shadow-sm" : ""
                  )}
                >
                  <div className="text-slate-400">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
                  </div>
                  الإعدادات والمتغيرات العامة
                </button>
                <button 
                  onClick={() => onSelectReport('tools', 'users')}
                  className={cn("flex items-center gap-3 text-sm text-slate-600 font-semibold px-4 py-3 w-full rounded-xl hover:bg-slate-50 hover:text-slate-900 hover:shadow-sm transition-all duration-300",
                    activeTab === 'tools' && activeReport === 'users' ? "bg-slate-50 text-slate-900 shadow-sm" : ""
                  )}
                >
                  <div className="text-slate-400">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                  </div>
                  إدارة المستخدمين
                </button>
                <div className="my-2 h-px bg-slate-100" />
              </>
            )}
            <button 
              onClick={onLogout}
              className="flex items-center gap-3 text-sm text-red-600 font-semibold px-4 py-3 w-full rounded-xl hover:bg-red-50 hover:shadow-sm transition-all duration-300"
            >
              <div className="text-red-400">
                <LogOut className="w-5 h-5" />
              </div>
              تسجيل الخروج
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}
