import { useState, useEffect, useMemo } from "react"
import { Card } from "./ui/card"
import { Button } from "./ui/button"
import { Input } from "./ui/input"
import { Filter, Download, Printer, Search } from "lucide-react"
import * as XLSX from 'xlsx'
import { cn } from "@/lib/utils"
import { ReportFilters, type ReportParam } from "./ReportFilters"
import {
  useReactTable,
  getCoreRowModel,
  flexRender,
  createColumnHelper,
  getSortedRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  type SortingState,
  type Column
} from '@tanstack/react-table'

// Helper component for column filtering
function ColumnFilter({ column, table }: { column: Column<any, unknown>, table: any }) {
  const columnFilterValue = column.getFilterValue()
  
  // Get unique values for this column to build a dropdown
  const uniqueValues = useMemo(() => {
    const values = new Set<string>()
    table.getPreFilteredRowModel().flatRows.forEach((row: any) => {
      const val = row.getValue(column.id)
      if (val !== undefined && val !== null) {
        values.add(String(val))
      }
    })
    return Array.from(values).sort()
  }, [column.id, table.getPreFilteredRowModel().flatRows])

  return (
    <select
      value={(columnFilterValue ?? '') as string}
      onChange={e => column.setFilterValue(e.target.value || undefined)}
      className="mt-2 w-full text-xs font-normal border-slate-200 rounded-md bg-white p-1 text-slate-600 focus:ring-1 focus:ring-indigo-500 outline-none print:hidden"
      onClick={e => e.stopPropagation()} // Prevent sort on filter click
    >
      <option value="">الكل</option>
      {uniqueValues.map(val => (
        <option key={val} value={val}>{val}</option>
      ))}
    </select>
  )
}

