from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, session
from flask_login import login_required, current_user
from app.database import get_conn
from app.utils.helpers import timed_cache, generate_zatca_qr_base64
from app.local_db import get_emp_code
from datetime import datetime

reports_bp = Blueprint('reports', __name__)

@timed_cache(seconds=600)  # Cache for 10 minutes
def get_salesman_metrics(rep_code):
    try:
        now = datetime.now()
        current_year = now.year
        current_month = now.month
        
        # Calculate dates
        import calendar
        year_start = f"{current_year}-01-01"
        year_end = f"{current_year}-12-31"
        
        last_day = calendar.monthrange(current_year, current_month)[1]
        month_start = f"{current_year}-{current_month:02d}-01"
        month_end = f"{current_year}-{current_month:02d}-{last_day:02d}"
        
        sql = """
        WITH sales_base AS (
            SELECT SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as sales
            FROM IAS20261.IAS_BILL_MST
            WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
              AND BILL_DATE <= TO_DATE(:date_to,'YYYY-MM-DD')
              AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
              AND TO_CHAR(CC_CODE) = TRIM(:rep_code)
        ),
        returns_base AS (
            SELECT SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as returns
            FROM IAS20261.IAS_RT_BILL_MST
            WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
              AND RT_BILL_DATE <= TO_DATE(:date_to,'YYYY-MM-DD')
              AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
              AND TO_CHAR(CC_CODE) = TRIM(:rep_code)
        ),
        ext_disc_base AS (
            SELECT SUM(NVL(p.CR_AMT,0)) as ext_disc
            FROM IAS20261.IAS_POST_DTL p
            WHERE p.DOC_TYPE = 15 AND NVL(p.CR_AMT,0) > 0 AND NVL(p.DOC_POST,0) = 1
              AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
              AND p.DOC_DATE <= TO_DATE(:date_to,'YYYY-MM-DD')
              AND TO_CHAR(p.CC_CODE) = TRIM(:rep_code)
        ),
        col_trans AS (
          SELECT p.CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as cash_ret
          FROM IAS20261.IAS_POST_DTL p
          WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
            AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE <= TO_DATE(:date_to,'YYYY-MM-DD')
            AND TO_CHAR(p.CC_CODE) = TRIM(:rep_code)
          UNION ALL
          SELECT 0, p.CR_AMT, 0, 0
          FROM IAS20261.IAS_POST_DTL p
          WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=1 AND p.JV_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
            AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE <= TO_DATE(:date_to,'YYYY-MM-DD')
            AND TO_CHAR(p.CC_CODE) = TRIM(:rep_code)
          UNION ALL
          SELECT 0, 0, NVL(p.DR_AMT,0), 0
          FROM IAS20261.IAS_BILL_MST b
          JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
          WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
            AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE <= TO_DATE(:date_to,'YYYY-MM-DD')
            AND TO_CHAR(b.CC_CODE) = TRIM(:rep_code)
          UNION ALL
          SELECT 0, 0, 0, p.CR_AMT
          FROM IAS20261.IAS_POST_DTL p
          WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=5 AND p.A_CODE LIKE '111%' AND NVL(p.CR_AMT,0)>0
            AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE <= TO_DATE(:date_to,'YYYY-MM-DD')
            AND TO_CHAR(p.CC_CODE) = TRIM(:rep_code)
        )
        SELECT 
          NVL((SELECT NVL(sales, 0) FROM sales_base), 0) - NVL((SELECT NVL(returns, 0) FROM returns_base), 0) - NVL((SELECT NVL(ext_disc, 0) FROM ext_disc_base), 0) as net_sales,
          NVL((SELECT NVL(SUM(rcpt + net_jrn + cash_sales - cash_ret), 0) FROM col_trans), 0) as total_collection
        FROM DUAL
        """
        
        with get_conn() as con:
            with con.cursor() as cur:
                # Year Metrics
                cur.execute(sql, {'date_from': year_start, 'date_to': year_end, 'rep_code': rep_code})
                y_row = cur.fetchone()
                
                # Month Metrics
                cur.execute(sql, {'date_from': month_start, 'date_to': month_end, 'rep_code': rep_code})
                m_row = cur.fetchone()
                
                # Load mapping from SQLite
                emp_code = get_emp_code(rep_code)

                # Employee / Salesman Debt
                emp_debt_sql = """
                    SELECT SUM(NVL(p.CR_AMT, 0) - NVL(p.DR_AMT, 0))
                    FROM IAS20261.IAS_POST_DTL p
                    WHERE (p.A_CODE LIKE '11402%' OR p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%')
                      AND TO_CHAR(p.AC_CODE_DTL) = :emp_code
                      AND NVL(p.DOC_POST, 0) = 1
                """
                cur.execute(emp_debt_sql, {'emp_code': emp_code})
                emp_row = cur.fetchone()
                total_employee_debt = float(emp_row[0]) if emp_row and emp_row[0] is not None else 0.0
                
                # Customer debt
                cust_debt_sql = """
                    WITH cust_bals AS (
                        SELECT TO_CHAR(p.C_CODE) as C_CODE, 
                               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as net_bal
                        FROM IAS20261.IAS_POST_DTL p
                        WHERE NVL(p.DOC_POST,0) = 1
                          AND p.C_CODE IS NOT NULL
                        GROUP BY TO_CHAR(p.C_CODE)
                    ),
                    vendor_bals AS (
                        SELECT TO_CHAR(p.V_CODE) as V_CODE, 
                               SUM(NVL(p.CR_AMT,0) - NVL(p.DR_AMT,0)) as v_net_bal
                        FROM IAS20261.IAS_POST_DTL p
                        WHERE NVL(p.DOC_POST,0) = 1
                          AND p.V_CODE IS NOT NULL
                        GROUP BY TO_CHAR(p.V_CODE)
                    )
                    SELECT cb.C_CODE, cb.net_bal, NVL(vb.v_net_bal, 0)
                    FROM IAS20261.CUSTOMER c
                    JOIN cust_bals cb ON cb.C_CODE = TO_CHAR(c.C_CODE)
                    LEFT JOIN vendor_bals vb ON vb.V_CODE = TO_CHAR(c.C_VENDOR)
                    WHERE TRIM(c.REP_CODE) = TRIM(:rep_code)
                """
                cur.execute(cust_debt_sql, {'rep_code': rep_code})
                total_cust_debt = 0.0
                for c_code, c_bal, v_bal in cur.fetchall():
                    c_bal = float(c_bal) if c_bal else 0.0
                    v_bal = float(v_bal) if v_bal else 0.0
                    
                    if v_bal > 0:
                        c_bal -= v_bal
                        
                    if c_bal > 0:
                        total_cust_debt += c_bal

                
        return {
            'current_month': current_month,
            'current_year': current_year,
            'year_sales': float(y_row[0] or 0),
            'year_col': float(y_row[1] or 0),
            'month_sales': float(m_row[0] or 0),
            'month_col': float(m_row[1] or 0),
            'total_cust_debt': total_cust_debt,
            'total_employee_debt': total_employee_debt
        }
    except Exception as e:
        print("Error getting metrics:", e)
        return {
            'current_month': datetime.now().month,
            'current_year': datetime.now().year,
            'year_sales': 0, 'year_col': 0, 'month_sales': 0, 'month_col': 0, 'total_cust_debt': 0, 'total_employee_debt': 0
        }

