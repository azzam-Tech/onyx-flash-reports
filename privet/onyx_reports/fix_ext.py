import os
filepath = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

bad_ext = """  SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
         0, 0, 0, 0, 0, CR_AMT
  FROM IAS20261.IAS_POST_DTL
  WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=15 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0"""

good_ext = """  SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
         0, 0, 0, 0, 0, CR_AMT
  FROM IAS20261.IAS_POST_DTL
  WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=15 AND NVL(CR_AMT,0)>0"""

if bad_ext in content:
    content = content.replace(bad_ext, good_ext)
    print("Fixed ext_notice")
else:
    # Just in case
    content = content.replace("AND DOC_TYPE=15 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0", "AND DOC_TYPE=15 AND NVL(CR_AMT,0)>0")
    print("Force replaced ext_notice")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done")
