import os
import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(
    user=os.environ.get('ORA_USER', 'RPT_USER'),
    password=os.environ.get('ORA_PASSWORD', 'ULT2016'),
    dsn=os.environ.get('ORA_DSN', '100.100.1.100:1521/ORCL')
)
cur = conn.cursor()

cur.execute("""
    SELECT p.C_CODE, SUM(NVL(p.CR_AMT,0)) as amt
    FROM IAS20261.IAS_POST_DTL p
    JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
    WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=2 AND NVL(p.CR_AMT,0)>0
      AND p.DOC_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') 
      AND p.DOC_DATE < TO_DATE('2026-07-01','YYYY-MM-DD')
      AND TO_CHAR(c.REP_CODE)='142'
    GROUP BY p.C_CODE
""")

receipts_by_cust = {}
for ccode, amt in cur.fetchall():
    receipts_by_cust[ccode] = amt

target = 40743.43

# We can use a DP or meet-in-the-middle subset sum to find which exact customers make up 40743.43
def subset_sum_dp(items, target, tolerance=0.01):
    # Scale by 100 to use integers for DP
    target_int = int(round(target * 100))
    # We only care about positive values, but just in case
    dp = {0: []}
    for name, val in items.items():
        val_int = int(round(val * 100))
        if val_int <= 0: continue
        new_dp = {}
        for s, subset in dp.items():
            new_dp[s] = subset
            new_s = s + val_int
            if new_s <= target_int + 5: # allow slight margin
                if new_s not in dp:
                    new_dp[new_s] = subset + [name]
        dp = new_dp
        if target_int in dp or target_int+1 in dp or target_int-1 in dp:
            best = target_int if target_int in dp else (target_int+1 if target_int+1 in dp else target_int-1)
            return dp[best]
    
    # check closest
    closest = -1
    min_diff = 999999999
    for s in dp:
        if abs(s - target_int) < min_diff:
            min_diff = abs(s - target_int)
            closest = s
    return dp.get(closest, []), closest / 100.0

res, closest_val = subset_sum_dp(receipts_by_cust, target)
if type(res) is list and len(res) > 0 and abs(closest_val - target) < 1.0:
    print(f"Found customers exactly matching {closest_val}:", res)
else:
    print(f"Closest match was {closest_val} using {res}")

cur.close()
conn.close()
