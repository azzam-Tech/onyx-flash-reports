import { ScrollArea } from "./ui/scroll-area"
import { cn } from "@/lib/utils"
import type { Tab } from "../App"
import { 
  LayoutDashboard, 
  FileText, 
  Settings, 
  Activity, 
  ChevronDown, 
  LogOut, 
  ChevronRight, 
  Menu,
  PieChart,
  LineChart,
  Calculator,
  TrendingUp,
  Package,
  FolderOpen,
  Users,
  ShoppingCart,
  Truck,
  ShoppingBag,
  Landmark,
  Briefcase
} from "lucide-react"
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
  const [isCollapsed, setIsCollapsed] = useState(false)

  useEffect(() => {
    if (activeTab && !expandedTabs.includes(activeTab)) {
      setExpandedTabs(prev => [...prev, activeTab])
    }
  }, [activeTab])

  const getTabIcon = (tabId: string) => {
    switch (tabId) {
      case 'summary': return <PieChart className="w-5 h-5 shrink-0" />;
      case 'sales': return <ShoppingCart className="w-5 h-5 shrink-0" />;
      case 'ar': return <Users className="w-5 h-5 shrink-0" />;
      case 'dts': return <Truck className="w-5 h-5 shrink-0" />;
      case 'pur': return <ShoppingBag className="w-5 h-5 shrink-0" />;
      case 'fin': return <Landmark className="w-5 h-5 shrink-0" />;
      case 'tax': return <Calculator className="w-5 h-5 shrink-0" />;
      case 'prof': return <TrendingUp className="w-5 h-5 shrink-0" />;
      case 'stock': return <Package className="w-5 h-5 shrink-0" />;
      case 'general': return <FolderOpen className="w-5 h-5 shrink-0" />;
      case 'hr': return <Briefcase className="w-5 h-5 shrink-0" />;
      case 'debt_movement_summary': return <LineChart className="w-5 h-5 shrink-0" />;
      default: return <LayoutDashboard className="w-5 h-5 shrink-0" />;
    }
  }

  const toggleTab = (tabId: string) => {
    setExpandedTabs(prev => 
      prev.includes(tabId) ? prev.filter(id => id !== tabId) : [...prev, tabId]
    )
  }

  return (
    <div className={cn(
      "h-full py-6 flex flex-col z-20 print:hidden transition-all duration-300",
      isCollapsed ? "w-[100px] pr-4" : "w-72 pr-6"
    )}>
      {/* Floating Soft Card Container */}
      <div className="bg-card flex flex-col h-full rounded-3xl shadow-[0_8px_30px_rgba(0,0,0,0.04)] border border-white/60 overflow-hidden transition-all duration-300">
        
        {/* Logo Area */}
        <div className={cn("p-6 pb-4 flex items-center transition-all", isCollapsed ? "justify-center flex-col gap-4" : "justify-between")}>
          <div className={cn("flex items-center gap-3", isCollapsed && "flex-col hidden")}>
            {!isCollapsed && (
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl gradient-primary flex shrink-0 items-center justify-center shadow-lg shadow-primary/30">
                  <Activity className="w-6 h-6 text-white" />
                </div>
                <div>
                  <h1 className="text-xl font-extrabold text-foreground tracking-tight">SREEN<span className="text-primary">Pro</span></h1>
                  <p className="text-[10px] text-muted-foreground font-medium whitespace-nowrap">لوحة التحكم والتقارير</p>
                </div>
              </div>
            )}
          </div>
          
          <button 
            onClick={() => setIsCollapsed(!isCollapsed)}
            className={cn("p-2 rounded-xl text-slate-400 hover:text-primary hover:bg-slate-50 transition-colors", isCollapsed && "w-10 h-10 flex items-center justify-center gradient-primary text-white shadow-lg shadow-primary/30")}
          >
            {isCollapsed ? <Activity className="w-6 h-6" /> : <Menu className="w-5 h-5" />}
          </button>
        </div>

        {/* Navigation Area */}
        <ScrollArea className="flex-1 px-4 py-4" dir="rtl">
          <div className="space-y-4">
            {tabs.map((tab) => {
              const isExpanded = expandedTabs.includes(tab.id) && !isCollapsed
              return (
                <div key={tab.id} className="flex flex-col">
                  <button 
                    onClick={() => {
                      if (isCollapsed) setIsCollapsed(false)
                      toggleTab(tab.id)
                    }}
                    className={cn(
                      "flex items-center w-full rounded-xl transition-all duration-200",
                      isCollapsed ? "justify-center p-3" : "justify-between px-4 py-3",
                      isExpanded ? "bg-slate-50/80 text-primary" : "text-slate-900 hover:bg-slate-50 hover:text-black font-bold"
                    )}
                    title={isCollapsed ? tab.title : undefined}
                  >
                    <div className={cn("flex items-center", isCollapsed ? "justify-center" : "gap-2 text-[12px] font-bold uppercase tracking-wider")}>
                      {getTabIcon(tab.id)}
                      {!isCollapsed && <span>{tab.title}</span>}
                    </div>
                    {!isCollapsed && <ChevronDown className={cn("w-4 h-4 transition-transform duration-300", isExpanded && "rotate-180")} />}
                  </button>
                  
                  <div className={cn(
                    "flex flex-col space-y-1 overflow-hidden transition-all duration-300 ease-in-out",
                    isCollapsed ? "px-0" : "px-2",
                    isExpanded ? "max-h-[1000px] opacity-100 mt-2" : "max-h-0 opacity-0 mt-0"
                  )}>
                    {tab.reports.map((report) => {
                      const isActive = activeTab === tab.id && activeReport === report.id
                      return (
                        <button
                          key={report.id}
                          onClick={() => {
                            if (isCollapsed) setIsCollapsed(false)
                            onSelectReport(tab.id, report.id)
                          }}
                          className={cn(
                            "w-full flex items-center text-right font-semibold rounded-xl transition-all duration-200",
                            isCollapsed ? "justify-center p-3" : "gap-3 pr-11 pl-4 py-2.5 text-sm",
                            isActive 
                              ? "gradient-primary hover:-translate-y-0.5 shadow-sm shadow-primary/20" 
                              : "text-slate-900 hover:bg-slate-100 hover:text-black hover:shadow-sm"
                          )}
                          title={isCollapsed ? report.title : undefined}
                        >
                          <FileText className={cn("w-4 h-4 shrink-0", isActive ? "text-white" : "text-slate-500")} />
                          {!isCollapsed && <span className="leading-snug">{report.title}</span>}
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
        <div className="p-4 mt-auto border-t border-slate-100/50">
          {!isCollapsed && <div className="text-xs font-bold text-slate-400 mb-3 px-2">أدوات</div>}
          <div className="space-y-2 flex flex-col items-center">
            {user?.role === 'admin' && (
              <>
                <button 
                  onClick={() => {
                    if (isCollapsed) setIsCollapsed(false)
                    onSelectReport('tools', 'settings')
                  }}
                  className={cn("flex items-center text-sm text-slate-900 font-bold w-full rounded-xl hover:bg-slate-50 hover:text-black hover:shadow-sm transition-all duration-300",
                    isCollapsed ? "justify-center p-3" : "gap-3 px-4 py-3",
                    activeTab === 'tools' && activeReport === 'settings' ? "bg-slate-50 text-black shadow-sm" : ""
                  )}
                  title={isCollapsed ? "الإعدادات والمتغيرات العامة" : undefined}
                >
                  <div className="text-slate-400 shrink-0">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
                  </div>
                  {!isCollapsed && <span>الإعدادات والمتغيرات العامة</span>}
                </button>
                <button 
                  onClick={() => {
                    if (isCollapsed) setIsCollapsed(false)
                    onSelectReport('tools', 'users')
                  }}
                  className={cn("flex items-center text-sm text-slate-900 font-bold w-full rounded-xl hover:bg-slate-50 hover:text-black hover:shadow-sm transition-all duration-300",
                    isCollapsed ? "justify-center p-3" : "gap-3 px-4 py-3",
                    activeTab === 'tools' && activeReport === 'users' ? "bg-slate-50 text-black shadow-sm" : ""
                  )}
                  title={isCollapsed ? "إدارة المستخدمين" : undefined}
                >
                  <div className="text-slate-400 shrink-0">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                  </div>
                  {!isCollapsed && <span>إدارة المستخدمين</span>}
                </button>
                <div className="my-2 w-full h-px bg-slate-100" />
              </>
            )}
            <button 
              onClick={onLogout}
              className={cn("flex items-center text-sm text-red-600 font-semibold w-full rounded-xl hover:bg-red-50 hover:shadow-sm transition-all duration-300",
                isCollapsed ? "justify-center p-3" : "gap-3 px-4 py-3"
              )}
              title={isCollapsed ? "تسجيل الخروج" : undefined}
            >
              <div className="text-red-400 shrink-0">
                <LogOut className="w-5 h-5" />
              </div>
              {!isCollapsed && <span>تسجيل الخروج</span>}
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}
