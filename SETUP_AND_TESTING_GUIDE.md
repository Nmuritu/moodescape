# Moodscape - Complete Setup and Testing Guide

## 🚀 Quick Start

### Option 1: Automated Testing (Recommended)
Run the comprehensive test suite that will set up everything and verify functionality:

```bash
cd /home/ghost/Programming/moodscape
python3 test_complete_app.py
```

This will:
- ✅ Check all dependencies
- ✅ Install backend and frontend dependencies
- ✅ Start the backend server
- ✅ Test all API endpoints
- ✅ Verify mobile app structure
- ✅ Generate a detailed test report

### Option 2: Manual Setup

#### 1. Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 -c "from models.database import init_database; init_database()"
python3 app/main.py
```

#### 2. Mobile App Setup
```bash
cd MoodscapeApp
npm install
npm start
```

## 🧪 Testing the Application

### 1. Backend API Testing
The backend provides a comprehensive REST API with the following endpoints:

#### Authentication Endpoints
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/refresh` - Refresh access token
- `POST /api/auth/verify-email` - Verify email
- `POST /api/auth/reset-password` - Reset password
- `POST /api/auth/change-password` - Change password

#### Mood Tracking Endpoints
- `POST /api/mood-entries` - Create mood entry
- `GET /api/mood-entries` - Get mood entries
- `GET /api/mood-entries/{id}` - Get specific mood entry
- `PUT /api/mood-entries/{id}` - Update mood entry
- `DELETE /api/mood-entries/{id}` - Delete mood entry

#### AI Analysis Endpoints
- `POST /api/ai/predict-mood` - Predict mood from text
- `POST /api/ai/sentiment-analysis` - Analyze text sentiment
- `POST /api/ai/advanced-prediction` - Advanced ML prediction
- `GET /api/ai/pattern-analysis` - Pattern analysis
- `POST /api/ai/smart-recommendations` - Get smart recommendations

#### Therapeutic AI Endpoints
- `POST /api/therapy/analyze-emotion` - Analyze emotional state
- `POST /api/therapy/feedback` - Submit therapy feedback
- `GET /api/therapy/insights` - Get therapeutic insights

### 2. Testing API Endpoints

#### Test Registration
```bash
curl -X POST "http://localhost:8000/api/auth/register" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "email=test@example.com&password=TestPassword123&name=Test User"
```

#### Test Login
```bash
curl -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "email=test@example.com&password=TestPassword123"
```

#### Test Mood Entry Creation
```bash
curl -X POST "http://localhost:8000/api/mood-entries" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "mood": 8,
    "energy": 7,
    "stress": 3,
    "sleep_hours": 8.5,
    "notes": "Feeling great today!",
    "activities": ["exercise", "socializing"]
  }'
```

#### Test AI Mood Prediction
```bash
curl -X POST "http://localhost:8000/api/ai/predict-mood" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{"text": "I am feeling very happy today!"}'
```

#### Test Therapeutic AI
```bash
curl -X POST "http://localhost:8000/api/therapy/analyze-emotion" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{"text": "I am feeling sad and lonely"}'
```

### 3. Mobile App Testing

#### Start the Mobile App
```bash
cd MoodscapeApp
npm start
```

#### Test on Device
1. Install Expo Go app on your Android device
2. Scan the QR code from the terminal
3. Test the following features:
   - User registration and login
   - Mood tracking
   - AI mood prediction
   - Insights and analytics
   - Profile management

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. Backend Won't Start
**Error**: `ModuleNotFoundError: No module named 'fastapi'`
**Solution**: 
```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt
```

#### 2. Database Issues
**Error**: `sqlalchemy.exc.OperationalError`
**Solution**:
```bash
cd backend
python3 -c "from models.database import init_database; init_database()"
```

#### 3. Mobile App Won't Start
**Error**: `expo: command not found`
**Solution**:
```bash
npm install -g @expo/cli
```

#### 4. API Connection Issues
**Error**: `Network request failed`
**Solution**:
- Ensure backend is running on `http://localhost:8000`
- Check if firewall is blocking the connection
- Verify API_BASE_URL in `MoodscapeApp/src/services/apiService.ts`

#### 5. Authentication Issues
**Error**: `401 Unauthorized`
**Solution**:
- Check if access token is valid
- Try logging in again to get a new token
- Verify JWT secret key in backend

### Debug Mode

#### Backend Debug
```bash
cd backend
source venv/bin/activate
export DEBUG=1
python3 app/main.py
```

#### Mobile App Debug
```bash
cd MoodscapeApp
export EXPO_DEBUG=1
npm start
```

## 📊 Performance Testing

### Load Testing
```bash
# Install Apache Bench
sudo apt-get install apache2-utils

# Test API performance
ab -n 100 -c 10 http://localhost:8000/health
```

### Memory Usage
```bash
# Monitor backend memory usage
ps aux | grep python

# Monitor mobile app memory
# Use React Native Debugger or Flipper
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
tail -f backend/logs/app.log

# Monitor API requests
tail -f backend/logs/access.log
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
4. ✅ User can register and login
5. ✅ Mood entries can be created and retrieved
6. ✅ AI features work correctly
7. ✅ Therapeutic AI provides appropriate responses
8. ✅ Data persists between sessions
9. ✅ Frontend-backend communication is seamless
10. ✅ All tests pass in the automated test suite

## 📞 Support

If you encounter issues:

1. Check the test report generated by `test_complete_app.py`
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
