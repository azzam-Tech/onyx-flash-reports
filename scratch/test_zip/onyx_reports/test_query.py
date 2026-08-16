import database
con = database.get_conn()
cur = con.cursor()
cur.execute("""
SELECT DOC_TYPE, IN_OUT, SUM(I_QTY) 
FROM IAS20261.ITEM_MOVEMENT 
WHERE I_CODE = 'FA-M120WU' 
AND W_CODE IN (105, 103, 121, 122, 118, 108, 119) 
AND I_DATE >= TO_DATE('2026-01-01', 'YYYY-MM-DD') 
AND I_DATE <= TO_DATE('2026-12-31', 'YYYY-MM-DD') 
GROUP BY DOC_TYPE, IN_OUT
""")
print("In 7 central warehouses:", cur.fetchall())

cur.execute("""
SELECT DOC_TYPE, IN_OUT, SUM(I_QTY) 
FROM IAS20261.ITEM_MOVEMENT 
WHERE I_CODE = 'FA-M120WU' 
AND I_DATE >= TO_DATE('2026-01-01', 'YYYY-MM-DD') 
AND I_DATE <= TO_DATE('2026-12-31', 'YYYY-MM-DD') 
GROUP BY DOC_TYPE, IN_OUT
""")
print("In ALL warehouses:", cur.fetchall())
