import sys
import os
import codecs
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_levels():
    with open('testing/levels_out.txt', 'w', encoding='utf-8') as f:
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute("SELECT LEV_NO, LEV_A_NAME FROM IAS_PRICING_LEVELS")
                for r in cur.fetchall():
                    f.write(f"Level {r[0]}: {r[1]}\n")

if __name__ == '__main__':
    check_levels()
