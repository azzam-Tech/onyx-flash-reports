# خطة تنفيذ التحول إلى Query Builder (SQLAlchemy Core) المؤجلة

## وصف المشكلة
تختفي البيانات أو يظهر خطأ `DPY-3015: password verifier type 0x939 is not supported by python-oracledb in thin mode` لأن أوراكل في وضع Thin لا يدعم خوارزمية التشفير القديمة. يجب التأكد من عمل SQLAlchemy بوضع Thick Mode (عبر `oracledb.init_oracle_client`) أو استخدام طريقة أخرى لبناء الاستعلامات.

## الحل المقترح (الذي تم تأجيله)
1. **استبدال النصوص الخام الضخمة (Massive Raw SQL)** في `dashboard.py` وفي `report_handlers.py` باستخدام أدوات Query Builder مثل `SQLAlchemy Core` (بدون استخدام ORM Objects).
2. **استبدال كلاس `InterceptCursor`** (الذي يقوم بعمل Hack لتغيير نص المخطط IAS20261) بدالة ديناميكية تقرأ المخطط من الـ Flask Context (`get_schema()`) وتمرره للـ Query Builder.

## التغييرات التي تمت جدولتها للعودة إليها مستقبلاً
1. إضافة `SQLAlchemy>=2.0` إلى `requirements.txt`.
2. إعداد `create_engine("oracle+oracledb://...", creator=creator)` في `database.py`.
3. تعديل `compute_dash()` في `dashboard.py` لاستخدام `select`, `func`, `and_`, `table` و `literal_column` لبناء نفس الاستعلامات بأمان وبدون نصوص خام.
