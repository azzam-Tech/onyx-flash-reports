@echo off
set ORA_LIB_DIR=C:\oracle64\instantclient_19_23
set TNS_ADMIN=C:\oracle64\instantclient_19_23
set ORA_USER=RPT_USER
set ORA_PASSWORD=ULT2016
set ORA_DSN=192.168.1.10:1521/orcl
cd /d "%~dp0"
py -c "from waitress import serve; import app; serve(app.app, host='0.0.0.0', port=8000)"
