# الخريطة المرجعية لقاعدة بيانات أونكس برو (Onyx Pro Database Map)

تم استخراج هذه الخريطة آلياً من ملف السكيما (1246 جدول) لتكون المرجع الشامل لكتابة استعلامات SQL متقدمة.

## 1. الحقول السيادية المشتركة (Common Linkage Fields)

هذه الحقول تتكرر في مئات الجداول وهي الأساس في بناء الروابط (JOINs):

- **BRANCH_NO**: متواجد في (0 جدول).
- **FISCAL_YEAR**: متواجد في (0 جدول).
- **P_YEAR**: متواجد في (10 جدول).
- **DOC_TYPE**: متواجد في (103 جدول).
- **DOC_NO**: متواجد في (302 جدول).
- **DOC_SER**: متواجد في (219 جدول).
- **C_CODE**: متواجد في (178 جدول).
- **I_CODE**: متواجد في (251 جدول).
- **A_CODE**: متواجد في (133 جدول).
- **REP_CODE**: متواجد في (108 جدول).
- **CC_CODE**: متواجد في (264 جدول).
- **W_CODE**: متواجد في (221 جدول).
- **IN_OUT**: متواجد في (17 جدول).

## 2. التصنيف الموديولي والجداول السيادية

### 📦 موديول: Integrated Accounts / Sales

**الجداول الحركية (Transactional):**
- `IAS_PI_BILL_MST`: مفتاح رئيسي (غير محدد)
- `IAS_POST_DTL`: مفتاح رئيسي (غير محدد)
- `IAS_BILL_MST_ADD_DISC`: مفتاح رئيسي (غير محدد)
- `IAS_PI_BILL_DTL`: مفتاح رئيسي (غير محدد)
- `IAS_RECEIPT_DOC`: مفتاح رئيسي (غير محدد)
- `IAS_AR_CNTRCT_MST`: مفتاح رئيسي (غير محدد)
- `IAS_SAL_CPN_MST`: مفتاح رئيسي (غير محدد)
- `IAS_BILL_MST_ADD_DISC_RQ`: مفتاح رئيسي (غير محدد)
- `IAS_GRNT_MST`: مفتاح رئيسي (غير محدد)
- `IAS_RQ_VCHR_MST`: مفتاح رئيسي (غير محدد)
- `IAS_FREIGHT_MST`: مفتاح رئيسي (غير محدد)
- `IAS_PI_BILL_MST_ADD_DISC`: مفتاح رئيسي (غير محدد)
- `IAS_GRNT_INCR_MST`: مفتاح رئيسي (غير محدد)
- `IAS_BILL_DTL_BKTMP`: مفتاح رئيسي (غير محدد)
- `IAS_AUD_ITM_OTHR_MST`: مفتاح رئيسي (غير محدد)

**الجداول الأساسية (Master Data):**
- `IAS_BILL_MST_BR`: مفتاح رئيسي (غير محدد)
- `IAS_BILL_MST`: مفتاح رئيسي (غير محدد)
- `IAS_ITEM_MST_TMP`: مفتاح رئيسي (غير محدد)
- `IAS_ITM_MST`: مفتاح رئيسي (غير محدد)
- `IAS_BILL_MSTBK2`: مفتاح رئيسي (غير محدد)
- `IAS_RT_BILL_MST`: مفتاح رئيسي (غير محدد)
- `IAS_RT_BILL_MST_BR`: مفتاح رئيسي (غير محدد)
- `IAS_RT_BILL_MST_RQ`: مفتاح رئيسي (غير محدد)
- `IAS_RT_BILL_MST_RQ_BR`: مفتاح رئيسي (غير محدد)
- `IAS_RT_BILL_DTL`: مفتاح رئيسي (غير محدد)
- `IAS_RT_BILL_DTL_BR`: مفتاح رئيسي (غير محدد)
- `IAS_RT_BILL_DTL_RQ`: مفتاح رئيسي (غير محدد)
- `IAS_PR_BILL_MST`: مفتاح رئيسي (غير محدد)
- `IAS_RT_BILL_DTL_RQ_BR`: مفتاح رئيسي (غير محدد)
- `IAS_WHTRNS_DTL_BR`: مفتاح رئيسي (غير محدد)

