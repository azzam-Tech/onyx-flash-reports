import { useState, useEffect, useRef } from "react"
import type { Customer } from "./CustomersTab"
import { Button } from "./ui/button"
import { X, FolderOpen, UploadCloud, FileText, Download, Loader2, Phone, MapPin, CreditCard, Edit2, Printer, Trash2, MessageCircle } from "lucide-react"
import { Toaster, toast } from "sonner"

export function CustomerProfile({ customer, onClose }: { customer: Customer, onClose: () => void }) {
  const [files, setFiles] = useState<string[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [isUploading, setIsUploading] = useState(false)
  const [renamingFile, setRenamingFile] = useState<string | null>(null)
  const [whatsappTemplates, setWhatsappTemplates] = useState<{id: number, icon: string, title: string, message: string}[]>([])
  const [isWhatsappMenuOpen, setIsWhatsappMenuOpen] = useState(false)
  const fileInputRef = useRef<HTMLInputElement>(null)

  const PREDEFINED_NAMES = ['هوية المالك', 'هوية المفوض', 'السجل التجاري', 'شهادة التسجيل الضريبي', 'العقد', 'سند لأمر', 'الوكالة']

  const fetchFiles = () => {
    setIsLoading(true)
    fetch(`/api/customers/${customer.c_code}/documents`)
      .then(res => res.json())
      .then(data => {
        if (data.status === 'success') {
          setFiles(data.files)
        }
        setIsLoading(false)
      })
      .catch(err => {
        console.error("Error fetching files:", err)
        toast.error("حدث خطأ أثناء جلب المستندات");
        setIsLoading(false)
      })
  }

  const handleDelete = async (filename: string) => {
    if (!window.confirm(`هل أنت متأكد من رغبتك في حذف المستند "${filename}"؟\nلا يمكن التراجع عن هذا الإجراء.`)) return;
    
    const toastId = toast.loading("جاري الحذف...");
    try {
      const res = await fetch(`/api/customers/${customer.c_code}/documents/${filename}`, {
        method: 'DELETE'
      });
      const data = await res.json();
      if (data.status === 'success') {
        toast.success("تم حذف المستند بنجاح", { id: toastId });
        fetchFiles();
      } else {
        toast.error("فشل في الحذف: " + data.message, { id: toastId });
      }
    } catch (e) {
      console.error(e);
      toast.error("حدث خطأ أثناء الاتصال بالخادم", { id: toastId });
    }
  }

  const handleRename = async (oldName: string, newName: string) => {
    if (!newName) {
      setRenamingFile(null);
      return;
    }
    try {
      const res = await fetch(`/api/customers/${customer.c_code}/documents/rename`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ old_name: oldName, new_name: newName })
      });
      const data = await res.json();
      if (data.status === 'success') {
        toast.success("تم تغيير اسم المستند بنجاح");
        fetchFiles();
      } else {
        toast.error("فشل في تغيير الاسم: " + data.message);
      }
    } catch (e) {
      console.error(e);
      toast.error("حدث خطأ أثناء الاتصال بالخادم");
    }
    setRenamingFile(null);
  }

  useEffect(() => {
    fetchFiles()
    fetch('/api/customers/whatsapp/templates')
      .then(res => res.json())
      .then(data => {
        if (data.status === 'success') {
          setWhatsappTemplates(data.templates)
        }
      })
      .catch(err => console.error("Error fetching whatsapp templates:", err))
  }, [customer.c_code])

  const handleSendWhatsapp = (templateStr: string) => {
    let msg = templateStr
    msg = msg.replace(/\[اسم العميل\]/g, customer.name || '')
    msg = msg.replace(/\[الكود\]/g, customer.c_code?.toString() || '')
    msg = msg.replace(/\[الرصيد الفعلي\]/g, customer.actual_balance?.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }) || '0')
    msg = msg.replace(/\[الحد الائتماني\]/g, customer.credit_limit?.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }) || '0')
    msg = msg.replace(/\[الرقم الضريبي\]/g, customer.tax_number || 'غير متوفر')
    msg = msg.replace(/\[السجل التجاري\]/g, customer.cr_number || 'غير متوفر')
    msg = msg.replace(/\[المدينة\]/g, (customer.city || customer.country) ? `${customer.city || ''} ${customer.country ? '- ' + customer.country : ''}`.trim() : 'غير متوفر')
    msg = msg.replace(/\[الحي\]/g, customer.district || 'غير متوفر')
    msg = msg.replace(/\[المبنى\]/g, (customer.building_no || customer.street) ? `${customer.building_no || ''} ${customer.street || ''}`.trim() : 'غير متوفر')
    msg = msg.replace(/\[الرمز البريدي\]/g, customer.postal_code || 'غير متوفر')
    msg = msg.replace(/\[الرقم الإضافي\]/g, customer.additional_no || 'غير متوفر')

    let phone = customer.phone || ''
    phone = phone.replace(/\s+/g, '') // remove spaces
    if (phone.startsWith('05')) {
      phone = '9665' + phone.substring(2)
    } else if (phone.startsWith('5') && phone.length === 9) {
      phone = '9665' + phone.substring(1)
    } else if (phone.startsWith('00')) {
      phone = phone.substring(2)
    } else if (phone.startsWith('+')) {
      phone = phone.substring(1)
    }

    if (!phone) {
      toast.error('لا يوجد رقم هاتف مسجل للعميل')
      return
    }

    const encodedMsg = encodeURIComponent(msg)
    window.open(`https://wa.me/${phone}?text=${encodedMsg}`, '_blank')
    setIsWhatsappMenuOpen(false)
  }

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFiles = e.target.files
    if (!selectedFiles || selectedFiles.length === 0) return

    setIsUploading(true)
    const formData = new FormData()
    for (let i = 0; i < selectedFiles.length; i++) {
      formData.append('files', selectedFiles[i])
    }

    const toastId = toast.loading("جاري الرفع...");
    fetch(`/api/customers/${customer.c_code}/documents`, {
      method: 'POST',
      body: formData,
    })
      .then(res => res.json())
      .then(data => {
        setIsUploading(false)
        if (data.status === 'success') {
          toast.success("تم رفع المستندات بنجاح", { id: toastId });
          fetchFiles() // Refresh list
        } else {
          toast.error('فشل رفع الملف: ' + data.message, { id: toastId })
        }
      })
      .catch(err => {
        setIsUploading(false)
        console.error("Upload error:", err)
        toast.error('حدث خطأ أثناء الرفع', { id: toastId })
      })
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-sm p-4 print:hidden">
      <Toaster position="top-center" richColors />
      <div className="bg-white w-full max-w-6xl rounded-3xl shadow-2xl flex flex-col max-h-[90vh] overflow-hidden animate-in fade-in zoom-in-95 duration-200">
        
        {/* Premium Header */}
        <div className="p-6 md:p-8 border-b border-slate-100 bg-white relative z-10 overflow-visible flex-shrink-0">
          <div className="absolute top-0 right-0 w-full h-32 bg-gradient-to-b from-slate-50 to-transparent opacity-50 pointer-events-none"></div>
          
          <div className="flex items-start justify-between relative">
            <div className="flex items-center gap-5">
              {/* Premium Avatar */}
              <div className="w-16 h-16 sm:w-20 sm:h-20 rounded-2xl bg-gradient-to-br from-slate-800 to-slate-700 text-white flex items-center justify-center shadow-lg shadow-slate-200 shrink-0 border-4 border-white ring-1 ring-slate-100 relative overflow-hidden">
                <div className="absolute inset-0 bg-white/10 backdrop-blur-sm"></div>
                <span className="text-2xl sm:text-3xl font-black tracking-tighter relative z-10">{customer.name.substring(0, 1)}</span>
              </div>
              
              <div className="flex flex-col">
                <div className="flex items-center gap-3 mb-2">
                  <h2 className="text-xl sm:text-2xl font-black text-slate-800 tracking-tight leading-none">
                    {customer.name}
                  </h2>
                  {customer.is_inactive ? (
                    <span className="px-2.5 py-0.5 rounded-full text-[10px] sm:text-xs font-extrabold bg-rose-100 text-rose-700 border border-rose-200 uppercase tracking-wider">العميل موقف</span>
                  ) : customer.is_inactive_sales ? (
                    <span className="px-2.5 py-0.5 rounded-full text-[10px] sm:text-xs font-extrabold bg-orange-100 text-orange-700 border border-orange-200 uppercase tracking-wider">البيع موقف</span>
                  ) : (
                    <span className="px-2.5 py-0.5 rounded-full text-[10px] sm:text-xs font-extrabold bg-emerald-50 text-emerald-600 border border-emerald-100 uppercase tracking-wider shadow-sm">نشط</span>
                  )}
                </div>
                
                {/* Meta Badges */}
                <div className="flex flex-wrap items-center gap-2 mt-1">
                  <div className="flex items-center gap-1.5 px-3 py-1.5 bg-slate-50 border border-slate-200/60 rounded-xl text-xs font-bold text-slate-600 shadow-sm">
                    <CreditCard className="w-3.5 h-3.5 text-primary" />
                    كود: <span className="text-slate-800">{customer.c_code}</span>
                  </div>
                  {(customer.city || customer.district) && (
                    <div className="flex items-center gap-1.5 px-3 py-1.5 bg-slate-50 border border-slate-200/60 rounded-xl text-xs font-bold text-slate-600 shadow-sm">
                      <MapPin className="w-3.5 h-3.5 text-rose-500" />
                      {customer.city} {customer.district ? `- ${customer.district}` : ''}
                    </div>
                  )}
                  {customer.phone && (
                    <div className="flex items-center gap-1.5 px-3 py-1.5 bg-slate-50 border border-slate-200/60 rounded-xl text-xs font-bold text-slate-600 shadow-sm" dir="ltr">
                      <Phone className="w-3.5 h-3.5 text-emerald-500" />
                      {customer.phone}
                    </div>
                  )}
                </div>
              </div>
            </div>

            <div className="flex items-center gap-2 relative">
              <div className="relative">
                <Button 
                  onClick={() => setIsWhatsappMenuOpen(!isWhatsappMenuOpen)} 
                  className={`rounded-full h-10 px-4 text-white font-bold transition-all duration-300 shadow-sm shrink-0 flex items-center gap-2 ${customer.phone ? 'bg-[#25D366] hover:bg-[#128C7E]' : 'bg-slate-300 cursor-not-allowed'}`}
                  title="مراسلة عبر واتساب"
                >
                  <MessageCircle className="w-4 h-4" />
                  <span className="hidden sm:inline text-xs">واتساب</span>
                </Button>
                
                {isWhatsappMenuOpen && customer.phone && (
                  <div className="absolute top-full left-0 mt-2 w-64 bg-white rounded-2xl shadow-xl border border-slate-100 z-50 overflow-hidden animate-in fade-in slide-in-from-top-2">
                    <div className="p-3 bg-slate-50 border-b border-slate-100">
                      <h4 className="text-xs font-bold text-slate-500">نماذج الرسائل السريعة</h4>
                    </div>
                    <div className="p-1 max-h-64 overflow-y-auto">
                      {whatsappTemplates.length > 0 ? (
                        whatsappTemplates.map(template => (
                          <button
                            key={template.id}
                            onClick={() => handleSendWhatsapp(template.message)}
                            className="w-full text-right flex items-center gap-3 p-3 hover:bg-slate-50 rounded-xl transition-colors group"
                          >
                            <span className="text-lg">{template.icon}</span>
                            <span className="text-sm font-semibold text-slate-700 group-hover:text-slate-900">{template.title}</span>
                          </button>
                        ))
                      ) : (
                        <div className="p-4 text-center text-xs text-slate-500">لا توجد قوالب رسائل متوفرة</div>
                      )}
                    </div>
                  </div>
                )}
              </div>

              <Button variant="ghost" size="icon" onClick={onClose} className="rounded-full w-10 h-10 bg-slate-50 hover:bg-rose-50 hover:text-rose-600 border border-slate-200/60 transition-all duration-300 shadow-sm shrink-0">
                <X className="w-4 h-4" />
              </Button>
            </div>
          </div>
        </div>

        {/* Content */}
        <div className="flex-1 overflow-auto bg-slate-50/50 p-6 md:p-8">
          <div className="flex flex-col gap-6">
            
            {/* Top Section: All Details */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              
              {/* Left Column: Financial & Identity */}
              <div className="space-y-6">
                
                {/* Premium Financial Dashboard Widget */}
                <div className="bg-slate-900 rounded-3xl p-6 relative overflow-hidden shadow-xl shadow-slate-900/10">
                  <div className="absolute top-0 right-0 w-64 h-64 bg-blue-500/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2 pointer-events-none"></div>
                  <div className="absolute bottom-0 left-0 w-64 h-64 bg-emerald-500/10 rounded-full blur-3xl translate-y-1/2 -translate-x-1/2 pointer-events-none"></div>
                  
                  <div className="relative z-10">
                    <h3 className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-6">الملخص المالي</h3>
                    
                    <div className="mb-6">
                      <p className="text-sm font-medium text-slate-300 mb-1">الرصيد الفعلي (لك / عليك)</p>
                      <div className="flex items-baseline gap-2">
                        <p className={`text-3xl sm:text-4xl font-black tracking-tight ${customer.actual_balance > 0 ? 'text-white' : 'text-emerald-400'}`} dir="ltr">
                          {customer.actual_balance.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
                        </p>
                        <span className="text-slate-500 font-bold">SAR</span>
                      </div>
                    </div>

                    <div className="pt-6 border-t border-slate-800">
                      <div className="flex justify-between items-end mb-2">
                        <div>
                          <p className="text-xs font-medium text-slate-400 mb-0.5">الحد الائتماني المسموح</p>
                          <p className="text-lg font-bold text-white" dir="ltr">
                            {customer.credit_limit.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })} <span className="text-xs text-slate-500">SAR</span>
                          </p>
                        </div>
                        {customer.credit_limit > 0 && (
                          <div className="text-right">
                            <span className="text-xs font-bold text-slate-400">الاستهلاك</span>
                            <p className="text-sm font-bold text-blue-400" dir="ltr">
                              {Math.min(100, Math.max(0, (customer.actual_balance / customer.credit_limit) * 100)).toFixed(1)}%
                            </p>
                          </div>
                        )}
                      </div>
                      
                      {/* Utilization Progress Bar */}
                      {customer.credit_limit > 0 && (
                        <div className="h-2 w-full bg-slate-800 rounded-full overflow-hidden mt-3 flex" dir="ltr">
                          <div 
                            className={`h-full rounded-full transition-all duration-1000 ease-out ${
                              (customer.actual_balance / customer.credit_limit) > 0.9 ? 'bg-rose-500' : 
                              (customer.actual_balance / customer.credit_limit) > 0.75 ? 'bg-amber-400' : 'bg-blue-500'
                            }`}
                            style={{ width: `${Math.min(100, Math.max(0, (customer.actual_balance / customer.credit_limit) * 100))}%` }}
                          ></div>
                        </div>
                      )}
                    </div>
                  </div>
                </div>

                {/* Identity & Registration - Unified Card */}
                <div className="bg-white rounded-3xl shadow-sm border border-slate-100 overflow-hidden">
                  <div className="grid grid-cols-3 divide-x divide-x-reverse divide-slate-100">
                    <div className="p-4 sm:p-5 flex flex-col items-center justify-center text-center hover:bg-slate-50 transition-colors">
                      <span className="text-[10px] sm:text-xs font-bold text-slate-400 uppercase tracking-wider mb-1.5">السجل التجاري</span>
                      <span className="text-sm font-extrabold text-slate-800">{customer.cr_number || '-'}</span>
                    </div>
                    <div className="p-4 sm:p-5 flex flex-col items-center justify-center text-center hover:bg-slate-50 transition-colors">
                      <span className="text-[10px] sm:text-xs font-bold text-slate-400 uppercase tracking-wider mb-1.5">الرقم الضريبي</span>
                      <span className="text-sm font-extrabold text-slate-800">{customer.tax_number || '-'}</span>
                    </div>
                    <div className="p-4 sm:p-5 flex flex-col items-center justify-center text-center hover:bg-slate-50 transition-colors">
                      <span className="text-[10px] sm:text-xs font-bold text-slate-400 uppercase tracking-wider mb-1.5">المعرف</span>
                      <span className="text-sm font-extrabold text-slate-800">{customer.identifier || '-'}</span>
                    </div>
                  </div>
                </div>
              </div>

              {/* Right Column: National Address Card */}
              <div className="bg-white rounded-3xl p-6 sm:p-8 border border-slate-100 shadow-sm relative overflow-hidden flex flex-col">
                <div className="flex items-center gap-4 mb-8">
                  <div className="w-12 h-12 rounded-2xl bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0 shadow-inner">
                    <MapPin className="w-6 h-6" />
                  </div>
                  <div>
                    <h3 className="text-lg font-black text-slate-800">العنوان الوطني</h3>
                    <p className="text-xs font-semibold text-slate-400 mt-0.5">تفاصيل الموقع الجغرافي للعميل</p>
                  </div>
                </div>
                
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 flex-1 content-start">
                  <div className="bg-slate-50 rounded-2xl p-4 border border-slate-100/60 hover:border-emerald-200 transition-colors">
                    <span className="flex items-center gap-2 text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-2">
                      <div className="w-1.5 h-1.5 rounded-full bg-emerald-400"></div> المبنى / الشارع
                    </span>
                    <span className="block text-sm font-extrabold text-slate-700">{(customer.building_no || customer.street) ? `${customer.building_no || ''} ${customer.street || ''}`.trim() : '-'}</span>
                  </div>
                  <div className="bg-slate-50 rounded-2xl p-4 border border-slate-100/60 hover:border-emerald-200 transition-colors">
                    <span className="flex items-center gap-2 text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-2">
                      <div className="w-1.5 h-1.5 rounded-full bg-emerald-400"></div> الحي
                    </span>
                    <span className="block text-sm font-extrabold text-slate-700">{customer.district || '-'}</span>
                  </div>
                  <div className="col-span-1 sm:col-span-2 bg-slate-50 rounded-2xl p-4 border border-slate-100/60 hover:border-emerald-200 transition-colors">
                    <span className="flex items-center gap-2 text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-2">
                      <div className="w-1.5 h-1.5 rounded-full bg-emerald-400"></div> المدينة / الدولة
                    </span>
                    <span className="block text-sm font-extrabold text-slate-700">{(customer.city || customer.country) ? `${customer.city || ''} ${customer.country ? '- ' + customer.country : ''}`.trim() : '-'}</span>
                  </div>
                  <div className="bg-slate-50 rounded-2xl p-4 border border-slate-100/60 hover:border-emerald-200 transition-colors">
                    <span className="flex items-center gap-2 text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-2">
                      <div className="w-1.5 h-1.5 rounded-full bg-emerald-400"></div> الرمز البريدي
                    </span>
                    <span className="block text-sm font-extrabold text-slate-700">{customer.postal_code || '-'}</span>
                  </div>
                  <div className="bg-slate-50 rounded-2xl p-4 border border-slate-100/60 hover:border-emerald-200 transition-colors">
                    <span className="flex items-center gap-2 text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-2">
                      <div className="w-1.5 h-1.5 rounded-full bg-emerald-400"></div> الرقم الإضافي
                    </span>
                    <span className="block text-sm font-extrabold text-slate-700">{customer.additional_no || '-'}</span>
                  </div>
                </div>
              </div>
            </div>

            {/* Bottom Section: Documents */}
            <div className="bg-white rounded-2xl border border-slate-100 shadow-sm overflow-hidden">
              <div className="p-4 border-b border-slate-100 bg-slate-50/50 flex flex-col sm:flex-row justify-between items-center gap-4">
                <h3 className="font-bold text-slate-700 flex items-center gap-2">
                  <FolderOpen className="w-5 h-5 text-slate-400" />
                  مستندات العميل ({files.length})
                </h3>
                
                <div className="flex items-center gap-2 w-full sm:w-auto">
                  <input 
                    type="file" 
                    multiple
                    ref={fileInputRef} 
                    onChange={handleFileUpload} 
                    className="hidden" 
                  />
                  <Button 
                    onClick={() => fileInputRef.current?.click()}
                    disabled={isUploading}
                    className="bg-blue-600 hover:bg-blue-700 text-white rounded-xl gap-2 w-full sm:w-auto"
                  >
                    {isUploading ? <Loader2 className="w-4 h-4 animate-spin" /> : <UploadCloud className="w-4 h-4" />}
                    {isUploading ? 'جاري الرفع...' : 'رفع مستند جديد'}
                  </Button>
                </div>
              </div>
                <div className="p-2">
                  {isLoading ? (
                    <div className="p-8 text-center text-slate-500 flex justify-center">
                      <Loader2 className="w-6 h-6 animate-spin" />
                    </div>
                  ) : files.length === 0 ? (
                    <div className="p-8 text-center">
                      <div className="w-12 h-12 rounded-full bg-slate-50 flex items-center justify-center mx-auto mb-3">
                        <FileText className="w-6 h-6 text-slate-300" />
                      </div>
                      <p className="text-slate-500 font-medium">لا توجد مستندات مرفوعة لهذا العميل حتى الآن</p>
                    </div>
                  ) : (
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                      {files.map(file => (
                        <div key={file} className="flex items-center justify-between p-3 rounded-xl border border-slate-100 hover:border-blue-200 hover:bg-blue-50/50 transition-colors group">
                          <div className="flex items-center gap-3 overflow-hidden flex-1">
                            <div className="w-10 h-10 rounded-lg bg-slate-100 text-slate-500 flex items-center justify-center group-hover:bg-white group-hover:text-blue-500 shrink-0">
                              <FileText className="w-5 h-5" />
                            </div>
                            {renamingFile === file ? (
                              <select 
                                className="flex-1 p-2 border border-blue-300 rounded-lg text-sm bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 mr-2"
                                autoFocus
                                onChange={(e) => handleRename(file, e.target.value)}
                                onBlur={() => setRenamingFile(null)}
                                defaultValue=""
                              >
                                <option value="" disabled>اختر اسماً للمستند...</option>
                                {PREDEFINED_NAMES.map(name => (
                                  <option key={name} value={name}>{name}</option>
                                ))}
                              </select>
                            ) : (
                              <span className="text-sm font-semibold text-slate-700 truncate" dir="ltr">{file}</span>
                            )}
                          </div>
                          <div className="flex items-center gap-1 shrink-0">
                            {renamingFile !== file && (
                              <button
                                onClick={() => setRenamingFile(file)}
                                className="p-2 text-slate-400 hover:text-orange-500 hover:bg-white rounded-lg transition-colors"
                                title="إعادة تسمية"
                              >
                                <Edit2 className="w-4 h-4" />
                              </button>
                            )}
                            <button
                              onClick={() => {
                                const url = `/api/customers/download/${customer.c_code}/${file}`;
                                const iframe = document.createElement('iframe');
                                iframe.style.display = 'none';
                                iframe.src = url;
                                document.body.appendChild(iframe);
                                iframe.onload = () => {
                                  setTimeout(() => {
                                    iframe.contentWindow?.print();
                                  }, 500);
                                };
                              }}
                              className="p-2 text-slate-400 hover:text-emerald-600 hover:bg-white rounded-lg transition-colors"
                              title="طباعة"
                            >
                              <Printer className="w-4 h-4" />
                            </button>
                            <a 
                              href={`/api/customers/download/${customer.c_code}/${file}`}
                              target="_blank"
                              rel="noreferrer"
                              download={file}
                              className="p-2 text-slate-400 hover:text-blue-600 hover:bg-white rounded-lg transition-colors"
                              title="تحميل"
                            >
                              <Download className="w-4 h-4" />
                            </a>
                            <button
                              onClick={() => handleDelete(file)}
                              className="p-2 text-slate-400 hover:text-rose-600 hover:bg-rose-50 rounded-lg transition-colors ml-1"
                              title="حذف"
                            >
                              <Trash2 className="w-4 h-4" />
                            </button>
                          </div>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              </div>

          </div>
        </div>

      </div>
    </div>
  )
}
