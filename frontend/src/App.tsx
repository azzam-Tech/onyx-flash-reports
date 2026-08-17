import { useState, useEffect } from "react"
import { Routes, Route, Navigate, useNavigate, useParams } from "react-router-dom"
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
  const [isLoading, setIsLoading] = useState(true)
  const navigate = useNavigate()

  // Authentication State
  const [isAuthenticated, setIsAuthenticated] = useState(false)
  const [user, setUser] = useState<any>(null)

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
            // Initial redirection logic if needed when visiting the root path directly
            const hash = window.location.hash.replace(/^#\/?/, '')
            if (!hash || hash === '/') {
               navigate(`/${finalTabs[0].id}/${finalTabs[0].reports[0].id}`, { replace: true })
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
    navigate("/", { replace: true })
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
        onLogout={handleLogout}
      />
      <div className="flex flex-1 flex-col overflow-hidden print:overflow-visible print:block">
        <Routes>
          <Route path="/dashboard/main" element={<Dashboard />} />
          <Route path="/tools/users" element={<UsersManagement />} />
          <Route path="/tools/settings" element={<SettingsManagement />} />
          <Route path="/:tabId/:reportId" element={<ReportViewerWrapper tabs={tabs} />} />
          <Route path="*" element={<Navigate to="/dashboard/main" replace />} />
        </Routes>
      </div>
    </div>
  )
}

function ReportViewerWrapper({ tabs }: { tabs: Tab[] }) {
  const { tabId, reportId } = useParams()
  
  if (!tabId || !reportId) return null

  if (tabId === 'tools') {
    return (
      <iframe 
        src={`http://localhost:8000/${reportId}`} 
        className="w-full h-full border-none bg-slate-50"
        title="External Tool"
      />
    )
  }

  const reportTitle = tabs.find(t => t.id === tabId)?.reports.find(r => r.id === reportId)?.title || "تقرير"
  
  return (
    <MainContent 
      key={`${tabId}-${reportId}`}
      tabId={tabId} 
      reportId={reportId} 
      reportTitle={reportTitle}
    />
  )
}
