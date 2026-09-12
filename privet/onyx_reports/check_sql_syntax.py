from database import get_conn
import sys

with get_conn() as con:
    with con.cursor() as cur:
        query = """
                    SELECT 
                        c.C_CODE,
                        c.C_A_NAME,
                        co.CNTRY_A_NAME,
                        ci.CITY_A_NAME,
                        c.DSTRCT_NM,
                        (SELECT NVL(SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)), 0) 
                         FROM IAS20261.IAS_POST_DTL 
                         WHERE (C_CODE = c.C_CODE OR C_V_CODE = TO_CHAR(c.C_CODE) OR V_C_CODE = TO_CHAR(c.C_CODE)) 
                         AND NVL(DOC_POST,0) = 1) as ACTUAL_BALANCE,
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
                    WHERE ROWNUM <= 2
        """
        try:
            cur.execute(query)
            print("Query successful!")
            print(cur.fetchall())
        except Exception as e:
            print("ERROR:", e)
