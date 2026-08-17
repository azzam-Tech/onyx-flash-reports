# -*- coding: utf-8 -*-
from database import get_conn
from . import repository
from report_handlers import run_sql_report, get_date_range
from reports_config import get_target_amount

def run_sales_collection_summary(rpt, args):
    year_val = args.get('year_val', '2026')
    period_type = args.get('period_type', 'monthly')
    period_val = args.get('period_val', 'all')
    grp_by = args.get('grp_by', 'cc')
    date_from, date_to = get_date_range(year_val, period_type, period_val)
    rep_filter = ''
    rep_filter = ''
    if grp_by == 'rep':
        grp_sales = 'TO_CHAR(REP_CODE)'
        grp_sales_b = 'TO_CHAR(b.REP_CODE)'
        grp_col = 'TO_CHAR(REP_CODE)'
        grp_ret = 'TO_CHAR(REP_CODE)'
        join_table = 'LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = NVL(ns.grp_code, cs.grp_code)'
        name_expr = 'MAX(sm.REPRS_A_NAME)'
        code_label = 'كود المندوب'
        name_label = 'اسم المندوب'
    elif grp_by == 'customer':
        grp_sales = 'TO_CHAR(C_CODE)'
        grp_sales_b = 'TO_CHAR(b.C_CODE)'
        grp_col = 'TO_CHAR(C_CODE)'
        grp_ret = 'TO_CHAR(C_CODE)'
        join_table = 'LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = NVL(ns.grp_code, cs.grp_code)'
        name_expr = 'MAX(c.C_A_NAME)'
        code_label = 'كود العميل'
        name_label = 'اسم العميل'
        rep_filter = 'AND (:rep_code IS NULL OR TO_CHAR(c.REP_CODE) = :rep_code)'
    elif grp_by == 'customer':
        grp_sales = 'TO_CHAR(C_CODE)'
        grp_sales_b = 'TO_CHAR(b.C_CODE)'
        grp_col = 'TO_CHAR(C_CODE)'
        grp_ret = 'TO_CHAR(C_CODE)'
        join_table = 'LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = NVL(ns.grp_code, cs.grp_code)'
        name_expr = 'MAX(c.C_A_NAME)'
        code_label = 'كود العميل'
        name_label = 'اسم العميل'
        rep_filter = 'AND (:rep_code IS NULL OR TO_CHAR(c.REP_CODE) = :rep_code)'
    elif grp_by == 'period':
        if period_type == 'quarterly':
            grp_sales = "'Q' || TO_CHAR(BILL_DATE, 'Q')"
            grp_sales_b = "'Q' || TO_CHAR(b.BILL_DATE, 'Q')"
            grp_col = "'Q' || TO_CHAR(DOC_DATE, 'Q')"
            grp_ret = "'Q' || TO_CHAR(RT_BILL_DATE, 'Q')"
        elif period_type == 'semi_annual':
            grp_sales = "CASE WHEN TO_CHAR(BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_sales_b = "CASE WHEN TO_CHAR(b.BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_col = "CASE WHEN TO_CHAR(DOC_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_ret = "CASE WHEN TO_CHAR(RT_BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
        else:
            grp_sales = "TO_CHAR(BILL_DATE, 'YYYY-MM')"
            grp_sales_b = "TO_CHAR(b.BILL_DATE, 'YYYY-MM')"
            grp_col = "TO_CHAR(DOC_DATE, 'YYYY-MM')"
            grp_ret = "TO_CHAR(RT_BILL_DATE, 'YYYY-MM')"
        join_table = ''
        name_expr = 'NVL(ns.grp_code, cs.grp_code)'
        code_label = 'الفترة الزمنية'
        name_label = 'البيان'
    else:
        grp_sales = 'TO_CHAR(CC_CODE)'
        grp_sales_b = 'TO_CHAR(b.CC_CODE)'
        grp_col = 'TO_CHAR(CC_CODE)'
        grp_ret = 'TO_CHAR(CC_CODE)'
        join_table = 'LEFT JOIN IAS20261.COST_CENTERS cc ON TO_CHAR(cc.CC_CODE) = NVL(ns.grp_code, cs.grp_code)'
        name_expr = 'MAX(cc.CC_A_NAME)'
        code_label = 'رمز مركز التكلفة'
        name_label = 'اسم مركز التكلفة'
    sql = f"\n    WITH sales_base AS (\n        SELECT {grp_sales} as grp_code,\n               SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as sales\n        FROM IAS20261.IAS_BILL_MST\n        WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') \n          AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n          AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)\n        GROUP BY {grp_sales}\n    ),\n    returns_base AS (\n        SELECT {grp_ret} as grp_code,\n               SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as returns\n        FROM IAS20261.IAS_RT_BILL_MST\n        WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') \n          AND RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n          AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)\n        GROUP BY {grp_ret}\n    ),\n    ext_disc_base AS (\n        SELECT {grp_col} as grp_code, ROUND(SUM(NVL(CR_AMT,0)) / 1.15, 2) as ext_disc\n        FROM IAS20261.IAS_POST_DTL\n        WHERE DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1\n          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') \n          AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n        GROUP BY {grp_col}\n    ),\n    net_sales_summary AS (\n        SELECT NVL(NVL(s.grp_code, r.grp_code), d.grp_code) AS grp_code,\n               SUM(NVL(s.sales, 0)) - SUM(NVL(r.returns, 0)) - SUM(NVL(d.ext_disc, 0)) AS net_sales\n        FROM sales_base s\n        FULL OUTER JOIN returns_base r ON s.grp_code = r.grp_code\n        FULL OUTER JOIN ext_disc_base d ON NVL(s.grp_code, r.grp_code) = d.grp_code\n        GROUP BY NVL(NVL(s.grp_code, r.grp_code), d.grp_code)\n    ),\n    col_trans AS (\n      -- Posted receipts with customer\n      SELECT {grp_col} as grp_code, CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as cash_ret, 0 as unposted_rcpt\n      FROM IAS20261.IAS_POST_DTL\n      WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL\n        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n      UNION ALL\n      -- Unposted receipts with customer\n      SELECT {grp_col}, 0, 0, 0, 0, CR_AMT\n      FROM IAS20261.IAS_POST_DTL\n      WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL\n        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n      UNION ALL\n      -- Network journals with customer\n      SELECT {grp_col}, 0, CR_AMT, 0, 0, 0\n      FROM IAS20261.IAS_POST_DTL\n      WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL\n        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n      UNION ALL\n      -- Cash Sales (posted DOC_TYPE=4)\n      SELECT {grp_sales_b}, 0, 0, NVL(p.DR_AMT,0), 0, 0\n      FROM IAS20261.IAS_BILL_MST b\n      JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'\n      WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0\n        AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n      UNION ALL\n      -- Cash Returns (posted DOC_TYPE=5)\n      SELECT {grp_col}, 0, 0, 0, CR_AMT, 0\n      FROM IAS20261.IAS_POST_DTL\n      WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0\n        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n    ),\n    col_summary AS (\n      SELECT grp_code,\n             SUM(rcpt + unposted_rcpt + net_jrn + cash_sales - cash_ret) as total_collection\n      FROM col_trans\n      GROUP BY grp_code\n    )\n    SELECT NVL(ns.grp_code, cs.grp_code) AS item_code,\n           {name_expr} AS item_name,\n           NVL(SUM(ns.net_sales), 0) AS net_sales,\n           NVL(SUM(cs.total_collection), 0) AS total_col\n    FROM net_sales_summary ns\n    FULL OUTER JOIN col_summary cs ON ns.grp_code = cs.grp_code\n    {join_table}\n    WHERE NVL(ns.grp_code, cs.grp_code) IS NOT NULL\n    GROUP BY NVL(ns.grp_code, cs.grp_code)\n    HAVING NVL(SUM(ns.net_sales), 0) <> 0 OR NVL(SUM(cs.total_collection), 0) <> 0\n    ORDER BY NVL(ns.grp_code, cs.grp_code)\n    "
    cols = [code_label, name_label, 'صافي المبيعات', 'المبيعات شامل الضريبة', 'إجمالي التحصيل', 'الفرق (المبيعات - التحصيل)', 'نسبة التحصيل', 'الهدف']
    rows = []
    with get_conn() as con:
        with con.cursor() as cur:
            params = {'date_from': date_from, 'date_to': date_to}
            if ':rep_code' in sql:
                params['rep_code'] = rep_code
            cur.execute(sql, params)
            for c_code, c_name, ns, col in cur.fetchall():
                ns_val = float(ns or 0.0)
                ns_vat_val = ns_val * 1.15
                col_val = float(col or 0.0)
                diff = ns_val - col_val
                ratio_str = f'{col_val / ns_val * 100:.1f}%' if ns_val > 0 else '0.0%'
                target_val = get_target_amount(year_val, period_type, period_val, grp_by, c_code)
                target_str = f'{target_val:,.2f}' if target_val > 0 else ''
                rows.append((c_code, c_name or str(c_code), f'{ns_val:,.2f}', f'{ns_vat_val:,.2f}', f'{col_val:,.2f}', f'{diff:,.2f}', ratio_str, target_str))
    return (cols, rows)

def run_debt_movement_summary(rpt, args):
    year_val = args.get('year_val', '2026')
    period_type = args.get('period_type', 'monthly')
    period_val = args.get('period_val', 'all')
    grp_by = args.get('grp_by', 'cc')
    rep_code = args.get('rep_code', '')
    if not rep_code:
        rep_code = None
    date_from, date_to = get_date_range(year_val, period_type, period_val)
    rep_filter = ''
    rep_filter = ''
    if grp_by == 'rep':
        grp_col = 'TO_CHAR(p.REP_CODE)'
        grp_col_debt = 'TO_CHAR(p.REP_CODE)'
        grp_sales = 'TO_CHAR(REP_CODE)'
        grp_sales_b = 'TO_CHAR(b.REP_CODE)'
        grp_ret = 'TO_CHAR(REP_CODE)'
        join_table = 'LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = ac.grp_code'
        name_expr = 'MAX(sm.REPRS_A_NAME)'
        code_label = 'كود المندوب'
        name_label = 'اسم المندوب'
    elif grp_by == 'customer':
        grp_col = 'TO_CHAR(p.C_CODE)'
        grp_col_debt = 'TO_CHAR(NVL(p.C_CODE, p.C_V_CODE))'
        grp_sales = 'TO_CHAR(C_CODE)'
        grp_sales_b = 'TO_CHAR(p.C_CODE)'
        grp_ret = 'TO_CHAR(C_CODE)'
        join_table = 'LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = ac.grp_code'
        name_expr = 'MAX(c.C_A_NAME)'
        code_label = 'كود العميل'
        name_label = 'اسم العميل'
        rep_filter = 'AND (:rep_code IS NULL OR TO_CHAR(c.REP_CODE) = :rep_code)'
    elif grp_by == 'period':
        if period_type == 'quarterly':
            grp_sales = "'Q' || TO_CHAR(BILL_DATE, 'Q')"
            grp_sales_b = "'Q' || TO_CHAR(b.BILL_DATE, 'Q')"
            grp_col = "'Q' || TO_CHAR(p.DOC_DATE, 'Q')"
            grp_ret = "'Q' || TO_CHAR(RT_BILL_DATE, 'Q')"
        elif period_type == 'semi_annual':
            grp_sales = "CASE WHEN TO_CHAR(BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_sales_b = "CASE WHEN TO_CHAR(b.BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_col = "CASE WHEN TO_CHAR(p.DOC_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_ret = "CASE WHEN TO_CHAR(RT_BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
        else:
            grp_sales = "TO_CHAR(BILL_DATE, 'YYYY-MM')"
            grp_sales_b = "TO_CHAR(b.BILL_DATE, 'YYYY-MM')"
            grp_col = "TO_CHAR(p.DOC_DATE, 'YYYY-MM')"
            grp_ret = "TO_CHAR(RT_BILL_DATE, 'YYYY-MM')"
        join_table = ''
        name_expr = 'ac.grp_code'
        code_label = 'الفترة الزمنية'
        name_label = 'البيان'
        grp_col_debt = grp_col
    else:
        grp_col = 'TO_CHAR(p.CC_CODE)'
        grp_col_debt = grp_col
        grp_sales = 'TO_CHAR(CC_CODE)'
        grp_sales_b = 'TO_CHAR(b.CC_CODE)'
        grp_ret = 'TO_CHAR(CC_CODE)'
        join_table = 'LEFT JOIN IAS20261.COST_CENTERS cc ON TO_CHAR(cc.CC_CODE) = ac.grp_code'
        name_expr = 'MAX(cc.CC_A_NAME)'
        code_label = 'رمز مركز التكلفة'
        name_label = 'اسم مركز التكلفة'
    sql = f"\n    WITH open_debt AS (\n        SELECT {grp_col_debt} as grp_code,\n               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as open_bal\n        FROM IAS20261.IAS_POST_DTL p\n        WHERE NVL(p.DOC_POST,0)=1 AND (p.C_CODE IS NOT NULL OR p.C_V_CODE IS NOT NULL)\n          AND (p.DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') OR NVL(p.DOC_TYPE,0) = 0)\n        GROUP BY {grp_col_debt}\n    ),\n    close_debt AS (\n        SELECT {grp_col_debt} as grp_code,\n               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as close_bal\n        FROM IAS20261.IAS_POST_DTL p\n        WHERE NVL(p.DOC_POST,0)=1 AND (p.C_CODE IS NOT NULL OR p.C_V_CODE IS NOT NULL)\n          AND (p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1)\n        GROUP BY {grp_col_debt}\n    ),\n    sales_base AS (\n        SELECT {grp_sales} as grp_code,\n               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as sales_with_vat,\n               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0)) as sales_no_vat\n        FROM IAS20261.IAS_BILL_MST\n        WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') \n          AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n          AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)\n        GROUP BY {grp_sales}\n    ),\n    returns_base AS (\n        SELECT {grp_ret} as grp_code,\n               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as returns_with_vat,\n               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0)) as returns_no_vat\n        FROM IAS20261.IAS_RT_BILL_MST\n        WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') \n          AND RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n          AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)\n        GROUP BY {grp_ret}\n    ),\n    ext_disc_base AS (\n        SELECT {grp_col} as grp_code, SUM(NVL(p.CR_AMT,0)) as ext_disc_with_vat\n        FROM IAS20261.IAS_POST_DTL p\n        WHERE p.DOC_TYPE = 15 AND NVL(p.CR_AMT,0) > 0 AND NVL(p.DOC_POST,0) = 1\n          AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') \n          AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n        GROUP BY {grp_col}\n    ),\n    net_sales_summary AS (\n        SELECT NVL(NVL(s.grp_code, r.grp_code), d.grp_code) AS grp_code,\n               SUM(NVL(s.sales_with_vat, 0)) - SUM(NVL(r.returns_with_vat, 0)) - SUM(NVL(d.ext_disc_with_vat, 0)) AS net_sales_vat,\n               SUM(NVL(s.sales_no_vat, 0)) - SUM(NVL(r.returns_no_vat, 0)) - SUM(ROUND(NVL(d.ext_disc_with_vat, 0)/1.15, 2)) AS net_sales_no_vat\n        FROM sales_base s\n        FULL OUTER JOIN returns_base r ON s.grp_code = r.grp_code\n        FULL OUTER JOIN ext_disc_base d ON NVL(s.grp_code, r.grp_code) = d.grp_code\n        GROUP BY NVL(NVL(s.grp_code, r.grp_code), d.grp_code)\n    ),\n    col_trans AS (\n      SELECT {grp_col} as grp_code, p.CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as cash_ret, 0 as unposted_rcpt\n      FROM IAS20261.IAS_POST_DTL p\n      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL\n        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n      UNION ALL\n      SELECT {grp_col}, 0, 0, 0, 0, p.CR_AMT\n      FROM IAS20261.IAS_POST_DTL p\n      WHERE NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL\n        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n      UNION ALL\n      SELECT {grp_col}, 0, p.CR_AMT, 0, 0, 0\n      FROM IAS20261.IAS_POST_DTL p\n      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=1 AND p.JV_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL\n        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n      UNION ALL\n      SELECT {grp_sales_b}, 0, 0, NVL(p.DR_AMT,0), 0, 0\n      FROM IAS20261.IAS_BILL_MST b\n      JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'\n      WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0\n        AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n      UNION ALL\n      SELECT {grp_col}, 0, 0, 0, p.CR_AMT, 0\n      FROM IAS20261.IAS_POST_DTL p\n      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=5 AND p.A_CODE LIKE '111%' AND NVL(p.CR_AMT,0)>0\n        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n    ),\n    col_summary AS (\n      SELECT grp_code,\n             SUM(rcpt + unposted_rcpt + net_jrn + cash_sales - cash_ret) as total_collection\n      FROM col_trans\n      GROUP BY grp_code\n    ),\n    all_codes AS (\n      SELECT grp_code FROM open_debt\n      UNION\n      SELECT grp_code FROM net_sales_summary\n      UNION\n      SELECT grp_code FROM col_summary\n      UNION\n      SELECT grp_code FROM close_debt\n    )\n    SELECT ac.grp_code,\n           {name_expr} as grp_name,\n           NVL(SUM(o.open_bal), 0) as open_bal,\n           NVL(SUM(ns.net_sales_vat), 0) as net_sales_vat,\n           NVL(SUM(ns.net_sales_no_vat), 0) as net_sales_no_vat,\n           NVL(SUM(cs.total_collection), 0) as total_col,\n           NVL(SUM(cd.close_bal), 0) as close_bal\n    FROM all_codes ac\n    LEFT JOIN open_debt o ON o.grp_code = ac.grp_code\n    LEFT JOIN net_sales_summary ns ON ns.grp_code = ac.grp_code\n    LEFT JOIN col_summary cs ON cs.grp_code = ac.grp_code\n    LEFT JOIN close_debt cd ON cd.grp_code = ac.grp_code\n    {join_table}\n    WHERE ac.grp_code IS NOT NULL\n      {rep_filter}\n      GROUP BY ac.grp_code\n    ORDER BY ac.grp_code\n    "
    cols = [code_label, name_label, 'المديونية الافتتاحية', 'صافي المبيعات شامل الضريبة', 'إجمالي التحصيل', 'الفرق (المبيعات - التحصيل)', 'نسبة التحصيل', 'المديونية النهائية', 'إجمالي المبيعات بدون الضريبة', 'الهدف', 'الفرق (الهدف - المبيعات)']
    rows = []
    with get_conn() as con:
        with con.cursor() as cur:
            params = {'date_from': date_from, 'date_to': date_to}
            if ':rep_code' in sql:
                params['rep_code'] = rep_code
            cur.execute(sql, params)
            for c_code, c_name, open_b, ns_vat, ns_no_vat, col, close_b in cur.fetchall():
                ob_val = float(open_b or 0.0)
                ns_vat_val = float(ns_vat or 0.0)
                ns_no_vat_val = float(ns_no_vat or 0.0)
                col_val = float(col or 0.0)
                closing_val = float(close_b or 0.0)
                total_due = ob_val + ns_vat_val
                if total_due > 0:
                    col_ratio = col_val / total_due * 100
                else:
                    col_ratio = 0.0
                target_val = get_target_amount(year_val, period_type, period_val, grp_by, c_code)
                target_str = f'{target_val:,.2f}' if target_val > 0 else ''
                diff_sales_col = ns_vat_val - col_val
                diff_target_sales = target_val - ns_no_vat_val if target_val > 0 else 0.0
                rows.append((c_code, c_name or str(c_code), f'{ob_val:,.2f}', f'{ns_vat_val:,.2f}', f'{col_val:,.2f}', f'{diff_sales_col:,.2f}', f'{col_ratio:,.2f}%', f'{closing_val:,.2f}', f'{ns_no_vat_val:,.2f}', target_str, f'{diff_target_sales:,.2f}' if target_val > 0 else ''))
    return (cols, rows)

def run_workflow_summary(rpt, args):
    year_val = args.get('year_val', '2026')
    period_type = args.get('period_type', 'monthly')
    period_val = args.get('period_val', 'all')
    grp_by = args.get('grp_by', 'cc')
    rep_code = args.get('rep_code', '')
    if not rep_code:
        rep_code = None
    date_from, date_to = get_date_range(year_val, period_type, period_val)
    rep_filter = ''
    if grp_by == 'rep':
        grp_col = 'TO_CHAR(p.REP_CODE)'
        grp_sales = 'TO_CHAR(REP_CODE)'
        grp_sales_b = 'TO_CHAR(b.REP_CODE)'
        grp_ret = 'TO_CHAR(REP_CODE)'
        join_table = 'LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = ac.grp_code'
        name_expr = 'MAX(sm.REPRS_A_NAME)'
        code_label = 'كود المندوب'
        name_label = 'اسم المندوب'
    elif grp_by == 'customer':
        grp_col = 'TO_CHAR(p.C_CODE)'
        grp_sales = 'TO_CHAR(C_CODE)'
        grp_sales_b = 'TO_CHAR(p.C_CODE)'
        grp_ret = 'TO_CHAR(C_CODE)'
        join_table = 'LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = ac.grp_code'
        name_expr = 'MAX(c.C_A_NAME)'
        code_label = 'كود العميل'
        name_label = 'اسم العميل'
        rep_filter = 'AND (:rep_code IS NULL OR TO_CHAR(c.REP_CODE) = :rep_code)'
    elif grp_by == 'period':
        if period_type == 'quarterly':
            grp_sales = "'Q' || TO_CHAR(BILL_DATE, 'Q')"
            grp_sales_b = "'Q' || TO_CHAR(b.BILL_DATE, 'Q')"
            grp_col = "'Q' || TO_CHAR(p.DOC_DATE, 'Q')"
            grp_ret = "'Q' || TO_CHAR(RT_BILL_DATE, 'Q')"
        elif period_type == 'semi_annual':
            grp_sales = "CASE WHEN TO_CHAR(BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_sales_b = "CASE WHEN TO_CHAR(b.BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_col = "CASE WHEN TO_CHAR(p.DOC_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_ret = "CASE WHEN TO_CHAR(RT_BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
        else:
            grp_sales = "TO_CHAR(BILL_DATE, 'YYYY-MM')"
            grp_sales_b = "TO_CHAR(b.BILL_DATE, 'YYYY-MM')"
            grp_col = "TO_CHAR(p.DOC_DATE, 'YYYY-MM')"
            grp_ret = "TO_CHAR(RT_BILL_DATE, 'YYYY-MM')"
        join_table = ''
        name_expr = 'ac.grp_code'
        code_label = 'الفترة الزمنية'
        name_label = 'البيان'
    else:
        grp_col = 'TO_CHAR(p.CC_CODE)'
        grp_sales = 'TO_CHAR(CC_CODE)'
        grp_sales_b = 'TO_CHAR(b.CC_CODE)'
        grp_ret = 'TO_CHAR(CC_CODE)'
        join_table = 'LEFT JOIN IAS20261.COST_CENTERS cc ON TO_CHAR(cc.CC_CODE) = ac.grp_code'
        name_expr = 'MAX(cc.CC_A_NAME)'
        code_label = 'رمز مركز التكلفة'
        name_label = 'اسم مركز التكلفة'
    sql = f"\n    WITH sales_base AS (\n        SELECT {grp_sales} as grp_code,\n               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as sales_with_vat,\n               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0)) as sales_no_vat\n        FROM IAS20261.IAS_BILL_MST\n        WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') \n          AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n          AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)\n        GROUP BY {grp_sales}\n    ),\n    returns_base AS (\n        SELECT {grp_ret} as grp_code,\n               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as returns_with_vat,\n               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0)) as returns_no_vat\n        FROM IAS20261.IAS_RT_BILL_MST\n        WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') \n          AND RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n          AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)\n        GROUP BY {grp_ret}\n    ),\n    ext_disc_base AS (\n        SELECT {grp_col} as grp_code, SUM(NVL(p.CR_AMT,0)) as ext_disc_with_vat\n        FROM IAS20261.IAS_POST_DTL p\n        WHERE p.DOC_TYPE = 15 AND NVL(p.CR_AMT,0) > 0 AND NVL(p.DOC_POST,0) = 1\n          AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') \n          AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n        GROUP BY {grp_col}\n    ),\n    net_sales_summary AS (\n        SELECT NVL(NVL(s.grp_code, r.grp_code), d.grp_code) AS grp_code,\n               SUM(NVL(s.sales_with_vat, 0)) - SUM(NVL(r.returns_with_vat, 0)) - SUM(NVL(d.ext_disc_with_vat, 0)) AS net_sales_vat,\n               SUM(NVL(s.sales_no_vat, 0)) - SUM(NVL(r.returns_no_vat, 0)) - SUM(ROUND(NVL(d.ext_disc_with_vat, 0)/1.15, 2)) AS net_sales_no_vat\n        FROM sales_base s\n        FULL OUTER JOIN returns_base r ON s.grp_code = r.grp_code\n        FULL OUTER JOIN ext_disc_base d ON NVL(s.grp_code, r.grp_code) = d.grp_code\n        GROUP BY NVL(NVL(s.grp_code, r.grp_code), d.grp_code)\n    ),\n    col_trans AS (\n      SELECT {grp_col} as grp_code, p.CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as cash_ret, 0 as unposted_rcpt\n      FROM IAS20261.IAS_POST_DTL p\n      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL\n        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n      UNION ALL\n      SELECT {grp_col}, 0, 0, 0, 0, p.CR_AMT\n      FROM IAS20261.IAS_POST_DTL p\n      WHERE NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL\n        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n      UNION ALL\n      SELECT {grp_col}, 0, p.CR_AMT, 0, 0, 0\n      FROM IAS20261.IAS_POST_DTL p\n      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=1 AND p.JV_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL\n        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n      UNION ALL\n      SELECT {grp_sales_b}, 0, 0, NVL(p.DR_AMT,0), 0, 0\n      FROM IAS20261.IAS_BILL_MST b\n      JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'\n      WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0\n        AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n      UNION ALL\n      SELECT {grp_col}, 0, 0, 0, p.CR_AMT, 0\n      FROM IAS20261.IAS_POST_DTL p\n      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=5 AND p.A_CODE LIKE '111%' AND NVL(p.CR_AMT,0)>0\n        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1\n    ),\n    col_summary AS (\n      SELECT grp_code,\n             SUM(rcpt + unposted_rcpt + net_jrn + cash_sales - cash_ret) as total_collection\n      FROM col_trans\n      GROUP BY grp_code\n    ),\n    all_codes AS (\n      SELECT grp_code FROM net_sales_summary\n      UNION\n      SELECT grp_code FROM col_summary\n    )\n    SELECT ac.grp_code,\n           {name_expr} as grp_name,\n           NVL(SUM(ns.net_sales_vat), 0) as net_sales_vat,\n           NVL(SUM(ns.net_sales_no_vat), 0) as net_sales_no_vat,\n           NVL(SUM(cs.total_collection), 0) as total_col\n    FROM all_codes ac\n    LEFT JOIN net_sales_summary ns ON ns.grp_code = ac.grp_code\n    LEFT JOIN col_summary cs ON cs.grp_code = ac.grp_code\n    {join_table}\n    WHERE ac.grp_code IS NOT NULL\n      {rep_filter}\n      GROUP BY ac.grp_code\n    ORDER BY ac.grp_code\n    "
    cols = [code_label, name_label, 'صافي المبيعات شامل الضريبة', 'إجمالي التحصيل', 'الفرق (المبيعات - التحصيل)', 'نسبة التحصيل', 'إجمالي المبيعات بدون الضريبة', 'الهدف', 'الفرق (الهدف - المبيعات)']
    rows = []
    with get_conn() as con:
        with con.cursor() as cur:
            params = {'date_from': date_from, 'date_to': date_to}
            if ':rep_code' in sql:
                params['rep_code'] = rep_code
            cur.execute(sql, params)
            for c_code, c_name, ns_vat, ns_no_vat, col in cur.fetchall():
                ns_vat_val = float(ns_vat or 0.0)
                ns_no_vat_val = float(ns_no_vat or 0.0)
                col_val = float(col or 0.0)
                total_due = ns_vat_val
                if total_due > 0:
                    col_ratio = col_val / total_due * 100
                else:
                    col_ratio = 0.0
                target_val = get_target_amount(year_val, period_type, period_val, grp_by, c_code)
                target_str = f'{target_val:,.2f}' if target_val > 0 else ''
                diff_sales_col = ns_vat_val - col_val
                diff_target_sales = target_val - ns_no_vat_val if target_val > 0 else 0.0
                rows.append((c_code, c_name or str(c_code), f'{ns_vat_val:,.2f}', f'{col_val:,.2f}', f'{diff_sales_col:,.2f}', f'{col_ratio:,.2f}%', f'{ns_no_vat_val:,.2f}', target_str, f'{diff_target_sales:,.2f}' if target_val > 0 else ''))
    return (cols, rows)


def handle_sales_report(report_id, rpt, args):
    if report_id == 'sales_collection_summary':
        return run_sales_collection_summary(rpt, args)
    if report_id == 'workflow_summary':
        return run_workflow_summary(rpt, args)
    if report_id == 'debt_movement_summary':
        return run_debt_movement_summary(rpt, args)
        
    repo_func_name = f"get_{report_id}_sql"
    if hasattr(repository, repo_func_name):
        rpt['sql'] = getattr(repository, repo_func_name)()
        
    if rpt.get('sql'):
        return run_sql_report(rpt, args)
        
    return [], []
