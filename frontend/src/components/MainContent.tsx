import { useState, useEffect, useMemo } from "react"
import { Card } from "./ui/card"
import { Button } from "./ui/button"
import { Input } from "./ui/input"
import { Filter, Download, Printer, Search, Check, ChevronsUpDown } from "lucide-react"
import * as XLSX from 'xlsx'
import { cn } from "@/lib/utils"
import { Popover, PopoverContent, PopoverTrigger } from "./ui/popover"
import { Command, CommandEmpty, CommandGroup, CommandInput, CommandItem, CommandList } from "./ui/command"
import { ReportFilters, type ReportParam } from "./ReportFilters"
import {
  useReactTable,
  getCoreRowModel,
  flexRender,
  createColumnHelper,
  getSortedRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getFacetedRowModel,
  getFacetedUniqueValues,
  type SortingState,
  type Column
} from '@tanstack/react-table'

// Helper component for column filtering
function ColumnFilter({ column, table }: { column: Column<any, unknown>, table: any }) {
  const columnFilterValue = column.getFilterValue() as string | undefined
  const [open, setOpen] = useState(false)
  
  // Get unique values for this column based on the faceted rows (respects other filters)
  const uniqueValues = useMemo(() => {
    const facetedMap = column.getFacetedUniqueValues()
    const values = new Set<string>()
    facetedMap.forEach((_, val) => {
      if (val !== undefined && val !== null) {
        values.add(String(val))
      }
    })
    return Array.from(values).sort()
  }, [column.getFacetedUniqueValues()])

  return (
    <Popover open={open} onOpenChange={setOpen}>
      <PopoverTrigger asChild>
        <button
          onClick={e => e.stopPropagation()} // Prevent sort on filter click
          className="mt-2 w-full flex items-center justify-between text-xs font-normal border border-slate-200 rounded-md bg-white px-2 py-1.5 text-slate-600 focus:ring-1 focus:ring-primary outline-none print:hidden hover:bg-slate-50 transition-colors"
        >
          <span className="truncate w-[85%] text-right">{columnFilterValue || 'الكل'}</span>
          <ChevronsUpDown className="ml-1 h-3 w-3 shrink-0 opacity-50" />
        </button>
      </PopoverTrigger>
      <PopoverContent className="w-[var(--radix-popover-trigger-width)] p-0 shadow-lg border-slate-200" align="start">
        <Command className="bg-white text-slate-700">
          <CommandInput placeholder="بحث..." className="h-9 outline-none border-none focus:ring-0 text-sm text-right bg-white" />
          <CommandList className="max-h-[220px] overflow-y-auto custom-scrollbar bg-white">
            <CommandEmpty className="py-4 text-center text-sm text-slate-500">لم يتم العثور على نتيجة.</CommandEmpty>
            <CommandGroup>
              <CommandItem
                value="الكل"
                onSelect={() => {
                  column.setFilterValue(undefined)
                  setOpen(false)
                }}
                className="text-right flex items-center justify-between cursor-pointer hover:bg-slate-100/50 py-1.5 aria-selected:bg-slate-100/50"
              >
                <span>الكل</span>
                {(!columnFilterValue) && (
                  <Check className="mr-2 h-3 w-3 text-primary" />
                )}
              </CommandItem>
              {uniqueValues.map(val => (
                <CommandItem
                  key={val}
                  value={val}
                  onSelect={() => {
                    column.setFilterValue(val === columnFilterValue ? undefined : val)
                    setOpen(false)
                  }}
                  className="text-right flex items-center justify-between cursor-pointer hover:bg-slate-100/50 py-1.5 aria-selected:bg-slate-100/50"
                >
                  <span className="truncate">{val}</span>
                  {columnFilterValue === val && (
                    <Check className="mr-2 h-3 w-3 text-primary" />
                  )}
                </CommandItem>
              ))}
            </CommandGroup>
          </CommandList>
        </Command>
      </PopoverContent>
    </Popover>
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
    const rawCols = data.cols

    if (data.metadata?.pivot_type === 'detailed_stock' && rawCols.length >= 22) {
      const groups = [
        { header: 'معلومات الصنف', colspan: 6 },
        { header: 'الرصيد الافتتاحي', colspan: 7 },
        { header: 'الحركة (صادر / وارد)', colspan: 2 },
        { header: 'الرصيد النهائي', colspan: 7 },
      ]
      
      let colIdx = 0
      const finalCols = []
      
      for (const group of groups) {
        const groupCols = []
        for (let i = 0; i < group.colspan; i++) {
          if (colIdx >= rawCols.length) break
          const rawCol = rawCols[colIdx]
          if (hiddenColsList.includes(rawCol)) { colIdx++; continue; }
          const cleanCol = rawCol.replace('افتتاحي ', '').replace('نهائي ', '').replace('صادر (مبيعات/تحويل)', 'صادر').replace('وارد (مشتريات/استرجاع)', 'وارد')
          const currentIndex = colIdx;
          groupCols.push({
            header: cleanCol,
            accessorFn: (row: any[]) => row[currentIndex],
            id: `col_${currentIndex}`,
            meta: { originalIndex: currentIndex }
          })
          colIdx++
        }
        if (groupCols.length > 0) {
          finalCols.push({ header: group.header, columns: groupCols, id: `group_${colIdx}` })
        }
      }
      return finalCols
    }

    if (data.metadata?.pivot_type === 'monthly_movement' && rawCols.length > 6) {
      const finalCols = []
      const itemInfoCols = []
      for (let i = 0; i < 6; i++) {
        if (i < rawCols.length && !hiddenColsList.includes(rawCols[i])) {
          itemInfoCols.push({
            header: rawCols[i],
            accessorFn: (row: any[]) => row[i],
            id: `col_${i}`,
            meta: { originalIndex: i }
          })
        }
      }
      if (itemInfoCols.length > 0) {
        finalCols.push({ header: 'معلومات الصنف', columns: itemInfoCols, id: 'group_items' })
      }
      
      const months = ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"]
      let monthIdx = 0
      
      for (let i = 6; i < rawCols.length; i += 2) {
        const monthGroup = []
        for (let j = 0; j < 2; j++) {
          const cIdx = i + j
          if (cIdx < rawCols.length && !hiddenColsList.includes(rawCols[cIdx])) {
             const cleanCol = rawCols[cIdx].replace(/يناير |فبراير |مارس |أبريل |مايو |يونيو |يوليو |أغسطس |سبتمبر |أكتوبر |نوفمبر |ديسمبر /g, '').replace(/\s*ش\d+/g, '').trim()
             monthGroup.push({
               header: cleanCol,
               accessorFn: (row: any[]) => row[cIdx],
               id: `col_${cIdx}`,
               meta: { originalIndex: cIdx, monthIdx }
             })
          }
        }
        if (monthGroup.length > 0) {
           finalCols.push({ header: months[monthIdx] || `شهر ${monthIdx+1}`, columns: monthGroup, id: `group_m_${monthIdx}`, meta: { isMonth: true, monthIdx } })
           monthIdx++
        }
      }
      return finalCols
    }

    // Default flat columns
    return (rawCols || [])
      .map((col: string, index: number) => ({
        header: col,
        accessorFn: (row: any[]) => row[index],
        id: `col_${index}`,
        meta: { originalIndex: index }
      }))
      .filter(c => !hiddenColsList.includes(c.header))
  }, [data.cols, reportId, data.metadata?.pivot_type])
  
  const totalRow = useMemo(() => data.rows.length > 0 ? data.rows[0] : null, [data.rows])
  const tableData = useMemo(() => data.rows.length > 1 ? data.rows.slice(1) : [], [data.rows])

  const table = useReactTable({
    data: tableData,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getFacetedRowModel: getFacetedRowModel(),
    getFacetedUniqueValues: getFacetedUniqueValues(),
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
    worksheet['!views'] = [{ rightToLeft: true }]
    
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
      
      {/* Top Report Parameters */}
      <ReportFilters 
        params={reportParams} 
        initialBinds={reportBinds} 
        onApply={setCurrentQuery} 
      >
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
        <div className="flex flex-wrap items-center gap-2">
          <button 
            className={cn("flex items-center gap-2 px-4 py-2 text-[13px] font-bold rounded-xl transition-all duration-300", showFilter ? "bg-primary text-white shadow-md shadow-primary/20" : "bg-white text-slate-600 border border-slate-200 hover:bg-slate-50 hover:border-primary/30")}
            onClick={() => setShowFilter(!showFilter)}
          >
            <Filter className="w-4 h-4" /> بحث سريع
          </button>
          <button 
            className="flex items-center gap-2 px-4 py-2 text-[13px] font-bold rounded-xl bg-emerald-50 text-emerald-600 border border-emerald-200 hover:bg-emerald-500 hover:text-white hover:shadow-md hover:shadow-emerald-500/20 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
            onClick={exportToExcel}
            disabled={isLoading || data.rows.length === 0}
          >
            <Download className="w-4 h-4" /> تصدير إكسل
          </button>
          <button 
            className="flex items-center gap-2 px-4 py-2 text-[13px] font-bold rounded-xl bg-white text-slate-600 border border-slate-200 hover:bg-slate-800 hover:text-white hover:shadow-md transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
            onClick={handlePrint}
            disabled={isLoading || data.rows.length === 0}
          >
            <Printer className="w-4 h-4" /> طباعة
          </button>
        </div>
      </ReportFilters>

      {/* Print-only Header */}
      <div className="hidden print:flex flex-col items-center justify-center mb-4 border-b border-slate-800 pb-2">
         <h1 className="text-xl font-extrabold text-slate-900">{reportTitle}</h1>
         <p className="text-xs text-slate-600 font-bold mt-1">تاريخ الطباعة: {new Date().toLocaleString('ar-SA')}</p>
      </div>

      {/* Table Area */}
      <div className="flex-1 overflow-hidden flex flex-col print:p-0 print:overflow-visible print:block">
        <div className="soft-card flex-1 flex flex-col min-h-0 overflow-hidden print:shadow-none print:border-none">
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
                <table className="w-full text-sm text-right print:text-[10px] border-collapse text-black">
                  <thead className="bg-slate-50/80 backdrop-blur-md text-black sticky top-0 z-10 print:static print:bg-gray-100 rounded-t-xl">
                    {table.getHeaderGroups().map(headerGroup => (
                      <tr key={headerGroup.id}>
                        {headerGroup.headers.map(header => {
                          const mIdx = (header.column.columnDef.meta as any)?.monthIdx;
                          const monthColors = [
                            'text-blue-700 bg-blue-50/80 border-b-blue-200', 'text-emerald-700 bg-emerald-50/80 border-b-emerald-200', 
                            'text-violet-700 bg-violet-50/80 border-b-violet-200', 'text-amber-700 bg-amber-50/80 border-b-amber-200',
                            'text-rose-700 bg-rose-50/80 border-b-rose-200', 'text-cyan-700 bg-cyan-50/80 border-b-cyan-200',
                            'text-fuchsia-700 bg-fuchsia-50/80 border-b-fuchsia-200', 'text-orange-700 bg-orange-50/80 border-b-orange-200',
                            'text-teal-700 bg-teal-50/80 border-b-teal-200', 'text-indigo-700 bg-indigo-50/80 border-b-indigo-200',
                            'text-pink-700 bg-pink-50/80 border-b-pink-200', 'text-lime-700 bg-lime-50/80 border-b-lime-200'
                          ];
                          const mColorClass = mIdx !== undefined ? monthColors[mIdx % monthColors.length] : '';

                          return (
                          <th 
                            key={header.id} 
                            colSpan={header.colSpan}
                            className={cn(
                              "px-4 py-2.5 font-bold whitespace-nowrap align-top select-none print:border print:border-slate-400 print:border-b-2 print:border-b-slate-800 min-w-[140px] print:min-w-0 first:rounded-tr-xl last:rounded-tl-xl border-b border-slate-200 text-right print:bg-slate-100 print:text-slate-800 print:text-[9px] print:px-1 print:py-1 print:whitespace-normal",
                              header.colSpan > 1 ? "text-center print:text-center" : "",
                              mColorClass ? mColorClass : (header.colSpan > 1 ? "bg-slate-100/80" : "")
                            )}
                          >
                            {header.isPlaceholder ? null : (
                              <>
                                <div 
                                  className={cn("flex items-center gap-1 cursor-pointer hover:opacity-80 transition-colors", header.colSpan > 1 ? "justify-center" : "justify-start")}
                                  onClick={header.column.getCanSort() ? header.column.getToggleSortingHandler() : undefined}
                                >
                                  {header.column.getCanSort() ? (
                                    {
                                      asc: ' 🔼',
                                      desc: ' 🔽',
                                    }[header.column.getIsSorted() as string] ?? null
                                  ) : null}
                                  {flexRender(
                                    header.column.columnDef.header,
                                    header.getContext()
                                  )}
                                </div>
                                {/* Column Filter Dropdown only on lowest level columns */}
                                {header.subHeaders.length === 0 && (
                                  <ColumnFilter column={header.column} table={table} />
                                )}
                              </>
                            )}
                          </th>
                        )})}
                      </tr>
                    ))}
                  </thead>
                  <tbody className="divide-y divide-slate-100/50 print:divide-slate-400 text-black">
                    {totalRow && (
                      <tr className="bg-primary/5 font-extrabold text-primary border-b-2 border-primary/10 shadow-sm relative z-0 print:bg-slate-200 print:border-b-2 print:border-b-slate-800 print:text-slate-900 print:shadow-none">
                        {table.getVisibleLeafColumns().map((col) => {
                          const originalIndex = (col.columnDef.meta as any)?.originalIndex;
                          return (
                            <td key={`total_${col.id}`} className="px-4 py-2 whitespace-nowrap print:whitespace-normal print:border print:border-slate-400 text-right print:px-1 print:py-0.5">
                              {originalIndex !== undefined ? totalRow[originalIndex] : null}
                            </td>
                          );
                        })}
                      </tr>
                    )}
                    {table.getRowModel().rows.length > 0 ? (
                      table.getRowModel().rows.map((row) => (
                        <tr 
                          key={row.id} 
                          className="hover:bg-slate-50/50 text-black font-medium transition-colors duration-200 print:text-slate-800"
                        >
                          {row.getVisibleCells().map(cell => (
                            <td key={cell.id} className="px-4 py-1.5 whitespace-nowrap print:whitespace-normal print:border print:border-slate-400 text-right print:px-1 print:py-0.5">
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
              <div className="flex flex-col sm:flex-row items-center justify-between px-4 py-2 border-t border-slate-100/50 bg-slate-50/50 print:hidden gap-3">
                <div className="flex items-center gap-1.5">
                  <button
                    className="soft-button px-3 py-1.5 text-[12px] font-bold text-slate-600 disabled:opacity-50 disabled:cursor-not-allowed hover:text-primary transition-colors rounded-lg"
                    onClick={() => table.previousPage()}
                    disabled={!table.getCanPreviousPage()}
                  >
                    السابق
                  </button>
                  <button
                    className="soft-button px-3 py-1.5 text-[12px] font-bold text-slate-600 disabled:opacity-50 disabled:cursor-not-allowed hover:text-primary transition-colors rounded-lg"
                    onClick={() => table.nextPage()}
                    disabled={!table.getCanNextPage()}
                  >
                    التالي
                  </button>
                </div>
                <span className="flex items-center gap-1.5 text-[12px] text-slate-600 font-bold">
                  <div>صفحة</div>
                  <strong className="text-primary bg-white px-2 py-0.5 rounded shadow-sm border border-slate-200">
                    {table.getState().pagination.pageIndex + 1}
                  </strong>
                  <div>من {table.getPageCount()}</div>
                </span>
                <select
                  value={table.getState().pagination.pageSize === 1000000 ? 1000000 : table.getState().pagination.pageSize}
                  onChange={e => {
                    table.setPageSize(Number(e.target.value))
                  }}
                  className="soft-button px-3 py-1.5 text-[12px] text-slate-600 font-bold outline-none cursor-pointer hover:text-primary transition-colors appearance-none rounded-lg bg-white"
                >
                  {[100, 250, 500, 1000, 1000000].map(pageSize => (
                    <option key={pageSize} value={pageSize}>
                      {pageSize === 1000000 ? 'عرض الكل' : `عرض ${pageSize} سطر`}
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
