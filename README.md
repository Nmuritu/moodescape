# Moodscape - AI-Powered Mood Tracking Application

A comprehensive mood tracking application built with React Native (Expo) for Android and a Python FastAPI backend with advanced AI capabilities.

##  Features

### Mobile App (React Native/Expo)
- **Mood Tracking**: Log daily mood, energy, stress, and sleep levels
- **AI-Powered Analysis**: Get intelligent insights and predictions about your mood patterns
- **Interactive Charts**: Visualize mood trends with beautiful charts and graphs
- **Activity Tracking**: Track activities that affect your mood
- **Smart Recommendations**: Receive personalized suggestions based on your data
- **Modern UI/UX**: Clean, intuitive interface with smooth animations

### Backend (Python FastAPI)
- **Advanced AI Models**: Machine learning models for mood prediction and pattern analysis
- **Sentiment Analysis**: Natural language processing for text-based mood analysis
- **Pattern Recognition**: Identify trends and correlations in mood data
- **Smart Insights**: Generate actionable recommendations based on user data
- **RESTful API**: Comprehensive API for all app functionality
- **Database Integration**: SQLAlchemy with SQLite/PostgreSQL support

##  Quick Start

### Prerequisites
- Node.js (v16 or higher)
- Python 3.8+
- Expo CLI (`npm install -g @expo/cli`)
- Android Studio (for Android development)

### Mobile App Setup

1. **Navigate to the app directory:**
   ```bash
   cd MoodscapeApp
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   # or
   expo start
   ```

4. **Run on Android:**
   ```bash
   npm run android
   # or
   expo start --android
   ```

### Backend Setup

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database:**
   ```bash
   python -c "from models.database import init_database; init_database()"
   ```

5. **Start the server:**
   ```bash
   python app/main.py
   # or
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`

##  App Screens

### Home Screen
- Daily mood overview
- Quick access to mood logging
- Recent insights and recommendations
- Quick action buttons

### Mood Tracker
- Interactive mood scale (1-10)
- Energy, stress, and sleep tracking
- Activity selection
- Notes and context logging

### Insights Screen
- Mood trend charts
- Statistical overview
- AI-generated insights
- Pattern analysis

### AI Prediction
- Text-based mood analysis
- AI-powered mood prediction
- Personalized recommendations
- Factor analysis

### Profile Screen
- User preferences
- Goals and settings
- Data export options
- App information

## 🤖 AI Features

### Mood Analysis
- **Sentiment Analysis**: Analyze text input for emotional content
- **Pattern Recognition**: Identify recurring mood patterns
- **Trend Analysis**: Track mood changes over time
- **Correlation Analysis**: Find relationships between different factors

### Machine Learning Models
- **Random Forest**: For mood prediction
- **Gradient Boosting**: For energy level prediction
- **Linear Regression**: For stress level prediction
- **Clustering**: For mood pattern grouping

### Smart Recommendations
- **Context-Aware**: Based on time, weather, and current state
- **Personalized**: Tailored to individual patterns
- **Actionable**: Specific, implementable suggestions
- **Proactive**: Anticipate needs based on patterns

##  Database Schema

### Core Tables
- **Users**: User accounts and authentication
- **Mood Entries**: Daily mood tracking data
- **User Profiles**: User preferences and settings
- **Insights**: AI-generated insights and recommendations
- **Activities**: Trackable activities and their mood impact
- **AI Models**: Stored ML models and their performance

##  API Endpoints

### Mood Tracking
- `POST /api/mood-entries` - Create mood entry
- `GET /api/mood-entries` - Get mood entries
- `PUT /api/mood-entries/{id}` - Update mood entry
- `DELETE /api/mood-entries/{id}` - Delete mood entry

### AI Analysis
- `POST /api/ai/predict-mood` - Predict mood from text
- `POST /api/ai/sentiment-analysis` - Analyze text sentiment
- `POST /api/ai/advanced-prediction` - Advanced ML prediction
- `GET /api/ai/pattern-analysis` - Pattern analysis
- `POST /api/ai/smart-recommendations` - Get smart recommendations

### Insights
- `GET /api/insights` - Get AI insights
- `GET /api/stats` - Get mood statistics
- `GET /api/trends` - Get mood trends

### User Management
- `GET /api/profile` - Get user profile
- `PUT /api/profile` - Update user profile

##  Design System

### Colors
- **Primary**: #6366f1 (Indigo)
- **Success**: #10b981 (Emerald)
- **Warning**: #f59e0b (Amber)
- **Error**: #ef4444 (Red)
- **Info**: #06b6d4 (Cyan)

### Typography
- **Headings**: Bold, 18-24px
- **Body**: Regular, 14-16px
- **Captions**: Regular, 12px

### Components
- **Cards**: Rounded corners, subtle shadows
- **Buttons**: Rounded, with hover states
- **Inputs**: Clean borders, focus states
- **Charts**: Interactive, responsive

##  Testing

### Mobile App
```bash
cd MoodscapeApp
npm test
```

### Backend
```bash
cd backend
pytest
```

##  Deployment

### Mobile App
1. **Build for production:**
   ```bash
   expo build:android
   ```

2. **Deploy to Google Play Store:**
   - Follow Expo's deployment guide
   - Configure app signing
   - Upload to Play Console

### Backend
1. **Docker deployment:**
   ```bash
   docker build -t moodscape-backend .
   docker run -p 8000:8000 moodscape-backend
   ```

2. **Cloud deployment:**
   - Deploy to Heroku, AWS, or Google Cloud
   - Configure environment variables
   - Set up database connection

##  Security

- **Authentication**: JWT tokens for API access
- **Data Encryption**: Sensitive data encrypted at rest
- **Input Validation**: Comprehensive input sanitization
- **Rate Limiting**: API rate limiting to prevent abuse
- **CORS**: Configured for secure cross-origin requests

##  Performance

### Mobile App
- **Optimized Images**: Compressed and cached
- **Lazy Loading**: Components loaded on demand
- **Memory Management**: Efficient state management
- **Smooth Animations**: 60fps animations

### Backend
- **Database Indexing**: Optimized queries
- **Caching**: Redis for frequently accessed data
- **Async Processing**: Non-blocking operations
- **Model Caching**: Pre-trained models cached

##  Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

##  License

This project is licensed under the MIT License - see the LICENSE file for details.

##  Acknowledgments

- **Expo**: For the amazing React Native platform
- **FastAPI**: For the high-performance Python framework
- **scikit-learn**: For machine learning capabilities
- **React Native Chart Kit**: For beautiful charts
- **Ionicons**: For the icon library

##  Support

For support, email support@moodscape.app or create an issue on GitHub.

---

**Built with LOVE for better mental health tracking**
