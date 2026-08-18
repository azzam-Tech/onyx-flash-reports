import sys
import os
# Add root path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def inspect_customer(c_code):
    with get_conn() as con:
        with con.cursor() as cur:
            sql = """
                SELECT DOC_DATE, DOC_NO, DOC_SER, DOC_TYPE, DR_AMT, CR_AMT, REF_NO
                FROM IAS_POST_DTL
                WHERE TO_CHAR(C_CODE) = :c_code
                AND (NVL(DOC_POST,0)=1 OR (NVL(DOC_POST,0)=0 AND DOC_TYPE=2))
                ORDER BY DOC_DATE, DOC_TYPE
            """
            cur.execute(sql, {'c_code': c_code})
            rows = cur.fetchall()
            
            print(f"Transactions for customer {c_code}:")
            print(f"{'Date':<12} | {'Doc No':<8} | {'Ser':<4} | {'Type':<4} | {'Dr':<10} | {'Cr':<10} | {'Ref'}")
            print("-" * 70)
            dr_tot = 0
            cr_tot = 0
            for r in rows:
                date = r[0].strftime('%Y-%m-%d')
                dno = r[1]
                dser = r[2]
                dtype = r[3]
                dr = float(r[4] or 0)
                cr = float(r[5] or 0)
                ref = r[6]
                dr_tot += dr
                cr_tot += cr
                print(f"{date:<12} | {dno:<8} | {dser:<4} | {dtype:<4} | {dr:<10.2f} | {cr:<10.2f} | {ref}")
            print("-" * 70)
            print(f"Total Debits : {dr_tot:.2f}")
            print(f"Total Credits: {cr_tot:.2f}")
            print(f"Balance      : {dr_tot - cr_tot:.2f}")

            # Let's also check return invoice links
            print("\nChecking Returns (DOC_TYPE=5) links in IAS_RT_BILL_DTL...")
            sql_links = """
                SELECT DISTINCT p.DOC_NO, p.DOC_SER, TO_CHAR(d.BILL_NO), TO_CHAR(d.BILL_SER)
                FROM IAS_POST_DTL p
                JOIN IAS_RT_BILL_DTL d 
                    ON p.DOC_NO = d.RT_BILL_NO AND p.DOC_SER = d.RT_BILL_SER
                WHERE p.DOC_TYPE = 5 AND p.CR_AMT > 0 
                  AND TO_CHAR(p.C_CODE) = :c_code
            """
            cur.execute(sql_links, {'c_code': c_code})
            links = cur.fetchall()
            for l in links:
                print(f"Return Doc {l[0]}-{l[1]} is linked to Bill {l[2]}-{l[3]}")

if __name__ == '__main__':
    inspect_customer('2051')
