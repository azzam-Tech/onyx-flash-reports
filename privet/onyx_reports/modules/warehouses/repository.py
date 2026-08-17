# -*- coding: utf-8 -*-
from database import get_conn

MAIN_WAREHOUSES_CODES = ['105', '103', '121', '122', '118', '108', '119']

def get_warehouse_names():
    wh_mapping = {'105': 'الغنامية نصرالله', '103': 'الغنامية عيظه', '121': 'جده', '122': 'الشمال', '118': 'الجنوب', '108': 'المنصورية 1', '119': 'الدمام'}
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                codes_str = ','.join(MAIN_WAREHOUSES_CODES)
                cur.execute(f"SELECT W_CODE, W_NAME FROM IAS20261.WAREHOUSE_DETAILS WHERE W_CODE IN ({codes_str})")
                for w_code, w_name in cur.fetchall():
                    wh_mapping[str(w_code)] = w_name
    except Exception as e:
        print('Error fetching warehouse names dynamically:', e)
    return wh_mapping

def get_main_wh_movement_data(date_from_str, date_to_str, i_code_str):
    item_filter = ''
    params = {'df': date_from_str, 'dt': date_to_str}
    
    if i_code_str:
        item_filter = ' AND dt.I_CODE = :icode '
        params['icode'] = i_code_str

    sql = f'''
        SELECT
            dt.I_CODE,
            MAX(m.I_NAME),
            dt.W_CODE,
            SUM(NVL(dt.I_QTY, 0)) AS net_qty
        FROM IAS20261.ITEM_MOVEMENT dt
        LEFT JOIN IAS20261.IAS_ITM_MST m ON m.I_CODE = dt.I_CODE
        WHERE dt.I_DATE >= TO_DATE(:df, 'YYYY-MM-DD')
          AND dt.I_DATE < TO_DATE(:dt, 'YYYY-MM-DD') + 1
          AND dt.W_CODE IN (105, 103, 121, 122, 118, 108, 119)
          AND dt.IN_OUT = -1
          {item_filter}
        GROUP BY dt.I_CODE, dt.W_CODE
        HAVING SUM(NVL(dt.I_QTY, 0)) > 0
    '''
    
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall()

