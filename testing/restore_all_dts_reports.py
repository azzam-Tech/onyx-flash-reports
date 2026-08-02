app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    content = f.read()

# Locate tab=dts section
dts_start = content.find('{"id":"dts"')
if dts_start == -1:
    print("ERROR: dts tab not found!")
    sys.exit(1)

# Locate the end of dts tab (where tab=pur starts)
pur_start = content.find('{"id":"pur"', dts_start)
if pur_start == -1:
    print("ERROR: pur tab not found!")
    sys.exit(1)

new_dts_tab = """{"id":"dts","title":"التوزيع والمناديب","icon":"M3 13l3-7h7l3 4h4v5M3 13h17M6 18a2 2 0 100-4 2 2 0 000 4zm11 0a2 2 0 100-4 2 2 0 000 4z","reports":[
        {"id":"collection_adopted","title":"التحصيل المعتمد (ديناميكي)","params":[DFROM,DTO,GRP,REP,INCR,INCN,INCC,INCRT],"sql":\"\"\"

      WITH 
      grp AS (
        SELECT 'rep' as typ, TO_CHAR(REPRS_CODE) as cd, MAX(REPRS_A_NAME) as nm FROM IAS20261.SALES_MAN GROUP BY TO_CHAR(REPRS_CODE)
        UNION ALL 
        SELECT 'cc' as typ, TO_CHAR(CC_CODE) as cd, MAX(CC_A_NAME) as nm FROM IAS20261.COST_CENTERS GROUP BY TO_CHAR(CC_CODE)
        UNION ALL
        SELECT 'cst' as typ, TO_CHAR(C_CODE) as cd, MAX(C_A_NAME) as nm FROM IAS20261.CUSTOMER GROUP BY TO_CHAR(C_CODE)
        UNION ALL
        SELECT 'cst' as typ, 'UNKNOWN' as cd, 'عميل نقدي عام' as nm FROM DUAL
      ),
      all_trans AS (
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END as grp_code,
               CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as inv_disc, 0 as cash_ret, 0 as ext_notice, 0 as rcpt_unknown, 0 as unposted_rcpt, 0 as unposted_unknown
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, 0, 0, CR_AMT, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, 0, 0, 0, CR_AMT
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, CR_AMT, 0, 0, 0, 0, 0, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(b.CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(b.C_CODE),'UNKNOWN') ELSE TO_CHAR(b.REP_CODE) END,
               0, 0, NVL(p.DR_AMT,0), NVL(b.DISC_AMT,0), 0, 0, 0, 0, 0
        FROM IAS20261.IAS_BILL_MST b
        JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
        WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
          AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, CR_AMT, 0, 0, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, CR_AMT, 0, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=15 AND NVL(CR_AMT,0)>0
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, 0, CR_AMT, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      ),
      base AS (
        SELECT grp_code,
               SUM(rcpt) rcpt, SUM(net_jrn) net_jrn, SUM(cash_sales) cash_sales, SUM(inv_disc) inv_disc, SUM(cash_ret) cash_ret, SUM(ext_notice) ext_notice, SUM(rcpt_unknown) rcpt_unknown, SUM(unposted_rcpt) unposted_rcpt, SUM(unposted_unknown) unposted_unknown,
               (CASE WHEN :inc_rcpt='1' THEN (SUM(rcpt) + SUM(unposted_rcpt) + SUM(unposted_unknown)) ELSE 0 END
              + CASE WHEN :inc_net='1'  THEN SUM(net_jrn) ELSE 0 END
              + CASE WHEN :inc_cash='1' THEN SUM(cash_sales) ELSE 0 END
              - CASE WHEN :inc_ret='1'  THEN SUM(cash_ret) ELSE 0 END
              ) total_inc
        FROM all_trans
        WHERE grp_code IS NOT NULL
          AND (:rep_code IS NULL OR (:grp_by = 'rep' AND grp_code = :rep_code))
        GROUP BY grp_code
      )
      SELECT * FROM (
        SELECT b.grp_code AS "الكود", NVL(MAX(g.nm), b.grp_code) AS "الجهة / الاسم",
               TO_CHAR(MAX(b.rcpt),'FM999,999,990.00')      AS "سندات القبض",
               TO_CHAR(MAX(b.unposted_rcpt),'FM999,999,990.00') AS "سندات غير مرحلة",
               TO_CHAR(MAX(b.unposted_unknown),'FM999,999,990.00') AS "غير مرحلة (بدون عميل)",
               TO_CHAR(MAX(b.rcpt_unknown),'FM999,999,990.00') AS "إيداعات وتسويات (بدون عميل)",
               TO_CHAR(MAX(b.net_jrn),'FM999,999,990.00')   AS "قيود الشبكة المنفصلة",
               TO_CHAR(MAX(b.cash_sales),'FM999,999,990.00') AS "المبيعات النقدية",
               TO_CHAR(MAX(b.inv_disc),'FM999,999,990.00')   AS "الخصم في الفاتورة",
               TO_CHAR(MAX(b.ext_notice),'FM999,999,990.00') AS "إشعار خصم مستقل (-)",
               TO_CHAR(MAX(b.cash_ret),'FM999,999,990.00')   AS "المرتجع النقدي (-)",
               TO_CHAR(MAX(b.total_inc),'FM999,999,990.00') AS "إجمالي التحصيل"
        FROM base b
        LEFT JOIN grp g ON g.cd = b.grp_code AND g.typ = :grp_by
        WHERE (b.rcpt > 0 OR b.net_jrn > 0 OR b.cash_sales > 0 OR b.cash_ret > 0 OR b.inv_disc > 0 OR b.ext_notice > 0 OR b.rcpt_unknown > 0 OR b.unposted_rcpt > 0 OR b.unposted_unknown > 0)
        GROUP BY b.grp_code
        ORDER BY MAX(b.total_inc) DESC
      ) WHERE ROWNUM <= 300
\"\"\"},
        {"id":"perf_aging_dynamic_analytical","title":"أعمار التحصيل الصافي (تحليلي)","fn":"run_perf_aging_fifo","params":[DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":\"\"\"
       -- This report dynamically processes valid collections via Python FIFO per customer
       SELECT 'Dynamic Analytical' as "Placeholder" FROM DUAL
       \"\"\"},
        {"id":"perf_aging_dynamic","title":"أعمار التحصيل الصافي (ديناميكي)","fn":"run_perf_aging_fifo","params":[DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":\"\"\"
       -- This report dynamically processes valid collections via Python FIFO
       SELECT 'Dynamic' as "Placeholder" FROM DUAL
       \"\"\"},
        {"id":"perf_aging_exact","title":"أعمار التحصيل (مطابق أونكس 100%)","params":[DFROM,DTO,REP],"sql":\"\"\"
      WITH cr AS (
        SELECT C_CODE,
          SUM(CASE WHEN PER_NO BETWEEN 0 AND 30   THEN DR_AMT ELSE 0 END) pos,
          SUM(CASE WHEN PER_NO BETWEEN -30 AND -1 THEN DR_AMT ELSE 0 END) neg,
          SUM(CASE WHEN PER_NO BETWEEN 31 AND 60  THEN DR_AMT ELSE 0 END) b2,
          SUM(CASE WHEN PER_NO BETWEEN 61 AND 90  THEN DR_AMT ELSE 0 END) b3,
          SUM(CASE WHEN PER_NO BETWEEN 91 AND 120 THEN DR_AMT ELSE 0 END) b4,
          SUM(CASE WHEN PER_NO > 120              THEN DR_AMT ELSE 0 END) b5,
          SUM(DR_AMT) crlim
        FROM IAS20261.IAS_CRLIMIT_TMP
        WHERE DOC_TYPE<>1 AND DOC_TYPE_REF IN (1,2)
          AND PAID_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND PAID_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY C_CODE),
      co AS (
        SELECT C_CODE, SUM(CR_AMT) col FROM IAS20261.IAS_COL_TMP
        WHERE DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY C_CODE),
      perc AS (
        SELECT cr.C_CODE,
          CASE WHEN cr.pos > 0 THEN cr.pos + cr.neg + GREATEST(0, NVL(co.col,0) - cr.crlim) ELSE 0 END b1,
          cr.b2, cr.b3, cr.b4, cr.b5
        FROM cr LEFT JOIN co ON co.C_CODE = cr.C_CODE)
      SELECT * FROM (
        SELECT c.REP_CODE AS "كود المندوب", MAX(sm.REPRS_A_NAME) AS "اسم المندوب",
               COUNT(DISTINCT perc.C_CODE) AS "عدد العملاء",
               TO_CHAR(SUM(perc.b1),'FM999,999,990.00') AS "0-30",
               TO_CHAR(SUM(perc.b2),'FM999,999,990.00') AS "31-60",
               TO_CHAR(SUM(perc.b3),'FM999,999,990.00') AS "61-90",
               TO_CHAR(SUM(perc.b4),'FM999,999,990.00') AS "91-120",
               TO_CHAR(SUM(perc.b5),'FM999,999,990.00') AS "أكثر من 120",
               TO_CHAR(SUM(perc.b1+perc.b2+perc.b3+perc.b4+perc.b5),'FM999,999,990.00') AS "إجمالي التحصيل"
        FROM perc JOIN IAS20261.CUSTOMER c ON c.C_CODE=perc.C_CODE
        LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=c.REP_CODE
        WHERE (:rep_code IS NULL OR c.REP_CODE = :rep_code)
        GROUP BY c.REP_CODE ORDER BY SUM(perc.b1+perc.b2+perc.b3+perc.b4+perc.b5) DESC
      ) WHERE ROWNUM <= 300
\"\"\"}
  ]},
  """

content = content[:dts_start] + new_dts_tab + content[pur_start:]

with open(app_path, "w", encoding="utf-8") as f:
    f.write(content)

print("RESTORED ALL 4 REPORTS IN TAB=DTS SUCCESSFULLY!")
