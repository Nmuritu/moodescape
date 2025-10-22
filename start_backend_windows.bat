@echo off
echo Starting Moodscape Backend Server...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

REM Navigate to backend directory
cd /d "%~dp0backend"

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Initialize database
echo Initializing database...
python -c "from models.database import init_database; init_database()"

REM Start the server
echo Starting FastAPI server...
echo Backend will be available at: http://localhost:8000
echo Press Ctrl+C to stop the server
python app/main.py

pause