export function MainContent({ tabId, reportId, reportTitle }: { tabId: string, reportId: string, reportTitle: string }) {
  const [data, setData] = useState<{cols: string[], rows: any[][]}>({ cols: [], rows: [] })
  const [isLoading, setIsLoading] = useState(false)
  
  // Table states
  const [sorting, setSorting] = useState<SortingState>([])
  const [globalFilter, setGlobalFilter] = useState('')
  const [showFilter, setShowFilter] = useState(false)

  // Report API Parameters states
  const [reportParams, setReportParams] = useState<ReportParam[]>([])
  const [reportBinds, setReportBinds] = useState<Record<string, string>>({})
  const [currentQuery, setCurrentQuery] = useState<Record<string, string>>({})

  // Reset query when report changes
  useEffect(() => {
    setCurrentQuery({})
  }, [tabId, reportId])

  useEffect(() => {
    if (!tabId || !reportId) return
    setIsLoading(true)
    const qs = new URLSearchParams(currentQuery).toString()
    fetch(`/api/reports/${tabId}/${reportId}?${qs}`)
      .then(res => res.json())
      .then(resData => {
        if (resData.cols) {
          setData(resData)
        } else {
          setData({ cols: [], rows: [] })
        }
        setReportParams(resData.params || [])
        setReportBinds(resData.binds || {})
        setIsLoading(false)
        setSorting([])
        setGlobalFilter('')
      })
      .catch(err => {
        console.error(err)
        setIsLoading(false)
      })
  }, [tabId, reportId, currentQuery])

  const hiddenColsList = ["الخصم في الفاتورة", "إيداعات وتسويات (بدون عميل)"]

  const columns = useMemo(() => {
    return data.cols
      .map((col, index) => ({
        header: col,
        accessorFn: (row: any[]) => row[index],
        id: `col_${index}`,
        meta: { originalIndex: index }
      }))
      .filter(c => !hiddenColsList.includes(c.header))
  }, [data.cols])
  
  const totalRow = useMemo(() => data.rows.length > 0 ? data.rows[0] : null, [data.rows])
  const tableData = useMemo(() => data.rows.length > 1 ? data.rows.slice(1) : [], [data.rows])

  const table = useReactTable({
    data: tableData,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    onSortingChange: setSorting,
    onGlobalFilterChange: setGlobalFilter,
    state: {
      sorting,
      globalFilter,
    },
    initialState: {
      pagination: {
        pageSize: 100,
      },
    },
  })

  const exportToExcel = () => {
    if (data.rows.length === 0) return
    const worksheetData: any[][] = [data.cols]
    if (totalRow) worksheetData.push(totalRow)
    worksheetData.push(...table.getFilteredRowModel().rows.map(r => r.original))
    const worksheet = XLSX.utils.aoa_to_sheet(worksheetData)
    const wscols = data.cols.map(() => ({ wch: 20 }))
    worksheet['!cols'] = wscols
    
    const workbook = XLSX.utils.book_new()
    XLSX.utils.book_append_sheet(workbook, worksheet, "Report")
    
    const date = new Date().toISOString().split('T')[0]
    XLSX.writeFile(workbook, `${reportTitle}_${date}.xlsx`)
  }

  const handlePrint = () => {
    window.print()
  }

  return (
    <div className="flex-1 flex flex-col h-full bg-transparent print:bg-white print:h-auto p-4 md:p-6 gap-6">
      
      {/* Top Header Card */}
      <div className="soft-card flex flex-col sm:flex-row items-start sm:items-center justify-between p-6 gap-4 print:hidden">
        <div>
          <h2 className="text-2xl font-bold text-foreground">{reportTitle}</h2>
          <p className="text-sm text-muted-foreground mt-1">عرض وتحليل بيانات التقرير</p>
        </div>
        
        <div className="flex flex-col sm:flex-row gap-3 w-full sm:w-auto">
          {showFilter && (
            <div className="relative w-full sm:w-64">
              <Search className="absolute right-3 top-1/2 -translate-y-1/2 h-4 w-4 text-slate-400" />
              <input
                placeholder="بحث في جميع الأعمدة..."
                value={globalFilter ?? ''}
                onChange={e => setGlobalFilter(e.target.value)}
                className="w-full h-10 pr-10 pl-4 rounded-xl border-none bg-slate-100/50 focus:bg-white shadow-inner outline-none focus:ring-2 focus:ring-primary/20 transition-all text-sm"
              />
            </div>
          )}
          <div className="flex gap-2">
            <button 
              className={cn("soft-button flex items-center gap-2 px-4 py-2 text-sm font-semibold", showFilter && "text-primary ring-1 ring-primary/20")}
              onClick={() => setShowFilter(!showFilter)}
            >
              <Filter className="w-4 h-4" /> بحث سريع
            </button>
            <button 
              className="soft-button flex items-center gap-2 px-4 py-2 text-sm font-semibold text-emerald-600 hover:text-emerald-700"
              onClick={exportToExcel}
              disabled={isLoading || data.rows.length === 0}
            >
              <Download className="w-4 h-4" /> تصدير إكسل
            </button>
            <button 
              className="soft-button flex items-center gap-2 px-4 py-2 text-sm font-semibold text-slate-600"
              onClick={handlePrint}
              disabled={isLoading || data.rows.length === 0}
            >
              <Printer className="w-4 h-4" /> طباعة
            </button>
          </div>
        </div>
      </div>
      
      {/* Top Report Parameters */}
      <ReportFilters 
        params={reportParams} 
        initialBinds={reportBinds} 
        onApply={setCurrentQuery} 
      />

      {/* Print-only Header */}
      <div className="hidden print:block p-6 pb-2 text-center border-b mb-4">
         <h1 className="text-2xl font-bold">{reportTitle}</h1>
         <p className="text-slate-500 mt-2">تاريخ الطباعة: {new Date().toLocaleString('ar-SA')}</p>
      </div>

      {/* Table Area */}
      <div className="flex-1 overflow-hidden flex flex-col print:p-0 print:overflow-visible print:block">
        <div className="soft-card flex-1 flex flex-col overflow-hidden bg-white/80 backdrop-blur-xl print:shadow-none print:overflow-visible print:block">
          {isLoading ? (
            <div className="flex h-full items-center justify-center">
              <div className="flex flex-col items-center gap-3">
                <div className="w-8 h-8 rounded-full border-4 border-primary/20 border-t-primary animate-spin"></div>
                <div className="text-sm font-medium text-slate-500">جاري جلب البيانات...</div>
              </div>
            </div>
          ) : data.cols.length > 0 ? (
            <>
              <div className="overflow-auto flex-1 p-2">
                <table className="w-full text-sm text-right print:text-xs border-collapse">
                  <thead className="bg-slate-50/80 backdrop-blur-md text-slate-600 sticky top-0 z-10 print:static print:bg-gray-100 rounded-t-xl">
                    {table.getHeaderGroups().map(headerGroup => (
                      <tr key={headerGroup.id}>
                        {headerGroup.headers.map(header => (
                          <th 
                            key={header.id} 
                            className="px-4 py-2.5 font-bold whitespace-nowrap align-top select-none print:border print:border-gray-300 min-w-[140px] first:rounded-tr-xl last:rounded-tl-xl"
                          >
                            <div 
                              className="flex items-center gap-1 justify-end cursor-pointer hover:text-primary transition-colors"
                              onClick={header.column.getToggleSortingHandler()}
                            >
                              {{
                                asc: ' 🔼',
                                desc: ' 🔽',
                              }[header.column.getIsSorted() as string] ?? null}
                              {flexRender(
                                header.column.columnDef.header,
                                header.getContext()
                              )}
                            </div>
                            {/* Column Filter Dropdown */}
                            <ColumnFilter column={header.column} table={table} />
                          </th>
                        ))}
                      </tr>
                    ))}
                  </thead>
                  <tbody className="divide-y divide-slate-100/50 print:divide-gray-300">
                    {totalRow && (
                      <tr className="bg-primary/5 font-extrabold text-primary border-b-2 border-primary/10 shadow-sm relative z-0 print:bg-gray-200 print:border-b-2">
                        {columns.map((col: any) => (
                          <td key={`total_${col.id}`} className="px-4 py-2 whitespace-nowrap print:border print:border-gray-300">
                            {totalRow[col.meta.originalIndex]}
                          </td>
                        ))}
                      </tr>
                    )}
                    {table.getRowModel().rows.length > 0 ? (
                      table.getRowModel().rows.map((row) => (
                        <tr 
                          key={row.id} 
                          className="hover:bg-slate-50/50 text-slate-600 font-medium transition-colors duration-200"
                        >
                          {row.getVisibleCells().map(cell => (
                            <td key={cell.id} className="px-4 py-1.5 whitespace-nowrap print:border print:border-gray-300">
                              {flexRender(cell.column.columnDef.cell, cell.getContext())}
                            </td>
                          ))}
                        </tr>
                      ))
                    ) : (
                      <tr>
                        <td colSpan={columns.length} className="px-4 py-12 text-center text-slate-400 font-medium">
                          لا توجد نتائج مطابقة للبحث
                        </td>
                      </tr>
                    )}
                  </tbody>
                </table>
              </div>
              
              {/* Pagination Controls */}
              <div className="flex flex-col sm:flex-row items-center justify-between px-6 py-4 border-t border-slate-100/50 bg-slate-50/50 print:hidden gap-4">
                <div className="flex items-center gap-2">
                  <button
                    className="soft-button px-4 py-2 text-sm font-semibold text-slate-600 disabled:opacity-50 disabled:cursor-not-allowed hover:text-primary transition-colors"
                    onClick={() => table.previousPage()}
                    disabled={!table.getCanPreviousPage()}
                  >
                    السابق
                  </button>
                  <button
                    className="soft-button px-4 py-2 text-sm font-semibold text-slate-600 disabled:opacity-50 disabled:cursor-not-allowed hover:text-primary transition-colors"
                    onClick={() => table.nextPage()}
                    disabled={!table.getCanNextPage()}
                  >
                    التالي
                  </button>
                </div>
                <span className="flex items-center gap-2 text-sm text-slate-600 font-medium">
                  <div>صفحة</div>
                  <strong className="text-primary font-bold">
                    {table.getState().pagination.pageIndex + 1}
                  </strong>
                  <div>من {table.getPageCount()}</div>
                </span>
                <select
                  value={table.getState().pagination.pageSize}
                  onChange={e => {
                    table.setPageSize(Number(e.target.value))
                  }}
                  className="soft-button px-4 py-2 text-sm text-slate-600 font-semibold outline-none cursor-pointer hover:text-primary transition-colors appearance-none"
                >
                  {[100, 250, 500, 1000].map(pageSize => (
                    <option key={pageSize} value={pageSize}>
                      عرض {pageSize} سطر
                    </option>
                  ))}
                </select>
              </div>
            </>

          ) : (
            <div className="flex h-full items-center justify-center text-slate-400 font-medium">لا توجد بيانات للعرض في هذا التقرير</div>
          )}
        </div>
      </div>
    </div>
  )
}
