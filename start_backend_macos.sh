#!/bin/bash

echo "🍎 Starting Moodscape Backend Server on macOS..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    echo "Please install Python 3.8+ using Homebrew: brew install python3"
    exit 1
fi

# Navigate to backend directory
cd "$(dirname "$0")/backend"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Initialize database
echo "🗄️ Initializing database..."
python3 -c "from models.database import init_database; init_database()"

# Start the server
echo "🚀 Starting FastAPI server..."
echo "Backend will be available at: http://localhost:8000"
echo "Press Ctrl+C to stop the server"
python3 app/main.py
