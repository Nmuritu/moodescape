# Moodscape - Cross-Platform Setup Guide

## 🌍 Supported Operating Systems

- **Windows** (10/11)
- **macOS** (10.15+)
- **Linux** (Ubuntu 18.04+, Debian 10+, CentOS 7+)

## 🚀 Quick Start (Any OS)

### Option 1: Automated Testing
Run the comprehensive cross-platform test suite:

```bash
python3 test_cross_platform.py
```

This will:
- ✅ Detect your operating system
- ✅ Check all dependencies
- ✅ Test backend and mobile setup
- ✅ Verify preview mode functionality
- ✅ Generate a detailed report

### Option 2: OS-Specific Setup

#### Windows Setup

**Backend:**
```cmd
# Double-click or run in Command Prompt
start_backend_windows.bat
```

**Mobile App:**
```cmd
# Double-click or run in Command Prompt
start_mobile_windows.bat
```

#### macOS Setup

**Backend:**
```bash
./start_backend_macos.sh
```

**Mobile App:**
```bash
./start_mobile_macos.sh
```

#### Linux Setup

**Backend:**
```bash
./start_backend.sh
```

**Mobile App:**
```bash
./start_mobile.sh
```

## 📋 Prerequisites

### All Operating Systems

1. **Python 3.8+**
   - Windows: Download from [python.org](https://python.org)
   - macOS: `brew install python3` or download from [python.org](https://python.org)
   - Linux: `sudo apt install python3 python3-pip` (Ubuntu/Debian)

2. **Node.js 16+**
   - Windows: Download from [nodejs.org](https://nodejs.org)
   - macOS: `brew install node` or download from [nodejs.org](https://nodejs.org)
   - Linux: `sudo apt install nodejs npm` (Ubuntu/Debian)

3. **Git** (for cloning the repository)
   - Windows: Download from [git-scm.com](https://git-scm.com)
   - macOS: `brew install git`
   - Linux: `sudo apt install git`

## 🔧 Manual Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd moodscape
```

### 2. Backend Setup

#### Windows
```cmd
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -c "from models.database import init_database; init_database()"
python app/main.py
```

#### macOS/Linux
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 -c "from models.database import init_database; init_database()"
python3 app/main.py
```

### 3. Mobile App Setup

#### All Operating Systems
```bash
cd MoodscapeApp
npm install
npx expo start
```

## 🧪 Testing the Application

### 1. Backend API Testing

The backend provides comprehensive REST APIs:

#### Preview Mode (No Account Required)
- `POST /api/preview/session` - Create preview session
- `POST /api/preview/mood-entries` - Create mood entry
- `GET /api/preview/mood-entries` - Get mood entries
- `POST /api/preview/analyze-mood` - AI mood analysis
- `GET /api/preview/insights` - Get insights

#### Full Mode (Account Required)
- `POST /api/auth/register` - Register user
- `POST /api/auth/login` - Login user
- `POST /api/mood-entries` - Create mood entry
- `POST /api/ai/predict-mood` - AI mood prediction
- `POST /api/therapy/analyze-emotion` - Therapeutic AI

### 2. Test API Endpoints

#### Test Preview Mode
```bash
# Create preview session
curl -X POST "http://localhost:8000/api/preview/session"

# Create mood entry (replace SESSION_ID)
curl -X POST "http://localhost:8000/api/preview/mood-entries" \
  -d "session_id=SESSION_ID&mood=8&energy=7&stress=3&sleep_hours=8.5&notes=Feeling great!"

# Analyze mood
curl -X POST "http://localhost:8000/api/preview/analyze-mood" \
  -H "Content-Type: application/json" \
  -d '{"session_id": "SESSION_ID", "text": "I am feeling happy today!"}'
```

#### Test Full Mode
```bash
# Register user
curl -X POST "http://localhost:8000/api/auth/register" \
  -d "email=test@example.com&password=TestPassword123&name=Test User"

# Login user
curl -X POST "http://localhost:8000/api/auth/login" \
  -d "email=test@example.com&password=TestPassword123"

# Create mood entry (replace ACCESS_TOKEN)
curl -X POST "http://localhost:8000/api/mood-entries" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ACCESS_TOKEN" \
  -d '{"mood": 8, "energy": 7, "stress": 3, "sleep_hours": 8.5, "notes": "Feeling great!", "activities": ["exercise", "socializing"]}'
```

### 3. Mobile App Testing

#### Start the Mobile App
```bash
cd MoodscapeApp
npm start
```

#### Test on Device
1. Install Expo Go app on your device
2. Scan the QR code from the terminal
3. Test the following features:
   - **Preview Mode**: Try without creating an account
   - **User Registration**: Create a new account
   - **Mood Tracking**: Log your mood
   - **AI Analysis**: Get AI-powered insights
   - **Therapeutic AI**: Get therapeutic responses

## 🔍 Preview Mode Features

### What Users Can Try (Without Account)
- ✅ Track up to 3 mood entries
- ✅ Get 5 AI mood analyses
- ✅ View 2 basic insights
- ✅ Basic mood tracking and analysis
- ✅ 24-hour session duration

### What Requires Full Account
- ❌ Advanced therapeutic AI
- ❌ Unlimited mood tracking
- ❌ Data export and cloud sync
- ❌ Advanced analytics
- ❌ Personalized recommendations
- ❌ Progress tracking over time

## 🐛 Troubleshooting

### Common Issues

#### 1. Python Not Found
**Windows:**
- Add Python to PATH during installation
- Or use `py` instead of `python`

**macOS:**
- Install Python via Homebrew: `brew install python3`
- Or download from [python.org](https://python.org)

**Linux:**
- Install Python: `sudo apt install python3 python3-pip`
- Or use `python3` instead of `python`

#### 2. Node.js Not Found
**All OS:**
- Download from [nodejs.org](https://nodejs.org)
- Or use package manager (brew, apt, etc.)

#### 3. Expo CLI Not Found
```bash
npm install -g @expo/cli
```

#### 4. Port Already in Use
**Backend (Port 8000):**
```bash
# Kill process using port 8000
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:8000 | xargs kill -9
```

**Mobile App (Port 8081):**
```bash
# Kill process using port 8081
# Windows
netstat -ano | findstr :8081
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:8081 | xargs kill -9
```

#### 5. Database Issues
```bash
cd backend
python3 -c "from models.database import init_database; init_database()"
```

#### 6. Permission Issues (Linux/macOS)
```bash
chmod +x *.sh
```

## 📊 Performance Testing

### Load Testing
```bash
# Install Apache Bench
# Ubuntu/Debian
sudo apt install apache2-utils

# macOS
brew install httpd

# Test API performance
ab -n 100 -c 10 http://localhost:8000/health
```

### Memory Usage
```bash
# Monitor backend memory usage
# Windows
tasklist | findstr python

# macOS/Linux
ps aux | grep python
```

## 🔒 Security Testing

### Test Authentication
1. Try accessing protected endpoints without token
2. Test with invalid/expired tokens
3. Verify password strength requirements
4. Test rate limiting

### Test Input Validation
1. Try SQL injection attacks
2. Test XSS prevention
3. Verify input sanitization

## 📱 Mobile App Features Testing

### Core Features
- [ ] Preview mode (no account required)
- [ ] User registration and login
- [ ] Mood entry creation and editing
- [ ] AI mood prediction
- [ ] Sentiment analysis
- [ ] Therapeutic AI responses
- [ ] Insights and analytics
- [ ] Profile management
- [ ] Data export

### UI/UX Testing
- [ ] Navigation between screens
- [ ] Form validation
- [ ] Loading states
- [ ] Error handling
- [ ] Responsive design
- [ ] Accessibility features
- [ ] Cross-platform compatibility

## 🚀 Deployment Testing

### Backend Deployment
1. Test with production database
2. Verify environment variables
3. Test SSL/TLS configuration
4. Check CORS settings

### Mobile App Deployment
1. Test production build
2. Verify app signing
3. Test on different devices
4. Check app store requirements

## 📈 Monitoring and Logging

### Backend Logs
```bash
# View backend logs
# Windows
type backend\logs\app.log

# macOS/Linux
tail -f backend/logs/app.log
```

### Mobile App Logs
```bash
# View React Native logs
npx react-native log-android

# View Expo logs
expo logs
```

## 🎯 Success Criteria

The application is considered successfully set up when:

1. ✅ Backend server starts without errors
2. ✅ All API endpoints respond correctly
3. ✅ Mobile app compiles and runs
4. ✅ Preview mode works without account
5. ✅ User can register and login
6. ✅ Mood entries can be created and retrieved
7. ✅ AI features work correctly
8. ✅ Therapeutic AI provides appropriate responses
9. ✅ Data persists between sessions
10. ✅ Frontend-backend communication is seamless
11. ✅ App works on the target operating system
12. ✅ All tests pass in the automated test suite

## 📞 Support

If you encounter issues:

1. Check the test report generated by `test_cross_platform.py`
2. Review the logs for error messages
3. Verify all dependencies are installed
4. Ensure ports 8000 (backend) and 8081 (mobile) are available
5. Check the troubleshooting section above

## 🎉 Next Steps

Once everything is working:

1. **Customize the app**: Modify colors, themes, and features
2. **Add more AI models**: Implement additional therapeutic approaches
3. **Deploy to production**: Set up cloud hosting and app stores
4. **Add more features**: Implement notifications, social features, etc.
5. **Gather user feedback**: Use analytics to improve the app

---

**Happy coding! 🌙✨**

## 📋 Quick Reference

### Windows Commands
```cmd
start_backend_windows.bat
start_mobile_windows.bat
python test_cross_platform.py
```

### macOS Commands
```bash
./start_backend_macos.sh
./start_mobile_macos.sh
python3 test_cross_platform.py
```

### Linux Commands
```bash
./start_backend.sh
./start_mobile.sh
python3 test_cross_platform.py
```