def get_detailed_stock_pivot_sql():
    return """
        WITH item_groups AS (
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
            GROUP BY m.I_CODE
        ),
        inventory_mov AS (
            SELECT 
                dt.I_CODE,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 105 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_105,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 103 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_103,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 121 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_121,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 122 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_122,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 118 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_118,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 108 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_108,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 119 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_119,
                SUM(CASE WHEN I_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as sales_qty,
                SUM(CASE WHEN I_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as sales_rtn_qty,
                SUM(CASE WHEN I_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as pur_qty,
                SUM(CASE WHEN I_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as pur_rtn_qty,
                
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 105 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_105,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 103 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_103,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 121 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_121,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 122 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_122,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 118 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_118,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 108 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_108,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 119 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_119
            FROM IAS20261.ITEM_MOVEMENT dt
            WHERE dt.W_CODE IN (105, 103, 121, 122, 118, 108, 119) OR dt.DOC_TYPE IN (1, 2, 3, 4)
            GROUP BY dt.I_CODE
        )
        SELECT 
            ig.main_grp AS "المجموعة الرئيسية",
            ig.sub_main_grp AS "الفرعية",
            ig.sub_grp AS "تحت الفرعية",
            ig.dtl_grp AS "التفصيلية",
            ig.I_CODE AS "رقم الصنف",
            ig.I_NAME AS "اسم الصنف",
            
            TO_CHAR(NVL(im.op_bal_105, 0), 'FM999,999,990.00') AS "افتتاحي 105",
            TO_CHAR(NVL(im.op_bal_103, 0), 'FM999,999,990.00') AS "افتتاحي 103",
            TO_CHAR(NVL(im.op_bal_121, 0), 'FM999,999,990.00') AS "افتتاحي 121",
            TO_CHAR(NVL(im.op_bal_122, 0), 'FM999,999,990.00') AS "افتتاحي 122",
            TO_CHAR(NVL(im.op_bal_118, 0), 'FM999,999,990.00') AS "افتتاحي 118",
            TO_CHAR(NVL(im.op_bal_108, 0), 'FM999,999,990.00') AS "افتتاحي 108",
            TO_CHAR(NVL(im.op_bal_119, 0), 'FM999,999,990.00') AS "افتتاحي 119",
            
            TO_CHAR(NVL(im.sales_qty, 0), 'FM999,999,990.00') AS "المبيعات",
            TO_CHAR(NVL(im.sales_rtn_qty, 0), 'FM999,999,990.00') AS "مردود المبيعات",
            TO_CHAR(NVL(im.pur_qty, 0), 'FM999,999,990.00') AS "المشتريات",
            TO_CHAR(NVL(im.pur_rtn_qty, 0), 'FM999,999,990.00') AS "مردود المشتريات",
            
            TO_CHAR(NVL(im.end_bal_105, 0), 'FM999,999,990.00') AS "نهائي 105",
            TO_CHAR(NVL(im.end_bal_103, 0), 'FM999,999,990.00') AS "نهائي 103",
            TO_CHAR(NVL(im.end_bal_121, 0), 'FM999,999,990.00') AS "نهائي 121",
            TO_CHAR(NVL(im.end_bal_122, 0), 'FM999,999,990.00') AS "نهائي 122",
            TO_CHAR(NVL(im.end_bal_118, 0), 'FM999,999,990.00') AS "نهائي 118",
            TO_CHAR(NVL(im.end_bal_108, 0), 'FM999,999,990.00') AS "نهائي 108",
            TO_CHAR(NVL(im.end_bal_119, 0), 'FM999,999,990.00') AS "نهائي 119"
            
        FROM item_groups ig
        JOIN inventory_mov im ON ig.I_CODE = im.I_CODE
        WHERE NVL(im.op_bal_105,0) <> 0 OR NVL(im.op_bal_103,0) <> 0 OR NVL(im.op_bal_121,0) <> 0 OR NVL(im.op_bal_122,0) <> 0 OR NVL(im.op_bal_118,0) <> 0 OR NVL(im.op_bal_108,0) <> 0 OR NVL(im.op_bal_119,0) <> 0
           OR NVL(im.sales_qty,0) <> 0 OR NVL(im.pur_qty,0) <> 0 OR NVL(im.sales_rtn_qty,0) <> 0 OR NVL(im.pur_rtn_qty,0) <> 0
           OR NVL(im.end_bal_105,0) <> 0 OR NVL(im.end_bal_103,0) <> 0 OR NVL(im.end_bal_121,0) <> 0 OR NVL(im.end_bal_122,0) <> 0 OR NVL(im.end_bal_118,0) <> 0 OR NVL(im.end_bal_108,0) <> 0 OR NVL(im.end_bal_119,0) <> 0
        ORDER BY ig.main_grp, ig.I_CODE
    """

