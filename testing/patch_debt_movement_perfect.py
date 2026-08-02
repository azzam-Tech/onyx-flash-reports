with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

start_pos = content.find('def run_debt_movement_summary(rpt, args):')
end_pos = content.find('def jv_options():')

new_run_debt_func = """def run_debt_movement_summary(rpt, args):
    year_val = args.get("year_val", "2026")
    period_type = args.get("period_type", "monthly")
    period_val = args.get("period_val", "all")
    grp_by = args.get("grp_by", "cc")
    
    date_from, date_to = get_date_range(year_val, period_type, period_val)
    
    if grp_by == "rep":
        grp_col = "TO_CHAR(p.REP_CODE)"
        grp_sales = "TO_CHAR(REP_CODE)"
        grp_sales_b = "TO_CHAR(b.REP_CODE)"
        grp_ret = "TO_CHAR(REP_CODE)"
        join_table = "LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = ac.grp_code"
        name_expr = "MAX(sm.REPRS_A_NAME)"
        code_label = "كود المندوب"
        name_label = "اسم المندوب"
    elif grp_by == "period":
        if period_type == "quarterly":
            grp_sales = "'Q' || TO_CHAR(BILL_DATE, 'Q')"
            grp_sales_b = "'Q' || TO_CHAR(b.BILL_DATE, 'Q')"
            grp_col = "'Q' || TO_CHAR(p.DOC_DATE, 'Q')"
            grp_ret = "'Q' || TO_CHAR(RT_BILL_DATE, 'Q')"
        elif period_type == "semi_annual":
            grp_sales = "CASE WHEN TO_CHAR(BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_sales_b = "CASE WHEN TO_CHAR(b.BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_col = "CASE WHEN TO_CHAR(p.DOC_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_ret = "CASE WHEN TO_CHAR(RT_BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
        else: # monthly or annual
            grp_sales = "TO_CHAR(BILL_DATE, 'YYYY-MM')"
            grp_sales_b = "TO_CHAR(b.BILL_DATE, 'YYYY-MM')"
            grp_col = "TO_CHAR(p.DOC_DATE, 'YYYY-MM')"
            grp_ret = "TO_CHAR(RT_BILL_DATE, 'YYYY-MM')"
        join_table = ""
        name_expr = "ac.grp_code"
        code_label = "الفترة الزمنية"
        name_label = "البيان"
    else: # default cc
        grp_col = "TO_CHAR(p.CC_CODE)"
        grp_sales = "TO_CHAR(CC_CODE)"
        grp_sales_b = "TO_CHAR(b.CC_CODE)"
        grp_ret = "TO_CHAR(CC_CODE)"
        join_table = "LEFT JOIN IAS20261.COST_CENTERS cc ON TO_CHAR(cc.CC_CODE) = ac.grp_code"
        name_expr = "MAX(cc.CC_A_NAME)"
        code_label = "رمز مركز التكلفة"
        name_label = "اسم مركز التكلفة"

    sql = f\"\"\"
    WITH open_debt AS (
        SELECT {grp_col} as grp_code,
               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as open_bal
        FROM IAS20261.IAS_POST_DTL p
        WHERE NVL(p.DOC_POST,0)=1 AND p.C_CODE IS NOT NULL
          AND (p.DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') OR NVL(p.DOC_TYPE,0) = 0)
        GROUP BY {grp_col}
    ),
    sales_base AS (
        SELECT {grp_sales} as grp_code,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as sales_with_vat,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0)) as sales_no_vat
        FROM IAS20261.IAS_BILL_MST
        WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY {grp_sales}
    ),
    returns_base AS (
        SELECT {grp_ret} as grp_code,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as returns_with_vat,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0)) as returns_no_vat
        FROM IAS20261.IAS_RT_BILL_MST
        WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY {grp_ret}
    ),
    ext_disc_base AS (
        SELECT {grp_col} as grp_code, SUM(NVL(p.CR_AMT,0)) as ext_disc_with_vat
        FROM IAS20261.IAS_POST_DTL p
        WHERE p.DOC_TYPE = 15 AND NVL(p.CR_AMT,0) > 0 AND NVL(p.DOC_POST,0) = 1
          AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY {grp_col}
    ),
    net_sales_summary AS (
        SELECT NVL(NVL(s.grp_code, r.grp_code), d.grp_code) AS grp_code,
               SUM(NVL(s.sales_with_vat, 0)) - SUM(NVL(r.returns_with_vat, 0)) - SUM(NVL(d.ext_disc_with_vat, 0)) AS net_sales_vat,
               SUM(NVL(s.sales_no_vat, 0)) - SUM(NVL(r.returns_no_vat, 0)) - SUM(ROUND(NVL(d.ext_disc_with_vat, 0)/1.15, 2)) AS net_sales_no_vat
        FROM sales_base s
        FULL OUTER JOIN returns_base r ON s.grp_code = r.grp_code
        FULL OUTER JOIN ext_disc_base d ON NVL(s.grp_code, r.grp_code) = d.grp_code
        GROUP BY NVL(NVL(s.grp_code, r.grp_code), d.grp_code)
    ),
    col_trans AS (
      SELECT {grp_col} as grp_code, p.CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as cash_ret, 0 as unposted_rcpt
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_col}, 0, 0, 0, 0, p.CR_AMT
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_col}, 0, p.CR_AMT, 0, 0, 0
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=1 AND p.JV_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_sales_b}, 0, 0, NVL(p.DR_AMT,0), 0, 0
      FROM IAS20261.IAS_BILL_MST b
      JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
      WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
        AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_col}, 0, 0, 0, p.CR_AMT, 0
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=5 AND p.A_CODE LIKE '111%' AND NVL(p.CR_AMT,0)>0
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
    ),
    col_summary AS (
      SELECT grp_code,
             SUM(rcpt + unposted_rcpt + net_jrn + cash_sales - cash_ret) as total_collection
      FROM col_trans
      GROUP BY grp_code
    ),
    all_codes AS (
      SELECT grp_code FROM open_debt
      UNION
      SELECT grp_code FROM net_sales_summary
      UNION
      SELECT grp_code FROM col_summary
    )
    SELECT ac.grp_code,
           {name_expr} as grp_name,
           NVL(SUM(o.open_bal), 0) as open_bal,
           NVL(SUM(ns.net_sales_vat), 0) as net_sales_vat,
           NVL(SUM(ns.net_sales_no_vat), 0) as net_sales_no_vat,
           NVL(SUM(cs.total_collection), 0) as total_col
    FROM all_codes ac
    LEFT JOIN open_debt o ON o.grp_code = ac.grp_code
    LEFT JOIN net_sales_summary ns ON ns.grp_code = ac.grp_code
    LEFT JOIN col_summary cs ON cs.grp_code = ac.grp_code
    {join_table}
    WHERE ac.grp_code IS NOT NULL
    GROUP BY ac.grp_code
    ORDER BY ac.grp_code
    \"\"\"

    cols = [
        code_label,
        name_label,
        "المديونية الافتتاحية",
        "صافي المبيعات شامل الضريبة",
        "إجمالي التحصيل",
        "المديونية النهائية",
        "إجمالي المبيعات بدون الضريبة",
        "الهدف"
    ]
    rows = []
    
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"date_from": date_from, "date_to": date_to})
            for c_code, c_name, open_b, ns_vat, ns_no_vat, col in cur.fetchall():
                ob_val = float(open_b or 0.0)
                ns_vat_val = float(ns_vat or 0.0)
                ns_no_vat_val = float(ns_no_vat or 0.0)
                col_val = float(col or 0.0)
                closing_val = ob_val + ns_vat_val - col_val
                
                rows.append((
                    c_code,
                    c_name or str(c_code),
                    f"{ob_val:,.2f}",
                    f"{ns_vat_val:,.2f}",
                    f"{col_val:,.2f}",
                    f"{closing_val:,.2f}",
                    f"{ns_no_vat_val:,.2f}",
                    ""
                ))
                
    return cols, rows

"""

if start_pos != -1 and end_pos != -1:
    content = content[:start_pos] + new_run_debt_func + content[end_pos:]
    with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully updated run_debt_movement_summary!")
else:
    print(f"Error finding positions: start={start_pos}, end={end_pos}")
