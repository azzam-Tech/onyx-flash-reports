import { useState, useEffect } from "react"
import { Users, Shield, ShieldCheck, Save, Trash2, Edit, Plus, UserPlus } from "lucide-react"
import { ScrollArea } from "./ui/scroll-area"

export function UsersManagement() {
  const [users, setUsers] = useState<any>({})
  const [tabsData, setTabsData] = useState<any[]>([])
  const [isLoading, setIsLoading] = useState(true)
  
  // Form State
  const [editingUser, setEditingUser] = useState("")
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [role, setRole] = useState("user")
  const [allowedTabs, setAllowedTabs] = useState<string[]>([])
  const [allowedReports, setAllowedReports] = useState<string[]>([])

  useEffect(() => {
    fetchData()
  }, [])

  const fetchData = async () => {
    try {
      const res = await fetch("/api/users_manage")
      const data = await res.json()
      if (data.users) setUsers(data.users)
      if (data.tabs) setTabsData(data.tabs)
    } catch (e) {
      console.error(e)
    } finally {
      setIsLoading(false)
    }
  }

  const handleEdit = (uname: string, udata: any) => {
    setEditingUser(uname)
    setUsername(uname)
    setPassword("") // Clear password field for editing
    setRole(udata.role)
    setAllowedTabs(udata.allowed_tabs || [])
    setAllowedReports(udata.allowed_reports || [])
  }

  const handleResetForm = () => {
    setEditingUser("")
    setUsername("")
    setPassword("")
    setRole("user")
    setAllowedTabs([])
    setAllowedReports([])
  }

  const handleSave = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      const res = await fetch("/api/users_manage", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          action: "add_or_update",
          username,
          password,
          role,
          allowed_tabs: role === 'admin' ? ["*"] : allowedTabs,
          allowed_reports: role === 'admin' ? ["*"] : allowedReports
        })
      })
      if (res.ok) {
        handleResetForm()
        fetchData()
      } else {
        alert("فشلت عملية الحفظ (تأكد من صلاحياتك كمدير)")
      }
    } catch (e) {
      console.error(e)
    }
  }

  const handleDelete = async (uname: string) => {
    if (!confirm(`هل أنت متأكد من حذف المستخدم ${uname}؟`)) return
    try {
      const res = await fetch("/api/users_manage", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          action: "delete",
          username: uname
        })
      })
      if (res.ok) {
        if (editingUser === uname) handleResetForm()
        fetchData()
      } else {
        alert("فشلت عملية الحذف")
      }
    } catch (e) {
      console.error(e)
    }
  }

  const toggleTab = (tabId: string) => {
    setAllowedTabs(prev => 
      prev.includes(tabId) ? prev.filter(t => t !== tabId) : [...prev, tabId]
    )
  }

  const toggleReport = (repId: string) => {
    setAllowedReports(prev => 
      prev.includes(repId) ? prev.filter(r => r !== repId) : [...prev, repId]
    )
  }

  if (isLoading) {
    return <div className="flex h-full items-center justify-center text-slate-500">جاري التحميل...</div>
  }

  return (
    <div className="min-h-full bg-slate-50 flex flex-col p-8 overflow-y-auto" dir="rtl">
      
      <div className="flex items-center justify-between mb-8">
        <div className="flex items-center gap-4">
          <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-blue-600 to-indigo-600 flex items-center justify-center shadow-lg shadow-indigo-600/20">
            <Users className="w-6 h-6 text-white" />
          </div>
          <div>
            <h1 className="text-2xl font-bold text-slate-900 tracking-tight">إدارة المستخدمين والصلاحيات</h1>
            <p className="text-sm text-slate-500 mt-1">إضافة، تعديل، وحذف المستخدمين وتحديد صلاحيات الوصول للتقارير.</p>
          </div>
        </div>
      </div>

      <div className="flex items-start gap-8 pb-10">
        
        {/* Users List (Right Side) */}
        <div className="w-1/3 flex flex-col gap-4 sticky top-0 h-[calc(100vh-140px)]">
          <div className="bg-white rounded-3xl p-6 shadow-sm border border-slate-100 flex-1 flex flex-col overflow-hidden">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-lg font-bold text-slate-800">المستخدمون ({Object.keys(users).length})</h2>
              <button 
                onClick={handleResetForm}
                className="flex items-center gap-2 text-sm text-indigo-600 bg-indigo-50 px-3 py-1.5 rounded-xl font-bold hover:bg-indigo-100 transition-colors"
              >
                <UserPlus className="w-4 h-4" />
                مستخدم جديد
              </button>
            </div>
            
            <ScrollArea className="flex-1 -mx-2 px-2" dir="rtl">
              <div className="space-y-3">
                {Object.entries(users).map(([uname, udata]: [string, any]) => (
                  <div key={uname} className="group p-4 rounded-2xl border border-slate-100 hover:border-indigo-200 hover:shadow-md transition-all duration-300 bg-slate-50 hover:bg-white relative overflow-hidden">
                    <div className="flex items-start justify-between">
                      <div>
                        <div className="flex items-center gap-2 mb-1">
                          <div className="w-8 h-8 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-600 font-bold uppercase">
                            {uname.charAt(0)}
                          </div>
                          <h3 className="font-bold text-slate-900">{uname}</h3>
                        </div>
                        <div className="flex items-center gap-2 mt-2">
                          <span className={`px-2.5 py-1 text-xs font-bold rounded-lg flex items-center gap-1.5 ${udata.role === 'admin' ? 'bg-red-100 text-red-700' : 'bg-emerald-100 text-emerald-700'}`}>
                            {udata.role === 'admin' ? <ShieldCheck className="w-3.5 h-3.5" /> : <Shield className="w-3.5 h-3.5" />}
                            {udata.role === 'admin' ? 'مدير نظام' : 'مستخدم عادي'}
                          </span>
                        </div>
                      </div>
                      
                      <div className="flex flex-col gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                        <button onClick={() => handleEdit(uname, udata)} className="w-8 h-8 flex items-center justify-center rounded-xl bg-slate-100 text-slate-600 hover:bg-indigo-600 hover:text-white transition-colors">
                          <Edit className="w-4 h-4" />
                        </button>
                        {uname !== 'admin' && (
                          <button onClick={() => handleDelete(uname)} className="w-8 h-8 flex items-center justify-center rounded-xl bg-slate-100 text-slate-600 hover:bg-red-500 hover:text-white transition-colors">
                            <Trash2 className="w-4 h-4" />
                          </button>
                        )}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </ScrollArea>
          </div>
        </div>

        {/* User Form (Left Side) */}
        <div className="w-2/3 bg-white rounded-3xl p-8 shadow-sm border border-slate-100 flex flex-col">
          <h2 className="text-xl font-bold text-slate-900 mb-6 flex items-center gap-2">
            {editingUser ? <Edit className="w-5 h-5 text-indigo-600" /> : <Plus className="w-5 h-5 text-indigo-600" />}
            {editingUser ? `تعديل المستخدم: ${editingUser}` : 'إضافة مستخدم جديد'}
          </h2>
          
          <form onSubmit={handleSave} className="flex flex-col">
            <div className="grid grid-cols-2 gap-6 mb-8">
              <div>
                <label className="block text-sm font-bold text-slate-700 mb-2">اسم المستخدم</label>
                <input 
                  type="text" 
                  value={username}
                  onChange={e => setUsername(e.target.value)}
                  disabled={editingUser === 'admin'}
                  required
                  placeholder="مثال: ahmad"
                  className="w-full bg-slate-50 border border-slate-200 px-4 py-3 rounded-xl text-slate-900 font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:bg-white transition-all disabled:opacity-60"
                />
              </div>
              <div>
                <label className="block text-sm font-bold text-slate-700 mb-2">رمز الدخول (PIN)</label>
                <input 
                  type="password" 
                  value={password}
                  onChange={e => setPassword(e.target.value)}
                  required={!editingUser}
                  placeholder={editingUser ? "اتركه فارغاً لعدم التغيير" : "• • • • •"}
                  className="w-full bg-slate-50 border border-slate-200 px-4 py-3 rounded-xl text-slate-900 font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:bg-white transition-all tracking-[0.2em]"
                />
              </div>
              <div className="col-span-2">
                <label className="block text-sm font-bold text-slate-700 mb-2">دور المستخدم</label>
                <div className="flex gap-4">
                  <label className={`flex-1 cursor-pointer border-2 rounded-2xl p-4 flex items-center gap-4 transition-all ${role === 'user' ? 'border-indigo-600 bg-indigo-50/50' : 'border-slate-100 hover:border-slate-200'}`}>
                    <input type="radio" name="role" value="user" checked={role === 'user'} onChange={() => setRole('user')} className="w-5 h-5 accent-indigo-600" disabled={editingUser === 'admin'} />
                    <div>
                      <div className="font-bold text-slate-900">مستخدم عادي</div>
                      <div className="text-xs text-slate-500 mt-1">يحتاج لتحديد صلاحيات التقارير بوضوح</div>
                    </div>
                  </label>
                  <label className={`flex-1 cursor-pointer border-2 rounded-2xl p-4 flex items-center gap-4 transition-all ${role === 'admin' ? 'border-red-500 bg-red-50/50' : 'border-slate-100 hover:border-slate-200'}`}>
                    <input type="radio" name="role" value="admin" checked={role === 'admin'} onChange={() => setRole('admin')} className="w-5 h-5 accent-red-500" disabled={editingUser === 'admin'} />
                    <div>
                      <div className="font-bold text-slate-900">مدير نظام</div>
                      <div className="text-xs text-slate-500 mt-1">يملك صلاحيات كاملة تلقائياً للوصول للكل</div>
                    </div>
                  </label>
                </div>
              </div>
            </div>

            {role === 'user' && (
              <div className="flex flex-col mb-6">
                <label className="block text-sm font-bold text-slate-700 mb-3 flex items-center justify-between">
                  <span>صلاحيات الوصول (للتقارير والتبويبات)</span>
                  <span className="text-xs font-normal text-slate-500 bg-slate-100 px-3 py-1 rounded-full">حدد ما يمكن للمستخدم رؤيته</span>
                </label>
                <div className="border border-slate-200 rounded-2xl bg-slate-50 p-5">
                  <div className="grid grid-cols-2 gap-4">
                    {tabsData.map(tab => (
                      <div key={tab.id} className="bg-white border border-slate-200 rounded-xl p-4">
                        <label className="flex items-center gap-3 mb-4 cursor-pointer">
                          <input 
                            type="checkbox" 
                            checked={allowedTabs.includes(tab.id) || allowedTabs.includes('*')}
                            onChange={() => toggleTab(tab.id)}
                            className="w-4 h-4 rounded text-indigo-600 focus:ring-indigo-500 accent-indigo-600"
                          />
                          <span className="font-bold text-slate-900 text-sm">تبويب: {tab.title}</span>
                        </label>
                        <div className="space-y-2 pr-6 border-r-2 border-slate-100">
                          {tab.reports.map((rep: any) => {
                            const repKey = `${tab.id}/${rep.id}`
                            return (
                              <label key={repKey} className="flex items-center gap-3 cursor-pointer group">
                                <input 
                                  type="checkbox" 
                                  checked={allowedReports.includes(repKey) || allowedReports.includes('*')}
                                  onChange={() => toggleReport(repKey)}
                                  className="w-4 h-4 rounded text-indigo-600 focus:ring-indigo-500 accent-indigo-600"
                                />
                                <span className="text-sm font-semibold text-slate-600 group-hover:text-slate-900 transition-colors">تقرير: {rep.title}</span>
                              </label>
                            )
                          })}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            )}

            <div className="mt-6 pt-6 border-t border-slate-100 flex items-center justify-end gap-3">
              {editingUser && (
                <button type="button" onClick={handleResetForm} className="px-6 py-3 rounded-xl font-bold text-slate-600 bg-slate-100 hover:bg-slate-200 transition-colors">
                  إلغاء التعديل
                </button>
              )}
              <button type="submit" className="flex items-center gap-2 px-8 py-3 rounded-xl font-bold text-white bg-indigo-600 hover:bg-indigo-700 shadow-md shadow-indigo-600/20 transition-colors">
                <Save className="w-5 h-5" />
                حفظ المستخدم
              </button>
            </div>
          </form>
        </div>

      </div>
    </div>
  )
}
