import { useState } from "react"
import { Lock, ArrowRight, Loader2, ShieldCheck } from "lucide-react"

interface LoginProps {
  onLoginSuccess: (userData: any) => void
}

export function Login({ onLoginSuccess }: LoginProps) {
  const [pin, setPin] = useState("")
  const [error, setError] = useState("")
  const [isLoading, setIsLoading] = useState(false)

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!pin) {
      setError("الرجاء إدخال رمز المرور")
      return
    }

    setIsLoading(true)
    setError("")

    try {
      const res = await fetch("/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ pin })
      })
      
      const data = await res.json()
      
      if (res.ok && data.success) {
        onLoginSuccess(data.user)
      } else {
        setError(data.error || "رمز المرور غير صحيح")
        setPin("")
      }
    } catch (e) {
      setError("حدث خطأ في الاتصال بالخادم")
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-slate-50 flex items-center justify-center p-4 font-['Cairo','Inter',sans-serif]" dir="rtl">
      
      <div className="w-full max-w-md">
        <div className="text-center mb-10">
          <div className="inline-flex items-center justify-center w-20 h-20 rounded-3xl bg-gradient-to-br from-indigo-500 to-purple-600 shadow-xl shadow-indigo-500/30 mb-6">
            <ShieldCheck className="w-10 h-10 text-white" />
          </div>
          <h1 className="text-3xl font-black text-slate-900 tracking-tight mb-2">تسجيل الدخول</h1>
          <p className="text-slate-500 font-medium">نظام SREEN للتقارير ولوحات القيادة</p>
        </div>

        <div className="bg-white rounded-3xl shadow-2xl shadow-slate-200/50 border border-slate-100 p-8 sm:p-10 relative overflow-hidden">
          {/* Decorative background blur */}
          <div className="absolute -top-24 -left-24 w-48 h-48 bg-indigo-50 rounded-full blur-3xl opacity-50 pointer-events-none"></div>
          <div className="absolute -bottom-24 -right-24 w-48 h-48 bg-purple-50 rounded-full blur-3xl opacity-50 pointer-events-none"></div>
          
          <form onSubmit={handleLogin} className="relative z-10 flex flex-col gap-6">
            
            {error && (
              <div className="bg-red-50 text-red-600 p-4 rounded-2xl text-sm font-bold border border-red-100 animate-in fade-in slide-in-from-top-2">
                {error}
              </div>
            )}

            <div>
              <label className="block text-sm font-bold text-slate-700 mb-3">رمز المرور (PIN)</label>
              <div className="relative">
                <div className="absolute inset-y-0 right-0 pr-4 flex items-center pointer-events-none text-slate-400">
                  <Lock className="w-5 h-5" />
                </div>
                <input 
                  type="password"
                  value={pin}
                  onChange={(e) => setPin(e.target.value)}
                  placeholder="• • • • •"
                  className="w-full bg-slate-50 border-2 border-slate-100 rounded-2xl py-4 pr-12 pl-4 text-center text-2xl tracking-[0.5em] font-bold text-slate-900 placeholder:text-slate-300 focus:outline-none focus:border-indigo-500 focus:bg-white transition-all shadow-sm"
                  autoFocus
                  inputMode="numeric"
                  disabled={isLoading}
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={isLoading || !pin}
              className="w-full mt-2 bg-gradient-to-r from-indigo-600 to-indigo-700 hover:from-indigo-500 hover:to-indigo-600 text-white rounded-2xl py-4 px-6 font-bold text-lg flex items-center justify-center gap-3 transition-all transform active:scale-[0.98] disabled:opacity-70 disabled:active:scale-100 shadow-lg shadow-indigo-600/20 group"
            >
              {isLoading ? (
                <>
                  <Loader2 className="w-6 h-6 animate-spin" />
                  جاري التحقق...
                </>
              ) : (
                <>
                  دخول للنظام
                  <ArrowRight className="w-5 h-5 group-hover:-translate-x-1 transition-transform" />
                </>
              )}
            </button>
          </form>
        </div>
        
        <div className="text-center mt-8 text-sm text-slate-400 font-medium">
          جميع الحقوق محفوظة &copy; 2026
        </div>
      </div>

    </div>
  )
}