@reports_bp.route('/refresh_dashboard')
@login_required
def refresh_dashboard():
    if 'rep_code' not in session:
        return redirect(url_for('auth.login'))
    
    rep_code = session['rep_code']
    get_salesman_metrics(rep_code, force_refresh=True)
    
    flash('تم تحديث البيانات بنجاح!', 'success')
    return redirect(url_for('reports.dashboard'))

@reports_bp.route('/dashboard')
@login_required
def dashboard():
    customers = []
    metrics = get_salesman_metrics(current_user.rep_code)
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute("""
                    SELECT C_CODE, C_A_NAME, NVL(C_MOBILE, NVL(C_PHONE, '')) 
                    FROM IAS20261.CUSTOMER 
                    WHERE TRIM(REP_CODE) = TRIM(:1)
                      AND NVL(INACTIVE, 0) = 0
                      AND NVL(BLK_LST, 0) = 0
                """, [current_user.rep_code])
                for row in cur.fetchall():
                    customers.append({
                        "code": row[0],
                        "name": row[1],
                        "mobile": row[2]
                    })
    except Exception as e:
        flash(f'خطأ في جلب بيانات العملاء: {str(e)}')
        
    return render_template('dashboard.html', salesman_name=current_user.name, customers=customers, metrics=metrics)

