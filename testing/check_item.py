import os
import oracledb
import datetime

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(
    user=os.environ.get('ORA_USER', 'RPT_USER'),
    password=os.environ.get('ORA_PASSWORD', 'ULT2016'),
    dsn=os.environ.get('ORA_DSN', '100.100.1.100:1521/ORCL')
)

i_code = 'OS32ATVHD'

query_balances = """
SELECT mv.W_CODE,
       MAX(w.W_NAME),
       SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) as balance
FROM IAS20261.ITEM_MOVEMENT mv
LEFT JOIN IAS20261.WAREHOUSE_DETAILS w ON w.W_CODE = mv.W_CODE
WHERE mv.I_CODE = :1
GROUP BY mv.W_CODE
HAVING SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) <> 0
ORDER BY balance DESC
"""

query_movement = """
SELECT TO_CHAR(mv.I_DATE, 'YYYY-MM-DD'),
       mv.DOC_TYPE,
       mv.DOC_NO,
       mv.W_CODE,
       MAX(w.W_NAME),
       CASE NVL(mv.IN_OUT,0) WHEN 1 THEN 'IN(+)' ELSE 'OUT(-)' END,
       NVL(mv.I_QTY,0)
FROM IAS20261.ITEM_MOVEMENT mv
LEFT JOIN IAS20261.WAREHOUSE_DETAILS w ON w.W_CODE = mv.W_CODE
WHERE mv.I_CODE = :1
  AND mv.I_DATE >= TO_DATE('2026-06-01', 'YYYY-MM-DD')
  AND mv.I_DATE <= TO_DATE('2026-07-04', 'YYYY-MM-DD')
GROUP BY mv.I_DATE, mv.DOC_TYPE, mv.DOC_NO, mv.W_CODE, mv.IN_OUT, mv.I_QTY
ORDER BY mv.I_DATE, mv.DOC_NO
"""

try:
    cur = conn.cursor()
    cur.execute(query_balances, [i_code])
    print("--- Current Balances ---")
    balances = cur.fetchall()
    for r in balances:
        print(f"[{r[0]}] {r[1]}: {r[2]}")
except Exception as e:
    print("Error in balances:", e)

try:
    cur = conn.cursor()
    cur.execute(query_movement, [i_code])
    print("\n--- Movement ---")
    movements = cur.fetchall()
    
    # Let's format the movement properly to print to terminal
    import io
    output = io.StringIO()
    output.write("| التاريخ | المستند | نوع المستند | المخزن | اسم المخزن | الحركة | الكمية |\n")
    output.write("|---|---|---|---|---|---|---|\n")
    for r in movements:
        # doc_type mapping
        dt_str = str(r[1])
        if r[1] == 1: dt_str = "فاتورة مبيعات"
        elif r[1] == 7: dt_str = "تحويل صادر/مبيعات مركزية"
        elif r[1] == 8: dt_str = "تحويل وارد"
        elif r[1] == 3: dt_str = "فاتورة مشتريات"
        elif r[1] == 4: dt_str = "مبيعات نقدية"
        
        output.write(f"| {r[0]} | {r[2]} | {dt_str} | {r[3]} | {r[4]} | {r[5]} | {r[6]} |\n")
        
    print(output.getvalue())
    
    with open(r'C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\mov_output.md', 'w', encoding='utf-8') as f:
        f.write("### الأرصدة الحالية للصنف OS32ATVHD\n\n")
        f.write("| المخزن | اسم المخزن | الرصيد الحالي |\n")
        f.write("|---|---|---|\n")
        for r in balances:
            f.write(f"| {r[0]} | {r[1]} | {r[2]} |\n")
        f.write("\n\n### حركة الصنف من 1 يونيو إلى 4 يوليو\n\n")
        f.write(output.getvalue())
        
except Exception as e:
    print("Error in movement:", e)

conn.close()
