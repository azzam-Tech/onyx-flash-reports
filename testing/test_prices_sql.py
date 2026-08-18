import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def test_sql():
    sql = """
        SELECT 
            G.G_A_NAME AS "المجموعة الرئيسية",
            I.I_CODE AS "كود الصنف",
            I.I_NAME AS "اسم الصنف",
            NVL((SELECT MAX(P.I_PRICE) FROM IAS_ITEM_PRICE P WHERE P.I_CODE = I.I_CODE AND P.LEV_NO = 2), 0) AS "التكلفة علينا",
            NVL((SELECT MAX(P.I_PRICE) FROM IAS_ITEM_PRICE P WHERE P.I_CODE = I.I_CODE AND P.LEV_NO = 1), 0) AS "الحد الادنى",
            NVL((SELECT SUM(M.I_QTY * NVL(M.IN_OUT, 1)) FROM ITEM_MOVEMENT M WHERE M.I_CODE = I.I_CODE AND M.W_CODE IN ('103','105','108')), 0) AS "الكمية (الرياض)",
            NVL((SELECT SUM(M.I_QTY * NVL(M.IN_OUT, 1)) FROM ITEM_MOVEMENT M WHERE M.I_CODE = I.I_CODE AND M.W_CODE = '118'), 0) AS "الكمية (الجنوب)",
            NVL((SELECT SUM(M.I_QTY * NVL(M.IN_OUT, 1)) FROM ITEM_MOVEMENT M WHERE M.I_CODE = I.I_CODE AND M.W_CODE = '122'), 0) AS "الكمية (الشمال)",
            NVL((SELECT SUM(M.I_QTY * NVL(M.IN_OUT, 1)) FROM ITEM_MOVEMENT M WHERE M.I_CODE = I.I_CODE AND M.W_CODE = '121'), 0) AS "الكمية (جدة)",
            NVL((SELECT SUM(M.I_QTY * NVL(M.IN_OUT, 1)) FROM ITEM_MOVEMENT M WHERE M.I_CODE = I.I_CODE AND M.W_CODE = '119'), 0) AS "الكمية (الدمام)"
        FROM IAS_ITM_MST I
        LEFT JOIN GROUP_DETAILS G ON G.G_CODE = I.G_CODE
        WHERE ROWNUM <= 20
        ORDER BY I.G_CODE, I.I_CODE
    """
    
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
            print(f"Fetched {len(rows)} rows.")
            for r in rows:
                print(r)

if __name__ == '__main__':
    test_sql()