@reports_bp.route('/customer/<path:c_code>')
@login_required
def customer_invoices(c_code):
    invoices = []
    customer_name = "عميل غير معروف"
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute("SELECT C_A_NAME FROM IAS20261.CUSTOMER WHERE C_CODE = :1 AND TRIM(REP_CODE) = TRIM(:2)", [c_code, current_user.rep_code])
                row = cur.fetchone()
                if not row:
                    flash('هذا العميل غير موجود أو غير مرتبط بك.')
                    return redirect(url_for('reports.dashboard'))
                
                customer_name = row[0]
                
                cur.execute("""
                    SELECT BILL_NO, TO_CHAR(BILL_DATE, 'YYYY-MM-DD'), BILL_AMT + NVL(VAT_AMT, 0) as TOT_AMT, BILL_DOC_TYPE
                    FROM IAS20261.IAS_BILL_MST 
                    WHERE C_CODE = :1 
                    ORDER BY BILL_DATE DESC
                    FETCH FIRST 50 ROWS ONLY
                """, [c_code])
                
                for inv in cur.fetchall():
                    invoices.append({
                        "bill_no": inv[0],
                        "date": inv[1],
                        "total": float(inv[2]),
                        "type": "نقدي" if str(inv[3]) == '1' else "آجل"
                    })
    except Exception as e:
        flash(f'خطأ في جلب الفواتير: {str(e)}')
        
    return render_template('customer.html', customer_name=customer_name, c_code=c_code, invoices=invoices)

@reports_bp.route('/customer_info/<path:c_code>')
@login_required
def customer_info(c_code):
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute("""
                    SELECT 
                        c.C_A_NAME,
                        c.BUILDING_NO,
                        c.STREET,
                        c.DSTRCT_NM,
                        ci.CITY_A_NAME,
                        co.CNTRY_A_NAME,
                        c.C_BOX_CODE,
                        c.ADD_NO,
                        c.C_TAX_CODE,
                        c.CR_NO,
                        c.CSTMR_IDNTFR
                    FROM IAS20261.CUSTOMER c
                    LEFT JOIN IAS20261.CITIES ci ON c.CITY_NO = ci.CITY_NO AND c.CNTRY_NO = ci.CNTRY_NO AND c.PROV_NO = ci.PROV_NO
                    LEFT JOIN IAS20261.CNTRY co ON c.CNTRY_NO = co.CNTRY_NO
                    WHERE c.C_CODE = :1 AND TRIM(c.REP_CODE) = TRIM(:2)
                """, [c_code, current_user.rep_code])
                
                row = cur.fetchone()
                if not row:
                    flash('هذا العميل غير موجود أو غير مرتبط بك.')
                    return redirect(url_for('reports.dashboard'))
                
                customer = {
                    "name": row[0],
                    "building": row[1],
                    "street": row[2],
                    "district": row[3],
                    "city": row[4],
                    "country": row[5],
                    "postal_code": row[6],
                    "additional_no": row[7],
                    "vat_no": row[8],
                    "crn": row[9],
                    "other_id": row[10]
                }
                
                return render_template('customer_info.html', customer=customer, c_code=c_code)
    except Exception as e:
        flash(f'خطأ في جلب بيانات العميل: {str(e)}')
        return redirect(url_for('reports.dashboard'))

