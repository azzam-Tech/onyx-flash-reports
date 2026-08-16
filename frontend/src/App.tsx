import { useState, useEffect } from "react"
import { Sidebar } from "./components/Sidebar"
import { MainContent } from "./components/MainContent"
import { Dashboard } from "./components/Dashboard"
import { UsersManagement } from "./components/UsersManagement"
import { SettingsManagement } from "./components/SettingsManagement"
import { Login } from "./components/Login"

export interface Tab {
  id: string
  title: string
  reports: { id: string; title: string }[]
}

export default function App() {
  const [tabs, setTabs] = useState<Tab[]>([])
  const [activeTab, setActiveTab] = useState<string>("")
  const [activeReport, setActiveReport] = useState<string>("")
  const [isLoading, setIsLoading] = useState(true)

  // Authentication State
  const [isAuthenticated, setIsAuthenticated] = useState(false)
  const [user, setUser] = useState<any>(null)

  // Listen to browser back/forward buttons (hash changes)
  useEffect(() => {
    const handleHashChange = () => {
      const hash = window.location.hash.replace(/^#\/?/, '')
      if (hash) {
        const [tab, report] = hash.split('/')
        if (tab && report) {
          setActiveTab(tab)
          setActiveReport(report)
        }
      }
    }
    window.addEventListener('hashchange', handleHashChange)
    return () => window.removeEventListener('hashchange', handleHashChange)
  }, [])

  useEffect(() => {
    // First, check session
    fetch("/api/session")
      .then(res => res.json())
      .then(data => {
        if (data.authenticated) {
          setIsAuthenticated(true)
          setUser(data.user)
          loadTabs(data.user)
        } else {
          setIsLoading(false)
        }
      })
      .catch(err => {
        console.error(err)
        setIsLoading(false)
      })
  }, [])

  const loadTabs = (currentUser: any) => {
    fetch("/api/tabs")
      .then((res) => res.json())
      .then((data) => {
        if (data.tabs) {
          const finalTabs = [...data.tabs]
          const canViewDashboard = currentUser?.role === 'admin' || currentUser?.allowed_tabs?.includes('*') || currentUser?.allowed_tabs?.includes('dashboard') || currentUser?.allowed_reports?.includes('*')
          
          if (canViewDashboard) {
            const dashboardTab: Tab = {
              id: 'dashboard',
              title: 'الرئيسية',
              reports: [{ id: 'main', title: 'لوحة القيادة' }]
            }
            finalTabs.unshift(dashboardTab)
          }
          
          setTabs(finalTabs)
          if (finalTabs.length > 0) {
            const hash = window.location.hash.replace(/^#\/?/, '')
            if (hash) {
              const [tab, report] = hash.split('/')
              if (tab && report) {
                setActiveTab(tab)
                setActiveReport(report)
                setIsLoading(false)
                return
              }
            }
            
            setActiveTab(finalTabs[0].id)
            if (finalTabs[0].reports && finalTabs[0].reports.length > 0) {
              setActiveReport(finalTabs[0].reports[0].id)
            }
          }
        }
        setIsLoading(false)
      })
      .catch((err) => {
        console.error(err)
        setIsLoading(false)
      })
  }

  const handleLoginSuccess = (userData: any) => {
    setIsAuthenticated(true)
    setUser(userData)
    setIsLoading(true)
    loadTabs(userData)
  }

  const handleLogout = async () => {
    try {
      await fetch("/api/logout", { method: "POST" })
    } catch (e) {
      console.error(e)
    }
    setIsAuthenticated(false)
    setUser(null)
    setTabs([])
    setActiveTab("")
    setActiveReport("")
  }

  if (isLoading) {
    return <div className="flex h-screen items-center justify-center bg-slate-50 text-slate-500 font-bold">جاري التحميل...</div>
  }

  if (!isAuthenticated) {
    return <Login onLoginSuccess={handleLoginSuccess} />
  }

  return (
    <div className="flex h-screen w-full bg-background overflow-hidden print:h-auto print:overflow-visible print:block print:bg-white" dir="rtl">
      <Sidebar 
        user={user}
        tabs={tabs} 
        activeTab={activeTab} 
        activeReport={activeReport}
        onSelectReport={(t, r) => {
          window.location.hash = `/${t}/${r}`
          setActiveTab(t)
          setActiveReport(r)
        }}
        onLogout={handleLogout}
      />
      <div className="flex flex-1 flex-col overflow-hidden print:overflow-visible print:block">
        {activeTab === 'dashboard' ? (
          <Dashboard />
        ) : activeTab === 'tools' && activeReport === 'users' ? (
          <UsersManagement />
        ) : activeTab === 'tools' && activeReport === 'settings' ? (
          <SettingsManagement />
        ) : activeTab === 'tools' ? (
          <iframe 
            src={`http://localhost:8000/${activeReport}`} 
            className="w-full h-full border-none bg-slate-50"
            title="External Tool"
          />
        ) : (
          <MainContent 
            key={`${activeTab}-${activeReport}`}
            tabId={activeTab} 
            reportId={activeReport} 
            reportTitle={
              tabs.find(t => t.id === activeTab)?.reports.find(r => r.id === activeReport)?.title || "تقرير"
            }
          />
        )}
      </div>
    </div>
  )
}
