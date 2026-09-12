import { useState, useEffect, useMemo } from "react"
import { Card } from "./ui/card"
import { Button } from "./ui/button"
import { Input } from "./ui/input"
import { Search, FolderOpen, MessageCircle } from "lucide-react"
import { CustomerProfile } from "./CustomerProfile"
import { toast } from "sonner"
import {
  useReactTable,
  getCoreRowModel,
  flexRender,
  getSortedRowModel,
  getFilteredRowModel,
  type SortingState,
  type ColumnDef
} from '@tanstack/react-table'

export interface Customer {
  c_code: string
  name: string
  country: string
  city: string
  district: string
  credit_limit: number
  actual_balance: number
  phone: string
  building_no?: string
  street?: string
  postal_code?: string
  additional_no?: string
  tax_number?: string
  cr_number?: string
  identifier?: string
  is_inactive?: boolean
  is_inactive_sales?: boolean
}

export function CustomersTab() {
  const [data, setData] = useState<Customer[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [sorting, setSorting] = useState<SortingState>([])
  const [globalFilter, setGlobalFilter] = useState('')
  const [selectedCustomer, setSelectedCustomer] = useState<Customer | null>(null)
  const [whatsappTemplates, setWhatsappTemplates] = useState<{ id: number, icon: string, title: string, message: string }[]>([])
  const [openWhatsappMenuId, setOpenWhatsappMenuId] = useState<string | null>(null)
  const [netSupplier, setNetSupplier] = useState(true)

  useEffect(() => {
    setIsLoading(true)
    fetch(`/api/customers/?net_supplier=${netSupplier}`)
      .then(res => res.json())
      .then(resData => {
        if (resData.status === 'success') {
          setData(resData.data)
        }
        setIsLoading(false)
      })
      .catch(err => {
        console.error(err)
        setIsLoading(false)
      })
  }, [netSupplier])

  useEffect(() => {
    fetch('/api/customers/whatsapp/templates')
      .then(res => res.json())
      .then(data => {
        if (data.status === 'success') {
          setWhatsappTemplates(data.templates)
        }
      })
      .catch(err => console.error("Error fetching whatsapp templates:", err))
  }, [])

  const handleSendWhatsapp = (templateStr: string, customer: Customer) => {
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
    setOpenWhatsappMenuId(null)
  }

  const columns = useMemo<ColumnDef<Customer>[]>(() => [
    {
      accessorKey: 'c_code',
      header: 'كود العميل',
      cell: info => <span className="font-bold text-slate-700">{info.getValue() as string}</span>,
    },
    {
      accessorKey: 'name',
      header: 'اسم العميل',
      cell: info => <span className="font-bold text-primary">{info.getValue() as string}</span>,
    },
    {
      id: 'status',
      header: 'الحالة',
      accessorFn: (row) => row.is_inactive ? 2 : (row.is_inactive_sales ? 1 : 0),
      cell: ({ row }) => {
        const customer = row.original;
        if (customer.is_inactive) {
          return <span className="px-1.5 py-0.5 rounded text-[10px] font-bold bg-rose-100 text-rose-700 border border-rose-200">موقف</span>;
        }
        if (customer.is_inactive_sales) {
          return <span className="px-1.5 py-0.5 rounded text-[10px] font-bold bg-orange-100 text-orange-700 border border-orange-200">البيع موقف</span>;
        }
        return <span className="text-slate-400 text-xs">-</span>;
      }
    },
    {
      accessorKey: 'phone',
      header: 'رقم الهاتف',
    },
    {
      accessorKey: 'actual_balance',
      header: 'الرصيد الفعلي',
      cell: info => {
        const val = info.getValue() as number
        return (
          <span className={`font-bold ${val > 0 ? 'text-rose-500' : 'text-emerald-500'}`} dir="ltr">
            {val.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
          </span>
        )
      }
    },
    {
      accessorKey: 'credit_limit',
      header: 'الحد الائتماني',
      cell: info => {
        const val = info.getValue() as number
        return <span dir="ltr">{val.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</span>
      }
    },
    {
      accessorKey: 'city',
      header: 'المدينة',
      cell: info => <span className="text-slate-600 font-medium">{info.getValue() as string}</span>
    },
    {
      id: 'actions',
      header: '',
      cell: ({ row }) => (
        <div className="flex items-center gap-2 relative">
          <Button
            variant="outline"
            size="sm"
            className="text-primary hover:text-white hover:bg-primary border-primary/20 hover:border-primary transition-all duration-300 w-full rounded-xl gap-2 font-bold shadow-sm hover:shadow-md hover:shadow-primary/20"
            onClick={() => setSelectedCustomer(row.original)}
          >
            <FolderOpen className="w-4 h-4" />
            الملفات والبيانات
          </Button>

          <div className="relative">
            <Button
              variant="outline"
              size="icon"
              className={`rounded-xl transition-all duration-300 w-9 h-9 flex items-center justify-center border ${row.original.phone ? 'text-[#25D366] hover:bg-[#25D366] hover:text-white border-[#25D366]/30 hover:border-[#25D366]' : 'text-slate-300 border-slate-200 cursor-not-allowed'}`}
              onClick={() => {
                if (row.original.phone) {
                  setOpenWhatsappMenuId(openWhatsappMenuId === row.original.c_code ? null : row.original.c_code)
                }
              }}
              title="مراسلة عبر واتساب"
            >
              <MessageCircle className="w-4 h-4" />
            </Button>

            {openWhatsappMenuId === row.original.c_code && row.original.phone && (
              <div className="absolute top-full left-1/2 -translate-x-1/2 mt-2 w-64 bg-white rounded-2xl shadow-xl border border-slate-100 z-[100] overflow-hidden animate-in fade-in slide-in-from-top-2" style={{ position: 'fixed', transform: 'translateX(-50%)' }} ref={(el) => {
                // Keep dropdown in viewport logic using simple fixed positioning or rely on table overflow
                if (el && el.parentElement) {
                  const rect = el.parentElement.getBoundingClientRect();
                  el.style.top = `${rect.bottom + 8}px`;
                  el.style.left = `${rect.left + rect.width / 2}px`;
                }
              }}>
                <div className="p-3 bg-slate-50 border-b border-slate-100">
                  <h4 className="text-xs font-bold text-slate-500">نماذج الرسائل السريعة</h4>
                </div>
                <div className="p-1 max-h-64 overflow-y-auto">
                  {whatsappTemplates.length > 0 ? (
                    whatsappTemplates.map(template => (
                      <button
                        key={template.id}
                        onClick={() => handleSendWhatsapp(template.message, row.original)}
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
        </div>
      )
    }
  ], [whatsappTemplates, openWhatsappMenuId])

  const table = useReactTable({
    data,
    columns,
    state: {
      sorting,
      globalFilter,
    },
    onSortingChange: setSorting,
    onGlobalFilterChange: setGlobalFilter,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
  })

  if (isLoading) {
    return <div className="flex h-full items-center justify-center text-slate-500 font-bold">جاري تحميل بيانات العملاء...</div>
  }

  return (
    <div className="flex flex-col h-full bg-slate-50/50 p-6 overflow-hidden">
      {/* Header section matching MainContent style */}
      <div className="flex flex-col mb-4">
        <h1 className="text-xl font-extrabold text-slate-800 tracking-tight flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl gradient-primary flex shrink-0 items-center justify-center shadow-lg shadow-primary/30">
            <FolderOpen className="w-5 h-5 text-white" />
          </div>
          بيانات وملفات العملاء
        </h1>
        <p className="text-sm text-slate-500 font-medium mt-1 pr-14">إدارة مستندات وعقود وهويات العملاء</p>
      </div>

      {/* Main Content Area */}
      <div className="flex-1 overflow-hidden flex flex-col print:p-0 print:overflow-visible print:block">
        <div className="soft-card flex-1 flex flex-col min-h-0 overflow-hidden print:shadow-none print:border-none">

          <div className="p-4 border-b border-slate-100 flex items-center gap-3 bg-white">
            <div className="relative flex-1 max-w-sm">
              <Search className="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
              <Input
                placeholder="بحث سريع..."
                value={globalFilter ?? ''}
                onChange={e => setGlobalFilter(e.target.value)}
                className="pr-9 font-medium text-sm h-9 bg-slate-50 border-slate-200"
              />
            </div>
            
            <label className="flex items-center gap-2 cursor-pointer bg-slate-50 px-3 py-1.5 rounded-xl border border-slate-200 hover:bg-slate-100 transition-colors">
              <span className="text-sm font-bold text-slate-700">عميل مرتبط بمورد</span>
              <div className="relative inline-block w-10 h-6">
                <input 
                  type="checkbox" 
                  className="peer sr-only"
                  checked={netSupplier}
                  onChange={(e) => setNetSupplier(e.target.checked)}
                />
                <div className="block bg-slate-200 w-10 h-6 rounded-full transition-colors peer-checked:bg-primary"></div>
                <div className="dot absolute right-1 top-1 bg-white w-4 h-4 rounded-full transition-transform peer-checked:-translate-x-4"></div>
              </div>
            </label>
          </div>

          {isLoading ? (
            <div className="flex h-full items-center justify-center">
              <div className="flex flex-col items-center gap-3">
                <div className="w-8 h-8 rounded-full border-4 border-primary/20 border-t-primary animate-spin"></div>
                <div className="text-sm font-medium text-slate-500">جاري جلب البيانات...</div>
              </div>
            </div>
          ) : (
            <div className="overflow-auto flex-1 p-4 bg-slate-50/30">
              <div className="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
                <table className="w-full text-sm text-right print:text-[10px] border-collapse text-slate-800">
                  <thead className="bg-slate-100/80 text-slate-600 sticky top-0 z-10 print:static print:bg-gray-100">
                    {table.getHeaderGroups().map(headerGroup => (
                      <tr key={headerGroup.id}>
                        {headerGroup.headers.map(header => (
                          <th
                            key={header.id}
                            className="px-6 py-4 font-extrabold whitespace-nowrap align-middle select-none print:border border-b border-slate-200 text-right text-xs uppercase tracking-wider"
                          >
                            <div
                              className="flex items-center gap-1.5 cursor-pointer hover:text-primary transition-colors"
                              onClick={header.column.getToggleSortingHandler()}
                            >
                              {header.column.getCanSort() ? (
                                {
                                  asc: ' 🔼',
                                  desc: ' 🔽',
                                }[header.column.getIsSorted() as string] ?? null
                              ) : null}
                              {flexRender(header.column.columnDef.header, header.getContext())}
                            </div>
                          </th>
                        ))}
                      </tr>
                    ))}
                  </thead>
                  <tbody className="divide-y divide-slate-100 print:divide-slate-400">
                    {table.getRowModel().rows.map(row => (
                      <tr key={row.id} className="hover:bg-slate-50/80 hover:shadow-sm group text-slate-700 font-medium transition-all duration-200 print:text-slate-800 bg-white">
                        {row.getVisibleCells().map(cell => (
                          <td key={cell.id} className="px-6 py-3 whitespace-nowrap align-middle print:whitespace-normal print:border print:border-slate-400 text-right print:px-1 print:py-0.5 group-hover:text-slate-900 transition-colors">
                            {flexRender(cell.column.columnDef.cell, cell.getContext())}
                          </td>
                        ))}
                      </tr>
                    ))}
                    {table.getRowModel().rows.length === 0 && (
                      <tr>
                        <td colSpan={columns.length} className="px-6 py-16 text-center text-slate-400 font-medium">
                          <div className="flex flex-col items-center justify-center gap-3">
                            <Search className="w-8 h-8 text-slate-300" />
                            لا يوجد عملاء مطابقين للبحث
                          </div>
                        </td>
                      </tr>
                    )}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* Pagination Controls */}
        </div>
      </div>

      {selectedCustomer && (
        <CustomerProfile
          customer={selectedCustomer}
          onClose={() => setSelectedCustomer(null)}
        />
      )}
    </div>
  )
}
