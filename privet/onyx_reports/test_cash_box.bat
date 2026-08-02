@echo off
set ORA_LIB_DIR=C:\oracle64\instantclient_19_23
set TNS_ADMIN=C:\oracle64\instantclient_19_23
set PATH=%ORA_LIB_DIR%;%PATH%
py privet\onyx_reports\test_cash_box.py
