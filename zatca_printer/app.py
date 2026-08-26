from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
import qrcode
import base64
from datetime import datetime
from dotenv import load_dotenv
import oracledb

load_dotenv()

app = Flask(__name__)
app.secret_key = "super_secret_onyx_key_123"
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, rep_code, name):
        self.id = str(id)
        self.rep_code = rep_code
        self.name = name

@login_manager.user_loader
def load_user(user_id):
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute("SELECT U_ID, REP_CODE, U_A_NAME FROM IAS20261.USER_R WHERE U_ID = :1", [user_id])
                row = cur.fetchone()
                if row:
                    return User(id=row[0], rep_code=row[1], name=row[2])
    except Exception as e:
        print("Error loading user:", e)
    return None

def decrypt_onyx_password(encrypted_pwd):
    if not encrypted_pwd: return ""
    L = len(encrypted_pwd)
    return "".join(chr(ord(c) - L) for c in encrypted_pwd)

def encrypt_onyx_password(plain_pwd):
    if not plain_pwd: return ""
    L = len(plain_pwd)
    return "".join(chr(ord(c) + L) for c in plain_pwd)
# Initialize Oracle Client with Thick Mode based on Env
lib_dir = os.getenv("ORA_LIB_DIR", r"C:\oracle\instantclient\instantclient_23_0")
try:
    oracledb.init_oracle_client(lib_dir=lib_dir)
except Exception as e:
    print("Warning: Oracle client init failed. It might be already initialized or path is wrong.", e)

def get_conn():
    return oracledb.connect(
        user=os.getenv("DB_USER", "RPT_USER"),
        password=os.getenv("DB_PASS", "ULT2016"),
        dsn=os.getenv("ORA_DSN", "100.100.1.100:1521/ORCL")
    )

def generate_tlv(tag, value):
    if isinstance(value, str):
        value_bytes = value.encode('utf-8')
    else:
        value_bytes = value
    return bytes([tag, len(value_bytes)]) + value_bytes

def generate_zatca_qr_base64(seller_name, vat_number, timestamp, total_amount, vat_amount):
    tlv1 = generate_tlv(1, seller_name)
    tlv2 = generate_tlv(2, vat_number)
    tlv3 = generate_tlv(3, timestamp)
    tlv4 = generate_tlv(4, str(total_amount))
    tlv5 = generate_tlv(5, str(vat_amount))
    full_tlv = tlv1 + tlv2 + tlv3 + tlv4 + tlv5
    return base64.b64encode(full_tlv).decode('utf-8')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
        
    if request.method == 'POST':
        rep_code = request.form.get('rep_code')
        password = request.form.get('password')
        
        try:
            with get_conn() as con:
                with con.cursor() as cur:
                    cur.execute("SELECT U_ID, REP_CODE, U_A_NAME, PASSWORD FROM IAS20261.USER_R WHERE REP_CODE = :1", [rep_code])
                    row = cur.fetchone()
                    if row:
                        u_id, r_code, u_name, encrypted_pwd = row
                        decrypted_pwd = decrypt_onyx_password(encrypted_pwd)
                        if password == decrypted_pwd:
                            user = User(id=u_id, rep_code=r_code, name=u_name)
                            login_user(user)
                            return redirect(url_for('dashboard'))
                        else:
                            flash('كلمة المرور غير صحيحة')
                    else:
                        flash('رقم المندوب غير موجود')
        except Exception as e:
            flash(f'خطأ في الاتصال بقاعدة البيانات: {str(e)}')
            
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    customers = []
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
        
    return render_template('dashboard.html', salesman_name=current_user.name, customers=customers)

@app.route('/customer/<path:c_code>')
@login_required
def customer_invoices(c_code):
    invoices = []
    customer_name = "عميل غير معروف"
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                # Verify customer belongs to salesman
                cur.execute("SELECT C_A_NAME FROM IAS20261.CUSTOMER WHERE C_CODE = :1 AND TRIM(REP_CODE) = TRIM(:2)", [c_code, current_user.rep_code])
                row = cur.fetchone()
                if not row:
                    flash('هذا العميل غير موجود أو غير مرتبط بك.')
                    return redirect(url_for('dashboard'))
                
                customer_name = row[0]
                
                # Fetch recent invoices for this customer
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

@app.route('/customer_info/<path:c_code>')
@login_required
def customer_info(c_code):
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                # Fetch detailed customer info
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
                    return redirect(url_for('dashboard'))
                
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
        return redirect(url_for('dashboard'))

