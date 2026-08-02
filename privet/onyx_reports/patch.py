# -*- coding: utf-8 -*-
with open('app.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """              TO_CHAR(inv_disc,'FM999,999,990.00')   AS "الخصم في الفاتورة",
              TO_CHAR(cash_ret,'FM999,999,990.00')   AS "المرتجع النقدي (-)",
              TO_CHAR(total_inc,'FM999,999,990.00') AS "إجمالي التحصيل"
        FROM base
        WHERE (rcpt > 0 OR net_jrn > 0 OR cash_sales > 0 OR cash_ret > 0 OR inv_disc > 0)
        ORDER BY total_inc DESC
      ) WHERE ROWNUM <= 300\"\"\"},"""

replacement = """              TO_CHAR(inv_disc,'FM999,999,990.00')   AS "الخصم في الفاتورة",
              TO_CHAR(ext_notice,'FM999,999,990.00') AS "إشعار خصم مستقل (-)",
              TO_CHAR(cash_ret,'FM999,999,990.00')   AS "المرتجع النقدي (-)",
              TO_CHAR(total_inc,'FM999,999,990.00') AS "إجمالي التحصيل"
        FROM base
        WHERE (rcpt > 0 OR net_jrn > 0 OR cash_sales > 0 OR cash_ret > 0 OR inv_disc > 0 OR ext_notice > 0)
        ORDER BY total_inc DESC
      ) WHERE ROWNUM <= 300\"\"\"},"""

if target in text:
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(text.replace(target, replacement))
    print("Replaced successfully")
else:
    print("Target still not found. Using regex.")
    import re
    target_regex = r'TO_CHAR\(inv_disc,\'FM999,999,990\.00\'\)\s+AS "الخصم في الفاتورة",\s+TO_CHAR\(cash_ret,\'FM999,999,990\.00\'\)\s+AS "المرتجع النقدي \(-\)",\s+TO_CHAR\(total_inc,\'FM999,999,990\.00\'\) AS "إجمالي التحصيل"\s+FROM base\s+WHERE \(rcpt > 0 OR net_jrn > 0 OR cash_sales > 0 OR cash_ret > 0 OR inv_disc > 0\)\s+ORDER BY total_inc DESC\s+\) WHERE ROWNUM <= 300"""},'
    replacement_regex = r'''TO_CHAR(inv_disc,'FM999,999,990.00')   AS "الخصم في الفاتورة",
              TO_CHAR(ext_notice,'FM999,999,990.00') AS "إشعار خصم مستقل (-)",
              TO_CHAR(cash_ret,'FM999,999,990.00')   AS "المرتجع النقدي (-)",
              TO_CHAR(total_inc,'FM999,999,990.00') AS "إجمالي التحصيل"
        FROM base
        WHERE (rcpt > 0 OR net_jrn > 0 OR cash_sales > 0 OR cash_ret > 0 OR inv_disc > 0 OR ext_notice > 0)
        ORDER BY total_inc DESC
      ) WHERE ROWNUM <= 300"""},'''
    text = re.sub(target_regex, replacement_regex, text)
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Replaced with regex.")
