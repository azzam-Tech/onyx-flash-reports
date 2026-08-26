BEGIN
  -- 1. محاولة حذف المناطق البيعية المخالفة
  FOR r IN (SELECT R_CODE FROM IAS20261.REGIONS WHERE PROV_NO < 101 OR PROV_NO > 113 OR PROV_NO IS NULL) LOOP
    BEGIN
      DELETE FROM IAS20261.REGIONS WHERE R_CODE = r.R_CODE;
    EXCEPTION 
      WHEN OTHERS THEN
        IF SQLCODE = -2292 THEN NULL; -- إذا كانت المنطقة مستخدمة، تجاوزها بصمت
        ELSE RAISE; 
        END IF;
    END;
  END LOOP;

  -- 2. محاولة حذف المدن المخالفة
  FOR c IN (SELECT CITY_NO FROM IAS20261.CITIES WHERE PROV_NO < 101 OR PROV_NO > 113 OR PROV_NO IS NULL) LOOP
    BEGIN
      DELETE FROM IAS20261.CITIES WHERE CITY_NO = c.CITY_NO;
    EXCEPTION 
      WHEN OTHERS THEN
        IF SQLCODE = -2292 THEN NULL; -- إذا كانت المدينة مستخدمة لأي غرض آخر، تجاوزها بصمت
        ELSE RAISE; 
        END IF;
    END;
  END LOOP;

  -- 3. محاولة حذف المحافظات المخالفة
  FOR p IN (SELECT PROV_NO FROM IAS20261.IAS_PROVINCES WHERE PROV_NO < 101 OR PROV_NO > 113 OR PROV_NO IS NULL) LOOP
    BEGIN
      DELETE FROM IAS20261.IAS_PROVINCES WHERE PROV_NO = p.PROV_NO;
    EXCEPTION 
      WHEN OTHERS THEN
        IF SQLCODE = -2292 THEN NULL; -- إذا كانت المحافظة مستخدمة، تجاوزها بصمت
        ELSE RAISE; 
        END IF;
    END;
  END LOOP;

  COMMIT;
END;
/