@reports_bp.route('/item_prices')
@login_required
def item_prices():
    try:
        sql = """
        WITH item_stats AS (
            SELECT 
                I_CODE, 
                SUM(NVL(IN_OUT, 0) * NVL(I_QTY, 0)) as net_qty, 
                SUM(CASE WHEN EXTRACT(YEAR FROM I_DATE) = 2026 THEN 1 ELSE 0 END) as mov_2026_count,
                SUM(CASE WHEN W_CODE IN ('103','105','108') THEN NVL(IN_OUT, 0) * NVL(I_QTY, 0) ELSE 0 END) as qty_riyadh,
                SUM(CASE WHEN W_CODE = '118' THEN NVL(IN_OUT, 0) * NVL(I_QTY, 0) ELSE 0 END) as qty_south,
                SUM(CASE WHEN W_CODE = '122' THEN NVL(IN_OUT, 0) * NVL(I_QTY, 0) ELSE 0 END) as qty_north,
                SUM(CASE WHEN W_CODE = '121' THEN NVL(IN_OUT, 0) * NVL(I_QTY, 0) ELSE 0 END) as qty_jeddah,
                SUM(CASE WHEN W_CODE = '119' THEN NVL(IN_OUT, 0) * NVL(I_QTY, 0) ELSE 0 END) as qty_dammam
            FROM IAS20261.ITEM_MOVEMENT
            GROUP BY I_CODE
        ),
        item_groups AS (
            SELECT 
                m.I_CODE,
                MAX(m.I_NAME) AS I_NAME,
                MAX(gd.G_A_NAME) AS main_grp,
                MAX(mg.MNG_A_NAME) AS sub_main_grp,
                MAX(sg.SUBG_A_NAME) AS sub_grp,
                MAX(dg.DETAIL_A_NAME) AS dtl_grp
            FROM IAS20261.IAS_ITM_MST m
            LEFT JOIN IAS20261.GROUP_DETAILS gd ON gd.G_CODE = m.G_CODE
            LEFT JOIN IAS20261.IAS_MAINSUB_GRP_DTL mg ON mg.MNG_CODE = m.MNG_CODE AND mg.G_CODE = m.G_CODE
            LEFT JOIN IAS20261.IAS_SUB_GRP_DTL sg ON sg.SUBG_CODE = m.SUBG_CODE
            LEFT JOIN IAS20261.IAS_DETAIL_GROUP dg ON dg.DETAIL_NO = m.DETAIL_NO
            JOIN item_stats s ON m.I_CODE = s.I_CODE
            WHERE NVL(m.INACTIVE, 0) = 0
              AND (s.net_qty > 0 OR s.mov_2026_count > 0)
              AND EXISTS (SELECT 1 FROM IAS20261.IAS_ITEM_PRICE p WHERE p.I_CODE = m.I_CODE)
            GROUP BY m.I_CODE
        )
        SELECT 
            ig.main_grp AS "المجموعة الرئيسية",
            ig.sub_main_grp AS "الفرعية",
            ig.sub_grp AS "تحت الفرعية",
            ig.dtl_grp AS "التفصيلية",
            ig.I_CODE AS "رقم الصنف",
            ig.I_NAME AS "اسم الصنف",
            NVL((SELECT MAX(P.I_PRICE) FROM IAS20261.IAS_ITEM_PRICE P WHERE P.I_CODE = ig.I_CODE AND P.LEV_NO = 1), 0) AS "التكلفة علينا",
            NVL((SELECT MAX(P.I_PRICE) FROM IAS20261.IAS_ITEM_PRICE P WHERE P.I_CODE = ig.I_CODE AND P.LEV_NO = 2), 0) AS "الحد الادنى",
            NVL(s.qty_riyadh, 0) AS "الرياض",
            NVL(s.qty_south, 0) AS "الجنوب",
            NVL(s.qty_north, 0) AS "الشمال",
            NVL(s.qty_jeddah, 0) AS "جدة",
            NVL(s.qty_dammam, 0) AS "الدمام"
        FROM item_groups ig
        JOIN item_stats s ON ig.I_CODE = s.I_CODE
        ORDER BY ig.main_grp, ig.sub_main_grp, ig.sub_grp, ig.dtl_grp, ig.I_CODE
        """
        items = []
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute(sql)
                columns = ['main_grp', 'sub_main_grp', 'sub_grp', 'dtl_grp', 'i_code', 'i_name', 'cost_price', 'min_price', 'qty_riyadh', 'qty_south', 'qty_north', 'qty_jeddah', 'qty_dammam']
                for row in cur.fetchall():
                    items.append(dict(zip(columns, row)))
        
        return render_template('item_prices.html', items=items)
    except Exception as e:
        flash(f'خطأ في جلب بيانات الأصناف: {str(e)}')
        return redirect(url_for('reports.dashboard'))

