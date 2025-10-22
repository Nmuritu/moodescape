# Moodscape - User Manual

## Table of Contents
1. [Getting Started](#getting-started)
2. [Preview Mode](#preview-mode)
3. [User Registration & Login](#user-registration--login)
4. [Main Features](#main-features)
5. [AI Features](#ai-features)
6. [Settings & Account Management](#settings--account-management)
7. [Admin Panel](#admin-panel)
8. [Troubleshooting](#troubleshooting)
9. [Technical Support](#technical-support)

## Getting Started

### System Requirements
- **Mobile App**: Android 6.0+ or iOS 10.0+
- **Backend**: Python 3.8+ with FastAPI
- **Cross-Platform**: Windows, macOS, Linux support

### Quick Start
1. **Start the Backend Server**:
   ```bash
   # Linux/macOS
   cd backend && source venv/bin/activate && python3 app/simple_main.py
   
   # Windows
   cd backend && venv\Scripts\activate && python app\simple_main.py
   ```

2. **Start the Mobile App**:
   ```bash
   cd MoodscapeApp && npm start
   ```

3. **Access the Application**:
   - Open Expo Go app on your mobile device
   - Scan the QR code displayed in the terminal
   - Or use the web version at `http://localhost:19006`

## Preview Mode

### What is Preview Mode?
Preview mode allows you to try Moodscape without creating an account. You get limited access to core features to experience the app before committing to registration.

### Preview Features
- ✅ Create mood entries (limited to 5 per session)
- ✅ Basic AI mood analysis (limited prompts)
- ✅ View basic insights
- ✅ Access upgrade information
- ❌ No data persistence
- ❌ No advanced AI features
- ❌ No user profile management

### Starting a Preview Session
1. Open the app
2. Tap "Try Preview Mode"
3. Enter your name (optional)
4. Start exploring limited features

### Preview Limitations
- **Session Duration**: 30 minutes maximum
- **Mood Entries**: 5 entries per session
- **AI Analysis**: 3 analysis requests per session
- **Data Storage**: No data saved between sessions

## User Registration & Login

### Creating an Account
1. Tap "Register" on the welcome screen
2. Fill in the registration form:
   - **Name**: Your full name
   - **Email**: Valid email address
   - **Password**: Minimum 8 characters
3. Tap "Create Account"
4. Check your email for verification link
5. Click the verification link to activate your account

### Logging In
1. Tap "Login" on the welcome screen
2. Enter your email and password
3. Tap "Login"
4. You'll be redirected to the main app

### Password Recovery
1. On the login screen, tap "Forgot Password?"
2. Enter your registered email
3. Check your email for reset instructions
4. Follow the link to create a new password

## Main Features

### Home Screen
The main dashboard showing:
- **Today's Mood**: Your current mood status
- **Recent Insights**: AI-generated insights from your data
- **Quick Actions**: 
  - Log Mood
  - View Trends
  - AI Analysis
  - Settings

### Mood Tracking
1. **Logging Your Mood**:
   - Tap the "Mood" tab
   - Select your mood (1-10 scale or emojis)
   - Rate your energy level
   - Rate your stress level
   - Add sleep quality
   - Select activities
   - Add notes (optional)
   - Tap "Save Entry"

2. **Mood Scales Available**:
   - **1-10 Scale**: Numerical rating
   - **1-5 Scale**: Simplified rating
   - **Emojis**: Visual mood representation

### Insights & Analytics
- **Mood Trends**: Visual charts showing mood patterns
- **Energy Analysis**: Track energy levels over time
- **Stress Patterns**: Identify stress triggers
- **Sleep Correlation**: Link sleep quality to mood
- **Activity Impact**: See how activities affect your mood

## AI Features

### AI Mood Analysis
1. Tap "AI Analysis" from the home screen
2. Enter text describing your current state
3. Tap "Analyze Mood"
4. Receive:
   - Predicted mood
   - Confidence level
   - Key factors
   - Personalized suggestions

### Therapeutic AI
The AI is trained in therapy-related topics and can:
- **Emotional Support**: Provide empathetic responses
- **Pattern Recognition**: Identify mood patterns
- **Crisis Detection**: Recognize concerning patterns
- **Personalized Recommendations**: Suggest coping strategies
- **Self-Learning**: Improves with each interaction

### AI Learning & Privacy
- The AI uses your communications to improve its responses
- Your data helps train the AI for better therapeutic support
- All data is anonymized and secure
- You can opt out of AI learning in settings

## Settings & Account Management

### Accessing Settings
1. Tap the "Settings" tab
2. Or tap your profile picture and select "Settings"

### Profile Management
- **View Profile**: See your account information
- **Edit Profile**: Update name, email, phone
- **Change Password**: Update your password
- **Privacy Settings**: Control data sharing

### Account Actions
- **Logout**: Sign out of your account
- **Delete Account**: Permanently remove your account
- **Data Export**: Download your data
- **Privacy Controls**: Manage AI learning preferences

### Notification Settings
- **Mood Reminders**: Daily mood logging prompts
- **Insight Notifications**: New insights available
- **Goal Reminders**: Progress tracking alerts
- **Custom Times**: Set your preferred reminder times

## Admin Panel

### Admin Access
- **Username**: makopolo
- **Password**: 123456
- **Access**: Full system access for testing

### Admin Features
- **System Monitoring**: Real-time system status
- **User Statistics**: User count and activity metrics
- **Error Logging**: System error tracking
- **Performance Metrics**: App performance data
- **Troubleshooting Tools**: Diagnostic utilities

### Admin Capabilities
- View all user data (anonymized)
- Monitor system health
- Access error logs
- Test system functionality
- Cannot delete admin account

## Troubleshooting

### Common Issues

#### App Won't Start
1. **Check Backend**: Ensure backend server is running
2. **Restart Services**: Stop and restart both backend and mobile app
3. **Clear Cache**: Clear app cache and restart
4. **Check Dependencies**: Run `npm install` in MoodscapeApp folder

#### Login Issues
1. **Verify Email**: Check if email is verified
2. **Reset Password**: Use forgot password feature
3. **Check Credentials**: Ensure correct email/password
4. **Clear Storage**: Clear app data and try again

#### AI Features Not Working
1. **Check Internet**: Ensure stable internet connection
2. **Restart App**: Close and reopen the application
3. **Check Backend**: Verify backend server is running
4. **Update App**: Ensure you have the latest version

#### Data Not Saving
1. **Check Authentication**: Ensure you're logged in
2. **Verify Backend**: Check if backend is responding
3. **Clear Cache**: Clear app cache and try again
4. **Check Storage**: Ensure sufficient device storage

### Error Codes
- **422**: Validation error - check input format
- **401**: Authentication required - log in
- **403**: Access denied - check permissions
- **500**: Server error - contact support

### Performance Issues
1. **Close Background Apps**: Free up device memory
2. **Restart Device**: Reboot your phone/tablet
3. **Update OS**: Ensure latest operating system
4. **Clear Storage**: Remove unnecessary files

## Technical Support

### Getting Help
1. **Check This Manual**: Review troubleshooting section
2. **Admin Panel**: Use admin tools for diagnostics
3. **Error Logs**: Check system logs for specific errors
4. **Contact Support**: Reach out to development team

### Reporting Issues
When reporting problems, include:
- **Device Information**: OS version, device model
- **App Version**: Current app version
- **Error Messages**: Exact error text
- **Steps to Reproduce**: How the issue occurred
- **Screenshots**: Visual evidence of the problem

### System Requirements
- **Minimum RAM**: 2GB
- **Storage Space**: 100MB free space
- **Internet**: Stable connection required
- **Browser**: Latest version for web access

### Data Backup
- **Automatic Backup**: Data synced to cloud
- **Manual Export**: Export data from settings
- **Account Recovery**: Use email for account recovery
- **Data Retention**: Data kept for 2 years after account deletion

---

## Quick Reference

### Keyboard Shortcuts (Web Version)
- **Ctrl + S**: Save current entry
- **Ctrl + N**: New mood entry
- **Ctrl + I**: Open insights
- **Ctrl + A**: Open AI analysis
- **Ctrl + P**: Open profile

### Important URLs
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health
- **Mobile App**: http://localhost:19006

### Emergency Contacts
- **Crisis Support**: 988 (US) or local crisis hotline
- **Technical Issues**: Contact development team
- **Data Concerns**: Review privacy policy in settings

---

*Last Updated: October 2024*
*Version: 1.0.0*
