# Moodscape - Project Overview

##  Project Summary

Moodscape is a comprehensive AI-powered mood tracking application designed to help users understand and improve their mental well-being. The application consists of a React Native mobile app for Android and a Python FastAPI backend with advanced machine learning capabilities.

##  Architecture

### Frontend (Mobile App)
- **Framework**: React Native with Expo
- **Language**: TypeScript
- **Navigation**: React Navigation (Stack + Bottom Tabs)
- **Charts**: React Native Chart Kit
- **Storage**: AsyncStorage for local data persistence
- **Icons**: Ionicons
- **Styling**: StyleSheet with modern design system

### Backend (API Server)
- **Framework**: FastAPI (Python)
- **Database**: SQLAlchemy with SQLite/PostgreSQL
- **AI/ML**: scikit-learn, transformers, pandas, numpy
- **Authentication**: JWT tokens
- **Documentation**: Auto-generated OpenAPI/Swagger docs

##  Mobile App Features

### Core Screens
1. **Home Screen**
   - Daily mood overview
   - Quick access to mood logging
   - Recent insights and recommendations
   - Quick action buttons

2. **Mood Tracker Screen**
   - Interactive mood scale (1-10 with emojis)
   - Energy, stress, and sleep level tracking
   - Activity selection with mood impact
   - Notes and context logging
   - Weather and location tracking

3. **Insights Screen**
   - Mood trend charts (7/30/90 days)
   - Statistical overview cards
   - AI-generated insights
   - Pattern analysis and correlations

4. **AI Prediction Screen**
   - Text-based mood analysis
   - AI-powered mood prediction
   - Personalized recommendations
   - Factor analysis and confidence scores

5. **Profile Screen**
   - User preferences and settings
   - Goals and tracking preferences
   - Data export options
   - App information and help

### Key Features
- **Intuitive UI**: Modern, clean design with smooth animations
- **Offline Support**: Local data storage with AsyncStorage
- **Real-time Updates**: Live data synchronization
- **Accessibility**: Screen reader support and high contrast
- **Responsive Design**: Adapts to different screen sizes

##  AI & Machine Learning Features

### Mood Analysis
- **Sentiment Analysis**: VADER, TextBlob, and transformer-based
- **Emotion Detection**: Multi-label emotion classification
- **Pattern Recognition**: Identify recurring mood patterns
- **Trend Analysis**: Track mood changes over time
- **Correlation Analysis**: Find relationships between factors

### Machine Learning Models
- **Random Forest**: For mood prediction
- **Gradient Boosting**: For energy level prediction
- **Linear Regression**: For stress level prediction
- **K-Means Clustering**: For mood pattern grouping
- **Feature Engineering**: Advanced feature extraction

### Smart Recommendations
- **Context-Aware**: Based on time, weather, and current state
- **Personalized**: Tailored to individual patterns
- **Actionable**: Specific, implementable suggestions
- **Proactive**: Anticipate needs based on patterns

##  Database Schema

### Core Tables
- **users**: User accounts and authentication
- **mood_entries**: Daily mood tracking data
- **user_profiles**: User preferences and settings
- **insights**: AI-generated insights and recommendations
- **activities**: Trackable activities and their mood impact
- **ai_models**: Stored ML models and their performance

### Data Relationships
- Users have many mood entries
- Users have one profile
- Users have many insights
- Users have many activities
- Users have many AI models

##  API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration
- `POST /api/auth/refresh` - Refresh JWT token

### Mood Tracking
- `POST /api/mood-entries` - Create mood entry
- `GET /api/mood-entries` - Get mood entries (with filtering)
- `GET /api/mood-entries/{id}` - Get specific mood entry
- `PUT /api/mood-entries/{id}` - Update mood entry
- `DELETE /api/mood-entries/{id}` - Delete mood entry

### AI Analysis
- `POST /api/ai/predict-mood` - Predict mood from text
- `POST /api/ai/sentiment-analysis` - Analyze text sentiment
- `POST /api/ai/advanced-prediction` - Advanced ML prediction
- `GET /api/ai/pattern-analysis` - Pattern analysis
- `POST /api/ai/smart-recommendations` - Get smart recommendations
- `POST /api/ai/train-models` - Train AI models