def get_monthly_movement_pivot_sql():
    return """
        WITH item_groups AS (
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
            GROUP BY m.I_CODE
        ),
        inventory_mov AS (
            SELECT 
                dt.I_CODE,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '01' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m01_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '01' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m01_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '01' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m01_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '01' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m01_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '02' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m02_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '02' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m02_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '02' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m02_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '02' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m02_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '03' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m03_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '03' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m03_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '03' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m03_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '03' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m03_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '04' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m04_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '04' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m04_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '04' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m04_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '04' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m04_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '05' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m05_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '05' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m05_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '05' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m05_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '05' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m05_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '06' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m06_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '06' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m06_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '06' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m06_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '06' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m06_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '07' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m07_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '07' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m07_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '07' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m07_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '07' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m07_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '08' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m08_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '08' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m08_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '08' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m08_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '08' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m08_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '09' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m09_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '09' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m09_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '09' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m09_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '09' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m09_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '10' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m10_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '10' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m10_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '10' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m10_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '10' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m10_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '11' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m11_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '11' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m11_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '11' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m11_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '11' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m11_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '12' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m12_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '12' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m12_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '12' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m12_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '12' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m12_pur_rtn
            FROM IAS20261.ITEM_MOVEMENT dt
            WHERE dt.DOC_TYPE IN (1, 2, 3, 4) AND TO_CHAR(dt.I_DATE, 'YYYY') = :p_year
            GROUP BY dt.I_CODE
        )
        SELECT 
            ig.main_grp AS "المجموعة الرئيسية",
            ig.sub_main_grp AS "الفرعية",
            ig.sub_grp AS "تحت الفرعية",
            ig.dtl_grp AS "التفصيلية",
            ig.I_CODE AS "رقم الصنف",
            ig.I_NAME AS "اسم الصنف",
            TO_CHAR(NVL(im.m01_sales, 0), 'FM999,999,990.00') AS "مبيعات ش1",
            TO_CHAR(NVL(im.m01_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش1",
            TO_CHAR(NVL(im.m01_pur, 0), 'FM999,999,990.00') AS "مشتريات ش1",
            TO_CHAR(NVL(im.m01_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش1",
            TO_CHAR(NVL(im.m02_sales, 0), 'FM999,999,990.00') AS "مبيعات ش2",
            TO_CHAR(NVL(im.m02_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش2",
            TO_CHAR(NVL(im.m02_pur, 0), 'FM999,999,990.00') AS "مشتريات ش2",
            TO_CHAR(NVL(im.m02_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش2",
            TO_CHAR(NVL(im.m03_sales, 0), 'FM999,999,990.00') AS "مبيعات ش3",
            TO_CHAR(NVL(im.m03_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش3",
            TO_CHAR(NVL(im.m03_pur, 0), 'FM999,999,990.00') AS "مشتريات ش3",
            TO_CHAR(NVL(im.m03_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش3",
            TO_CHAR(NVL(im.m04_sales, 0), 'FM999,999,990.00') AS "مبيعات ش4",
            TO_CHAR(NVL(im.m04_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش4",
            TO_CHAR(NVL(im.m04_pur, 0), 'FM999,999,990.00') AS "مشتريات ش4",
            TO_CHAR(NVL(im.m04_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش4",
            TO_CHAR(NVL(im.m05_sales, 0), 'FM999,999,990.00') AS "مبيعات ش5",
            TO_CHAR(NVL(im.m05_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش5",
            TO_CHAR(NVL(im.m05_pur, 0), 'FM999,999,990.00') AS "مشتريات ش5",
            TO_CHAR(NVL(im.m05_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش5",
            TO_CHAR(NVL(im.m06_sales, 0), 'FM999,999,990.00') AS "مبيعات ش6",
            TO_CHAR(NVL(im.m06_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش6",
            TO_CHAR(NVL(im.m06_pur, 0), 'FM999,999,990.00') AS "مشتريات ش6",
            TO_CHAR(NVL(im.m06_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش6",
            TO_CHAR(NVL(im.m07_sales, 0), 'FM999,999,990.00') AS "مبيعات ش7",
            TO_CHAR(NVL(im.m07_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش7",
            TO_CHAR(NVL(im.m07_pur, 0), 'FM999,999,990.00') AS "مشتريات ش7",
            TO_CHAR(NVL(im.m07_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش7",
            TO_CHAR(NVL(im.m08_sales, 0), 'FM999,999,990.00') AS "مبيعات ش8",
            TO_CHAR(NVL(im.m08_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش8",
            TO_CHAR(NVL(im.m08_pur, 0), 'FM999,999,990.00') AS "مشتريات ش8",
            TO_CHAR(NVL(im.m08_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش8",
            TO_CHAR(NVL(im.m09_sales, 0), 'FM999,999,990.00') AS "مبيعات ش9",
            TO_CHAR(NVL(im.m09_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش9",
            TO_CHAR(NVL(im.m09_pur, 0), 'FM999,999,990.00') AS "مشتريات ش9",
            TO_CHAR(NVL(im.m09_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش9",
            TO_CHAR(NVL(im.m10_sales, 0), 'FM999,999,990.00') AS "مبيعات ش10",
            TO_CHAR(NVL(im.m10_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش10",
            TO_CHAR(NVL(im.m10_pur, 0), 'FM999,999,990.00') AS "مشتريات ش10",
            TO_CHAR(NVL(im.m10_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش10",
            TO_CHAR(NVL(im.m11_sales, 0), 'FM999,999,990.00') AS "مبيعات ش11",
            TO_CHAR(NVL(im.m11_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش11",
            TO_CHAR(NVL(im.m11_pur, 0), 'FM999,999,990.00') AS "مشتريات ش11",
            TO_CHAR(NVL(im.m11_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش11",
            TO_CHAR(NVL(im.m12_sales, 0), 'FM999,999,990.00') AS "مبيعات ش12",
            TO_CHAR(NVL(im.m12_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش12",
            TO_CHAR(NVL(im.m12_pur, 0), 'FM999,999,990.00') AS "مشتريات ش12",
            TO_CHAR(NVL(im.m12_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش12"
        FROM item_groups ig
        JOIN inventory_mov im ON ig.I_CODE = im.I_CODE
        ORDER BY ig.main_grp, ig.I_CODE
    """

