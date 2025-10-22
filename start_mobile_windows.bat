@echo off
echo Starting Moodscape Mobile App...

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo Node.js is not installed or not in PATH
    echo Please install Node.js from https://nodejs.org
    pause
    exit /b 1
)

REM Check if Expo CLI is installed
expo --version >nul 2>&1
if errorlevel 1 (
    echo Installing Expo CLI...
    npm install -g @expo/cli
)

REM Navigate to mobile app directory
cd /d "%~dp0MoodscapeApp"

REM Install dependencies
echo Installing dependencies...
npm install

REM Start the development server
echo Starting Expo development server...
echo Mobile app will be available at: http://localhost:8081
echo Scan the QR code with Expo Go app on your device
expo start

pause