### Insights & Analytics
- `GET /api/insights` - Get AI insights
- `GET /api/stats` - Get mood statistics
- `GET /api/trends` - Get mood trends
- `POST /api/analyze` - Comprehensive mood analysis

### User Management
- `GET /api/profile` - Get user profile
- `PUT /api/profile` - Update user profile
- `GET /api/activities` - Get user activities
- `POST /api/activities` - Create activity

##  Design System

### Color Palette
- **Primary**: #6366f1 (Indigo) - Main brand color
- **Success**: #10b981 (Emerald) - Positive actions
- **Warning**: #f59e0b (Amber) - Caution/attention
- **Error**: #ef4444 (Red) - Errors/danger
- **Info**: #06b6d4 (Cyan) - Information
- **Neutral**: #6b7280 (Gray) - Text and borders

### Typography
- **Headings**: Bold, 18-24px, primary color
- **Body**: Regular, 14-16px, neutral color
- **Captions**: Regular, 12px, muted color
- **Labels**: Medium, 14px, neutral color

### Components
- **Cards**: 12px border radius, subtle shadow
- **Buttons**: 8px border radius, hover states
- **Inputs**: 8px border radius, focus states
- **Charts**: Interactive, responsive design

##  Security Features

### Authentication & Authorization
- JWT tokens for stateless authentication
- Secure password hashing with bcrypt
- Token refresh mechanism
- Role-based access control

### Data Protection
- Input validation and sanitization
- SQL injection prevention
- XSS protection
- CORS configuration
- Rate limiting

### Privacy
- Local data encryption
- Secure API communication
- User data anonymization options
- GDPR compliance features

##  Performance Optimizations

### Mobile App
- **Image Optimization**: Compressed and cached images
- **Lazy Loading**: Components loaded on demand
- **Memory Management**: Efficient state management
- **Smooth Animations**: 60fps animations
- **Bundle Splitting**: Code splitting for faster loading

### Backend
- **Database Indexing**: Optimized query performance
- **Caching**: Redis for frequently accessed data
- **Async Processing**: Non-blocking operations
- **Model Caching**: Pre-trained models cached
- **Connection Pooling**: Efficient database connections

##  Testing Strategy

### Mobile App Testing
- **Unit Tests**: Component and function testing
- **Integration Tests**: API integration testing
- **E2E Tests**: Full user journey testing
- **Performance Tests**: Load and stress testing

### Backend Testing
- **Unit Tests**: Service and model testing
- **API Tests**: Endpoint testing
- **Integration Tests**: Database integration
- **ML Tests**: Model accuracy testing

##  Deployment

### Mobile App Deployment
1. **Development**: Expo development server
2. **Staging**: Expo preview builds
3. **Production**: Google Play Store
4. **CI/CD**: Automated builds and testing

### Backend Deployment
1. **Development**: Local development server
2. **Staging**: Docker containers
3. **Production**: Cloud deployment (AWS/Heroku)
4. **Monitoring**: Health checks and logging

##  Future Enhancements

### Planned Features
- **iOS Support**: Native iOS app
- **Web Dashboard**: Web-based analytics dashboard
- **Social Features**: Mood sharing and support groups
- **Wearable Integration**: Smartwatch compatibility
- **Voice Notes**: Voice-based mood logging
- **Advanced Analytics**: More sophisticated ML models

### Technical Improvements
- **Real-time Sync**: WebSocket connections
- **Offline AI**: On-device ML models
- **Advanced Security**: Biometric authentication
- **Performance**: Further optimizations
- **Scalability**: Microservices architecture

##  Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Set up development environment
4. Make changes and add tests
5. Submit a pull request

### Code Standards
- **TypeScript**: Strict type checking
- **Python**: PEP 8 style guide
- **Testing**: Comprehensive test coverage
- **Documentation**: Clear and up-to-date
- **Commits**: Conventional commit messages

##  Support & Documentation

### Resources
- **README**: Quick start guide
- **API Docs**: Interactive API documentation
- **Code Comments**: Inline documentation
- **Issues**: GitHub issue tracking
- **Discussions**: Community discussions

### Contact
- **Email**: support@moodscape.app
- **GitHub**: github.com/moodscape
- **Documentation**: docs.moodscape.app

---

**Built with LOVE for better mental health tracking and awareness**
