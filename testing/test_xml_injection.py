import os
import sys
from dotenv import load_dotenv
os.environ["NLS_LANG"] = "ARABIC_SAUDI ARABIA.AR8MSWIN1256"

# Add zatca_printer to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'zatca_printer')))

load_dotenv(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'zatca_printer', '.env')))

from app.database import get_conn
import oracledb

def build_xml(sys_no=70):
    xml = f"""
    <BILL>
        <IAS_BILL_MST>
            <SYS_NO>70</SYS_NO>
            <BRN_NO>1</BRN_NO>
            <DOC_NO>0</DOC_NO>
            <DOC_SER_EXTRNL>12345</DOC_SER_EXTRNL>
            <DOC_DATE>06/09/2026</DOC_DATE>
            <REP_CODE>144</REP_CODE>
            <EXTERNAL_POST>70</EXTERNAL_POST>
            <SI_TYPE>1</SI_TYPE>
            <C_CODE>2303</C_CODE>
            <CUR_CODE>SAR</CUR_CODE>
            <E_INVC_MTHD_NO>3</E_INVC_MTHD_NO>
            <BILL_DOC_TYPE>5</BILL_DOC_TYPE>
            <CLC_TYP_NO_TAX>5</CLC_TYP_NO_TAX>
            <W_CODE>144</W_CODE>
            <CC_CODE>144</CC_CODE>
            <VAT_AMT>22.5</VAT_AMT>
            <AD_U_ID>144</AD_U_ID>
            <BRN_USR>1</BRN_USR>
        </IAS_BILL_MST>
        <IAS_BILL_DTL>
            <I_CODE>GSRF-92DF</I_CODE>
            <W_CODE>144</W_CODE>
            <I_QTY>1</I_QTY>
            <P_QTY>1</P_QTY>
            <P_SIZE>1</P_SIZE>
            <I_PRICE>150.0</I_PRICE>
            <VAT_PER>15</VAT_PER>
            <VAT_AMT>22.5</VAT_AMT>
            <RCRD_NO>1</RCRD_NO>
            <SI_TYPE>1</SI_TYPE>
            <EXTERNAL_POST>70</EXTERNAL_POST>
        </IAS_BILL_DTL>
    </BILL>
    """
    return xml.strip()

def test_insert_invoice():
    import json
    print("Testing Oracle XML Injection...")
    
    conn = get_conn(readonly=False)
    try:
        with conn.cursor() as cur:
            sys_no = 70
            print(f"Using SYS_NO: {sys_no}")
            
            xml_payload = build_xml(sys_no)
            
            p_json_rslt = cur.var(oracledb.DB_TYPE_VARCHAR)
            
            p_xml = cur.var(oracledb.DB_TYPE_CLOB)
            p_xml.setvalue(0, xml_payload)
            
            print(f"Calling INSRT_DOC_INTO_ONYX with payload: {xml_payload}")
            
            cur.callproc('ARS_API_TRNS_PKG.INSRT_DOC_INTO_ONYX', [
                5,      # P_Doc_Typ (5 for credit sales invoice)
                1,      # P_COMMIT_FLG (0 for ROLLBACK, 1 for COMMIT)
                0,      # P_CLC_TAX_METHOD (0 for Ext Calc Tax when Offline)
                1,      # P_Lng_No (1 for Arabic)
                p_xml,  # P_Xml
                p_json_rslt # P_Json_Rslt
            ])
            
            result = p_json_rslt.getvalue()
            with open("test_result.json", "w", encoding="utf-8") as f:
                f.write(result)
            print(f"Result JSON written to test_result.json")
            
            # Check if invoice was created and delete it immediately
            try:
                res_dict = json.loads(result)
                doc_ser_str = res_dict.get("_Result", {}).get("_Doc_Ser", "")
                if doc_ser_str:
                    doc_ser = int(doc_ser_str)
                    print(f"Invoice created with Doc Ser: {doc_ser}. Deleting it now to ensure no data is saved...")
                    
                    p_msg_txt = cur.var(oracledb.DB_TYPE_VARCHAR)
                    p_err_no = cur.var(oracledb.DB_TYPE_VARCHAR)
                    p_pkg_nm = cur.var(oracledb.DB_TYPE_VARCHAR)
                    
                    # Delete_Bill (P_Doc_Typ, P_Doc_Ser, P_Msg_Txt OUT, P_Err_No OUT, P_Pkg_Nm OUT)
                    cur.callproc('ARS_API_TRNS_PKG.Delete_Bill', [5, doc_ser, p_msg_txt, p_err_no, p_pkg_nm])
                    print(f"Delete_Bill called. ErrNo: {p_err_no.getvalue()}, Msg: {p_msg_txt.getvalue()}")
            except Exception as e:
                print(f"Error parsing result or deleting bill: {e}")
            
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        print("Closing connection...")
        conn.close()

if __name__ == '__main__':
    test_insert_invoice()