@reports_bp.route('/print_last_invoice')
@login_required
def print_last_invoice():
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute("""
                    SELECT m.BILL_NO
                    FROM IAS20261.IAS_BILL_MST m
                    WHERE m.C_CODE IN (
                        SELECT C_CODE FROM IAS20261.CUSTOMER WHERE TRIM(REP_CODE) = TRIM(:1)
                    )
                    ORDER BY m.BILL_DATE DESC, m.AD_DATE DESC
                    FETCH FIRST 1 ROWS ONLY
                """, [current_user.rep_code])
                row = cur.fetchone()
                if row:
                    return redirect(url_for('reports.index', bill_no=row[0]))
                else:
                    flash('لا توجد فواتير تم إصدارها مؤخراً لعملائك.')
                    return redirect(url_for('reports.dashboard'))
    except Exception as e:
        flash(f'خطأ: {str(e)}')
        return redirect(url_for('reports.dashboard'))

@reports_bp.route('/')
@login_required
def root():
    return redirect(url_for('reports.dashboard'))

@reports_bp.route('/print')
@login_required
def index():
    return render_template('index.html')

@reports_bp.route('/api/invoice/<path:bill_no>')
@login_required
def get_invoice(bill_no):
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                # Get Invoice Master Data
                cur.execute("""
                    SELECT 
                        m.BILL_NO, 
                        TO_CHAR(m.BILL_DATE, 'DD/MM/YYYY'), 
                        TO_CHAR(m.AD_DATE, 'HH:MI:SS AM'),
                        m.BILL_AMT,
                        NVL(m.VAT_AMT, 0) as VAT_AMT,
                        NVL(m.C_NAME, NVL(c.C_A_NAME, cash_c.CUST_L_NM)) as C_NAME,
                        m.BILL_DATE,
                        m.BILL_DOC_TYPE,
                        NVL(c.BUILDING_NO, cash_c.BUILDING_NO),
                        NVL(c.STREET, cash_c.STREET),
                        NVL(c.DSTRCT_NM, cash_c.DSTRCT_NM),
                        NVL(c.C_BOX_CODE, cash_c.PBOX),
                        NVL(c.ADD_NO, cash_c.ADD_NO),
                        NVL(c.C_TAX_CODE, cash_c.C_TAX_CODE),
                        NVL(c.CR_NO, cash_c.CR_NO),
                        NVL(c.CSTMR_IDNTFR, cash_c.CSTMR_IDNTFR),
                        m.TAX_BILL_TYP,
                        TO_CHAR(m.AD_DATE, 'HH24:MI:SS'),
                        ci.CITY_A_NAME,
                        co.CNTRY_A_NAME,
                        TO_CHAR(NVL(m.BILL_DUE_DATE, m.BILL_DATE), 'DD/MM/YYYY')
                    FROM IAS20261.IAS_BILL_MST m
                    LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = m.C_CODE
                    LEFT JOIN IAS20261.IAS_CASH_CUSTMR cash_c ON m.C_CODE_CSH = cash_c.CUST_CODE
                    LEFT JOIN IAS20261.CITIES ci ON NVL(c.CITY_NO, cash_c.CITY_NO) = ci.CITY_NO AND NVL(c.CNTRY_NO, cash_c.CNTRY_NO) = ci.CNTRY_NO AND NVL(c.PROV_NO, cash_c.PROV_NO) = ci.PROV_NO
                    LEFT JOIN IAS20261.CNTRY co ON NVL(c.CNTRY_NO, cash_c.CNTRY_NO) = co.CNTRY_NO
                    WHERE m.BILL_NO = :1 AND TO_CHAR(m.CC_CODE) = TRIM(:2)
                """, [bill_no, current_user.rep_code])
                
                mst_row = cur.fetchone()
                if not mst_row:
                    return jsonify({"error": "الفاتورة غير موجودة"}), 404
                    
                b_no, b_date, b_time, b_amt, v_amt, c_name, raw_date, doc_type, c_building, c_street, c_district, c_postal, c_add_no, c_vat, c_crn, c_other_id, tax_bill_typ, time_24h, c_city, c_country, due_date_str = mst_row
                
                pay_method = "نقد / Cash" if str(doc_type) == '1' else "آجل / Credit"
                
                cur.execute("""
                    SELECT 
                        CMP_LNAME || ' - ' || BRN_LNAME as S_NAME,
                        BUILDING_NO,
                        STREET,
                        DSTRCT_NM,
                        POSTAL_CODE,
                        ADD_NO,
                        BRN_TAX_CODE,
                        RC_CODE,
                        BRN_IDNTFR
                    FROM IAS20261.S_BRN 
                    WHERE BRN_NO = 1
                """)
                s_row = cur.fetchone()
                if s_row:
                    s_name, s_building, s_street, s_district, s_postal, s_add_no, s_vat, s_crn, s_other_id = s_row
                else:
                    s_name = s_building = s_street = s_district = s_postal = s_add_no = s_vat = s_crn = s_other_id = ""

                if str(tax_bill_typ) == '2':
                    inv_type_ar = "فاتورة ضريبية"
                    inv_type_en = "Tax Invoice"
                else:
                    inv_type_ar = "فاتورة ضريبية مبسطة"
                    inv_type_en = "Simplified Tax Invoice"
                
                cur.execute("""
                    SELECT 
                        d.I_CODE,
                        NVL(m.I_NAME, 'صنف غير معروف'),
                        d.I_QTY,
                        d.I_PRICE,
                        NVL(d.DIS_AMT, 0),
                        NVL(d.VAT_AMT, 0),
                        (d.I_QTY * (d.I_PRICE - NVL(d.DIS_AMT, 0) + NVL(d.VAT_AMT, 0))) as TOT_AMT
                    FROM IAS20261.IAS_BILL_DTL d
                    LEFT JOIN IAS20261.IAS_ITM_MST m ON d.I_CODE = m.I_CODE
                    WHERE d.BILL_NO = :1
                """, [bill_no])
                
                items = []
                for r in cur.fetchall():
                    items.append({
                        "item_id": r[0],
                        "item_name": r[1],
                        "quantity": r[2],
                        "amount": r[3],
                        "discount": r[4],
                        "tax": r[5],
                        "total_due": r[6]
                    })
                
                seller_name_qr = s_name or "مؤسسة عاصمة المجد للتجارة - سرين"
                vat_no_qr = s_vat or "302145687600003"
                
                try:
                    time_str = str(time_24h) if time_24h else "00:00:00"
                    if len(time_str) == 5: 
                        time_str += ":00"
                    dt_str = raw_date.strftime('%Y-%m-%d') + "T" + time_str + "Z"
                except:
                    dt_str = "2026-08-08T18:09:00Z"
                
                total_discount = sum(i["quantity"] * i["discount"] for i in items)
                total_excluding_vat = float(b_amt)
                total_taxable = total_excluding_vat - total_discount
                v_amt_float = float(v_amt)
                total_with_tax = total_taxable + v_amt_float
                
                qr_base64 = generate_zatca_qr_base64(
                    seller_name_qr, 
                    vat_no_qr, 
                    dt_str, 
                    "{:.2f}".format(total_with_tax), 
                    "{:.2f}".format(v_amt_float)
                )
                
                try:
                    from app.utils.tafqeet import do_tafqeet
                    amount_in_words = do_tafqeet(total_with_tax)
                except:
                    amount_in_words = ""

                return jsonify({
                    "invoice_no": b_no,
                    "invoice_date": b_date,
                    "invoice_time": b_time,
                    "due_date": due_date_str,
                    "payment_method": pay_method,
                    "invoice_type_ar": inv_type_ar,
                    "invoice_type_en": inv_type_en,
                    "amount_in_words": amount_in_words,
                    "seller": {
                        "name": s_name,
                        "building": s_building,
                        "street": s_street,
                        "district": s_district,
                        "city": "الرياض",
                        "country": "المملكة العربية السعودية",
                        "postal_code": s_postal,
                        "additional_no": s_add_no,
                        "vat_no": s_vat,
                        "crn": s_crn,
                        "other_id": s_other_id
                    },
                    "buyer": {
                        "name": c_name or "عميل نقدي",
                        "building": c_building or "",
                        "street": c_street or "",
                        "district": c_district or "",
                        "city": c_city or "",
                        "country": c_country or "",
                        "postal_code": c_postal or "",
                        "additional_no": c_add_no or "",
                        "vat_no": c_vat or "",
                        "crn": c_crn or "",
                        "other_id": c_other_id or ""
                    },
                    "items": items,
                    "totals": {
                        "total_qty": sum(i["quantity"] for i in items),
                        "total_excluding_vat": total_excluding_vat,
                        "discount": total_discount,
                        "charges": 0.00,
                        "total_taxable": total_taxable,
                        "tax": v_amt_float,
                        "total_with_tax": total_with_tax,
                        "text": amount_in_words
                    },
                    "qr_base64": qr_base64
                })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
