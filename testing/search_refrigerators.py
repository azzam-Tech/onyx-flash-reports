import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            tables = [
                'IAS_MAINSUB_GRP_DTL',
                'IAS_SUB_GRP_DTL',
                'IAS_GRP_ITM_LVL',
                'IAS_GRP_ITM_LVL_TREE',
                'GLS_AC_CODE_DTL_GRPS',
                'IAS_ITM_MST'
            ]
            
            for t in tables:
                cur.execute(f"""
                    SELECT COLUMN_NAME 
                    FROM ALL_TAB_COLUMNS 
                    WHERE OWNER = 'IAS20261' AND TABLE_NAME = '{t}' 
                      AND DATA_TYPE IN ('VARCHAR2', 'NVARCHAR2', 'CHAR')
                """)
                cols = [c[0] for c in cur.fetchall()]
                
                for c in cols:
                    try:
                        cur.execute(f"SELECT COUNT(*) FROM {t} WHERE {c} LIKE '%الثلاجات%'")
                        cnt = cur.fetchone()[0]
                        if cnt > 0:
                            print(f"Found 'الثلاجات' in table {t}, column {c} (Count: {cnt})")
                            cur.execute(f"SELECT * FROM {t} WHERE {c} LIKE '%الثلاجات%' FETCH FIRST 3 ROWS ONLY")
                            for r in cur.fetchall():
                                print("  ", r)
                    except Exception as e:
                        # some columns might be restricted or error out
                        pass
            
except Exception as e:
    print(f"Error: {e}")
