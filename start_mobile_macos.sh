#!/bin/bash

echo "🍎 Starting Moodscape Mobile App on macOS..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed"
    echo "Please install Node.js from https://nodejs.org or using Homebrew: brew install node"
    exit 1
fi

# Check if Expo CLI is installed
if ! command -v expo &> /dev/null; then
    echo "📦 Installing Expo CLI..."
    npm install -g @expo/cli
fi

# Navigate to mobile app directory
cd "$(dirname "$0")/MoodscapeApp"

# Install dependencies
echo "📥 Installing dependencies..."
npm install

# Start the development server
echo "🚀 Starting Expo development server..."
echo "Mobile app will be available at: http://localhost:8081"
echo "Scan the QR code with Expo Go app on your device"
expo start
