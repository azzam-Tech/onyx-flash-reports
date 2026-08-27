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
            FROM IAS_ITM_MST m
            LEFT JOIN GROUP_DETAILS gd ON gd.G_CODE = m.G_CODE
            LEFT JOIN IAS_MAINSUB_GRP_DTL mg ON mg.MNG_CODE = m.MNG_CODE AND mg.G_CODE = m.G_CODE
            LEFT JOIN IAS_SUB_GRP_DTL sg ON sg.SUBG_CODE = m.SUBG_CODE
            LEFT JOIN IAS_DETAIL_GROUP dg ON dg.DETAIL_NO = m.DETAIL_NO
            GROUP BY m.I_CODE
        ),
        inventory_mov AS (
            SELECT 
                dt.I_CODE,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '01' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '01' AND DOC_TYPE = 3 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m01_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '01' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '01' AND DOC_TYPE = 4 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m01_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '02' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '02' AND DOC_TYPE = 3 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m02_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '02' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '02' AND DOC_TYPE = 4 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m02_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '03' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '03' AND DOC_TYPE = 3 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m03_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '03' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '03' AND DOC_TYPE = 4 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m03_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '04' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '04' AND DOC_TYPE = 3 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m04_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '04' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '04' AND DOC_TYPE = 4 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m04_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '05' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '05' AND DOC_TYPE = 3 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m05_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '05' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '05' AND DOC_TYPE = 4 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m05_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '06' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '06' AND DOC_TYPE = 3 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m06_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '06' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '06' AND DOC_TYPE = 4 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m06_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '07' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '07' AND DOC_TYPE = 3 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m07_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '07' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '07' AND DOC_TYPE = 4 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m07_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '08' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '08' AND DOC_TYPE = 3 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m08_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '08' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '08' AND DOC_TYPE = 4 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m08_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '09' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '09' AND DOC_TYPE = 3 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m09_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '09' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '09' AND DOC_TYPE = 4 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m09_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '10' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '10' AND DOC_TYPE = 3 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m10_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '10' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '10' AND DOC_TYPE = 4 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m10_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '11' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '11' AND DOC_TYPE = 3 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m11_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '11' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '11' AND DOC_TYPE = 4 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m11_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '12' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '12' AND DOC_TYPE = 3 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m12_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '12' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) WHEN TO_CHAR(I_DATE, 'MM') = '12' AND DOC_TYPE = 4 THEN -NVL(dt.I_QTY,0) ELSE 0 END) as m12_pur
            FROM ITEM_MOVEMENT dt
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
            TO_CHAR(NVL(im.m01_pur, 0), 'FM999,999,990.00') AS "مشتريات ش1",
            TO_CHAR(NVL(im.m02_sales, 0), 'FM999,999,990.00') AS "مبيعات ش2",
            TO_CHAR(NVL(im.m02_pur, 0), 'FM999,999,990.00') AS "مشتريات ش2",
            TO_CHAR(NVL(im.m03_sales, 0), 'FM999,999,990.00') AS "مبيعات ش3",
            TO_CHAR(NVL(im.m03_pur, 0), 'FM999,999,990.00') AS "مشتريات ش3",
            TO_CHAR(NVL(im.m04_sales, 0), 'FM999,999,990.00') AS "مبيعات ش4",
            TO_CHAR(NVL(im.m04_pur, 0), 'FM999,999,990.00') AS "مشتريات ش4",
            TO_CHAR(NVL(im.m05_sales, 0), 'FM999,999,990.00') AS "مبيعات ش5",
            TO_CHAR(NVL(im.m05_pur, 0), 'FM999,999,990.00') AS "مشتريات ش5",
            TO_CHAR(NVL(im.m06_sales, 0), 'FM999,999,990.00') AS "مبيعات ش6",
            TO_CHAR(NVL(im.m06_pur, 0), 'FM999,999,990.00') AS "مشتريات ش6",
            TO_CHAR(NVL(im.m07_sales, 0), 'FM999,999,990.00') AS "مبيعات ش7",
            TO_CHAR(NVL(im.m07_pur, 0), 'FM999,999,990.00') AS "مشتريات ش7",
            TO_CHAR(NVL(im.m08_sales, 0), 'FM999,999,990.00') AS "مبيعات ش8",
            TO_CHAR(NVL(im.m08_pur, 0), 'FM999,999,990.00') AS "مشتريات ش8",
            TO_CHAR(NVL(im.m09_sales, 0), 'FM999,999,990.00') AS "مبيعات ش9",
            TO_CHAR(NVL(im.m09_pur, 0), 'FM999,999,990.00') AS "مشتريات ش9",
            TO_CHAR(NVL(im.m10_sales, 0), 'FM999,999,990.00') AS "مبيعات ش10",
            TO_CHAR(NVL(im.m10_pur, 0), 'FM999,999,990.00') AS "مشتريات ش10",
            TO_CHAR(NVL(im.m11_sales, 0), 'FM999,999,990.00') AS "مبيعات ش11",
            TO_CHAR(NVL(im.m11_pur, 0), 'FM999,999,990.00') AS "مشتريات ش11",
            TO_CHAR(NVL(im.m12_sales, 0), 'FM999,999,990.00') AS "مبيعات ش12",
            TO_CHAR(NVL(im.m12_pur, 0), 'FM999,999,990.00') AS "مشتريات ش12"
        FROM item_groups ig
        JOIN inventory_mov im ON ig.I_CODE = im.I_CODE
        ORDER BY ig.main_grp, ig.I_CODE
    """
