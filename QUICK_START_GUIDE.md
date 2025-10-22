# Moodscape - Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Start the Backend
```bash
# Navigate to backend directory
cd backend

# Activate virtual environment
source venv/bin/activate  # Linux/macOS
# OR
venv\Scripts\activate     # Windows

# Start the server
python3 app/simple_main.py
```

### Step 2: Start the Mobile App
```bash
# Navigate to mobile app directory
cd MoodscapeApp

# Install dependencies (if not done already)
npm install

# Start the Expo development server
npm start
```

### Step 3: Access the App
- **Mobile**: Open Expo Go app and scan the QR code
- **Web**: Open http://localhost:19006 in your browser
- **API Docs**: Visit http://localhost:8000/docs

## 🎯 Quick Test

### Test Preview Mode
1. Open the app
2. Tap "Try Preview Mode"
3. Enter your name
4. Log a mood entry
5. Try AI analysis

### Test Full Features
1. Register a new account
2. Verify your email
3. Login with your credentials
4. Explore all features

### Test Admin Panel
1. Login with:
   - Username: `makopolo`
   - Password: `123456`
2. Access admin features
3. Monitor system status

## ✅ Verification Checklist

- [ ] Backend server running (port 8000)
- [ ] Mobile app accessible
- [ ] Preview mode working
- [ ] User registration working
- [ ] Admin panel accessible
- [ ] AI features responding
- [ ] No console errors

## 🔧 Troubleshooting

### If Backend Won't Start
```bash
# Check Python version
python3 --version

# Install missing dependencies
pip install -r requirements.txt

# Check port availability
netstat -tulpn | grep :8000
```

### If Mobile App Won't Start
```bash
# Clear npm cache
npm cache clean --force

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install

# Reset Expo cache
expo r -c
```

### If Dependencies Mismatch
```bash
# Fix React Native SVG version
npm install react-native-svg@15.12.1

# Update all packages
npm update
```

## 📱 Platform-Specific Instructions

### Windows
```cmd
# Backend
cd backend
venv\Scripts\activate
python app\simple_main.py

# Mobile App
cd MoodscapeApp
npm start
```

### macOS
```bash
# Backend
cd backend
source venv/bin/activate
python3 app/simple_main.py

# Mobile App
cd MoodscapeApp
npm start
```

### Linux
```bash
# Backend
cd backend
source venv/bin/activate
python3 app/simple_main.py

# Mobile App
cd MoodscapeApp
npm start
```

## 🎉 You're Ready!

Once both services are running:
- **Backend**: http://localhost:8000
- **Mobile App**: http://localhost:19006
- **API Health**: http://localhost:8000/health

For detailed instructions, see the [User Manual](USER_MANUAL.md).

---
*Need help? Check the troubleshooting section in the User Manual.*