@app.route('/print_last_invoice')
@login_required
def print_last_invoice():
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                # Find the most recent invoice for this salesman's customers
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
                    return redirect(url_for('index', bill_no=row[0]))
                else:
                    flash('لا توجد فواتير تم إصدارها مؤخراً لعملائك.')
                    return redirect(url_for('dashboard'))
    except Exception as e:
        flash(f'خطأ: {str(e)}')
        return redirect(url_for('dashboard'))

@app.route('/')
@login_required
def root():
    return redirect(url_for('dashboard'))

@app.route('/print')
@login_required
def index():
    return render_template('index.html')

@app.route('/api/invoice/<path:bill_no>')
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
                        co.CNTRY_A_NAME
                    FROM IAS20261.IAS_BILL_MST m
                    LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = m.C_CODE
                    LEFT JOIN IAS20261.IAS_CASH_CUSTMR cash_c ON m.C_CODE_CSH = cash_c.CUST_CODE
                    LEFT JOIN IAS20261.CITIES ci ON NVL(c.CITY_NO, cash_c.CITY_NO) = ci.CITY_NO AND NVL(c.CNTRY_NO, cash_c.CNTRY_NO) = ci.CNTRY_NO AND NVL(c.PROV_NO, cash_c.PROV_NO) = ci.PROV_NO
                    LEFT JOIN IAS20261.CNTRY co ON NVL(c.CNTRY_NO, cash_c.CNTRY_NO) = co.CNTRY_NO
                    WHERE m.BILL_NO = :1
                """, [bill_no])
                
                mst_row = cur.fetchone()
                if not mst_row:
                    return jsonify({"error": "الفاتورة غير موجودة"}), 404
                    
                b_no, b_date, b_time, b_amt, v_amt, c_name, raw_date, doc_type, c_building, c_street, c_district, c_postal, c_add_no, c_vat, c_crn, c_other_id, tax_bill_typ, time_24h, c_city, c_country = mst_row
                
                # Payment method string
                pay_method = "نقد / Cash" if str(doc_type) == '1' else "آجل / Credit"
                
                # Fetch Seller Data (Branch)
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

                # Determine Invoice Type from TAX_BILL_TYP
                # 2 = Standard Tax Invoice (B2B)
                # 1 = Simplified Tax Invoice (B2C)
                if str(tax_bill_typ) == '2':
                    inv_type_ar = "فاتورة ضريبية"
                    inv_type_en = "Tax Invoice"
                else:
                    inv_type_ar = "فاتورة ضريبية مبسطة"
                    inv_type_en = "Simplified Tax Invoice"
                
                # Fetch Details
                cur.execute("""
                    SELECT 
                        d.I_CODE,
                        NVL(m.I_NAME, 'صنف غير معروف'),
                        d.I_QTY,
                        d.I_PRICE,
                        NVL(d.DIS_AMT, 0),
                        NVL(d.VAT_AMT, 0),
                        (d.I_QTY * d.I_PRICE) - NVL(d.DIS_AMT, 0) + NVL(d.VAT_AMT, 0) as TOT_AMT
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
                
                # Generate QR Code
                seller_name_qr = s_name or "مؤسسة عاصمة المجد للتجارة - سرين"
                vat_no_qr = s_vat or "302145687600003"
                
                # Format timestamp for ZATCA (ISO 8601)
                try:
                    time_str = str(time_24h) if time_24h else "00:00:00"
                    if len(time_str) == 5: # HH:MM
                        time_str += ":00"
                    dt_str = raw_date.strftime('%Y-%m-%d') + "T" + time_str + "Z"
                except:
                    dt_str = "2026-08-08T18:09:00Z"
                
                total_with_tax = float(b_amt) + float(v_amt)
                
                qr_base64 = generate_zatca_qr_base64(
                    seller_name_qr, 
                    vat_no_qr, 
                    dt_str, 
                    "{:.2f}".format(total_with_tax), 
                    "{:.2f}".format(float(v_amt))
                )
                
                try:
                    from tafqeet import do_tafqeet
                    amount_in_words = do_tafqeet(total_with_tax)
                except:
                    amount_in_words = ""

                # Dummy Data for Seller/Buyer Addresses for now
                return jsonify({
                    "invoice_no": b_no,
                    "invoice_date": b_date,
                    "invoice_time": b_time,
                    "due_date": b_date,
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
                        "total_excluding_vat": b_amt,
                        "discount": sum(i["discount"] for i in items),
                        "charges": 0.00,
                        "total_taxable": b_amt,
                        "tax": v_amt,
                        "total_with_tax": total_with_tax,
                        "text": "ثلاثة عشر ألف و مئتين و خمسة و عشرون ريال سعودي" # We can add Tafqeet later
                    },
                    "qr_base64": qr_base64
                })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
