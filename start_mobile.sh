#!/bin/bash

# Moodscape Mobile App Startup Script

echo "📱 Starting Moodscape Mobile App"
echo "==============================="

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 16 or higher."
    exit 1
fi

# Check if Expo CLI is installed
if ! command -v expo &> /dev/null; then
    echo "📦 Installing Expo CLI..."
    npm install -g @expo/cli
fi

# Navigate to mobile app directory
cd MoodscapeApp

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📥 Installing dependencies..."
    npm install
fi

# Start the development server
echo "🌟 Starting Expo development server..."
echo "App will be available in Expo Go app on your phone"
echo "Or scan the QR code with Expo Go"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

npm start