---

### 📦 موديول: Other

**الجداول الحركية (Transactional):**
- `LC_MASTER`: مفتاح رئيسي (غير محدد)
- `GLS_BILL_ADVNC`: مفتاح رئيسي (غير محدد)
- `GLS_RTRN_BILL_ADVNC`: مفتاح رئيسي (غير محدد)
- `GR_NOTE_BR`: مفتاح رئيسي (غير محدد)
- `GR_NOTE`: مفتاح رئيسي (غير محدد)
- `GLS_ADVNC_EXPNS_RVNU_MST`: مفتاح رئيسي (غير محدد)
- `TMS_PLAN_DTL`: مفتاح رئيسي (غير محدد)
- `GUARN_ISSUE`: مفتاح رئيسي (غير محدد)
- `HPS_ADMSON_MST`: مفتاح رئيسي (غير محدد)
- `HPS_DCTR_ORDR_MST`: مفتاح رئيسي (غير محدد)
- `S_JRNL_FILE_DTL`: مفتاح رئيسي (غير محدد)
- `GLS_BNK_IDNTF_MST`: مفتاح رئيسي (غير محدد)
- `HPS_DCTR_VISIT`: مفتاح رئيسي (غير محدد)
- `GLS_RQ_EXCH_CUR_MST`: مفتاح رئيسي (غير محدد)
- `TMS_PLAN_MST`: مفتاح رئيسي (غير محدد)

**الجداول الأساسية (Master Data):**
- `CUSTOMER`: مفتاح رئيسي (غير محدد)
- `CUSTOMER_RQ`: مفتاح رئيسي (غير محدد)
- `SALES_ORDER`: مفتاح رئيسي (غير محدد)
- `VOUCHER_DETAIL`: مفتاح رئيسي (غير محدد)
- `SALES_MAN`: مفتاح رئيسي (غير محدد)
- `P_ORDER`: مفتاح رئيسي (غير محدد)
- `QUOTATION`: مفتاح رئيسي (غير محدد)
- `GR_DETAIL`: مفتاح رئيسي (غير محدد)
- `V_DETAILS`: مفتاح رئيسي (غير محدد)
- `QUOTATION_RQ`: مفتاح رئيسي (غير محدد)
- `DETAIL_JOURNAL_V`: مفتاح رئيسي (غير محدد)
- `GR_DETAIL_BR`: مفتاح رئيسي (غير محدد)
- `P_ORDER_DETAIL_BKTMP`: مفتاح رئيسي (غير محدد)
- `MASTER_OUT_BILLS`: مفتاح رئيسي (غير محدد)
- `MASTER_OUT_BILLS_BR`: مفتاح رئيسي (غير محدد)

---

### 📦 موديول: General / System

**الجداول الحركية (Transactional):**
- `GNR_TAX_ITM_MOVMNT`: مفتاح رئيسي (غير محدد)
- `GNR_TAX_ITM_MOVMNT_BR`: مفتاح رئيسي (غير محدد)
- `GNR_TAX_INPT_MOVMNT`: مفتاح رئيسي (غير محدد)
- `GNR_TAX_INPT_MOVMNT_BR`: مفتاح رئيسي (غير محدد)
- `GNR_RQ_TAX_INPT_MOVMNT`: مفتاح رئيسي (غير محدد)
- `GNR_RQ_TAX_ITM_MOVMNT`: مفتاح رئيسي (غير محدد)
- `GNR_RQ_TAX_ITM_MOVMNT_BR`: مفتاح رئيسي (غير محدد)
- `GNR_EXTRNL_DOC_SYNC`: مفتاح رئيسي (غير محدد)
- `GNR_CONN_AUD_ACC_GRP`: مفتاح رئيسي (غير محدد)
- `GNR_DOC_POST_AUDIT_HST`: مفتاح رئيسي (غير محدد)
- `GNR_OCR_DOC_MST`: مفتاح رئيسي (غير محدد)

