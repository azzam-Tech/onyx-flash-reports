# -*- coding: utf-8 -*-
"""لوحة تقارير SREEN — Flask + Oracle (RTL). تبويبات رئيسية وفرعية موصولة بالاستعلامات."""

import os
import json
import oracledb
import io
from urllib.parse import urlencode
from datetime import datetime
from flask import Flask, request, render_template_string, Response, session

app = Flask(__name__)
app.secret_key = os.environ.get("SREEN_SECRET", "sreen-reports-2026-secret-key")
SETTINGS_PIN = os.environ.get("SETTINGS_PIN", "00900")
APP_PIN = os.environ.get("APP_PIN", "00900")

_lib = r"C:\oracle\instantclient\instantclient_23_0"
try:
    oracledb.init_oracle_client(lib_dir=_lib) if _lib else oracledb.init_oracle_client()
    print("Thick mode ON")
except Exception as e:
    print("thick warn:", e)

DB_USER     = os.environ.get("ORA_USER",     "RPT_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD", "ULT2016")
DB_DSN      = os.environ.get("ORA_DSN",      "100.100.1.100:1521/ORCL")

LOGIN_PAGE = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <title>تسجيل الدخول - نظام التقارير</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800&display=swap');
    body { margin: 0; padding: 0; background-color: #f4f5f8; font-family: 'Cairo', sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; }
    .card { background: #fff; padding: 40px; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); text-align: center; max-width: 400px; width: 100%; border-top: 6px solid #4f46e5; }
    h2 { color: #1e293b; font-weight: 800; margin-bottom: 5px; }
    p { color: #64748b; margin-bottom: 25px; }
    input[type=password] { width: 100%; padding: 12px; margin-bottom: 20px; border: 2px solid #e2e8f0; border-radius: 8px; font-size: 16px; text-align: center; font-family: inherit; font-weight: 600; box-sizing: border-box; }
    input[type=password]:focus { outline: none; border-color: #4f46e5; }
    button { background: #4f46e5; color: #fff; border: none; border-radius: 8px; padding: 12px 20px; font-size: 16px; cursor: pointer; width: 100%; font-weight: 600; transition: background 0.2s; }
    button:hover { background: #4338ca; }
    .err { color: #ef4444; background: #fee2e2; padding: 10px; border-radius: 8px; margin-bottom: 15px; font-size: 14px; }
  </style>
</head>
<body>
  <div class="card">
    <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#4f46e5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:10px;"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
    <h2>نظام التقارير</h2>
    <p>يرجى إدخال رمز المرور للمتابعة</p>
    {% if error %}<div class="err">{{ error }}</div>{% endif %}
    <form method="POST">
      <input type="password" name="pin" placeholder="الرمز السري (PIN)" autofocus required>
      <button type="submit">دخول آمن</button>
    </form>
  </div>
</body>
</html>"""

from flask import redirect

@app.before_request
def require_login():
    if request.endpoint not in ('login', 'static') and not session.get('logged_in'):
        return redirect('/login')

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form.get("pin") == APP_PIN:
            session['logged_in'] = True
            return redirect('/')
        else:
            error = "الرمز غير صحيح، حاول مرة أخرى."
    return render_template_string(LOGIN_PAGE, error=error)

@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    return redirect('/login')



def get_conn():
    return oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)

SETTINGS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings.json")
# كل ما يخص الربح: يُخفى عند تفعيل "إخفاء الربح"
PROFIT_TABS = {"prof"}
PROFIT_REPORTS = {"fin/income_statement", "fin/cost_centers"}
def _load_raw():
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}
def load_hidden_raw():
    d = _load_raw()
    return set(d.get("tabs", [])), set(d.get("reports", []))
def load_hide_profit():
    return bool(_load_raw().get("hide_profit"))
def load_hidden():
    """المجموعات الفعّالة المطبَّقة على الواجهة (تشمل إخفاء الربح إن كان مفعّلاً)."""
    tabs, reps = load_hidden_raw()
    if load_hide_profit():
        tabs = tabs | PROFIT_TABS
        reps = reps | PROFIT_REPORTS
    return tabs, reps
def save_hidden(tabs, reports, hide_profit=False):
    try:
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump({"tabs": list(tabs), "reports": list(reports),
                       "hide_profit": bool(hide_profit)}, f, ensure_ascii=False)
    except Exception as e:
        print("settings save error:", e)

DFROM = {"name":"date_from","label":"من تاريخ","type":"date","default":"2026-01-01"}
DTO   = {"name":"date_to","label":"إلى تاريخ","type":"date","default":"2026-07-10"}
REP   = {"name":"rep_code","label":"المندوب (اختياري)","type":"text","default":""}
INCR  = {"name":"inc_rcpt","label":"سندات القبض","type":"select","default":"1","options":[["1","تضمين"],["0","استبعاد"]]}
INCN  = {"name":"inc_net","label":"قيود الشبكة المنفصلة","type":"select","default":"1","options":[["1","تضمين"],["0","استبعاد"]]}
INCC  = {"name":"inc_cash","label":"المبيعات النقدية","type":"select","default":"1","options":[["1","تضمين"],["0","استبعاد"]]}
INCRT = {"name":"inc_ret","label":"المرتجع النقدي (خصم)","type":"select","default":"1","options":[["1","خصم"],["0","تجاهل"]]}
INCEX = {"name":"inc_ext","label":"إشعار خصم مستقل (خصم)","type":"select","default":"0","hidden":True,"options":[["1","خصم"],["0","تجاهل"]]}
GRP   = {"name":"grp_by","label":"تجميع حسب","type":"select","default":"rep","options":[["rep","المندوب"],["cc","مركز التكلفة"],["cst","العميل"]]}
CST   = {"name":"c_code","label":"العميل (اختياري)","type":"text","default":""}
BTYPE = {"name":"bill_type","label":"نوع المستند","type":"select","default":"",
         "options":[["","الكل"],["1","مبيعات نقدية"],["4","مبيعات آجلة"],["2","مرتجع نقدي"],["5","مرتجع آجل"]]}

TABS = [
 {"id":"dash","title":"لوحة القيادة","icon":"M3 13h8V3H3zM13 21h8V3h-8zM3 21h8v-6H3z","dash":True,"reports":[{"id":"overview","title":"نظرة عامة","params":[{"name":"date_from","label":"من تاريخ","type":"date","default":"2026-01-01"},{"name":"date_to","label":"إلى تاريخ","type":"date","default":"2026-12-31"}]}]},
 {"id":"sales","title":"المبيعات","icon":"M4 20V10M10 20V4M16 20v-7M22 20H2","reports":[
   {"id":"bills","title":"فواتير المبيعات","params":[DFROM,DTO,BTYPE,REP,CST],"sql":"""
     SELECT CASE b.BILL_DOC_TYPE WHEN 1 THEN 'مبيعات نقدية' WHEN 4 THEN 'مبيعات آجلة' 
                 WHEN 2 THEN 'مرتجع نقدي' WHEN 5 THEN 'مرتجع آجل' ELSE 'أخرى' END AS "نوع المستند",
            b.BILL_NO AS "رقم الفاتورة", TO_CHAR(b.BILL_DATE,'YYYY-MM-DD') AS "التاريخ",
            b.C_CODE AS "كود العميل", MAX(c.C_A_NAME) AS "اسم العميل", b.REP_CODE AS "المندوب",
            TO_CHAR(NVL(b.BILL_AMT,0),'FM999,999,990.00') AS "المبلغ",
            TO_CHAR(NVL(d.itm_disc,0),'FM999,999,990.00') AS "خصم الأصناف",
            TO_CHAR(NVL(b.DISC_AMT,0),'FM999,999,990.00') AS "الخصم الإجمالي",
            TO_CHAR(NVL(b.VAT_AMT,0),'FM999,999,990.00') AS "الضريبة",
            TO_CHAR((NVL(b.BILL_AMT,0)-NVL(b.DISC_AMT,0)-NVL(d.itm_disc,0)+NVL(b.VAT_AMT,0)+NVL(b.OTHR_AMT,0)) * CASE WHEN b.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 1 END,'FM999,999,990.00') AS "الصافي",
            CASE NVL(b.BILL_POST,0) WHEN 1 THEN 'مرحّلة' ELSE 'غير مرحّلة' END AS "الحالة"
     FROM IAS20261.IAS_BILL_MST b
     LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = b.C_CODE
     LEFT JOIN (
         SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as itm_disc
         FROM IAS20261.IAS_BILL_DTL
         GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
     ) d ON b.BILL_DOC_TYPE = d.BILL_DOC_TYPE AND b.BILL_NO = d.BILL_NO AND b.BILL_SER = d.BILL_SER
     WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       AND b.BILL_DOC_TYPE IN (1,4,2,5)
       AND (:bill_type IS NULL OR b.BILL_DOC_TYPE = :bill_type)
       AND (:rep_code IS NULL OR b.REP_CODE = :rep_code)
       AND (:c_code IS NULL OR b.C_CODE = :c_code)
     GROUP BY b.BILL_DOC_TYPE, b.BILL_NO, b.BILL_DATE, b.C_CODE, b.REP_CODE, b.BILL_AMT, b.DISC_AMT, b.VAT_AMT, b.OTHR_AMT, b.BILL_POST, d.itm_disc
     ORDER BY b.BILL_DATE DESC, b.BILL_NO DESC FETCH FIRST 300 ROWS ONLY"""},
   {"id":"by_item","title":"حسب الصنف","params":[DFROM,DTO],"sql":"""
     WITH dt AS (
       SELECT dt.I_CODE,
              CASE WHEN b.BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) THEN 1 WHEN b.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              NVL(dt.I_QTY,0) as qty,
              (NVL(dt.I_QTY,0) * NVL(dt.I_PRICE,0) - NVL(dt.DIS_AMT,0)) as item_net,
              CASE WHEN NVL(b.BILL_AMT,0) = 0 THEN 0 ELSE 
                ((NVL(dt.I_QTY,0) * NVL(dt.I_PRICE,0)) / b.BILL_AMT) * NVL(b.DISC_AMT,0) 
              END as prorated_disc
       FROM IAS20261.IAS_BILL_DTL dt
       JOIN IAS20261.IAS_BILL_MST b ON b.BILL_DOC_TYPE=dt.BILL_DOC_TYPE AND b.BILL_NO=dt.BILL_NO AND b.BILL_SER=dt.BILL_SER
       WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND b.BILL_DOC_TYPE IN (1,4,2,5)
     )
     SELECT dt.I_CODE AS "كود الصنف", MAX(m.I_NAME) AS "اسم الصنف",
            ROUND(SUM(CASE WHEN dt.sign=1 THEN dt.qty ELSE 0 END),2) AS "كمية المبيعات",
            ROUND(SUM(CASE WHEN dt.sign=-1 THEN dt.qty ELSE 0 END),2) AS "كمية المردودات (-)",
            TO_CHAR(SUM(dt.item_net * dt.sign),'FM999,999,999,990.00') AS "قيمة المبيعات",
            TO_CHAR(SUM(dt.prorated_disc * dt.sign),'FM999,999,999,990.00') AS "نصيب الصنف من الخصم (-)",
            TO_CHAR(SUM((dt.item_net - dt.prorated_disc) * dt.sign),'FM999,999,999,990.00') AS "الصافي"
     FROM dt
     LEFT JOIN IAS20261.IAS_ITM_MST m ON m.I_CODE=dt.I_CODE
     GROUP BY dt.I_CODE
     ORDER BY SUM((dt.item_net - dt.prorated_disc) * dt.sign) DESC 
     FETCH FIRST 300 ROWS ONLY"""},
   {"id":"by_customer","title":"حسب العميل","params":[DFROM,DTO],"sql":"""
     WITH s AS (
       SELECT b.C_CODE, b.REP_CODE,
              CASE WHEN b.BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) THEN 1 ELSE 0 END as is_sale,
              CASE WHEN b.BILL_DOC_TYPE IN (2,5) THEN 1 ELSE 0 END as is_ret,
              CASE WHEN b.BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) THEN 1 WHEN b.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              NVL(b.BILL_AMT,0) amt, NVL(b.DISC_AMT,0) + NVL(d.itm_disc,0) disc, 0 as ext_disc, NVL(b.VAT_AMT,0) vat, NVL(b.OTHR_AMT,0) othr
       FROM IAS20261.IAS_BILL_MST b
       LEFT JOIN (
           SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as itm_disc
           FROM IAS20261.IAS_BILL_DTL
           GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
       ) d ON b.BILL_DOC_TYPE = d.BILL_DOC_TYPE AND b.BILL_NO = d.BILL_NO AND b.BILL_SER = d.BILL_SER
       WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND b.BILL_DOC_TYPE IN (1,4,2,5)
       UNION ALL
       SELECT C_CODE, REP_CODE,
              0 as is_sale, 0 as is_ret, 0 as sign,
              0 as amt, 0 as disc, NVL(CR_AMT,0) as ext_disc, 0 as vat, 0 as othr
       FROM IAS20261.IAS_POST_DTL
       WHERE DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
     )
     SELECT s.C_CODE AS "كود العميل", MAX(c.C_A_NAME) AS "اسم العميل", MAX(s.REP_CODE) AS "المندوب",
            SUM(s.is_sale) AS "فواتير مبيعات",
            SUM(s.is_ret) AS "فواتير مرتجعات",
            TO_CHAR(SUM(s.amt * s.is_sale),'FM999,999,999,990.00') AS "المبيعات",
            TO_CHAR(SUM(s.amt * s.is_ret),'FM999,999,999,990.00') AS "المردودات (-)",
            TO_CHAR(SUM(s.disc * s.sign),'FM999,999,999,990.00') AS "خصم الفواتير والأصناف (-)",
            TO_CHAR(SUM(s.ext_disc),'FM999,999,999,990.00') AS "إشعار خصم مستقل (-)",
            TO_CHAR(SUM((s.amt - s.disc) * s.sign) - SUM(s.ext_disc),'FM999,999,999,990.00') AS "الصافي قبل الضريبة",
            TO_CHAR(SUM((s.amt - s.disc + s.vat + s.othr) * s.sign) - SUM(s.ext_disc),'FM999,999,999,990.00') AS "الإجمالي بالضريبة"
     FROM s LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE=s.C_CODE
     WHERE s.C_CODE IS NOT NULL
     GROUP BY s.C_CODE 
     ORDER BY SUM((s.amt - s.disc) * s.sign) - SUM(s.ext_disc) DESC 
     FETCH FIRST 300 ROWS ONLY"""},
   {"id":"by_salesman","title":"حسب المندوب","params":[DFROM,DTO],"sql":"""
     WITH s AS (
       SELECT b.REP_CODE, b.C_CODE,
              CASE WHEN b.BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) THEN 1 ELSE 0 END as is_sale,
              CASE WHEN b.BILL_DOC_TYPE IN (2,5) THEN 1 ELSE 0 END as is_ret,
              CASE WHEN b.BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) THEN 1 WHEN b.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              NVL(b.BILL_AMT,0) amt, NVL(b.DISC_AMT,0) + NVL(d.itm_disc,0) disc, 0 as ext_disc, NVL(b.VAT_AMT,0) vat, NVL(b.OTHR_AMT,0) othr
       FROM IAS20261.IAS_BILL_MST b
       LEFT JOIN (
           SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as itm_disc
           FROM IAS20261.IAS_BILL_DTL
           GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
       ) d ON b.BILL_DOC_TYPE = d.BILL_DOC_TYPE AND b.BILL_NO = d.BILL_NO AND b.BILL_SER = d.BILL_SER
       WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND b.BILL_DOC_TYPE IN (1,4,2,5)
       UNION ALL
       SELECT REP_CODE, C_CODE,
              0 as is_sale, 0 as is_ret, 0 as sign,
              0 as amt, 0 as disc, NVL(CR_AMT,0) as ext_disc, 0 as vat, 0 as othr
       FROM IAS20261.IAS_POST_DTL
       WHERE DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
     )
     SELECT s.REP_CODE AS "كود المندوب", MAX(sm.REPRS_A_NAME) AS "اسم المندوب",
            COUNT(DISTINCT s.C_CODE) AS "عدد العملاء",
            SUM(s.is_sale) AS "فواتير مبيعات",
            SUM(s.is_ret) AS "فواتير مرتجعات",
            TO_CHAR(SUM(s.amt * s.is_sale),'FM999,999,999,990.00') AS "المبيعات",
            TO_CHAR(SUM(s.amt * s.is_ret),'FM999,999,999,990.00') AS "المردودات (-)",
            TO_CHAR(SUM(s.disc * s.sign),'FM999,999,999,990.00') AS "خصم الفواتير والأصناف (-)",
# MISSING LINE 251

# MISSING LINE 252

# MISSING LINE 253

# MISSING LINE 254

# MISSING LINE 255

# MISSING LINE 256

# MISSING LINE 257

# MISSING LINE 258

# MISSING LINE 259

# MISSING LINE 260

# MISSING LINE 261

# MISSING LINE 262

# MISSING LINE 263

# MISSING LINE 264

# MISSING LINE 265

# MISSING LINE 266

# MISSING LINE 267

# MISSING LINE 268

# MISSING LINE 269

# MISSING LINE 270

# MISSING LINE 271

# MISSING LINE 272

# MISSING LINE 273

# MISSING LINE 274

# MISSING LINE 275

# MISSING LINE 276

# MISSING LINE 277

# MISSING LINE 278

# MISSING LINE 279

# MISSING LINE 280

# MISSING LINE 281

# MISSING LINE 282

# MISSING LINE 283

# MISSING LINE 284

# MISSING LINE 285

# MISSING LINE 286

# MISSING LINE 287

# MISSING LINE 288

# MISSING LINE 289

# MISSING LINE 290

# MISSING LINE 291

# MISSING LINE 292

# MISSING LINE 293

# MISSING LINE 294

# MISSING LINE 295

# MISSING LINE 296

# MISSING LINE 297

# MISSING LINE 298

# MISSING LINE 299

# MISSING LINE 300

# MISSING LINE 301

# MISSING LINE 302

# MISSING LINE 303

# MISSING LINE 304

# MISSING LINE 305

# MISSING LINE 306

# MISSING LINE 307

# MISSING LINE 308

# MISSING LINE 309

# MISSING LINE 310

# MISSING LINE 311

# MISSING LINE 312

# MISSING LINE 313

# MISSING LINE 314

# MISSING LINE 315

# MISSING LINE 316

# MISSING LINE 317

# MISSING LINE 318

# MISSING LINE 319

# MISSING LINE 320

# MISSING LINE 321

# MISSING LINE 322

# MISSING LINE 323

# MISSING LINE 324

# MISSING LINE 325

# MISSING LINE 326

# MISSING LINE 327

# MISSING LINE 328

# MISSING LINE 329

# MISSING LINE 330

# MISSING LINE 331

# MISSING LINE 332

# MISSING LINE 333

# MISSING LINE 334

# MISSING LINE 335

# MISSING LINE 336

# MISSING LINE 337

# MISSING LINE 338

# MISSING LINE 339

# MISSING LINE 340

# MISSING LINE 341

# MISSING LINE 342

# MISSING LINE 343

# MISSING LINE 344

# MISSING LINE 345

# MISSING LINE 346

# MISSING LINE 347

# MISSING LINE 348

# MISSING LINE 349

# MISSING LINE 350

# MISSING LINE 351

# MISSING LINE 352

# MISSING LINE 353

# MISSING LINE 354

# MISSING LINE 355

# MISSING LINE 356

# MISSING LINE 357

# MISSING LINE 358

# MISSING LINE 359

# MISSING LINE 360

# MISSING LINE 361

# MISSING LINE 362

# MISSING LINE 363

# MISSING LINE 364

# MISSING LINE 365

# MISSING LINE 366

# MISSING LINE 367

# MISSING LINE 368

# MISSING LINE 369

# MISSING LINE 370

# MISSING LINE 371

# MISSING LINE 372

# MISSING LINE 373

# MISSING LINE 374

# MISSING LINE 375

# MISSING LINE 376

# MISSING LINE 377

# MISSING LINE 378

# MISSING LINE 379

# MISSING LINE 380

# MISSING LINE 381

# MISSING LINE 382

# MISSING LINE 383

# MISSING LINE 384

# MISSING LINE 385

# MISSING LINE 386

# MISSING LINE 387

# MISSING LINE 388

# MISSING LINE 389

# MISSING LINE 390

# MISSING LINE 391

# MISSING LINE 392

# MISSING LINE 393

# MISSING LINE 394

# MISSING LINE 395

# MISSING LINE 396

# MISSING LINE 397

# MISSING LINE 398

# MISSING LINE 399

# MISSING LINE 400

# MISSING LINE 401

# MISSING LINE 402

# MISSING LINE 403

# MISSING LINE 404

# MISSING LINE 405

# MISSING LINE 406

# MISSING LINE 407

# MISSING LINE 408

# MISSING LINE 409

# MISSING LINE 410

# MISSING LINE 411

# MISSING LINE 412

# MISSING LINE 413

# MISSING LINE 414

# MISSING LINE 415

# MISSING LINE 416

# MISSING LINE 417

# MISSING LINE 418

# MISSING LINE 419

# MISSING LINE 420

# MISSING LINE 421

# MISSING LINE 422

# MISSING LINE 423

# MISSING LINE 424

# MISSING LINE 425

# MISSING LINE 426

# MISSING LINE 427

# MISSING LINE 428

# MISSING LINE 429

# MISSING LINE 430

# MISSING LINE 431

# MISSING LINE 432

# MISSING LINE 433

# MISSING LINE 434

# MISSING LINE 435

# MISSING LINE 436

# MISSING LINE 437

# MISSING LINE 438

# MISSING LINE 439

# MISSING LINE 440

# MISSING LINE 441

# MISSING LINE 442

# MISSING LINE 443

# MISSING LINE 444

# MISSING LINE 445

# MISSING LINE 446

# MISSING LINE 447

# MISSING LINE 448

# MISSING LINE 449

# MISSING LINE 450

# MISSING LINE 451

# MISSING LINE 452

# MISSING LINE 453

# MISSING LINE 454

# MISSING LINE 455

# MISSING LINE 456

# MISSING LINE 457

# MISSING LINE 458

# MISSING LINE 459

# MISSING LINE 460

# MISSING LINE 461

# MISSING LINE 462

# MISSING LINE 463

# MISSING LINE 464

# MISSING LINE 465

# MISSING LINE 466

# MISSING LINE 467

# MISSING LINE 468

# MISSING LINE 469

# MISSING LINE 470

# MISSING LINE 471

# MISSING LINE 472

# MISSING LINE 473

# MISSING LINE 474

# MISSING LINE 475

# MISSING LINE 476

# MISSING LINE 477

# MISSING LINE 478

# MISSING LINE 479

# MISSING LINE 480

# MISSING LINE 481

# MISSING LINE 482

# MISSING LINE 483

# MISSING LINE 484

# MISSING LINE 485

# MISSING LINE 486

# MISSING LINE 487

# MISSING LINE 488

# MISSING LINE 489

# MISSING LINE 490

# MISSING LINE 491

# MISSING LINE 492

# MISSING LINE 493

# MISSING LINE 494

# MISSING LINE 495

# MISSING LINE 496

# MISSING LINE 497

# MISSING LINE 498

# MISSING LINE 499

# MISSING LINE 500

# MISSING LINE 501

# MISSING LINE 502

# MISSING LINE 503

# MISSING LINE 504

# MISSING LINE 505

# MISSING LINE 506

# MISSING LINE 507

# MISSING LINE 508

# MISSING LINE 509

# MISSING LINE 510

# MISSING LINE 511

# MISSING LINE 512

# MISSING LINE 513

# MISSING LINE 514

# MISSING LINE 515

# MISSING LINE 516

# MISSING LINE 517

# MISSING LINE 518

# MISSING LINE 519

# MISSING LINE 520

# MISSING LINE 521

# MISSING LINE 522

# MISSING LINE 523

# MISSING LINE 524

# MISSING LINE 525

# MISSING LINE 526

# MISSING LINE 527

# MISSING LINE 528

# MISSING LINE 529

# MISSING LINE 530

# MISSING LINE 531

# MISSING LINE 532

# MISSING LINE 533

# MISSING LINE 534

# MISSING LINE 535

# MISSING LINE 536

# MISSING LINE 537

# MISSING LINE 538

# MISSING LINE 539

# MISSING LINE 540

# MISSING LINE 541

# MISSING LINE 542

# MISSING LINE 543

# MISSING LINE 544

# MISSING LINE 545

# MISSING LINE 546

# MISSING LINE 547

# MISSING LINE 548

# MISSING LINE 549

# MISSING LINE 550

# MISSING LINE 551

# MISSING LINE 552

# MISSING LINE 553

# MISSING LINE 554

# MISSING LINE 555

# MISSING LINE 556

# MISSING LINE 557

# MISSING LINE 558

# MISSING LINE 559

# MISSING LINE 560

# MISSING LINE 561

# MISSING LINE 562

# MISSING LINE 563

# MISSING LINE 564

# MISSING LINE 565

# MISSING LINE 566

# MISSING LINE 567

# MISSING LINE 568

# MISSING LINE 569

# MISSING LINE 570

# MISSING LINE 571

# MISSING LINE 572

# MISSING LINE 573

# MISSING LINE 574

# MISSING LINE 575

# MISSING LINE 576

# MISSING LINE 577

# MISSING LINE 578

# MISSING LINE 579

# MISSING LINE 580

# MISSING LINE 581

# MISSING LINE 582

# MISSING LINE 583

# MISSING LINE 584

# MISSING LINE 585

# MISSING LINE 586

# MISSING LINE 587

# MISSING LINE 588

# MISSING LINE 589

# MISSING LINE 590

# MISSING LINE 591

# MISSING LINE 592

# MISSING LINE 593

# MISSING LINE 594

# MISSING LINE 595

# MISSING LINE 596

# MISSING LINE 597

# MISSING LINE 598

# MISSING LINE 599

# MISSING LINE 600

# MISSING LINE 601

# MISSING LINE 602

# MISSING LINE 603

# MISSING LINE 604

# MISSING LINE 605

# MISSING LINE 606

# MISSING LINE 607

# MISSING LINE 608

# MISSING LINE 609

# MISSING LINE 610

# MISSING LINE 611

# MISSING LINE 612

# MISSING LINE 613

# MISSING LINE 614

# MISSING LINE 615

# MISSING LINE 616

# MISSING LINE 617

# MISSING LINE 618

# MISSING LINE 619

                fmt = lambda x: f"{x:,.2f}" if x != 0 else "0.00"
                new_rows.append((r[0], r[1], fmt(tot_rcpt), fmt(net_jrn), fmt(net_cash), fmt(final_tot)))
            
            cols = new_cols
            rows = new_rows

    except Exception as e:
        return "خطأ: " + str(e), 500
    filt = []
    for p in rpt["params"]:
        v = request.args.get(p["name"], p.get("default",""))
        if v not in ("", None): filt.append((p["label"], v))
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    title = rpt["title"] + (" (نموذج 2)" if request.args.get("model") == "2" else "")
    return render_template_string(PRINT_PAGE, title=title, cols=cols, rows=rows, filt=filt, now=now)

SETTINGS_PAGE = """<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>الإعدادات</title>""" + STYLE + """</head><body>
<div class="app"><div class="main">
 <div class="top">""" + LOGO + """<div class="ttl">الإعدادات</div></div>
 <div class="wrap">
   <a class="back" href="/" style="color:#4f46e5;font-weight:700;display:inline-block;margin-bottom:10px">&#8594; رجوع للتقارير</a>
   {% if saved %}<div style="background:#e8f4ec;color:#1e7b34;padding:10px 14px;border-radius:8px;margin:6px 0 12px">تم حفظ الإعدادات</div>{% endif %}
   <h1>إظهار / إخفاء التبويبات والتقارير</h1>
   <p style="color:#6b7280;font-size:13px;margin-bottom:12px">ضع علامة على ما تريد إخفاءه من الواجهة، ثم احفظ.</p>
   <form method="post" action="/settings">
     <input type="hidden" name="action" value="save">
     <div class="card" style="margin-bottom:16px;border:2px solid #f59e0b;background:#fffbeb">
       <label style="font-weight:800;font-size:15px;color:#b45309"><input type="checkbox" name="hide_profit" {{ 'checked' if hide_profit else '' }}> 🔒 إخفاء كل ما يخص الربح من النظام</label>
       <div style="margin-top:6px;color:#92400e;font-size:12.5px">عند التفعيل يُخفى: تبويب «الربحية» بالكامل، بطاقتا «مجمل الربح» و«صافي الربح» في لوحة القيادة، وتقريرا «قائمة الدخل» و«مراكز التكلفة» في التبويب المالي.</div>
     </div>
# MISSING LINE 651

# MISSING LINE 652

# MISSING LINE 653

# MISSING LINE 654

# MISSING LINE 655

# MISSING LINE 656

# MISSING LINE 657

# MISSING LINE 658

# MISSING LINE 659

# MISSING LINE 660

# MISSING LINE 661

# MISSING LINE 662

# MISSING LINE 663

# MISSING LINE 664

# MISSING LINE 665

# MISSING LINE 666

# MISSING LINE 667

# MISSING LINE 668

# MISSING LINE 669

# MISSING LINE 670

# MISSING LINE 671

# MISSING LINE 672

# MISSING LINE 673

# MISSING LINE 674

# MISSING LINE 675

# MISSING LINE 676

# MISSING LINE 677

# MISSING LINE 678

# MISSING LINE 679

# MISSING LINE 680

# MISSING LINE 681

# MISSING LINE 682

# MISSING LINE 683

# MISSING LINE 684

# MISSING LINE 685

# MISSING LINE 686

# MISSING LINE 687

# MISSING LINE 688

# MISSING LINE 689

# MISSING LINE 690

# MISSING LINE 691

# MISSING LINE 692

# MISSING LINE 693

# MISSING LINE 694

# MISSING LINE 695

# MISSING LINE 696

# MISSING LINE 697

# MISSING LINE 698

# MISSING LINE 699

# MISSING LINE 700

# MISSING LINE 701

# MISSING LINE 702

# MISSING LINE 703

# MISSING LINE 704

# MISSING LINE 705

# MISSING LINE 706

# MISSING LINE 707

# MISSING LINE 708

# MISSING LINE 709

# MISSING LINE 710

# MISSING LINE 711

# MISSING LINE 712

# MISSING LINE 713

# MISSING LINE 714

# MISSING LINE 715

# MISSING LINE 716

# MISSING LINE 717

# MISSING LINE 718

# MISSING LINE 719

# MISSING LINE 720

# MISSING LINE 721

# MISSING LINE 722

# MISSING LINE 723

# MISSING LINE 724

# MISSING LINE 725

# MISSING LINE 726

# MISSING LINE 727

# MISSING LINE 728

# MISSING LINE 729

# MISSING LINE 730

# MISSING LINE 731

# MISSING LINE 732

# MISSING LINE 733

# MISSING LINE 734

# MISSING LINE 735

# MISSING LINE 736

# MISSING LINE 737

# MISSING LINE 738

# MISSING LINE 739

# MISSING LINE 740

# MISSING LINE 741

# MISSING LINE 742

# MISSING LINE 743

# MISSING LINE 744

# MISSING LINE 745

# MISSING LINE 746

# MISSING LINE 747

# MISSING LINE 748

# MISSING LINE 749

# MISSING LINE 750

# MISSING LINE 751

# MISSING LINE 752

# MISSING LINE 753

# MISSING LINE 754

# MISSING LINE 755

# MISSING LINE 756

# MISSING LINE 757

# MISSING LINE 758

# MISSING LINE 759

# MISSING LINE 760

# MISSING LINE 761

# MISSING LINE 762

# MISSING LINE 763

# MISSING LINE 764

# MISSING LINE 765

# MISSING LINE 766

# MISSING LINE 767

# MISSING LINE 768

# MISSING LINE 769

# MISSING LINE 770

# MISSING LINE 771

# MISSING LINE 772

# MISSING LINE 773

# MISSING LINE 774

# MISSING LINE 775

# MISSING LINE 776

# MISSING LINE 777

# MISSING LINE 778

# MISSING LINE 779

# MISSING LINE 780

# MISSING LINE 781

# MISSING LINE 782

# MISSING LINE 783

# MISSING LINE 784

# MISSING LINE 785

# MISSING LINE 786

# MISSING LINE 787

# MISSING LINE 788

# MISSING LINE 789

# MISSING LINE 790

# MISSING LINE 791

# MISSING LINE 792

# MISSING LINE 793

# MISSING LINE 794

# MISSING LINE 795

# MISSING LINE 796

# MISSING LINE 797

# MISSING LINE 798

# MISSING LINE 799

# MISSING LINE 800

# MISSING LINE 801

# MISSING LINE 802

# MISSING LINE 803

# MISSING LINE 804

# MISSING LINE 805

# MISSING LINE 806

# MISSING LINE 807

# MISSING LINE 808

# MISSING LINE 809

# MISSING LINE 810

# MISSING LINE 811

# MISSING LINE 812

# MISSING LINE 813

# MISSING LINE 814

# MISSING LINE 815

# MISSING LINE 816

# MISSING LINE 817

# MISSING LINE 818

# MISSING LINE 819

# MISSING LINE 820

# MISSING LINE 821

# MISSING LINE 822

# MISSING LINE 823

# MISSING LINE 824

# MISSING LINE 825

# MISSING LINE 826

# MISSING LINE 827

# MISSING LINE 828

# MISSING LINE 829

# MISSING LINE 830

# MISSING LINE 831

# MISSING LINE 832

# MISSING LINE 833

# MISSING LINE 834

# MISSING LINE 835

# MISSING LINE 836

# MISSING LINE 837

# MISSING LINE 838

# MISSING LINE 839

# MISSING LINE 840

# MISSING LINE 841

# MISSING LINE 842

# MISSING LINE 843

# MISSING LINE 844

# MISSING LINE 845

# MISSING LINE 846

# MISSING LINE 847

# MISSING LINE 848

# MISSING LINE 849

# MISSING LINE 850

# MISSING LINE 851

# MISSING LINE 852

# MISSING LINE 853

# MISSING LINE 854

# MISSING LINE 855

# MISSING LINE 856

# MISSING LINE 857

# MISSING LINE 858

# MISSING LINE 859

# MISSING LINE 860

# MISSING LINE 861

# MISSING LINE 862

# MISSING LINE 863

# MISSING LINE 864

# MISSING LINE 865

# MISSING LINE 866

# MISSING LINE 867

# MISSING LINE 868

# MISSING LINE 869

# MISSING LINE 870

# MISSING LINE 871

# MISSING LINE 872

# MISSING LINE 873

# MISSING LINE 874

# MISSING LINE 875

# MISSING LINE 876

# MISSING LINE 877

# MISSING LINE 878

# MISSING LINE 879

# MISSING LINE 880

# MISSING LINE 881

# MISSING LINE 882

# MISSING LINE 883

# MISSING LINE 884

# MISSING LINE 885

# MISSING LINE 886

# MISSING LINE 887

# MISSING LINE 888

# MISSING LINE 889

# MISSING LINE 890

# MISSING LINE 891

# MISSING LINE 892

# MISSING LINE 893

# MISSING LINE 894

# MISSING LINE 895

# MISSING LINE 896

# MISSING LINE 897

# MISSING LINE 898

# MISSING LINE 899

# MISSING LINE 900

# MISSING LINE 901

# MISSING LINE 902

# MISSING LINE 903

# MISSING LINE 904

# MISSING LINE 905

# MISSING LINE 906

# MISSING LINE 907

# MISSING LINE 908

# MISSING LINE 909

# MISSING LINE 910

# MISSING LINE 911

# MISSING LINE 912

# MISSING LINE 913

# MISSING LINE 914

# MISSING LINE 915

# MISSING LINE 916

# MISSING LINE 917

# MISSING LINE 918

# MISSING LINE 919

# MISSING LINE 920

# MISSING LINE 921

# MISSING LINE 922

# MISSING LINE 923

# MISSING LINE 924

# MISSING LINE 925

# MISSING LINE 926

# MISSING LINE 927

# MISSING LINE 928

# MISSING LINE 929

# MISSING LINE 930

# MISSING LINE 931

# MISSING LINE 932

# MISSING LINE 933

# MISSING LINE 934

# MISSING LINE 935

# MISSING LINE 936

# MISSING LINE 937

# MISSING LINE 938

# MISSING LINE 939

# MISSING LINE 940

# MISSING LINE 941

# MISSING LINE 942

# MISSING LINE 943

# MISSING LINE 944

# MISSING LINE 945

# MISSING LINE 946

# MISSING LINE 947

# MISSING LINE 948

# MISSING LINE 949

# MISSING LINE 950

# MISSING LINE 951

# MISSING LINE 952

# MISSING LINE 953

# MISSING LINE 954

# MISSING LINE 955

# MISSING LINE 956

# MISSING LINE 957

# MISSING LINE 958

# MISSING LINE 959

# MISSING LINE 960

# MISSING LINE 961

# MISSING LINE 962

# MISSING LINE 963

# MISSING LINE 964

# MISSING LINE 965

# MISSING LINE 966

# MISSING LINE 967

# MISSING LINE 968

# MISSING LINE 969

# MISSING LINE 970

# MISSING LINE 971

# MISSING LINE 972

# MISSING LINE 973

# MISSING LINE 974

# MISSING LINE 975

# MISSING LINE 976

# MISSING LINE 977

# MISSING LINE 978

# MISSING LINE 979

# MISSING LINE 980

# MISSING LINE 981

# MISSING LINE 982

# MISSING LINE 983

# MISSING LINE 984

# MISSING LINE 985

# MISSING LINE 986

# MISSING LINE 987

# MISSING LINE 988

# MISSING LINE 989

# MISSING LINE 990

# MISSING LINE 991

# MISSING LINE 992

# MISSING LINE 993

# MISSING LINE 994

# MISSING LINE 995

# MISSING LINE 996

# MISSING LINE 997

# MISSING LINE 998

# MISSING LINE 999

# MISSING LINE 1000

# MISSING LINE 1001

# MISSING LINE 1002

# MISSING LINE 1003

# MISSING LINE 1004

# MISSING LINE 1005

# MISSING LINE 1006

# MISSING LINE 1007

# MISSING LINE 1008

# MISSING LINE 1009

# MISSING LINE 1010

# MISSING LINE 1011

# MISSING LINE 1012

# MISSING LINE 1013

# MISSING LINE 1014

# MISSING LINE 1015

# MISSING LINE 1016

# MISSING LINE 1017

# MISSING LINE 1018

# MISSING LINE 1019

# MISSING LINE 1020

# MISSING LINE 1021

# MISSING LINE 1022

# MISSING LINE 1023

# MISSING LINE 1024

# MISSING LINE 1025

# MISSING LINE 1026

# MISSING LINE 1027

# MISSING LINE 1028

# MISSING LINE 1029

# MISSING LINE 1030

# MISSING LINE 1031

# MISSING LINE 1032

# MISSING LINE 1033

# MISSING LINE 1034

# MISSING LINE 1035

# MISSING LINE 1036

# MISSING LINE 1037

# MISSING LINE 1038

# MISSING LINE 1039

# MISSING LINE 1040

# MISSING LINE 1041

# MISSING LINE 1042

# MISSING LINE 1043

# MISSING LINE 1044

# MISSING LINE 1045

# MISSING LINE 1046

# MISSING LINE 1047

# MISSING LINE 1048

# MISSING LINE 1049

# MISSING LINE 1050

# MISSING LINE 1051

# MISSING LINE 1052

# MISSING LINE 1053

# MISSING LINE 1054

# MISSING LINE 1055

# MISSING LINE 1056

# MISSING LINE 1057

# MISSING LINE 1058

# MISSING LINE 1059

# MISSING LINE 1060

# MISSING LINE 1061

# MISSING LINE 1062

# MISSING LINE 1063

# MISSING LINE 1064

# MISSING LINE 1065

# MISSING LINE 1066

# MISSING LINE 1067

# MISSING LINE 1068

# MISSING LINE 1069

# MISSING LINE 1070

# MISSING LINE 1071

# MISSING LINE 1072

# MISSING LINE 1073

# MISSING LINE 1074

# MISSING LINE 1075

# MISSING LINE 1076

# MISSING LINE 1077

# MISSING LINE 1078

# MISSING LINE 1079

# MISSING LINE 1080

# MISSING LINE 1081

# MISSING LINE 1082

# MISSING LINE 1083

# MISSING LINE 1084

# MISSING LINE 1085

# MISSING LINE 1086

# MISSING LINE 1087

# MISSING LINE 1088

# MISSING LINE 1089

# MISSING LINE 1090

# MISSING LINE 1091

# MISSING LINE 1092

# MISSING LINE 1093

# MISSING LINE 1094

# MISSING LINE 1095

# MISSING LINE 1096

# MISSING LINE 1097

# MISSING LINE 1098

# MISSING LINE 1099

# MISSING LINE 1100

# MISSING LINE 1101

# MISSING LINE 1102

# MISSING LINE 1103

# MISSING LINE 1104

# MISSING LINE 1105

# MISSING LINE 1106

# MISSING LINE 1107

# MISSING LINE 1108

# MISSING LINE 1109

# MISSING LINE 1110

# MISSING LINE 1111

# MISSING LINE 1112

# MISSING LINE 1113

# MISSING LINE 1114

# MISSING LINE 1115

# MISSING LINE 1116

# MISSING LINE 1117

# MISSING LINE 1118

# MISSING LINE 1119

# MISSING LINE 1120

# MISSING LINE 1121

# MISSING LINE 1122

# MISSING LINE 1123

# MISSING LINE 1124

# MISSING LINE 1125

# MISSING LINE 1126

# MISSING LINE 1127

# MISSING LINE 1128

# MISSING LINE 1129

# MISSING LINE 1130

# MISSING LINE 1131

# MISSING LINE 1132

# MISSING LINE 1133

# MISSING LINE 1134

# MISSING LINE 1135

# MISSING LINE 1136

# MISSING LINE 1137

# MISSING LINE 1138

# MISSING LINE 1139

# MISSING LINE 1140

# MISSING LINE 1141

# MISSING LINE 1142

# MISSING LINE 1143

# MISSING LINE 1144

# MISSING LINE 1145

# MISSING LINE 1146

# MISSING LINE 1147

# MISSING LINE 1148

# MISSING LINE 1149

# MISSING LINE 1150

# MISSING LINE 1151

# MISSING LINE 1152

# MISSING LINE 1153

# MISSING LINE 1154

# MISSING LINE 1155

# MISSING LINE 1156

# MISSING LINE 1157

# MISSING LINE 1158

# MISSING LINE 1159

# MISSING LINE 1160

# MISSING LINE 1161

# MISSING LINE 1162

# MISSING LINE 1163

# MISSING LINE 1164

# MISSING LINE 1165

# MISSING LINE 1166

# MISSING LINE 1167

# MISSING LINE 1168

# MISSING LINE 1169

# MISSING LINE 1170

# MISSING LINE 1171

# MISSING LINE 1172

# MISSING LINE 1173

# MISSING LINE 1174

# MISSING LINE 1175

# MISSING LINE 1176

# MISSING LINE 1177

# MISSING LINE 1178

# MISSING LINE 1179

# MISSING LINE 1180

# MISSING LINE 1181

# MISSING LINE 1182

# MISSING LINE 1183

# MISSING LINE 1184

# MISSING LINE 1185

# MISSING LINE 1186

# MISSING LINE 1187

# MISSING LINE 1188

# MISSING LINE 1189

# MISSING LINE 1190

# MISSING LINE 1191

# MISSING LINE 1192

# MISSING LINE 1193

# MISSING LINE 1194

# MISSING LINE 1195

# MISSING LINE 1196

# MISSING LINE 1197

# MISSING LINE 1198

# MISSING LINE 1199

# MISSING LINE 1200

# MISSING LINE 1201

# MISSING LINE 1202

# MISSING LINE 1203

# MISSING LINE 1204

# MISSING LINE 1205

# MISSING LINE 1206

# MISSING LINE 1207

# MISSING LINE 1208

# MISSING LINE 1209

# MISSING LINE 1210

# MISSING LINE 1211

# MISSING LINE 1212

# MISSING LINE 1213

# MISSING LINE 1214

# MISSING LINE 1215

# MISSING LINE 1216

# MISSING LINE 1217

# MISSING LINE 1218

# MISSING LINE 1219

# MISSING LINE 1220

# MISSING LINE 1221

# MISSING LINE 1222

# MISSING LINE 1223

# MISSING LINE 1224

# MISSING LINE 1225

# MISSING LINE 1226

# MISSING LINE 1227

# MISSING LINE 1228

# MISSING LINE 1229

# MISSING LINE 1230

# MISSING LINE 1231

# MISSING LINE 1232

# MISSING LINE 1233

# MISSING LINE 1234

# MISSING LINE 1235

# MISSING LINE 1236

# MISSING LINE 1237

# MISSING LINE 1238

# MISSING LINE 1239

# MISSING LINE 1240

# MISSING LINE 1241

# MISSING LINE 1242

# MISSING LINE 1243

# MISSING LINE 1244

# MISSING LINE 1245

# MISSING LINE 1246

# MISSING LINE 1247

# MISSING LINE 1248

# MISSING LINE 1249

# MISSING LINE 1250

# MISSING LINE 1251

# MISSING LINE 1252

# MISSING LINE 1253

# MISSING LINE 1254

# MISSING LINE 1255

# MISSING LINE 1256

# MISSING LINE 1257

# MISSING LINE 1258

# MISSING LINE 1259

# MISSING LINE 1260

# MISSING LINE 1261

# MISSING LINE 1262

# MISSING LINE 1263

# MISSING LINE 1264

# MISSING LINE 1265

# MISSING LINE 1266

# MISSING LINE 1267

# MISSING LINE 1268

# MISSING LINE 1269

# MISSING LINE 1270

# MISSING LINE 1271

# MISSING LINE 1272

# MISSING LINE 1273

# MISSING LINE 1274

# MISSING LINE 1275

# MISSING LINE 1276

# MISSING LINE 1277

# MISSING LINE 1278

# MISSING LINE 1279

# MISSING LINE 1280

# MISSING LINE 1281

# MISSING LINE 1282

# MISSING LINE 1283

# MISSING LINE 1284

# MISSING LINE 1285

# MISSING LINE 1286

# MISSING LINE 1287

# MISSING LINE 1288

# MISSING LINE 1289

# MISSING LINE 1290

# MISSING LINE 1291

# MISSING LINE 1292

# MISSING LINE 1293

# MISSING LINE 1294

# MISSING LINE 1295

# MISSING LINE 1296

# MISSING LINE 1297

# MISSING LINE 1298

# MISSING LINE 1299

# MISSING LINE 1300

# MISSING LINE 1301

# MISSING LINE 1302

# MISSING LINE 1303

# MISSING LINE 1304

# MISSING LINE 1305

# MISSING LINE 1306

# MISSING LINE 1307

# MISSING LINE 1308

# MISSING LINE 1309

# MISSING LINE 1310

# MISSING LINE 1311

# MISSING LINE 1312

# MISSING LINE 1313

# MISSING LINE 1314

# MISSING LINE 1315

# MISSING LINE 1316

# MISSING LINE 1317

# MISSING LINE 1318

# MISSING LINE 1319

# MISSING LINE 1320

# MISSING LINE 1321

# MISSING LINE 1322

# MISSING LINE 1323

# MISSING LINE 1324

# MISSING LINE 1325

# MISSING LINE 1326

# MISSING LINE 1327

# MISSING LINE 1328

# MISSING LINE 1329

# MISSING LINE 1330

# MISSING LINE 1331

# MISSING LINE 1332

# MISSING LINE 1333

# MISSING LINE 1334

# MISSING LINE 1335

# MISSING LINE 1336

# MISSING LINE 1337

# MISSING LINE 1338

# MISSING LINE 1339

# MISSING LINE 1340

# MISSING LINE 1341

# MISSING LINE 1342

# MISSING LINE 1343

# MISSING LINE 1344

# MISSING LINE 1345

# MISSING LINE 1346

# MISSING LINE 1347

# MISSING LINE 1348

# MISSING LINE 1349

# MISSING LINE 1350

# MISSING LINE 1351

# MISSING LINE 1352

# MISSING LINE 1353

# MISSING LINE 1354

# MISSING LINE 1355

# MISSING LINE 1356

# MISSING LINE 1357

# MISSING LINE 1358

# MISSING LINE 1359

# MISSING LINE 1360

# MISSING LINE 1361

# MISSING LINE 1362

# MISSING LINE 1363

# MISSING LINE 1364

# MISSING LINE 1365

# MISSING LINE 1366

# MISSING LINE 1367

# MISSING LINE 1368

# MISSING LINE 1369

# MISSING LINE 1370

# MISSING LINE 1371

# MISSING LINE 1372

# MISSING LINE 1373

# MISSING LINE 1374

# MISSING LINE 1375

# MISSING LINE 1376

# MISSING LINE 1377

# MISSING LINE 1378

# MISSING LINE 1379

# MISSING LINE 1380

# MISSING LINE 1381

# MISSING LINE 1382

# MISSING LINE 1383

# MISSING LINE 1384

# MISSING LINE 1385

# MISSING LINE 1386

# MISSING LINE 1387

# MISSING LINE 1388

# MISSING LINE 1389

# MISSING LINE 1390

# MISSING LINE 1391

# MISSING LINE 1392

# MISSING LINE 1393

# MISSING LINE 1394

# MISSING LINE 1395

# MISSING LINE 1396

# MISSING LINE 1397

# MISSING LINE 1398

# MISSING LINE 1399

# MISSING LINE 1400

# MISSING LINE 1401

# MISSING LINE 1402

# MISSING LINE 1403

# MISSING LINE 1404

# MISSING LINE 1405

# MISSING LINE 1406

# MISSING LINE 1407

# MISSING LINE 1408

# MISSING LINE 1409

# MISSING LINE 1410

# MISSING LINE 1411

# MISSING LINE 1412

# MISSING LINE 1413

# MISSING LINE 1414

# MISSING LINE 1415

# MISSING LINE 1416

# MISSING LINE 1417

# MISSING LINE 1418

# MISSING LINE 1419

            if c_ret > 0:
                cust_results["CASH_SALES_" + str(r_code)]["total"] -= c_ret
                cust_results["CASH_SALES_" + str(r_code)]["b"][0] -= c_ret

    cols = ["رقم العميل", "اسم العميل", "0-30", "31-60", "61-90", "91-120", "أكثر من 120", "إجمالي التحصيل"]
    rows = []
    
    for ccode, data in cust_results.items():
        if round(data["total"], 2) == 0 and sum(abs(x) for x in data["b"]) < 0.01: continue
        
        if str(ccode).startswith("CASH_SALES_"):
            c_name = "مبيعات نقدية (للمندوب)"
            disp_code = "-"
        else:
            c_name = cust_names.get(str(ccode), str(ccode))
            disp_code = str(ccode)
            
        row = (
            disp_code,
            c_name,
            f"{data['b'][0]:,.2f}",
            f"{data['b'][1]:,.2f}",
            f"{data['b'][2]:,.2f}",
            f"{data['b'][3]:,.2f}",
            f"{data['b'][4]:,.2f}",
            f"{data['total']:,.2f}"
        )
        rows.append(row)
        
    rows.sort(key=lambda x: float(x[7].replace(',','')), reverse=True)
    return cols, rows


def run_main_wh_movement(rpt, args):
    from collections import defaultdict
    date_from_str = args.get("date_from", "2026-01-01")
    date_to_str = args.get("date_to", "2026-12-31")
    i_code_str = args.get("i_code", "").split(" - ")[0].strip()
    
    print(f"[DEBUG WH] date_from: {date_from_str}, date_to: {date_to_str}, i_code: {i_code_str}")
    
    wh_mapping = {
        "105": "مخزن عيضة",
# MISSING LINE 1463

# MISSING LINE 1464

# MISSING LINE 1465

# MISSING LINE 1466

# MISSING LINE 1467

# MISSING LINE 1468

# MISSING LINE 1469

# MISSING LINE 1470

# MISSING LINE 1471

# MISSING LINE 1472

# MISSING LINE 1473

# MISSING LINE 1474

# MISSING LINE 1475

# MISSING LINE 1476

# MISSING LINE 1477

# MISSING LINE 1478

# MISSING LINE 1479

# MISSING LINE 1480

# MISSING LINE 1481

# MISSING LINE 1482

# MISSING LINE 1483

# MISSING LINE 1484

# MISSING LINE 1485

# MISSING LINE 1486

# MISSING LINE 1487

# MISSING LINE 1488

# MISSING LINE 1489

# MISSING LINE 1490

# MISSING LINE 1491

# MISSING LINE 1492

# MISSING LINE 1493

# MISSING LINE 1494

# MISSING LINE 1495

# MISSING LINE 1496

# MISSING LINE 1497

# MISSING LINE 1498

# MISSING LINE 1499

# MISSING LINE 1500

# MISSING LINE 1501

# MISSING LINE 1502

# MISSING LINE 1503

# MISSING LINE 1504

# MISSING LINE 1505

# MISSING LINE 1506

# MISSING LINE 1507

# MISSING LINE 1508

# MISSING LINE 1509

# MISSING LINE 1510

# MISSING LINE 1511

# MISSING LINE 1512

# MISSING LINE 1513

# MISSING LINE 1514

# MISSING LINE 1515

# MISSING LINE 1516

# MISSING LINE 1517

# MISSING LINE 1518

# MISSING LINE 1519

# MISSING LINE 1520

# MISSING LINE 1521

# MISSING LINE 1522

# MISSING LINE 1523

# MISSING LINE 1524

# MISSING LINE 1525

# MISSING LINE 1526

# MISSING LINE 1527

# MISSING LINE 1528

# MISSING LINE 1529

# MISSING LINE 1530

# MISSING LINE 1531

# MISSING LINE 1532

# MISSING LINE 1533

# MISSING LINE 1534

# MISSING LINE 1535

# MISSING LINE 1536

# MISSING LINE 1537

# MISSING LINE 1538

# MISSING LINE 1539

# MISSING LINE 1540

# MISSING LINE 1541

# MISSING LINE 1542

# MISSING LINE 1543

# MISSING LINE 1544

# MISSING LINE 1545

# MISSING LINE 1546

# MISSING LINE 1547

# MISSING LINE 1548

# MISSING LINE 1549

# MISSING LINE 1550

# MISSING LINE 1551

# MISSING LINE 1552

# MISSING LINE 1553

# MISSING LINE 1554

# MISSING LINE 1555

# MISSING LINE 1556

# MISSING LINE 1557

# MISSING LINE 1558

# MISSING LINE 1559

# MISSING LINE 1560

# MISSING LINE 1561

# MISSING LINE 1562

# MISSING LINE 1563

# MISSING LINE 1564

# MISSING LINE 1565

# MISSING LINE 1566

# MISSING LINE 1567

# MISSING LINE 1568

# MISSING LINE 1569

# MISSING LINE 1570

# MISSING LINE 1571

# MISSING LINE 1572

# MISSING LINE 1573

# MISSING LINE 1574

# MISSING LINE 1575

# MISSING LINE 1576

# MISSING LINE 1577

# MISSING LINE 1578

# MISSING LINE 1579

# MISSING LINE 1580

# MISSING LINE 1581

# MISSING LINE 1582

# MISSING LINE 1583

# MISSING LINE 1584

# MISSING LINE 1585

# MISSING LINE 1586

# MISSING LINE 1587

# MISSING LINE 1588

# MISSING LINE 1589

# MISSING LINE 1590

# MISSING LINE 1591

# MISSING LINE 1592

# MISSING LINE 1593

# MISSING LINE 1594

# MISSING LINE 1595

# MISSING LINE 1596

# MISSING LINE 1597

# MISSING LINE 1598

# MISSING LINE 1599

# MISSING LINE 1600

# MISSING LINE 1601

# MISSING LINE 1602

# MISSING LINE 1603

# MISSING LINE 1604

# MISSING LINE 1605

# MISSING LINE 1606

# MISSING LINE 1607

# MISSING LINE 1608

# MISSING LINE 1609

# MISSING LINE 1610

# MISSING LINE 1611

# MISSING LINE 1612

# MISSING LINE 1613

# MISSING LINE 1614

# MISSING LINE 1615

# MISSING LINE 1616

# MISSING LINE 1617

# MISSING LINE 1618

# MISSING LINE 1619

# MISSING LINE 1620

# MISSING LINE 1621

# MISSING LINE 1622

# MISSING LINE 1623

# MISSING LINE 1624

# MISSING LINE 1625

# MISSING LINE 1626

# MISSING LINE 1627

# MISSING LINE 1628

# MISSING LINE 1629

# MISSING LINE 1630

# MISSING LINE 1631

# MISSING LINE 1632

# MISSING LINE 1633

# MISSING LINE 1634

# MISSING LINE 1635

# MISSING LINE 1636

# MISSING LINE 1637

# MISSING LINE 1638

# MISSING LINE 1639

# MISSING LINE 1640

# MISSING LINE 1641

# MISSING LINE 1642

# MISSING LINE 1643

# MISSING LINE 1644

# MISSING LINE 1645

# MISSING LINE 1646

# MISSING LINE 1647

# MISSING LINE 1648

# MISSING LINE 1649

# MISSING LINE 1650

# MISSING LINE 1651

# MISSING LINE 1652

# MISSING LINE 1653

# MISSING LINE 1654

# MISSING LINE 1655

# MISSING LINE 1656

# MISSING LINE 1657

# MISSING LINE 1658

# MISSING LINE 1659

# MISSING LINE 1660

# MISSING LINE 1661

# MISSING LINE 1662

# MISSING LINE 1663

# MISSING LINE 1664

# MISSING LINE 1665

# MISSING LINE 1666

# MISSING LINE 1667

# MISSING LINE 1668

# MISSING LINE 1669

# MISSING LINE 1670

# MISSING LINE 1671

# MISSING LINE 1672

# MISSING LINE 1673

# MISSING LINE 1674

# MISSING LINE 1675

# MISSING LINE 1676

# MISSING LINE 1677

# MISSING LINE 1678

# MISSING LINE 1679

# MISSING LINE 1680

# MISSING LINE 1681

# MISSING LINE 1682

# MISSING LINE 1683

# MISSING LINE 1684

# MISSING LINE 1685

# MISSING LINE 1686

# MISSING LINE 1687

# MISSING LINE 1688

# MISSING LINE 1689

# MISSING LINE 1690

# MISSING LINE 1691

# MISSING LINE 1692

# MISSING LINE 1693

# MISSING LINE 1694

# MISSING LINE 1695

# MISSING LINE 1696

# MISSING LINE 1697

# MISSING LINE 1698

# MISSING LINE 1699

# MISSING LINE 1700

# MISSING LINE 1701

# MISSING LINE 1702

# MISSING LINE 1703

# MISSING LINE 1704

# MISSING LINE 1705

# MISSING LINE 1706

# MISSING LINE 1707

# MISSING LINE 1708

# MISSING LINE 1709

# MISSING LINE 1710

# MISSING LINE 1711

# MISSING LINE 1712

# MISSING LINE 1713

# MISSING LINE 1714

# MISSING LINE 1715

# MISSING LINE 1716

# MISSING LINE 1717

# MISSING LINE 1718

# MISSING LINE 1719

# MISSING LINE 1720

# MISSING LINE 1721

# MISSING LINE 1722

# MISSING LINE 1723

# MISSING LINE 1724

# MISSING LINE 1725

# MISSING LINE 1726

# MISSING LINE 1727

# MISSING LINE 1728

# MISSING LINE 1729

# MISSING LINE 1730

# MISSING LINE 1731

# MISSING LINE 1732

# MISSING LINE 1733

# MISSING LINE 1734

# MISSING LINE 1735

# MISSING LINE 1736

# MISSING LINE 1737

# MISSING LINE 1738

# MISSING LINE 1739

# MISSING LINE 1740

# MISSING LINE 1741

# MISSING LINE 1742

# MISSING LINE 1743

# MISSING LINE 1744

# MISSING LINE 1745

# MISSING LINE 1746

# MISSING LINE 1747

# MISSING LINE 1748

# MISSING LINE 1749

# MISSING LINE 1750

# MISSING LINE 1751

# MISSING LINE 1752

# MISSING LINE 1753

# MISSING LINE 1754

# MISSING LINE 1755

# MISSING LINE 1756

# MISSING LINE 1757

# MISSING LINE 1758

# MISSING LINE 1759

# MISSING LINE 1760

# MISSING LINE 1761

# MISSING LINE 1762

# MISSING LINE 1763

# MISSING LINE 1764

# MISSING LINE 1765

# MISSING LINE 1766

# MISSING LINE 1767

# MISSING LINE 1768

# MISSING LINE 1769

# MISSING LINE 1770

# MISSING LINE 1771

# MISSING LINE 1772

# MISSING LINE 1773

# MISSING LINE 1774

# MISSING LINE 1775

# MISSING LINE 1776

# MISSING LINE 1777

# MISSING LINE 1778

# MISSING LINE 1779

# MISSING LINE 1780

# MISSING LINE 1781

# MISSING LINE 1782

# MISSING LINE 1783

# MISSING LINE 1784

# MISSING LINE 1785

# MISSING LINE 1786

# MISSING LINE 1787

# MISSING LINE 1788

# MISSING LINE 1789

# MISSING LINE 1790

# MISSING LINE 1791

# MISSING LINE 1792

# MISSING LINE 1793

# MISSING LINE 1794

# MISSING LINE 1795

# MISSING LINE 1796

# MISSING LINE 1797

# MISSING LINE 1798

# MISSING LINE 1799

# MISSING LINE 1800

# MISSING LINE 1801

# MISSING LINE 1802

# MISSING LINE 1803

# MISSING LINE 1804

# MISSING LINE 1805

# MISSING LINE 1806

# MISSING LINE 1807

# MISSING LINE 1808

# MISSING LINE 1809

# MISSING LINE 1810

# MISSING LINE 1811

# MISSING LINE 1812

# MISSING LINE 1813

# MISSING LINE 1814

# MISSING LINE 1815

# MISSING LINE 1816

# MISSING LINE 1817

# MISSING LINE 1818

# MISSING LINE 1819

# MISSING LINE 1820

# MISSING LINE 1821

# MISSING LINE 1822

# MISSING LINE 1823

# MISSING LINE 1824

# MISSING LINE 1825

# MISSING LINE 1826

# MISSING LINE 1827

# MISSING LINE 1828

# MISSING LINE 1829

# MISSING LINE 1830

# MISSING LINE 1831

# MISSING LINE 1832

# MISSING LINE 1833

# MISSING LINE 1834

# MISSING LINE 1835

# MISSING LINE 1836

# MISSING LINE 1837

# MISSING LINE 1838

.filters input, .filters select { width: 100%; padding: 12px 16px; border: 1px solid var(--line); border-radius: 12px; font-family: inherit; font-size: 14px; font-weight: 500; color: var(--ink-dark); background: #f8fafc; outline: none; transition: 0.3s; }
.filters input:focus, .filters select:focus { border-color: var(--primary); background: #fff; box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.1); }
.filters .btn { background: var(--primary); color: #fff; border: 0; padding: 14px 24px; border-radius: 12px; font-weight: 600; font-size: 14px; cursor: pointer; transition: 0.3s; height: 46px; }
.filters .btn:hover { background: var(--primary-hover); transform: translateY(-2px); box-shadow: 0 10px 20px rgba(79, 70, 229, 0.2); }

.tw { overflow-x: auto; background: var(--card-bg); border-radius: 20px; box-shadow: var(--sh); padding: 10px; }
table { border-collapse: collapse; width: 100%;  }
thead th { white-space: nowrap; color: var(--ink); padding: 8px 12px; text-align: right; font-size: 13px; font-weight: 600; border-bottom: 2px solid var(--line);  }
tbody td { white-space: nowrap; padding: 6px 12px; border-bottom: 1px solid var(--line); font-size: 13px; font-weight: 500; color: var(--ink-dark);  transition: 0.2s; }
tbody tr:hover td { background: #f8fafc; }

.rhead { display: flex; align-items: center; gap: 16px; margin-bottom: 10px; }
.rhead h1 { margin: 0; flex: 1; font-size: 20px; color: var(--ink-dark); font-weight: 800; border:0; padding:0; }
.rhead h1::before { display: none; }
.cnt { color: var(--ink); font-size: 13px; font-weight: 600; margin-bottom: 10px; }
.exps { display: flex; gap: 10px; }
.exp { border: 0; border-radius: 10px; padding: 10px 20px; font-weight: 600; font-size: 13px; color: #fff; cursor: pointer; transition: 0.3s; }
.exp:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
.exp.xl { background: #10b981; } .exp.pf { background: #ef4444; }
.err { background: #fef2f2; color: #b91c1c; padding: 16px; border-radius: 12px; font-weight: 600; }

.gdwrap { display: flex; flex-direction: column; gap: 24px; }
.gkpis { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }
.gk { background: var(--card-bg); border-radius: 24px; padding: 24px; display: flex; flex-direction: column; gap: 16px; box-shadow: var(--sh); position: relative; overflow: hidden; }
.gk:nth-child(1) { background: var(--primary); color: #fff; }
.gk:nth-child(1) .gl { color: rgba(255,255,255,0.8); }
.gk:nth-child(1) .gv { color: #fff; }
.gk .gic { width: 48px; height: 48px; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 20px; }
.gk:nth-child(1) .gic { background: rgba(255,255,255,0.2); }
.gk:nth-child(2) .gic { background: #dcfce7; color: #16a34a; }
.gk:nth-child(3) .gic { background: #ffedd5; color: #f97316; }
.gk:nth-child(4) .gic { background: #e0e7ff; color: #4f46e5; }
.gk:nth-child(5) .gic { background: #d1fae5; color: #059669; }
.gk:nth-child(6) .gic { background: #fee2e2; color: #dc2626; }
.gk:nth-child(7) .gic { background: #e0f2fe; color: #0284c7; }
.gk:nth-child(8) .gic { background: #fef3c7; color: #d97706; }
.gk .gl { font-size: 13px; font-weight: 600; color: var(--ink); margin-bottom: 4px; }
.gk .gv { font-size: 26px; font-weight: 800; color: var(--ink-dark); }
.gcharts { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
.gc { background: var(--card-bg); border-radius: 24px; padding: 24px; box-shadow: var(--sh); }
.gc h3 { font-size: 16px; font-weight: 700; margin: 0 0 20px; color: var(--ink-dark); }
.app-logo { color:#4f46e5; font-weight:900; font-size:26px; letter-spacing:-1px; }
.mobile-dropdown { display: none; }
.mobile-dropdown select { width: 100%; padding: 12px 16px; border: 2px solid var(--primary); border-radius: 12px; font-family: inherit; font-size: 15px; font-weight: 700; color: var(--primary); background: #f8fafc; outline: none; text-align: center; cursor: pointer; margin-bottom: 15px; box-shadow: var(--sh); }

@media(max-width:900px){
  .app { flex-direction:column; padding:10px; }
  .sb { width:100%; flex-direction:row; padding:10px; overflow-x:auto; border-radius:16px; gap:8px; align-items:flex-start; -webkit-overflow-scrolling: touch; }
  .brand { margin:0; padding-right:10px; align-self: center; }
  .brand span { display:none; }
  .menu-lbl { display:none; }
  .sb a { margin:0; padding:8px 10px; flex-shrink: 0; flex-direction: column; justify-content: center; gap: 5px; min-width: 65px; text-align: center; }

PAGE = """<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>تقارير SREEN</title>""" + STYLE + """</head><body>
<div class="app">
 <aside class="sb">
   <div class="brand"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg><span>Onyx Deck</span></div>
   <div class="menu-lbl">القائمة الرئيسية</div>
   
   {% for t in tabs %}{% if t.id not in hidden_tabs %}
     <a class="{{ 'on' if t.id==cur_tab else '' }}" href="/?tab={{t.id}}">
       <svg viewBox="0 0 24 24"><path d="{{t.icon}}"/></svg><span>{{ t.title }}</span></a>
   {% endif %}{% endfor %}
   <div class="menu-lbl" style="margin-top:auto">أدوات</div>
   <a href="/settings"><svg viewBox="0 0 24 24"><path d="M4 6h9M4 12h5M4 18h7"/><circle cx="17" cy="6" r="2.3"/><circle cx="13" cy="12" r="2.3"/><circle cx="15" cy="18" r="2.3"/></svg><span>الإعدادات</span></a>
 </aside>
 <div class="main">
   <div class="top">""" + LOGO + """<div class="ttl">لوحة <b>التقارير</b></div></div>
   <div class="wrap">
     {% if dash %}
     <div class="rhead"><h1>لوحة القيادة</h1></div>
     <form class="filters" method="get" action="/">
       <input type="hidden" name="tab" value="{{cur_tab}}"><input type="hidden" name="report" value="overview">
       <div><label>من تاريخ</label><input type="date" name="date_from" value="{{ binds.get('date_from') or '2026-01-01' }}"></div>
       <div><label>إلى تاريخ</label><input type="date" name="date_to" value="{{ binds.get('date_to') or '2026-12-31' }}"></div>
       <div><button class="btn" type="submit">تحديث</button></div>
     </form>
     {% if error %}<div class="err">خطأ: {{error}}</div>{% else %}
     <div class="gdwrap">
       <div class="gkpis">
         <div class="gk"><div class="gic" style="background:#dbeafe">💵</div><div><div class="gl">إجمالي المبيعات</div><div class="gv">{{ "{:,.0f}".format(dash.sales) }}</div></div></div>
         <div class="gk"><div class="gic" style="background:#dcfce7">💰</div><div><div class="gl">إجمالي التحصيل</div><div class="gv">{{ "{:,.0f}".format(dash.collect) }}</div></div></div>
         <div class="gk"><div class="gic" style="background:#ffedd5">🛒</div><div><div class="gl">إجمالي المشتريات</div><div class="gv">{{ "{:,.0f}".format(dash.purch) }}</div></div></div>
         {% if not hide_profit %}<div class="gk"><div class="gic" style="background:#ede9fe">📈</div><div><div class="gl">مجمل الربح</div><div class="gv">{{ "{:,.0f}".format(dash.gross) }}</div></div></div>
         <div class="gk"><div class="gic" style="background:#d1fae5">✅</div><div><div class="gl">صافي الربح</div><div class="gv">{{ "{:,.0f}".format(dash.netprofit) }}</div></div></div>{% endif %}
         <div class="gk"><div class="gic" style="background:#fee2e2">🧾</div><div><div class="gl">الذمم المدينة</div><div class="gv">{{ "{:,.0f}".format(dash.recv) }}</div></div></div>
         <div class="gk"><div class="gic" style="background:#e0f2fe">📦</div><div><div class="gl">قيمة المخزون</div><div class="gv">{{ "{:,.0f}".format(dash.invval) }}</div></div></div>
         <div class="gk"><div class="gic" style="background:#fef3c7">🏛️</div><div><div class="gl">صافي الضريبة</div><div class="gv">{{ "{:,.0f}".format(dash.vat) }}</div></div></div>
       </div>
       <div class="gcharts" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
          <div class="gc" style="grid-column: 1 / -1;"><h3>المبيعات والتحصيل شهرياً</h3><div style="position:relative;height:280px;width:100%"><canvas id="c1"></canvas></div></div>
          <div class="gc"><h3>أفضل 5 مناديب</h3><div style="position:relative;height:250px;width:100%"><canvas id="c2"></canvas></div></div>
          <div class="gc"><h3>أفضل 5 أصناف</h3><div style="position:relative;height:250px;width:100%"><canvas id="c3"></canvas></div></div>
          <div class="gc" style="grid-column: 1 / -1;"><h3>المشتريات شهرياً</h3><div style="position:relative;height:280px;width:100%"><canvas id="c4"></canvas></div></div>
        </div>
     </div>
          <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
     <script>
     var D={{ dash|tojson }};
     window.addEventListener("load",function(){ 
       if(!window.Chart) return; 
       Chart.defaults.font.family = "'Cairo', 'Inter', sans-serif";
       Chart.defaults.color = "#64748b";
       
       const commonOptions = {
         responsive: true,
         maintainAspectRatio: false,
         plugins: {
           legend: { display: false },
           tooltip: { backgroundColor: '#1e293b', padding: 14, titleFont: { size: 14, family: "'Cairo', sans-serif", weight: 'bold' }, bodyFont: { size: 14, family: "'Cairo', sans-serif" }, cornerRadius: 10, displayColors: true, boxPadding: 6 }
         }
       };
       
       // C1: Bar Chart (Sales & Collection)
       new Chart(document.getElementById("c1"),{
         type:"bar",
         data:{
           labels:D.months,
           datasets:[
             {label:"مبيعات", data:D.msales, backgroundColor:"#4f46e5", borderRadius:8, maxBarThickness: 32},
             {label:"تحصيل", data:D.mcollect, backgroundColor:"#38bdf8", borderRadius:8, maxBarThickness: 32}
           ]
         },
         options: {
           ...commonOptions,
           plugins: { ...commonOptions.plugins, legend: { display: true, position: 'top', align: 'end', labels: { usePointStyle: true, boxWidth: 10, font: { family: "'Cairo'", size: 13, weight: 'bold' } } } },
           scales: {
             x: { grid: { display: false }, border: { display: false } },
             y: { grid: { color: '#f1f5f9', borderDash: [6, 4] }, border: { display: false } }
           }
         }
       });

       // C2: Doughnut (Salesmen)
       new Chart(document.getElementById("c2"),{
         type:"doughnut",
         data:{
           labels:D.rep_labels.slice(0,5),
           datasets:[{data:D.rep_vals.slice(0,5), backgroundColor:["#4f46e5", "#38bdf8", "#10b981", "#f59e0b", "#8b5cf6"], borderWidth: 0, hoverOffset: 4}]
         },
         options: {
           responsive: true, maintainAspectRatio: false, cutout: '75%',
           plugins: { legend: { display: true, position: 'bottom', labels: { usePointStyle: true, boxWidth: 8, font: { size: 11 } } } }
         }
       });

       // C3: Doughnut (Items)
       new Chart(document.getElementById("c3"),{
         type:"doughnut",
         data:{
           labels:D.itm_labels.slice(0,5),
           datasets:[{data:D.itm_vals.slice(0,5), backgroundColor:["#f43f5e", "#d946ef", "#0ea5e9", "#14b8a6", "#eab308"], borderWidth: 0, hoverOffset: 4}]
         },
         options: {
           responsive: true, maintainAspectRatio: false, cutout: '75%',
           plugins: { legend: { display: true, position: 'bottom', labels: { usePointStyle: true, boxWidth: 8, font: { size: 11 } } } }
         }
       });

       // C4: Line Chart (Purchases)
       const ctx4 = document.getElementById("c4").getContext('2d');
       const grad4 = ctx4.createLinearGradient(0, 0, 0, 300);
       grad4.addColorStop(0, 'rgba(16, 185, 129, 0.4)');
       grad4.addColorStop(1, 'rgba(16, 185, 129, 0.0)');
       
       new Chart(ctx4,{
         type:"line",
         data:{
           labels:D.months,
           datasets:[{
             label: "مشتريات", data:D.mpurch, borderColor:"#10b981", borderWidth: 3, backgroundColor: grad4, fill:true, tension:0.4, pointRadius: 0, pointHoverRadius: 6, pointBackgroundColor: "#fff", pointBorderColor: "#10b981", pointBorderWidth: 2
           }]
         },
         options: {
           ...commonOptions,
           interaction: { mode: 'index', intersect: false },
           scales: {
             x: { grid: { display: false }, border: { display: false } },
             y: { grid: { color: '#f1f5f9', borderDash: [6, 4] }, border: { display: false } }
           }
         }
       });
     });
     </script>
     <script>
     var D={{ dash|tojson }};
     window.addEventListener("load",function(){ 
       if(!window.Chart) return; 
       Chart.defaults.font.family = "'Cairo', 'Inter', sans-serif";
       Chart.defaults.color = "#64748b";
       
       const commonOptions = {
         responsive: true,
         maintainAspectRatio: false,
         plugins: {
           legend: { display: false },
           tooltip: {
             backgroundColor: '#1e293b',
             padding: 14,
             titleFont: { size: 14, family: "'Cairo', sans-serif", weight: 'bold' },
             bodyFont: { size: 14, family: "'Cairo', sans-serif" },
             cornerRadius: 10,
             displayColors: true,
             boxPadding: 6
           }
         },
         scales: {
           x: { grid: { display: false }, border: { display: false }, ticks: { font: { weight: '600' } } },
           y: { grid: { color: '#f1f5f9', borderDash: [6, 4] }, border: { display: false }, ticks: { font: { weight: '600' }, padding: 10 } }
         }
       };

       const horizontalOptions = JSON.parse(JSON.stringify(commonOptions));
       horizontalOptions.indexAxis = "y";
       horizontalOptions.scales.x = { grid: { color: '#f1f5f9', borderDash: [6, 4] }, border: { display: false }, ticks: { font: { weight: '600' } } };
       horizontalOptions.scales.y = { grid: { display: false }, border: { display: false }, ticks: { font: { weight: '600' }, padding: 10 } };
       
       // C1: Bar Chart (Sales & Collection)
       new Chart(document.getElementById("c1"),{
         type:"bar",
         data:{
           labels:D.months,
           datasets:[
             {label:"مبيعات", data:D.msales, backgroundColor:"#4f46e5", borderRadius:8, maxBarThickness: 32, borderSkipped: false},
             {label:"تحصيل", data:D.mcollect, backgroundColor:"#38bdf8", borderRadius:8, maxBarThickness: 32, borderSkipped: false}
           ]
         },
         options: {
           ...commonOptions,
           plugins: {
             ...commonOptions.plugins,
             legend: { display: true, position: 'top', align: 'end', labels: { usePointStyle: true, boxWidth: 10, padding: 20, font: { family: "'Cairo'", size: 13, weight: 'bold' } } }
           }
         }
       });

       // C2: Horizontal Bar (Salesmen)
       new Chart(document.getElementById("c2"),{
         type:"bar",
         data:{
           labels:D.rep_labels,
           datasets:[{label: "مبيعات", data:D.rep_vals, backgroundColor:"#8b5cf6", borderRadius:8, maxBarThickness: 24, borderSkipped: false}]
         },
         options: horizontalOptions
       });

       // C3: Horizontal Bar (Items)
       new Chart(document.getElementById("c3"),{
         type:"bar",
         data:{
           labels:D.itm_labels,
           datasets:[{label: "مبيعات", data:D.itm_vals, backgroundColor:"#10b981", borderRadius:8, maxBarThickness: 24, borderSkipped: false}]
         },
         options: horizontalOptions
       });

       // C4: Line Chart (Purchases)
       const ctx4 = document.getElementById("c4").getContext('2d');
       const grad4 = ctx4.createLinearGradient(0, 0, 0, 300);
       grad4.addColorStop(0, 'rgba(249, 115, 22, 0.4)');
       grad4.addColorStop(1, 'rgba(249, 115, 22, 0.0)');
       
       new Chart(ctx4,{
         type:"line",
         data:{
           labels:D.months,
           datasets:[{
             label: "مشتريات",
             data:D.mpurch,
             borderColor:"#f97316",
             borderWidth: 3,
             backgroundColor: grad4,
             fill:true,
             tension:0.4,
             pointRadius: 0,
             pointHoverRadius: 6,
             pointBackgroundColor: "#fff",
             pointBorderColor: "#f97316",
             pointBorderWidth: 2
           }]
         },
         options: {
           ...commonOptions,
           interaction: { mode: 'index', intersect: false }
         }
       });
     });
     </script>
     {% endif %}
     {% else %}
     <div class="pills">
       {% for r in tab.reports %}{% if (cur_tab ~ '/' ~ r.id) not in hidden_reports %}
         <a class="pill {{ 'on' if r.id==rpt.id else '' }}" href="/?tab={{cur_tab}}&report={{r.id}}">{{ r.title }}</a>
       {% endif %}{% endfor %}
     </div>
     <div class="mobile-dropdown">
       <select onchange="window.location.href=this.value">
         {% for r in tab.reports %}{% if (cur_tab ~ '/' ~ r.id) not in hidden_reports %}
           <option value="/?tab={{cur_tab}}&report={{r.id}}" {{ 'selected' if r.id==rpt.id else '' }}>{{ r.title }}</option>
         {% endif %}{% endfor %}
       </select>
     </div>
     <div class="rhead">
  <h1>{{ rpt.title }}</h1>
  <div class="exps">
    <a class="exp xl" href="/export?{{qs}}&format=xlsx">Excel</a>
    {% if rpt.id == 'collection_adopted' %}
      <select id="pdfModel" style="padding:4px 8px; border:1px solid #cbd5e1; border-radius:4px; margin-left:4px; font-family:inherit; font-size:13px;">
        <option value="1">PDF (النموذج الافتراضي)</option>
        <option value="2">PDF (نموذج 2)</option>
      </select>
      <button class="exp pf" style="border:none; cursor:pointer;" onclick="window.open('/print?{{qs|safe}}&model=' + document.getElementById('pdfModel').value, '_blank')">طباعة</button>
    {% else %}
      <a class="exp pf" href="/print?{{qs}}" target="_blank">PDF</a>
    {% endif %}
  </div>
</div>
     {% if rpt.params %}
     <form class="filters" method="get" action="/">
       <input type="hidden" name="tab" value="{{cur_tab}}"><input type="hidden" name="report" value="{{rpt.id}}">
       {% for p in rpt.params %}
         <div><label>{{p.label}}</label>
         {% if p.type=='select' %}
           <select name="{{p.name}}">{% for o in p.options %}<option value="{{o[0]}}" {{'selected' if binds.get(p.name)==o[0] else ''}}>{{o[1]}}</option>{% endfor %}</select>
         {% elif p.get('_list') %}
           <input type="text" name="{{p.name}}" list="dl_{{p.name}}" autocomplete="off" placeholder="ابحث بالكود أو الاسم" value="{{ binds.get(p.name) if binds.get(p.name) is not none else '' }}">
           <datalist id="dl_{{p.name}}">{% for o in p.get('_list') %}<option value="{{o}}"></option>{% endfor %}</datalist>
         {% else %}
           <input type="{{p.type}}" name="{{p.name}}" value="{{ binds.get(p.name) if binds.get(p.name) is not none else '' }}">
         {% endif %}
         </div>
       {% endfor %}
       <div><button class="btn" type="submit">عرض التقرير</button></div>
     </form>
     {% endif %}
     {% if error %}<div class="err">خطأ: {{error}}</div>
     {% else %}
       <div class="cnt">عدد الصفوف: {{rows|length}}</div>
       <div class="tw"><table><thead><tr>{% for c in cols %}<th onclick="sortTable({{loop.index0}})" style="cursor:pointer" title="اضغط للترتيب">{{c}} <span style="font-size:10px; opacity:0.5; margin-right:4px">↕</span></th>{% endfor %}</tr></thead>
       <tbody>{% for row in rows %}<tr>{% for cell in row %}<td>{{ '' if cell is none else cell }}</td>{% endfor %}</tr>{% endfor %}</tbody></table></div>
     {% endif %}
     {% endif %}
   </div>
 </div>
 <script>
 document.addEventListener('DOMContentLoaded', function() {
   var activeTab = document.querySelector('.sb a.on');
   if (activeTab) { activeTab.scrollIntoView({ behavior: 'auto', block: 'nearest', inline: 'center' }); }
   var activePill = document.querySelector('.pills a.on');
   if (activePill) { activePill.scrollIntoView({ behavior: 'auto', block: 'nearest', inline: 'center' }); }
 });

    function sortTable(colIndex) {
      const tbody = document.querySelector('tbody');
      if (!tbody) return;
      
      const rows = Array.from(tbody.querySelectorAll('tr'));
      if (rows.length <= 1) return; 
      
      const totalRow = rows.shift(); 
      
      let dir = tbody.getAttribute('data-sort-dir') === 'asc' ? 'desc' : 'asc';
      tbody.setAttribute('data-sort-dir', dir);
      
      rows.sort((a, b) => {
        let valA = a.children[colIndex].textContent.trim();
        let valB = b.children[colIndex].textContent.trim();
        
        let numA = parseFloat(valA.replace(/,/g, ''));
        let numB = parseFloat(valB.replace(/,/g, ''));
        
        let isNumA = !isNaN(numA) && valA !== '';
        let isNumB = !isNaN(numB) && valB !== '';
        
        let cmp = 0;
        if (isNumA && isNumB) {
          cmp = numA - numB;
        } else {
          cmp = valA.localeCompare(valB, 'ar');
        }
        
        return dir === 'asc' ? cmp : -cmp;
      });
      
      tbody.innerHTML = '';
      tbody.appendChild(totalRow);
      rows.forEach(r => tbody.appendChild(r));
      
      // Update PDF and Excel export links
      let exps = document.querySelectorAll('.exp');
      let colName = document.querySelectorAll('thead th')[colIndex].textContent.replace(' ↕', '').trim();
      exps.forEach(a => {
        let url = new URL(a.href, window.location.origin);
        url.searchParams.set('sort_col', colName);
        url.searchParams.set('sort_dir', dir);
        a.href = url.pathname + url.search;
      });
    }
 </script>

    <script>
      document.addEventListener("DOMContentLoaded", function() {
        const typeSelect = document.querySelector('select[name="p_type"]');
        const valSelect = document.querySelector('select[name="p_val"]');
        if(typeSelect && valSelect) {
          const valWrapper = valSelect.parentElement; // Usually a div grouping label + select
          
          function updateOptions() {
            const val = typeSelect.value;
            valSelect.innerHTML = ''; // clear options
            valWrapper.style.display = 'block';
# MISSING LINE 2251

# MISSING LINE 2252

# MISSING LINE 2253

# MISSING LINE 2254

# MISSING LINE 2255

# MISSING LINE 2256

# MISSING LINE 2257

# MISSING LINE 2258

# MISSING LINE 2259

# MISSING LINE 2260

# MISSING LINE 2261

# MISSING LINE 2262

# MISSING LINE 2263

# MISSING LINE 2264

# MISSING LINE 2265

# MISSING LINE 2266

# MISSING LINE 2267

# MISSING LINE 2268

# MISSING LINE 2269

# MISSING LINE 2270

# MISSING LINE 2271

# MISSING LINE 2272

# MISSING LINE 2273

# MISSING LINE 2274

# MISSING LINE 2275

# MISSING LINE 2276

# MISSING LINE 2277

# MISSING LINE 2278

# MISSING LINE 2279

# MISSING LINE 2280

# MISSING LINE 2281

# MISSING LINE 2282

# MISSING LINE 2283

# MISSING LINE 2284


TARGETS_PAGE = """<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<title>تارقت المناديب</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
body { margin:0; padding:20px; font-family:'Cairo',sans-serif; background:#f4f5f8; color:#1e293b; }
.card { background:#fff; padding:20px; border-radius:12px; box-shadow:0 5px 15px rgba(0,0,0,0.05); }
.header { display:flex; justify-content:space-between; align-items:center; margin-bottom:20px; }
h2 { margin:0; color:#4f46e5; }
select { padding:10px; border-radius:8px; border:1px solid #cbd5e1; font-family:inherit; outline:none; }
button { padding:10px 20px; background:#4f46e5; color:#fff; border:none; border-radius:8px; font-weight:bold; cursor:pointer; font-family:inherit; }
button:hover { background:#4338ca; }
.btn-back { background:#64748b; margin-left:10px; text-decoration:none; display:inline-block; }
.btn-back:hover { background:#475569; }
table { width:100%; border-collapse:collapse; margin-top:20px; font-size:14px; }
th, td { border:1px solid #e2e8f0; padding:8px; text-align:center; }
th { background:#f8fafc; color:#475569; position:sticky; top:0; z-index:1; }
input[type=number] { width:80px; padding:6px; border:1px solid #cbd5e1; border-radius:6px; text-align:center; font-family:inherit; }
input[type=number]:focus { outline:none; border-color:#4f46e5; }
.total-cell { font-weight:bold; color:#4f46e5; background:#f8fafc; }
</style>
</head>
<body>
  <div class="card">
    <div class="header">
      <h2>تارقت المناديب</h2>
      <div>
        <select id="yearSelect">
          <option value="2024">2024</option>
          <option value="2025">2025</option>
          <option value="2026" selected>2026</option>
          <option value="2027">2027</option>
        </select>
        <button onclick="saveTargets()">حفظ التعديلات</button>
        <a href="/" class="btn-back button">عودة للرئيسية</a>
      </div>
    </div>
    
    <div style="overflow-x:auto; max-height:75vh;">
    <table>
      <thead>
        <tr>
          <th>كود</th>
          <th style="min-width:150px;">المندوب</th>
          <th>يناير</th><th>فبراير</th><th>مارس</th><th>أبريل</th><th>مايو</th><th>يونيو</th>
          <th>يوليو</th><th>أغسطس</th><th>سبتمبر</th><th>أكتوبر</th><th>نوفمبر</th><th>ديسمبر</th>
          <th>الإجمالي السنوي</th>
        </tr>
      </thead>
      <tbody id="tbody">
        <!-- populated by js -->
      </tbody>
    </table>
    </div>
  </div>

<script>
  const backendData = {{ data | tojson }};
  const salesmen = {{ salesmen | tojson }};
  const tbody = document.getElementById('tbody');
  const yearSelect = document.getElementById('yearSelect');
  
  function renderTable(year) {
    tbody.innerHTML = '';
    const yearData = backendData[year] || {};
    
    salesmen.forEach(sm => {
      const tr = document.createElement('tr');
      const codeTd = document.createElement('td'); codeTd.textContent = sm.code; tr.appendChild(codeTd);
      const nameTd = document.createElement('td'); nameTd.textContent = sm.name; tr.appendChild(nameTd);
      
      const smData = yearData[sm.code] || {};
      let smTotal = 0;
      
      const inputs = [];
      for(let m=1; m<=12; m++) {
        const td = document.createElement('td');
        const input = document.createElement('input');
        input.type = 'number';
        input.dataset.code = sm.code;
        input.dataset.month = m;
        let val = smData[m] || 0;
        if(val > 0) input.value = val;
        smTotal += val;
        
        input.addEventListener('input', updateRowTotal);
        inputs.push(input);
        
        td.appendChild(input);
        tr.appendChild(td);
      }
      
      const totalTd = document.createElement('td');
      totalTd.className = 'total-cell';
      totalTd.textContent = smTotal.toLocaleString();
      tr.appendChild(totalTd);
      
      tr.inputs = inputs;
      tr.totalTd = totalTd;
      tbody.appendChild(tr);
    });
  }
  
  function updateRowTotal(e) {
    const tr = e.target.closest('tr');
    let sum = 0;
    tr.inputs.forEach(inp => {
      const v = parseFloat(inp.value);
      if(!isNaN(v)) sum += v;
    });
    tr.totalTd.textContent = sum.toLocaleString();
  }
  
  yearSelect.addEventListener('change', () => renderTable(yearSelect.value));
  
  function saveTargets() {
# MISSING LINE 2401

# MISSING LINE 2402

# MISSING LINE 2403

# MISSING LINE 2404

# MISSING LINE 2405

# MISSING LINE 2406

# MISSING LINE 2407

# MISSING LINE 2408

# MISSING LINE 2409

# MISSING LINE 2410

# MISSING LINE 2411

# MISSING LINE 2412

# MISSING LINE 2413

# MISSING LINE 2414

# MISSING LINE 2415

# MISSING LINE 2416

# MISSING LINE 2417

# MISSING LINE 2418

# MISSING LINE 2419

# MISSING LINE 2420

# MISSING LINE 2421

# MISSING LINE 2422

# MISSING LINE 2423

# MISSING LINE 2424

# MISSING LINE 2425

# MISSING LINE 2426

# MISSING LINE 2427

# MISSING LINE 2428

# MISSING LINE 2429

# MISSING LINE 2430

# MISSING LINE 2431

# MISSING LINE 2432

# MISSING LINE 2433

# MISSING LINE 2434

# MISSING LINE 2435

# MISSING LINE 2436

# MISSING LINE 2437

# MISSING LINE 2438

# MISSING LINE 2439

# MISSING LINE 2440

# MISSING LINE 2441

# MISSING LINE 2442

# MISSING LINE 2443

# MISSING LINE 2444

# MISSING LINE 2445

# MISSING LINE 2446

# MISSING LINE 2447

# MISSING LINE 2448

# MISSING LINE 2449

# MISSING LINE 2450

# MISSING LINE 2451

# MISSING LINE 2452

# MISSING LINE 2453

# MISSING LINE 2454

# MISSING LINE 2455

# MISSING LINE 2456

# MISSING LINE 2457

# MISSING LINE 2458

# MISSING LINE 2459

# MISSING LINE 2460

# MISSING LINE 2461

# MISSING LINE 2462

# MISSING LINE 2463

# MISSING LINE 2464

# MISSING LINE 2465

# MISSING LINE 2466

# MISSING LINE 2467

# MISSING LINE 2468

# MISSING LINE 2469

# MISSING LINE 2470

# MISSING LINE 2471

# MISSING LINE 2472

# MISSING LINE 2473

# MISSING LINE 2474

# MISSING LINE 2475

# MISSING LINE 2476

# MISSING LINE 2477

# MISSING LINE 2478

# MISSING LINE 2479

# MISSING LINE 2480

# MISSING LINE 2481

# MISSING LINE 2482

# MISSING LINE 2483

# MISSING LINE 2484

# MISSING LINE 2485

# MISSING LINE 2486

# MISSING LINE 2487

# MISSING LINE 2488

# MISSING LINE 2489

# MISSING LINE 2490

# MISSING LINE 2491

# MISSING LINE 2492

# MISSING LINE 2493

# MISSING LINE 2494

# MISSING LINE 2495

# MISSING LINE 2496

# MISSING LINE 2497

# MISSING LINE 2498

# MISSING LINE 2499

# MISSING LINE 2500

# MISSING LINE 2501

# MISSING LINE 2502

# MISSING LINE 2503

# MISSING LINE 2504

# MISSING LINE 2505

# MISSING LINE 2506

# MISSING LINE 2507

# MISSING LINE 2508

# MISSING LINE 2509

# MISSING LINE 2510

# MISSING LINE 2511

# MISSING LINE 2512

# MISSING LINE 2513

# MISSING LINE 2514

# MISSING LINE 2515

# MISSING LINE 2516

# MISSING LINE 2517

# MISSING LINE 2518

# MISSING LINE 2519

# MISSING LINE 2520

# MISSING LINE 2521

# MISSING LINE 2522

# MISSING LINE 2523

# MISSING LINE 2524

# MISSING LINE 2525

# MISSING LINE 2526

# MISSING LINE 2527

# MISSING LINE 2528

# MISSING LINE 2529

# MISSING LINE 2530

# MISSING LINE 2531

# MISSING LINE 2532

# MISSING LINE 2533

# MISSING LINE 2534

# MISSING LINE 2535

# MISSING LINE 2536

# MISSING LINE 2537

# MISSING LINE 2538

# MISSING LINE 2539

# MISSING LINE 2540

# MISSING LINE 2541

# MISSING LINE 2542

# MISSING LINE 2543

# MISSING LINE 2544

# MISSING LINE 2545

# MISSING LINE 2546

# MISSING LINE 2547

# MISSING LINE 2548

# MISSING LINE 2549

# MISSING LINE 2550

# MISSING LINE 2551

# MISSING LINE 2552

# MISSING LINE 2553

# MISSING LINE 2554

# MISSING LINE 2555

# MISSING LINE 2556

# MISSING LINE 2557

# MISSING LINE 2558

# MISSING LINE 2559

# MISSING LINE 2560

# MISSING LINE 2561

# MISSING LINE 2562

# MISSING LINE 2563

# MISSING LINE 2564

# MISSING LINE 2565

# MISSING LINE 2566

# MISSING LINE 2567

# MISSING LINE 2568

# MISSING LINE 2569

# MISSING LINE 2570

# MISSING LINE 2571

# MISSING LINE 2572

# MISSING LINE 2573

# MISSING LINE 2574

# MISSING LINE 2575

# MISSING LINE 2576

# MISSING LINE 2577

# MISSING LINE 2578

# MISSING LINE 2579

# MISSING LINE 2580

# MISSING LINE 2581

# MISSING LINE 2582

# MISSING LINE 2583

# MISSING LINE 2584

# MISSING LINE 2585

# MISSING LINE 2586

# MISSING LINE 2587

# MISSING LINE 2588

# MISSING LINE 2589

# MISSING LINE 2590

# MISSING LINE 2591

# MISSING LINE 2592

# MISSING LINE 2593

# MISSING LINE 2594

# MISSING LINE 2595

# MISSING LINE 2596

# MISSING LINE 2597

# MISSING LINE 2598

# MISSING LINE 2599

# MISSING LINE 2600

# MISSING LINE 2601

# MISSING LINE 2602

# MISSING LINE 2603

# MISSING LINE 2604

# MISSING LINE 2605

# MISSING LINE 2606

# MISSING LINE 2607

# MISSING LINE 2608

# MISSING LINE 2609

# MISSING LINE 2610

# MISSING LINE 2611

# MISSING LINE 2612

# MISSING LINE 2613

# MISSING LINE 2614

# MISSING LINE 2615

# MISSING LINE 2616

# MISSING LINE 2617

# MISSING LINE 2618

# MISSING LINE 2619

# MISSING LINE 2620

# MISSING LINE 2621

# MISSING LINE 2622

# MISSING LINE 2623

# MISSING LINE 2624

# MISSING LINE 2625

# MISSING LINE 2626

# MISSING LINE 2627

# MISSING LINE 2628

# MISSING LINE 2629

# MISSING LINE 2630

# MISSING LINE 2631

# MISSING LINE 2632

# MISSING LINE 2633

# MISSING LINE 2634

# MISSING LINE 2635

# MISSING LINE 2636

# MISSING LINE 2637

# MISSING LINE 2638

# MISSING LINE 2639

# MISSING LINE 2640

# MISSING LINE 2641

# MISSING LINE 2642

# MISSING LINE 2643

# MISSING LINE 2644

# MISSING LINE 2645

# MISSING LINE 2646

# MISSING LINE 2647

# MISSING LINE 2648

# MISSING LINE 2649

# MISSING LINE 2650

# MISSING LINE 2651

# MISSING LINE 2652

# MISSING LINE 2653

# MISSING LINE 2654

# MISSING LINE 2655

# MISSING LINE 2656

# MISSING LINE 2657

# MISSING LINE 2658

# MISSING LINE 2659

# MISSING LINE 2660

# MISSING LINE 2661

# MISSING LINE 2662

# MISSING LINE 2663

# MISSING LINE 2664

# MISSING LINE 2665

# MISSING LINE 2666

# MISSING LINE 2667

# MISSING LINE 2668

# MISSING LINE 2669

# MISSING LINE 2670

# MISSING LINE 2671

# MISSING LINE 2672

# MISSING LINE 2673

# MISSING LINE 2674

# MISSING LINE 2675

# MISSING LINE 2676

# MISSING LINE 2677

# MISSING LINE 2678

# MISSING LINE 2679

# MISSING LINE 2680

# MISSING LINE 2681

# MISSING LINE 2682

# MISSING LINE 2683

# MISSING LINE 2684

# MISSING LINE 2685

# MISSING LINE 2686

# MISSING LINE 2687

# MISSING LINE 2688

# MISSING LINE 2689

# MISSING LINE 2690

# MISSING LINE 2691

# MISSING LINE 2692

# MISSING LINE 2693

# MISSING LINE 2694

# MISSING LINE 2695

# MISSING LINE 2696

# MISSING LINE 2697

# MISSING LINE 2698

# MISSING LINE 2699

# MISSING LINE 2700

# MISSING LINE 2701

# MISSING LINE 2702

# MISSING LINE 2703

# MISSING LINE 2704

# MISSING LINE 2705

# MISSING LINE 2706

# MISSING LINE 2707

# MISSING LINE 2708

# MISSING LINE 2709

# MISSING LINE 2710

# MISSING LINE 2711

# MISSING LINE 2712

# MISSING LINE 2713

# MISSING LINE 2714

# MISSING LINE 2715

# MISSING LINE 2716

# MISSING LINE 2717

# MISSING LINE 2718

# MISSING LINE 2719

# MISSING LINE 2720

# MISSING LINE 2721

DASHBOARD_PAGE = '''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>لوحة القيادة SREEN</title>
     <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
     <script>
     var D={{ dash|tojson }};
     window.addEventListener("load",function(){ 
       if(!window.Chart) return; 
       Chart.defaults.font.family = "'Cairo', 'Inter', sans-serif";
       Chart.defaults.color = "#64748b";
       
       const commonOptions = {
         responsive: true,
         maintainAspectRatio: false,
         plugins: {
           legend: { display: false },
           tooltip: { backgroundColor: '#1e293b', padding: 14, titleFont: { size: 14, family: "'Cairo', sans-serif", weight: 'bold' }, bodyFont: { size: 14, family: "'Cairo', sans-serif" }, cornerRadius: 10, displayColors: true, boxPadding: 6 }
         }
       };
       
       // C1: Bar Chart (Sales & Collection)
       new Chart(document.getElementById("c1"),{
         type:"bar",
         data:{
           labels:D.months,
           datasets:[
             {label:"مبيعات", data:D.msales, backgroundColor:"#4f46e5", borderRadius:8, maxBarThickness: 32},
             {label:"تحصيل", data:D.mcollect, backgroundColor:"#38bdf8", borderRadius:8, maxBarThickness: 32}
           ]
         },
         options: {
           ...commonOptions,
           plugins: { ...commonOptions.plugins, legend: { display: true, position: 'top', align: 'end', labels: { usePointStyle: true, boxWidth: 10, font: { family: "'Cairo'", size: 13, weight: 'bold' } } } },
           scales: {
             x: { grid: { display: false }, border: { display: false } },
             y: { grid: { color: '#f1f5f9', borderDash: [6, 4] }, border: { display: false } }
           }
         }
       });

       // C2: Doughnut (Salesmen)
       new Chart(document.getElementById("c2"),{
         type:"doughnut",
         data:{
           labels:D.rep_labels.slice(0,5),
           datasets:[{data:D.rep_vals.slice(0,5), backgroundColor:["#4f46e5", "#38bdf8", "#10b981", "#f59e0b", "#8b5cf6"], borderWidth: 0, hoverOffset: 4}]
         },
         options: {
           responsive: true, maintainAspectRatio: false, cutout: '75%',
           plugins: { legend: { display: true, position: 'bottom', labels: { usePointStyle: true, boxWidth: 8, font: { size: 11 } } } }
         }
       });

       // C3: Doughnut (Items)
       new Chart(document.getElementById("c3"),{
         type:"doughnut",
         data:{
           labels:D.itm_labels.slice(0,5),
           datasets:[{data:D.itm_vals.slice(0,5), backgroundColor:["#f43f5e", "#d946ef", "#0ea5e9", "#14b8a6", "#eab308"], borderWidth: 0, hoverOffset: 4}]
         },
         options: {
           responsive: true, maintainAspectRatio: false, cutout: '75%',
           plugins: { legend: { display: true, position: 'bottom', labels: { usePointStyle: true, boxWidth: 8, font: { size: 11 } } } }
         }
       });

       // C4: Line Chart (Purchases)
       const ctx4 = document.getElementById("c4").getContext('2d');
       const grad4 = ctx4.createLinearGradient(0, 0, 0, 300);
       grad4.addColorStop(0, 'rgba(16, 185, 129, 0.4)');
       grad4.addColorStop(1, 'rgba(16, 185, 129, 0.0)');
       
       new Chart(ctx4,{
         type:"line",
         data:{
           labels:D.months,
           datasets:[{
             label: "مشتريات", data:D.mpurch, borderColor:"#10b981", borderWidth: 3, backgroundColor: grad4, fill:true, tension:0.4, pointRadius: 0, pointHoverRadius: 6, pointBackgroundColor: "#fff", pointBorderColor: "#10b981", pointBorderWidth: 2
           }]
         },
         options: {
           ...commonOptions,
           interaction: { mode: 'index', intersect: false },
           scales: {
             x: { grid: { display: false }, border: { display: false } },
             y: { grid: { color: '#f1f5f9', borderDash: [6, 4] }, border: { display: false } }
           }
         }
       });
     });
     </script>
<style>
 *{box-sizing:border-box;font-family:Tahoma,Arial}
 body{margin:0;background:#f1f5f9;color:#0f172a}
 .hd{background:linear-gradient(90deg,#0f766e,#134e4a);color:#fff;padding:14px 24px;display:flex;align-items:center;gap:14px;flex-wrap:wrap}
 .hd h1{margin:0;font-size:19px} .hd .sp{flex:1}
 .hd a{color:#fff;text-decoration:none;background:rgba(255,255,255,.15);padding:8px 14px;border-radius:8px;font-size:14px}
 .hd form{display:flex;gap:8px;align-items:center;font-size:13px}
 .hd input{padding:7px;border:0;border-radius:6px} .hd button{padding:8px 14px;border:0;border-radius:6px;background:#fbbf24;font-weight:700;cursor:pointer}
 .wrap{padding:22px;max-width:1300px;margin:auto}
 .kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:22px}
 @media(max-width:900px){.kpis{grid-template-columns:repeat(2,1fr)}}
 .kpi{background:#fff;border-radius:14px;padding:16px;box-shadow:0 1px 3px rgba(0,0,0,.08);border-right:4px solid #0f766e}
 .kpi .l{color:#64748b;font-size:13px;margin-bottom:6px} .kpi .v{font-size:21px;font-weight:800}
 .kpi.g{border-color:#16a34a}.kpi.b{border-color:#2563eb}.kpi.o{border-color:#ea580c}.kpi.r{border-color:#dc2626}.kpi.p{border-color:#7c3aed}
 .charts{display:grid;grid-template-columns:1fr 1fr;gap:14px}
 @media(max-width:900px){.charts{grid-template-columns:1fr}}
 .ch{background:#fff;border-radius:14px;padding:16px;box-shadow:0 1px 3px rgba(0,0,0,.08)}
 .ch h3{margin:0 0 12px;font-size:15px}
</style></head><body>
 <div class="hd"><h1>📊 لوحة القيادة — SREEN</h1>
   <form method="get" action="/dashboard"><span>من</span><input type="date" name="date_from" value="{{f}}"><span>إلى</span><input type="date" name="date_to" value="{{t}}"><button type="submit">تحديث</button></form>
   <div class="sp"></div><a href="/">← التقارير</a></div>
 <div class="wrap">
   <div class="kpis">
     <div class="kpi b"><div class="l">إجمالي المبيعات</div><div class="v">{{ "{:,.0f}".format(data.sales) }}</div></div>
     <div class="kpi g"><div class="l">إجمالي التحصيل</div><div class="v">{{ "{:,.0f}".format(data.collect) }}</div></div>
     <div class="kpi o"><div class="l">إجمالي المشتريات</div><div class="v">{{ "{:,.0f}".format(data.purch) }}</div></div>
     {% if not hide_profit|default(false) %}<div class="kpi p"><div class="l">مجمل الربح</div><div class="v">{{ "{:,.0f}".format(data.gross) }}</div></div>
     <div class="kpi g"><div class="l">صافي الربح</div><div class="v">{{ "{:,.0f}".format(data.netprofit) }}</div></div>{% endif %}
     <div class="kpi r"><div class="l">الذمم المدينة</div><div class="v">{{ "{:,.0f}".format(data.recv) }}</div></div>
     <div class="kpi b"><div class="l">قيمة المخزون</div><div class="v">{{ "{:,.0f}".format(data.invval) }}</div></div>
     <div class="kpi o"><div class="l">صافي الضريبة</div><div class="v">{{ "{:,.0f}".format(data.vat) }}</div></div>
   </div>
   <div class="charts">
     <div class="ch"><h3>المبيعات والتحصيل شهرياً</h3><canvas id="c1" height="140"></canvas></div>
     <div class="ch"><h3>أفضل المناديب (مبيعات)</h3><canvas id="c2" height="140"></canvas></div>
     <div class="ch"><h3>أفضل الأصناف (مبيعات)</h3><canvas id="c3" height="140"></canvas></div>
     <div class="ch"><h3>المشتريات شهرياً</h3><canvas id="c4" height="140"></canvas></div>
   </div></div>
<script>
const D={{ data|tojson }};
Chart.defaults.font.family="Tahoma";
new Chart(c1,{type:"bar",data:{labels:D.months,datasets:[{label:"مبيعات",data:D.msales,backgroundColor:"#2563eb"},{label:"تحصيل",data:D.mcollect,backgroundColor:"#16a34a"}]}});
new Chart(c2,{type:"bar",data:{labels:D.rep_labels,datasets:[{label:"مبيعات",data:D.rep_vals,backgroundColor:"#0f766e"}]},options:{indexAxis:"y",plugins:{legend:{display:false}}}});
new Chart(c3,{type:"bar",data:{labels:D.itm_labels,datasets:[{label:"مبيعات",data:D.itm_vals,backgroundColor:"#ea580c"}]},options:{indexAxis:"y",plugins:{legend:{display:false}}}});
new Chart(c4,{type:"line",data:{labels:D.months,datasets:[{label:"مشتريات",data:D.mpurch,borderColor:"#ea580c",backgroundColor:"rgba(234,88,12,.12)",fill:true,tension:.3}]},options:{plugins:{legend:{display:false}}}});
</script></body></html>'''

def compute_dash(f, t):
    b = {"f": f, "t": t}
    P="TO_DATE(:f,\'YYYY-MM-DD\')"; Q="TO_DATE(:t,\'YYYY-MM-DD\')+1"
    d = {"sales":0,"collect":0,"purch":0,"gross":0,"netprofit":0,"recv":0,"invval":0,"vat":0,
         "months":[],"msales":[],"mcollect":[],"mpurch":[],"rep_labels":[],"rep_vals":[],"itm_labels":[],"itm_vals":[]}
    try:
        with get_conn() as con:
            cur = con.cursor()
            def sc(sql):
                try:
                    cur.execute(sql,{k:v for k,v in b.items() if (":"+k) in sql}); r=cur.fetchone()
                    return round(float(r[0]),2) if r and r[0] is not None else 0.0
                except Exception: return 0.0
            def rw(sql):
                try:
                    cur.execute(sql,{k:v for k,v in b.items() if (":"+k) in sql}); return cur.fetchall()
                except Exception: return []
            d["sales"]=sc("SELECT NVL(SUM(NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)),0) FROM IAS20261.IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND BILL_DATE>="+P+" AND BILL_DATE<"+Q)
            d["collect"]=sc("SELECT NVL(SUM(NVL(CR_AMT,0)),0) FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND C_CODE IS NOT NULL AND DOC_DATE>="+P+" AND DOC_DATE<"+Q)
            d["purch"]=sc("SELECT NVL(SUM(NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)),0) FROM IAS20261.IAS_PI_BILL_MST WHERE BILL_DATE>="+P+" AND BILL_DATE<"+Q)
            d["gross"]=sc("SELECT NVL(SUM(NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))-NVL(x.I_QTY,0)*NVL(x.STK_COST,0)),0) FROM IAS20261.IAS_BILL_DTL x JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=x.BILL_DOC_TYPE AND m.BILL_NO=x.BILL_NO AND m.BILL_SER=x.BILL_SER WHERE m.BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.BILL_DATE>="+P+" AND m.BILL_DATE<"+Q)
            d["netprofit"]=sc("SELECT NVL(SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)),0) FROM IAS20261.IAS_POST_DTL p JOIN IAS20261.ACCOUNT a ON a.A_CODE=p.A_CODE WHERE NVL(p.DOC_POST,0)=1 AND a.A_REPORT=2 AND p.DOC_DATE>="+P+" AND p.DOC_DATE<"+Q)
            d["recv"]=sc("SELECT NVL(SUM(bal),0) FROM (SELECT SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0)) bal FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND C_CODE IS NOT NULL AND DOC_DATE<"+Q+" GROUP BY C_CODE HAVING SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0))>0)")
            d["invval"]=sc("SELECT NVL(SUM(NVL(I_QTY,0)*NVL(IN_OUT,0)*NVL(STK_COST,0)),0) FROM IAS20261.ITEM_MOVEMENT WHERE I_DATE<"+Q)
            ov=sc("SELECT NVL(SUM(NVL(VAT_AMT,0)),0) FROM IAS20261.IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND BILL_DATE>="+P+" AND BILL_DATE<"+Q)
            iv=sc("SELECT NVL(SUM(NVL(VAT_AMT,0)),0) FROM IAS20261.IAS_PI_BILL_MST WHERE BILL_DATE>="+P+" AND BILL_DATE<"+Q)
            d["vat"]=round(ov-iv,2)
            def mm(sql):
                m={}
                for r in rw(sql):
                    m[str(r[0])]=round(float(r[1] or 0),2)
                return m
            ms=mm("SELECT TO_CHAR(BILL_DATE,\'YYYY-MM\'), SUM(NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) FROM IAS20261.IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND BILL_DATE>="+P+" AND BILL_DATE<"+Q+" GROUP BY TO_CHAR(BILL_DATE,\'YYYY-MM\')")
            mc=mm("SELECT TO_CHAR(DOC_DATE,\'YYYY-MM\'), SUM(NVL(CR_AMT,0)) FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND C_CODE IS NOT NULL AND DOC_DATE>="+P+" AND DOC_DATE<"+Q+" GROUP BY TO_CHAR(DOC_DATE,\'YYYY-MM\')")
            mp=mm("SELECT TO_CHAR(BILL_DATE,\'YYYY-MM\'), SUM(NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) FROM IAS20261.IAS_PI_BILL_MST WHERE BILL_DATE>="+P+" AND BILL_DATE<"+Q+" GROUP BY TO_CHAR(BILL_DATE,\'YYYY-MM\')")
            months=sorted(set(list(ms)+list(mc)+list(mp)))
            d["months"]=months
            d["msales"]=[ms.get(x,0) for x in months]
            d["mcollect"]=[mc.get(x,0) for x in months]
            d["mpurch"]=[mp.get(x,0) for x in months]
            for r in rw("SELECT NVL(sm.REPRS_A_NAME, m.REP_CODE) nm, SUM(NVL(m.BILL_AMT,0)-(NVL(m.DISC_AMT,0)-NVL(m.ADD_DISC_AMT_MST,0))+NVL(m.VAT_AMT,0)+NVL(m.OTHR_AMT,0)) v FROM IAS20261.IAS_BILL_MST m LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=m.REP_CODE WHERE m.BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.BILL_DATE>="+P+" AND m.BILL_DATE<"+Q+" GROUP BY NVL(sm.REPRS_A_NAME,m.REP_CODE) ORDER BY v DESC FETCH FIRST 7 ROWS ONLY"):
                d["rep_labels"].append(str(r[0])); d["rep_vals"].append(round(float(r[1] or 0),2))
            for r in rw("SELECT NVL(i.I_NAME, x.I_CODE) nm, SUM(NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))) v FROM IAS20261.IAS_BILL_DTL x JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=x.BILL_DOC_TYPE AND m.BILL_NO=x.BILL_NO AND m.BILL_SER=x.BILL_SER LEFT JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE=x.I_CODE WHERE m.BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.BILL_DATE>="+P+" AND m.BILL_DATE<"+Q+" GROUP BY NVL(i.I_NAME,x.I_CODE) ORDER BY v DESC FETCH FIRST 7 ROWS ONLY"):
                d["itm_labels"].append(str(r[0])[:22]); d["itm_vals"].append(round(float(r[1] or 0),2))
    except Exception as e:
        d["err"]=str(e)
    return d


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
