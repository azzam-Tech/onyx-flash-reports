# توثيق مشكلة انقطاع الاتصال بقاعدة البيانات (ORA-12541)

## وصف المشكلة
توقف نظام التقارير فجأة عن العمل سواء من جهاز التطوير المحلي (عبر شبكة Tailscale) أو من الجهاز الوسيط نفسه، وظهر الخطأ التالي:
`ORA-12541: Cannot connect. No listener at host 100.100.1.100 port 1521.`

## تحليل المشكلة والأسباب الجذرية
بعد الفحص الدقيق، تبين وجود تداخل في إعدادات الاتصال والشبكة:
1. **توقف خدمة التوجيه (Portproxy):** كان الجهاز الوسيط (192.168.1.9) يعتمد على أداة `netsh portproxy` في الويندوز لاستقبال الطلبات على عنوان تيل سكيل `100.100.1.100` وتحويلها إلى سيرفر قاعدة البيانات الأساسي `192.168.1.10`. تعطلت خدمة `IP Helper` في الويندوز مما أدى لفشل التوجيه وظهور خطأ `No listener`.
2. **غياب متغير الاتصال في بيئة الإنتاج:** ملف التشغيل `.bat` في الجهاز الوسيط لم يكن يحتوي على متغير `ORA_DSN`، مما جعل كود البايثون يلجأ للعنوان الافتراضي المبرمج داخلياً `100.100.1.100`. وبسبب توقف خدمة التوجيه، فشل النظام في الاتصال بقاعدة البيانات رغم أنه موجود معها في نفس الشبكة المحلية.
3. **ثغرة أمنية:** كان ملف التشغيل يستخدم حساب الإدارة `ULT` بدلاً من حساب القراءة المخصص للتقارير `RPT_USER`.

## خطوات الحل والأوامر التي تم تطبيقها

### 1. إصلاح نظام التقارير في الجهاز الوسيط (بيئة الإنتاج)
تم تعديل ملف التشغيل `.bat` لتوجيه النظام للاتصال بقاعدة البيانات مباشرة عبر الشبكة المحلية (بدون الاعتماد على التوجيه)، وتم تأمين الحساب:
```batch
@echo off
set ORA_LIB_DIR=C:\oracle64\instantclient_19_23
set TNS_ADMIN=C:\oracle64\instantclient_19_23
set ORA_USER=RPT_USER
set ORA_PASSWORD=ULT2016
set ORA_DSN=192.168.1.10:1521/orcl
cd /d C:\Users\sultan\Desktop\privet\onyx_reports
py -c "from waitress import serve; import app; serve(app.app, host='0.0.0.0', port=8000)"
```

### 2. إصلاح الاتصال للمطورين (عبر Tailscale)
لإعادة تمكين جهاز التطوير من الوصول لقاعدة البيانات عبر تيل سكيل، تم تنفيذ الأوامر التالية في (PowerShell كمسؤول) على الجهاز الوسيط:

أ) تشغيل خدمة `IP Helper`:
```powershell
Set-Service iphlpsvc -StartupType Automatic
Start-Service iphlpsvc
```
ب) تنظيف قواعد التوجيه القديمة:
```powershell
netsh interface portproxy delete v4tov4 listenport=1521 listenaddress=100.100.1.100
netsh interface portproxy delete v4tov4 listenport=1521 listenaddress=0.0.0.0
```
ج) إضافة قاعدة التوجيه الآمنة للشبكة الوهمية فقط:
```powershell
netsh interface portproxy add v4tov4 listenport=1521 listenaddress=100.100.1.100 connectport=1521 connectaddress=192.168.1.10
```

### 3. الجانب الأمني: حظر جهاز معين من الوصول لقاعدة البيانات
لضمان عدم وصول الـ IP `100.80.87.1` إلى قاعدة البيانات مع إبقائه في شبكة تيل سكيل، تم إنشاء قاعدة حظر في جدار حماية الويندوز (Windows Firewall) في الجهاز الوسيط:
```powershell
New-NetFirewallRule -DisplayName "Block DB Access for 100.80.87.1" -Direction Inbound -Action Block -Protocol TCP -LocalPort 1521 -RemoteAddress 100.80.87.1
```
