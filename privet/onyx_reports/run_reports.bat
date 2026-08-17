@echo off
cd /d "%~dp0"
..\..\.venv\Scripts\python.exe -c "from waitress import serve; import app; serve(app.app, host='0.0.0.0', port=8000)"
pause
