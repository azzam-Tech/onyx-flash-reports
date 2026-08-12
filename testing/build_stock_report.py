import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn

def main():
    conn = get_conn()
    
    sql = """
    WITH item_groups AS (
        SELECT 
            m.I_CODE,
            m.I_NAME,
            gd.G_A_NAME AS main_grp,
            mg.MNG_A_NAME as sub_main_grp,
            sg.SUBG_A_NAME as sub_grp,
            dg.DETAIL_A_NAME as dtl_grp
        FROM IAS20261.IAS_ITM_MST m
        LEFT JOIN IAS20261.GROUP_DETAILS gd ON gd.G_CODE = m.G_CODE
        LEFT JOIN IAS20261.IAS_MAINSUB_GRP_DTL mg ON mg.MNG_CODE = m.MNG_CODE AND mg.G_CODE = m.G_CODE
        LEFT JOIN IAS20261.IAS_SUB_GRP_DTL sg ON sg.SUBG_CODE = m.SUBG_CODE AND sg.MNG_CODE = m.MNG_CODE AND sg.G_CODE = m.G_CODE
        LEFT JOIN IAS20261.IAS_DETAIL_GROUP dg ON dg.DET_I_CODE = m.DETAIL_NO AND dg.SUBG_CODE = m.SUBG_CODE AND dg.MNG_CODE = m.MNG_CODE AND dg.G_CODE = m.G_CODE
    ),
    inventory_mov AS (
        SELECT 
            I_CODE,
            W_CODE,
            SUM(CASE WHEN DOC_DATE < TO_DATE('2026-06-01', 'YYYY-MM-DD') THEN NVL(I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal,
            SUM(CASE WHEN DOC_DATE >= TO_DATE('2026-06-01', 'YYYY-MM-DD') AND DOC_DATE <= TO_DATE('2026-06-30', 'YYYY-MM-DD') AND IN_OUT = -1 THEN NVL(I_QTY,0) ELSE 0 END) as sales_qty,
            SUM(CASE WHEN DOC_DATE >= TO_DATE('2026-06-01', 'YYYY-MM-DD') AND DOC_DATE <= TO_DATE('2026-06-30', 'YYYY-MM-DD') AND IN_OUT = 1 THEN NVL(I_QTY,0) ELSE 0 END) as pur_qty,
            SUM(CASE WHEN DOC_DATE <= TO_DATE('2026-06-30', 'YYYY-MM-DD') THEN NVL(I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal
        FROM IAS20261.ITEM_MOVEMENT
        WHERE W_CODE IN (105, 103, 121, 122, 118, 108, 119)
        GROUP BY I_CODE, W_CODE
    )
    SELECT * FROM item_groups WHERE ROWNUM <= 5
    """
    
    df = pd.read_sql(sql, conn)
    print(df)

    conn.close()

if __name__ == "__main__":
    main()
