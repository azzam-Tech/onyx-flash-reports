from flask import Blueprint, jsonify, request, send_from_directory
import os, json
from database import get_conn
from werkzeug.utils import secure_filename

customers_api_bp = Blueprint('customers_api', __name__, url_prefix='/api/customers')

# Base directory for customer documents (outside the backend code, in project root)
# __file__ is in dbOnyxOnAntigravity/privet/onyx_reports/routes/
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
BASE_STORAGE = os.path.join(ROOT_DIR, 'customers_data')

if not os.path.exists(BASE_STORAGE):
    os.makedirs(BASE_STORAGE)

@customers_api_bp.route('/', methods=['GET'])
def get_customers():
    try:
        net_supplier = request.args.get('net_supplier', 'false').lower() == 'true'
        customers = []
        with get_conn() as con:
            with con.cursor() as cur:
                
                if net_supplier:
                    query = """
                        WITH CustBal AS (
                            SELECT C_CODE, SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)) as BAL
                            FROM IAS20261.IAS_POST_DTL 
                            WHERE C_CODE IS NOT NULL AND NVL(DOC_POST,0) = 1
                            GROUP BY C_CODE
                        ),
                        VendBal AS (
                            SELECT C_V_CODE, SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)) as BAL
                            FROM IAS20261.IAS_POST_DTL 
                            WHERE C_V_CODE IS NOT NULL AND V_CODE IS NOT NULL AND NVL(DOC_POST,0) = 1
                            GROUP BY C_V_CODE
                        )
                        SELECT 
                            c.C_CODE,
                            c.C_A_NAME,
                            co.CNTRY_A_NAME,
                            ci.CITY_A_NAME,
                            c.DSTRCT_NM,
                            NVL(cb.BAL, 0) + NVL(vb.BAL, 0) as ACTUAL_BALANCE,
                            c.BUILDING_NO,
                            c.STREET,
                            c.C_BOX_CODE,
                            c.ADD_NO,
                            c.C_TAX_CODE,
                            c.CR_NO,
                            c.CSTMR_IDNTFR,
                            NVL(c.C_PHONE, c.C_MOBILE) as TEL,
                            c.C_MOBILE as MOBILE,
                            c.C_A_NAME as C_NAME_AR,
                            c.C_E_NAME as C_NAME_EN,
                            NVL(lmt.CR_LIMIT, 0) as CREDIT_LIMIT,
                            c.CR_NO as REGISTRATION_NUMBER,
                            c.C_TAX_CODE as TAX_NUMBER,
                            ci.CITY_A_NAME as CITY,
                            co.CNTRY_A_NAME as COUNTRY,
                            NVL(c.INACTIVE, 0) as INACTIVE,
                            NVL(c.INACTIVE_SALES, 0) as INACTIVE_SALES
                        FROM IAS20261.CUSTOMER c
                        LEFT JOIN IAS20261.DTS_GET_CST_CRDT_PRD lmt ON c.C_CODE = lmt.C_CODE
                        LEFT JOIN IAS20261.CITIES ci ON c.CITY_NO = ci.CITY_NO AND c.CNTRY_NO = ci.CNTRY_NO AND c.PROV_NO = ci.PROV_NO
                        LEFT JOIN IAS20261.CNTRY co ON c.CNTRY_NO = co.CNTRY_NO
                        LEFT JOIN CustBal cb ON c.C_CODE = cb.C_CODE
                        LEFT JOIN VendBal vb ON TO_CHAR(c.C_CODE) = vb.C_V_CODE
                    """
                else:
                    query = """
                        WITH CustBal AS (
                            SELECT C_CODE, SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)) as BAL
                            FROM IAS20261.IAS_POST_DTL 
                            WHERE C_CODE IS NOT NULL AND NVL(DOC_POST,0) = 1
                            GROUP BY C_CODE
                        )
                        SELECT 
                            c.C_CODE,
                            c.C_A_NAME,
                            co.CNTRY_A_NAME,
                            ci.CITY_A_NAME,
                            c.DSTRCT_NM,
                            NVL(cb.BAL, 0) as ACTUAL_BALANCE,
                            c.BUILDING_NO,
                            c.STREET,
                            c.C_BOX_CODE,
                            c.ADD_NO,
                            c.C_TAX_CODE,
                            c.CR_NO,
                            c.CSTMR_IDNTFR,
                            NVL(c.C_PHONE, c.C_MOBILE) as TEL,
                            c.C_MOBILE as MOBILE,
                            c.C_A_NAME as C_NAME_AR,
                            c.C_E_NAME as C_NAME_EN,
                            NVL(lmt.CR_LIMIT, 0) as CREDIT_LIMIT,
                            c.CR_NO as REGISTRATION_NUMBER,
                            c.C_TAX_CODE as TAX_NUMBER,
                            ci.CITY_A_NAME as CITY,
                            co.CNTRY_A_NAME as COUNTRY,
                            NVL(c.INACTIVE, 0) as INACTIVE,
                            NVL(c.INACTIVE_SALES, 0) as INACTIVE_SALES
                        FROM IAS20261.CUSTOMER c
                        LEFT JOIN IAS20261.DTS_GET_CST_CRDT_PRD lmt ON c.C_CODE = lmt.C_CODE
                        LEFT JOIN IAS20261.CITIES ci ON c.CITY_NO = ci.CITY_NO AND c.CNTRY_NO = ci.CNTRY_NO AND c.PROV_NO = ci.PROV_NO
                        LEFT JOIN IAS20261.CNTRY co ON c.CNTRY_NO = co.CNTRY_NO
                        LEFT JOIN CustBal cb ON c.C_CODE = cb.C_CODE
                    """
                cur.execute(query)
                for row in cur.fetchall():
                    customers.append({
                        "c_code": row[0],
                        "name": row[1],
                        "country": row[2] if row[2] else "",
                        "city": row[3] if row[3] else "",
                        "district": row[4] if row[4] else "",
                        "credit_limit": float(row[17]),
                        "actual_balance": float(row[5]) if row[5] else 0.0,
                        "phone": row[13] if row[13] else "",
                        "building_no": row[6] if row[6] else "",
                        "street": row[7] if row[7] else "",
                        "postal_code": row[8] if row[8] else "",
                        "additional_no": row[9] if row[9] else "",
                        "tax_number": row[10] if row[10] else "",
                        "cr_number": row[11] if row[11] else "",
                        "identifier": row[12] if row[12] else "",
                        "is_inactive": bool(row[22]),
                        "is_inactive_sales": bool(row[23])
                    })
        return jsonify({"status": "success", "data": customers})
    except Exception as e:
        print("Error fetching customers:", e)
        return jsonify({"status": "error", "message": str(e)}), 500

