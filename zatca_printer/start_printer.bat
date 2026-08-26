@echo off
title ZATCA Invoice Printer Server

echo ==============================================
echo   Starting ZATCA Printer Server (Production)
echo ==============================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH!
    pause
    exit /b
)

:: Rename .env.production to .env if .env doesn't exist
if not exist .env (
    if exist .env.production (
        echo [INFO] Copying .env.production to .env
        copy .env.production .env >nul
    ) else (
        echo [WARNING] No .env or .env.production found!
    )
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
echo [INFO] Starting Waitress server...
python server.py

pause