def get_warehouse_rebalancing_sql():
    return """
        WITH wh_stock AS (
            SELECT mv.I_CODE, mv.W_CODE,
                   SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) as qty
            FROM IAS20261.ITEM_MOVEMENT mv
            WHERE mv.W_CODE IN ('105', '103', '121', '122', '118', '108', '119')
              AND mv.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1
            GROUP BY mv.I_CODE, mv.W_CODE
        ),
        item_matrix AS (
            SELECT I_CODE,
                   SUM(CASE WHEN W_CODE = '105' THEN qty ELSE 0 END) as w_105,
                   SUM(CASE WHEN W_CODE = '103' THEN qty ELSE 0 END) as w_103,
                   SUM(CASE WHEN W_CODE = '121' THEN qty ELSE 0 END) as w_121,
                   SUM(CASE WHEN W_CODE = '122' THEN qty ELSE 0 END) as w_122,
                   SUM(CASE WHEN W_CODE = '118' THEN qty ELSE 0 END) as w_118,
                   SUM(CASE WHEN W_CODE = '108' THEN qty ELSE 0 END) as w_108,
                   SUM(CASE WHEN W_CODE = '119' THEN qty ELSE 0 END) as w_119,
                   MAX(qty) as max_qty,
                   MIN(qty) as min_qty,
                   SUM(qty) as tot_qty
            FROM wh_stock
            GROUP BY I_CODE
            HAVING SUM(qty) > 0
        )
        SELECT m.I_CODE AS "رمز الصنف",
               i.I_NAME AS "اسم الصنف",
               TO_CHAR(m.tot_qty, 'FM999,999,990') AS "إجمالي الأرصدة (كل الفروع)",
               TO_CHAR(m.w_103, 'FM999,999,990') AS "الغنامية عيظه (103)",
               TO_CHAR(m.w_121, 'FM999,999,990') AS "جده (121)",
               TO_CHAR(m.w_122, 'FM999,999,990') AS "الشمال (122)",
               TO_CHAR(m.w_105, 'FM999,999,990') AS "الغنامية نصرالله (105)",
               TO_CHAR(m.w_118, 'FM999,999,990') AS "الجنوب خميس مشيط (118)",
               TO_CHAR(m.w_119, 'FM999,999,990') AS "الدمام (119)",
               TO_CHAR(m.w_108, 'FM999,999,990') AS "المنصورية 1 (108)"
        FROM item_matrix m
        JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE = m.I_CODE
        WHERE m.min_qty = 0 AND m.max_qty > 0
          AND (:i_code IS NULL OR m.I_CODE = :i_code)
        ORDER BY m.tot_qty DESC
      """