@customers_api_bp.route('/<c_code>/documents', methods=['GET'])
def list_documents(c_code):
    customer_dir = os.path.join(BASE_STORAGE, str(c_code))
    if not os.path.exists(customer_dir):
        return jsonify({"status": "success", "files": []})
    
    files = []
    for filename in os.listdir(customer_dir):
        if os.path.isfile(os.path.join(customer_dir, filename)):
            files.append(filename)
            
    return jsonify({"status": "success", "files": files})

@customers_api_bp.route('/<c_code>/documents', methods=['POST'])
def upload_document(c_code):
    if 'files' not in request.files:
        return jsonify({"status": "error", "message": "No files provided"}), 400
        
    uploaded_files = request.files.getlist('files')
    if not uploaded_files or uploaded_files[0].filename == '':
        return jsonify({"status": "error", "message": "Empty filename"}), 400
        
    customer_dir = os.path.join(BASE_STORAGE, str(c_code))
    if not os.path.exists(customer_dir):
        os.makedirs(customer_dir)
        
    saved_files = []
    for file in uploaded_files:
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file_path = os.path.join(customer_dir, filename)
            
            base_name = os.path.splitext(filename)[0]
            ext = os.path.splitext(filename)[1]
            counter = 1
            while os.path.exists(file_path):
                filename = f"{base_name} ({counter}){ext}"
                file_path = os.path.join(customer_dir, filename)
                counter += 1
                
            file.save(file_path)
            saved_files.append(filename)
            
    return jsonify({"status": "success", "message": f"{len(saved_files)} files uploaded successfully", "filenames": saved_files})

@customers_api_bp.route('/<c_code>/documents/rename', methods=['POST'])
def rename_document(c_code):
    data = request.json
    if not data or 'old_name' not in data or 'new_name' not in data:
        return jsonify({"status": "error", "message": "Missing names"}), 400
        
    old_name = data['old_name'].replace('/', '').replace('\\', '')
    new_name = data['new_name'].replace('/', '').replace('\\', '')
    
    customer_dir = os.path.join(BASE_STORAGE, str(c_code))
    old_path = os.path.join(customer_dir, old_name)
    
    # Extract extension from old name and append to new name if it doesn't have one
    ext = os.path.splitext(old_name)[1]
    if not new_name.lower().endswith(ext.lower()):
        new_name += ext
        
    new_path = os.path.join(customer_dir, new_name)
    
    if not os.path.exists(old_path):
        return jsonify({"status": "error", "message": "File not found"}), 404
        
    # Handle duplicate names by appending a counter
    base_name = os.path.splitext(new_name)[0]
    counter = 1
    while os.path.exists(new_path) and old_path != new_path:
        new_name = f"{base_name} ({counter}){ext}"
        new_path = os.path.join(customer_dir, new_name)
        counter += 1
        
    try:
        if old_path != new_path:
            os.rename(old_path, new_path)
        return jsonify({"status": "success", "new_name": new_name})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@customers_api_bp.route('/whatsapp/templates', methods=['GET'])
def get_whatsapp_templates():
    templates_path = os.path.join(ROOT_DIR, 'privet', 'onyx_reports', 'whatsapp_templates.json')
    try:
        if not os.path.exists(templates_path):
            return jsonify({"status": "error", "message": "Templates file not found"}), 404
            
        with open(templates_path, 'r', encoding='utf-8') as f:
            templates = json.load(f)
        return jsonify({"status": "success", "templates": templates})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
@customers_api_bp.route('/download/<c_code>/<filename>', methods=['GET'])
def download_document(c_code, filename):
    customer_dir = os.path.join(BASE_STORAGE, str(c_code))
    return send_from_directory(customer_dir, filename)

@customers_api_bp.route('/<c_code>/documents/<filename>', methods=['DELETE'])
def delete_document(c_code, filename):
    customer_dir = os.path.join(BASE_STORAGE, str(c_code))
    file_path = os.path.join(customer_dir, secure_filename(filename.replace('/', '').replace('\\', '')))
    
    if not os.path.exists(file_path):
        return jsonify({"status": "error", "message": "File not found"}), 404
        
    try:
        os.remove(file_path)
        return jsonify({"status": "success", "message": "File deleted successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