### 📦 موديول: Inventory

**الجداول الحركية (Transactional):**
- `ITEM_MOVEMENT`: مفتاح رئيسي (غير محدد)
- `INV_RQ_ASSMBL_DTL`: مفتاح رئيسي (غير محدد)
- `INV_RQ_ASSMBL_MST`: مفتاح رئيسي (غير محدد)
- `INV_ITM_FREE_SMPL_MVMNT`: مفتاح رئيسي (غير محدد)
- `INV_RQ_STK_ADJST_DTL`: مفتاح رئيسي (غير محدد)
- `INV_RQ_STK_ADJST_MST`: مفتاح رئيسي (غير محدد)
- `INV_ITM_QR_CODE_MOVMNT`: مفتاح رئيسي (غير محدد)
- `INV_ITM_PARTITION_MST`: مفتاح رئيسي (غير محدد)
- `INV_ITM_QR_CODE`: مفتاح رئيسي (غير محدد)
- `INV_ITM_QR_CODE_MOVMNT_BR`: مفتاح رئيسي (غير محدد)
- `INV_ITM_QR_CODE_MOVMNT_OTHR`: مفتاح رئيسي (غير محدد)
- `INV_ITM_BIN_MOVMNT`: مفتاح رئيسي (غير محدد)
- `INV_RQ_ASSMBL_SUB_DTL`: مفتاح رئيسي (غير محدد)
- `INV_OTHER_CHARGES`: مفتاح رئيسي (غير محدد)
- `INV_ITM_INC_PARTITION_DTL`: مفتاح رئيسي (غير محدد)

**الجداول الأساسية (Master Data):**
- `INV_VNDR_OPEN_STOCK`: مفتاح رئيسي (غير محدد)
- `WAREHOUSE_DETAILS`: مفتاح رئيسي (غير محدد)

---

## 3. قوالب استعلامات قياسية ومجربة (Standard JOIN Templates)

### قالب 1: الفواتير وتفاصيلها (Triple Join Rule)
```sql
SELECT m.BILL_NO, m.BILL_DATE, d.I_CODE, d.I_QTY
FROM IAS_BILL_MST m
JOIN IAS_BILL_DTL d 
  ON m.BILL_DOC_TYPE = d.BILL_DOC_TYPE
 AND m.BILL_NO = d.BILL_NO
 AND m.BILL_SER = d.BILL_SER
WHERE m.BILL_DOC_TYPE = 1;
```

### قالب 2: القيود اليومية والدفعات (Net Journal / Receipts)
```sql
SELECT p.DOC_NO, p.DOC_DATE, p.CR_AMT, c.C_A_NAME, s.REPRS_A_NAME
FROM IAS_POST_DTL p
LEFT JOIN CUSTOMER c ON c.C_CODE = p.C_CODE
LEFT JOIN SALES_MAN s ON s.REPRS_CODE = p.REP_CODE
WHERE p.DOC_TYPE = 2 AND p.DOC_POST = 1;
```

### قالب 3: أرصدة وحركة المخزون للمستودعات المركزية
```sql
SELECT dt.I_CODE, m.I_NAME, dt.W_CODE, SUM(dt.I_QTY) as net_qty
FROM ITEM_MOVEMENT dt
LEFT JOIN IAS_ITM_MST m ON m.I_CODE = dt.I_CODE
WHERE dt.IN_OUT = -1 AND dt.DOC_TYPE = 7
  AND dt.W_CODE IN (105, 103, 121, 122, 118, 108, 119)
GROUP BY dt.I_CODE, m.I_NAME, dt.W_CODE;
```