def get_dead_stock_value_sql():
    return """
        WITH stock_movements AS (
            SELECT mv.W_CODE,
                   mv.I_CODE,
                   SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) as qty,
                   MAX(NVL(mv.STK_COST,0)) as unit_cost,
                   MAX(CASE WHEN NVL(mv.IN_OUT,0) <> 1 THEN mv.I_DATE END) as last_out_date
            FROM IAS20261.ITEM_MOVEMENT mv
            WHERE mv.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1
            GROUP BY mv.W_CODE, mv.I_CODE
            HAVING SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) > 0
        )
        SELECT s.W_CODE AS "رقم المستودع",
               MAX(w.W_A_NAME) AS "اسم المستودع",
               COUNT(s.I_CODE) AS "عدد الأصناف",
               TO_CHAR(SUM(s.qty), 'FM999,999,990.00') AS "الكمية",
               TO_CHAR(SUM(s.qty * s.unit_cost), 'FM999,999,990.00') AS "القيمة المالية"
        FROM stock_movements s
        LEFT JOIN (
           SELECT '103' as W_CODE, 'الغنامية عيظه' as W_A_NAME FROM DUAL UNION ALL
           SELECT '121' as W_CODE, 'جده' as W_A_NAME FROM DUAL UNION ALL
           SELECT '122' as W_CODE, 'الشمال' as W_A_NAME FROM DUAL UNION ALL
           SELECT '105' as W_CODE, 'الغنامية نصرالله' as W_A_NAME FROM DUAL UNION ALL
           SELECT '118' as W_CODE, 'الجنوب خميس مشيط' as W_A_NAME FROM DUAL UNION ALL
           SELECT '119' as W_CODE, 'الدمام' as W_A_NAME FROM DUAL UNION ALL
           SELECT '108' as W_CODE, 'المنصورية 1' as W_A_NAME FROM DUAL
        ) w ON w.W_CODE = TO_CHAR(s.W_CODE)
        WHERE (TRUNC(TO_DATE(:as_of,'YYYY-MM-DD')) - TRUNC(s.last_out_date) >= :days
               OR s.last_out_date IS NULL)
        GROUP BY s.W_CODE
        ORDER BY SUM(s.qty * s.unit_cost) DESC
      """

def get_smart_replenishment_sql():
    return """
        WITH stock AS (
            SELECT mv.I_CODE, 
                   MAX(i.I_NAME) as I_NAME,
                   SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) as current_qty
            FROM IAS20261.ITEM_MOVEMENT mv
            LEFT JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE = mv.I_CODE
            WHERE mv.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1
            AND (:i_code IS NULL OR mv.I_CODE = :i_code)
            GROUP BY mv.I_CODE
            HAVING SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) > 0
        ),
        sales AS (
            SELECT dt.I_CODE, 
                   SUM(CASE WHEN dt.IN_OUT = -1 AND dt.DOC_TYPE IN (1, 7) THEN NVL(dt.I_QTY,0) 
                            WHEN dt.IN_OUT = 1 AND dt.DOC_TYPE = 3 THEN -NVL(dt.I_QTY,0) 
                            ELSE 0 END) as sold_qty
            FROM IAS20261.ITEM_MOVEMENT dt
            WHERE dt.I_DATE >= TO_DATE(:as_of,'YYYY-MM-DD') - :days 
              AND dt.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1
              AND (:i_code IS NULL OR dt.I_CODE = :i_code)
            GROUP BY dt.I_CODE
        )
        SELECT s.I_CODE AS "رمز الصنف", 
               s.I_NAME AS "اسم الصنف",
               TO_CHAR(s.current_qty, 'FM999,999,990.00') AS "الرصيد الحالي",
               TO_CHAR(NVL(sa.sold_qty, 0), 'FM999,999,990.00') AS "إجمالي السحب",
               TO_CHAR(NVL(sa.sold_qty, 0) / :days, 'FM999,999,990.00') AS "متوسط السحب اليومي",
               CASE WHEN NVL(sa.sold_qty, 0) > 0 THEN
                  TO_CHAR(s.current_qty / (sa.sold_qty / :days), 'FM999,999,990')
               ELSE 'ركود تام' END AS "أيام التغطية المتبقية",
               CASE 
                  WHEN NVL(sa.sold_qty, 0) <= 0 THEN 'مكدس (لا يوجد سحب)'
                  WHEN (s.current_qty / (sa.sold_qty / :days)) < 15 THEN 'حرج (شراء فوري)'
                  WHEN (s.current_qty / (sa.sold_qty / :days)) <= 60 THEN 'مستقر'
                  ELSE 'مكدس (فائض)'
               END AS "حالة الصنف"
        FROM stock s
        LEFT JOIN sales sa ON sa.I_CODE = s.I_CODE
        ORDER BY 
            CASE 
               WHEN NVL(sa.sold_qty, 0) <= 0 THEN 999999
               ELSE s.current_qty / (sa.sold_qty / :days) 
            END ASC
        """

