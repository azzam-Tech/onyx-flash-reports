@echo off
set ORA_LIB_DIR=C:\oracle64\instantclient_19_23
set TNS_ADMIN=C:\oracle64\instantclient_19_23
set ORA_USER=ULT
set ORA_PASSWORD=ULT2017
cd /d "%~dp0"
..\..\.venv\Scripts\python.exe -c "from waitress import serve; import app; serve(app.app, host='0.0.0.0', port=8000)"

pause