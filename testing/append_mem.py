import codecs

content = """
### Income Statement and GL accounts grouping
- For revenue and expenses accounts (e.g. 41101, 32101), `IAS_POST_DTL` does not populate `REP_CODE` or `AC_CODE_DTL`. The account number is in `A_CODE`, and the Salesman/Cost Center is populated in `CC_CODE`.
- When filtering GL reports by Salesman, always check `CC_CODE` as well: `(REP_CODE = :rep_code OR CC_CODE = :rep_code)`.
- Sales returns in `ITEM_MOVEMENT` use `DOC_TYPE = 3` (not 2).
- Previous year returns in `IAS_RT_BILL_MST` are identified by `PREV_YEAR IS NOT NULL`.
"""

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\AI_MEMORY.md", 'a', 'utf-8') as f:
    f.write(content)