def get_stock_bal_sql():
    return """
      SELECT * FROM (
        SELECT mv.I_CODE AS "كود الصنف", MAX(i.I_NAME) AS "اسم الصنف",
               TO_CHAR(SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))),'FM999,999,990.00') AS "الرصيد",
               TO_CHAR(SUM(CASE WHEN mv.W_CODE = '103' THEN DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0)) ELSE 0 END), 'FM999,999,990.00') AS "الغنامية عيظه (103)",
               TO_CHAR(SUM(CASE WHEN mv.W_CODE = '121' THEN DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0)) ELSE 0 END), 'FM999,999,990.00') AS "جده (121)",
               TO_CHAR(SUM(CASE WHEN mv.W_CODE = '122' THEN DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0)) ELSE 0 END), 'FM999,999,990.00') AS "الشمال (122)",
               TO_CHAR(SUM(CASE WHEN mv.W_CODE = '105' THEN DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0)) ELSE 0 END), 'FM999,999,990.00') AS "الغنامية نصرالله (105)",
               TO_CHAR(SUM(CASE WHEN mv.W_CODE = '118' THEN DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0)) ELSE 0 END), 'FM999,999,990.00') AS "الجنوب خميس مشيط (118)",
               TO_CHAR(SUM(CASE WHEN mv.W_CODE = '119' THEN DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0)) ELSE 0 END), 'FM999,999,990.00') AS "الدمام (119)",
               TO_CHAR(SUM(CASE WHEN mv.W_CODE = '108' THEN DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0)) ELSE 0 END), 'FM999,999,990.00') AS "المنصورية 1 (108)",
               TO_CHAR(SUM(CASE WHEN mv.W_CODE NOT IN ('103','121','122','105','118','119','108') THEN DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0)) ELSE 0 END), 'FM999,999,990.00') AS "مستودعات أخرى",
               TO_CHAR(SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))*NVL(mv.STK_COST,0)),'FM999,999,999,990.00') AS "قيمة الرصيد (تقريبية)"
        FROM IAS20261.ITEM_MOVEMENT mv LEFT JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE=mv.I_CODE
        WHERE mv.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1
          AND (:w_code IS NULL OR mv.W_CODE = :w_code)
          AND (:i_code IS NULL OR mv.I_CODE = :i_code)
        GROUP BY mv.I_CODE HAVING SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))) <> 0
        ORDER BY SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))*NVL(mv.STK_COST,0)) DESC
      ) """

def get_stock_move_sql():
    return """
      SELECT * FROM (
        SELECT TO_CHAR(mv.I_DATE,'DD/MM/YYYY') AS "التاريخ", mv.DOC_NO AS "المستند",
               CASE NVL(mv.IN_OUT,0) WHEN 1 THEN 'وارد' ELSE 'صادر' END AS "الاتجاه",
               TO_CHAR(NVL(mv.I_QTY,0),'FM999,999,990.00') AS "الكمية",
               TO_CHAR(NVL(mv.STK_COST,0),'FM999,999,990.00') AS "التكلفة",
               mv.W_CODE AS "المستودع"
        FROM IAS20261.ITEM_MOVEMENT mv
        WHERE mv.I_CODE = :i_code
          AND mv.I_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND mv.I_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        ORDER BY mv.I_DATE, mv.DOC_NO
      ) """

