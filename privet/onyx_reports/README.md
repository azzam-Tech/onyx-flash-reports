# لوحة تقارير Onyx

## التشغيل على جهاز الأونكس
1) ثبّت المكتبات:
   py -m pip install -r requirements.txt
2) اضبط كلمة المرور كمتغيّر بيئة (أفضل من تعديل الملف):
   $env:ORA_PASSWORD="كلمة_المرور"
3) شغّل:
   py app.py
4) افتح: http://localhost:5000

## للنشر عبر الشبكة (بعد نجاح التجربة)
   py -m waitress --listen=0.0.0.0:8000 app:app
ثم افتح منفذ 8000 لشبكة Tailscale.

## إضافة تقرير
أضِف فقرة إلى قاموس REPORTS في app.py: عنوان + params + استعلام (استخدم :param).
