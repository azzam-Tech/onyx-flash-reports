/* =====================================================================
   Onyx Pro - تحديد موقع كل الأجهزة الفعلية (READ-ONLY)
   الهدف: العثور على الـ 17 تابلت الحقيقية ومقارنتها بالجدول المرخّص (4).
   كله SELECT فقط - آمن على الإنتاج.
   ===================================================================== */

/* (1) الأجهزة المرتبطة بالمستخدمين (المرشّح الأقوى لتابلت المناديب) */
SELECT COUNT(*)                                             AS إجمالي,
       COUNT(DISTINCT HND_DVC_SRL)                          AS أجهزة_مميّزة,
       SUM(CASE NVL(INACTIVE,0) WHEN 0 THEN 1 ELSE 0 END)   AS النشط
FROM   IAS20261.S_USR_HND_DVC;

/* (2) الأجهزة المرتبطة بالموظفين */
SELECT COUNT(*)                                             AS إجمالي,
       COUNT(DISTINCT HND_DVC_SRL)                          AS أجهزة_مميّزة,
       SUM(CASE NVL(INACTIVE,0) WHEN 0 THEN 1 ELSE 0 END)   AS النشط
FROM   IAS20261.S_EMP_HND_DVC;

/* (3) الأجهزة المرتبطة بالعملاء */
SELECT COUNT(*)                                             AS إجمالي,
       COUNT(DISTINCT HND_DVC_SRL)                          AS أجهزة_مميّزة,
       SUM(CASE NVL(INACTIVE,0) WHEN 0 THEN 1 ELSE 0 END)   AS النشط
FROM   IAS20261.S_CST_HND_DVC;

/* (4) الأجهزة التي اتصلت فعلاً (سجل الاتصالات الناجحة) - آخر 60 يوماً */
SELECT COUNT(DISTINCT DVC_SRL)                              AS أجهزة_متصلة_مميّزة
FROM   IAS_SYS.MOBILE_SUCC_CONN_HSTRY
WHERE  AD_DATE >= SYSDATE - 60;

/* (5) قائمة الأجهزة المتصلة مؤخراً بتفاصيلها */
SELECT DISTINCT DVC_SRL, DVC_NM, DVC_OS, BRN_USR, MAX(AD_DATE) AS آخر_اتصال
FROM   IAS_SYS.MOBILE_SUCC_CONN_HSTRY
WHERE  AD_DATE >= SYSDATE - 60
GROUP  BY DVC_SRL, DVC_NM, DVC_OS, BRN_USR
ORDER  BY آخر_اتصال DESC;

/* (6) رموز الإشعارات (جهاز لكل توكن) */
SELECT COUNT(DISTINCT HND_DVC_SRL) AS أجهزة_بالإشعارات
FROM   IAS20261.IAS_MOBILE_NTFCTN;

/* (7) التقاطع: هل أجهزة المستخدمين مسجّلة أصلاً في الجدول المرخّص؟
       إن رجع صفراً/قليلاً = التابلت تتّصل خارج بوابة الترخيص تماماً. */
SELECT COUNT(*) AS مسجّلة_في_الجدول_المرخّص
FROM   IAS20261.S_USR_HND_DVC u
WHERE  EXISTS (SELECT 1 FROM IAS_SYS.IAS_OBJ_HND_DVC d
               WHERE d.IMEI = u.HND_DVC_SRL);