def get_stock_dormant_sql():
    return """
      WITH item_stats AS (
        SELECT mv.I_CODE,
               MAX(i.I_NAME) AS I_NAME,
               SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) AS total_bal,
               SUM(CASE WHEN mv.W_CODE = '103' THEN DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0)) ELSE 0 END) AS bal_103,
               SUM(CASE WHEN mv.W_CODE = '105' THEN DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0)) ELSE 0 END) AS bal_105,
               SUM(CASE WHEN mv.W_CODE = '108' THEN DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0)) ELSE 0 END) AS bal_108,
               SUM(CASE WHEN mv.W_CODE = '118' THEN DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0)) ELSE 0 END) AS bal_118,
               SUM(CASE WHEN mv.W_CODE = '119' THEN DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0)) ELSE 0 END) AS bal_119,
               SUM(CASE WHEN mv.W_CODE = '121' THEN DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0)) ELSE 0 END) AS bal_121,
               SUM(CASE WHEN mv.W_CODE = '122' THEN DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0)) ELSE 0 END) AS bal_122,
               MAX(CASE WHEN mv.DOC_TYPE IN (1, 7) AND NVL(mv.IN_OUT,0) = -1 THEN mv.I_DATE END) AS last_sale_date,
               SUM(CASE WHEN NVL(mv.IN_OUT,0) = 1 THEN NVL(mv.I_QTY,0) ELSE 0 END) AS total_in,
               SUM(CASE WHEN NVL(mv.IN_OUT,0) = -1 AND mv.DOC_TYPE IN (1, 7) THEN NVL(mv.I_QTY,0) 
                        WHEN NVL(mv.IN_OUT,0) = 1 AND mv.DOC_TYPE = 3 THEN -NVL(mv.I_QTY,0) ELSE 0 END) AS total_sales
        FROM IAS20261.ITEM_MOVEMENT mv 
        LEFT JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE = mv.I_CODE
        WHERE mv.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1
        GROUP BY mv.I_CODE
        HAVING SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) > 0
      )
      SELECT I_CODE AS "كود الصنف",
             I_NAME AS "اسم الصنف",
             TO_CHAR(total_bal, 'FM999,999,990.00') AS "إجمالي الرصيد",
             TO_CHAR(bal_103, 'FM999,999,990.00') AS "الغنامية عيظه (103)",
             TO_CHAR(bal_105, 'FM999,999,990.00') AS "الغنامية نصرالله (105)",
             TO_CHAR(bal_108, 'FM999,999,990.00') AS "المنصورية 1 (108)",
             TO_CHAR(bal_118, 'FM999,999,990.00') AS "الجنوب خميس مشيط (118)",
             TO_CHAR(bal_119, 'FM999,999,990.00') AS "الدمام (119)",
             TO_CHAR(bal_121, 'FM999,999,990.00') AS "جده (121)",
             TO_CHAR(bal_122, 'FM999,999,990.00') AS "الشمال (122)",
             TO_CHAR(last_sale_date, 'DD/MM/YYYY') AS "آخر صرف",
             TRUNC(TO_DATE(:as_of,'YYYY-MM-DD')) - TRUNC(last_sale_date) AS "أيام منذ آخر صرف",
             TO_CHAR(ROUND(NVL((NVL(total_sales,0) / NULLIF(total_in, 0)) * 100, 0), 2), 'FM990.00') || '%' AS "نسبة المبيعات للوارد"
      FROM item_stats
      WHERE 
          ( last_sale_date IS NULL OR TRUNC(TO_DATE(:as_of,'YYYY-MM-DD')) - TRUNC(last_sale_date) >= :days )
          AND 
          ( NVL(total_sales, 0) <= 0 OR NVL((NVL(total_sales,0) / NULLIF(total_in, 0)) * 100, 0) <= :dormancy_pct )
      ORDER BY total_bal DESC"""

