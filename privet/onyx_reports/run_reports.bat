@echo off
title Sreen Reports Server (Production)

cd /d "%~dp0"

echo ==============================================
echo   Starting Sreen Reports Server
echo ==============================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH!
    pause
    exit /b
)

:: Create virtual environment if it doesn't exist
if not exist venv (
    echo [INFO] Creating virtual environment...
    python -m venv venv
)

:: Activate virtual environment
call venv\Scripts\activate

:: Install requirements
echo [INFO] Checking dependencies...
pip install -r requirements.txt >nul

:: Start the server
echo [INFO] Starting Waitress server on port 8000...
python -c "from waitress import serve; import app; serve(app.app, host='0.0.0.0', port=8000)"

pause
