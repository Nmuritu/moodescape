#!/usr/bin/env python3
"""
Test script for Moodscape application
This script tests the basic functionality of the backend API
"""

import requests
import json
import time
from datetime import datetime

# API base URL
BASE_URL = "http://localhost:8000"

def test_health_check():
    """Test the health check endpoint"""
    print("Testing health check...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

def test_mood_entry_creation():
    """Test creating a mood entry"""
    print("Testing mood entry creation...")
    try:
        mood_data = {
            "mood": 8,
            "energy": 7,
            "stress": 3,
            "sleep_hours": 8.5,
            "notes": "Feeling great today!",
            "activities": ["exercise", "socializing"],
            "weather": "sunny",
            "location": "home"
        }
        
        response = requests.post(
            f"{BASE_URL}/api/mood-entries",
            json=mood_data,
            headers={"Authorization": "Bearer demo_token"}
        )
        
        if response.status_code == 200:
            print("✅ Mood entry creation passed")
            return True
        else:
            print(f"❌ Mood entry creation failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Mood entry creation error: {e}")
        return False

def test_ai_prediction():
    """Test AI mood prediction"""
    print("Testing AI mood prediction...")
    try:
        text = "I'm feeling really happy and energetic today!"
        
        response = requests.post(
            f"{BASE_URL}/api/ai/predict-mood",
            json={"text": text},
            headers={"Authorization": "Bearer demo_token"}
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ AI prediction passed: {result}")
            return True
        else:
            print(f"❌ AI prediction failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ AI prediction error: {e}")
        return False

def test_sentiment_analysis():
    """Test sentiment analysis"""
    print("Testing sentiment analysis...")
    try:
        text = "I'm feeling a bit stressed and overwhelmed with work."
        
        response = requests.post(
            f"{BASE_URL}/api/ai/sentiment-analysis",
            json={"text": text},
            headers={"Authorization": "Bearer demo_token"}
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Sentiment analysis passed: {result}")
            return True
        else:
            print(f"❌ Sentiment analysis failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Sentiment analysis error: {e}")
        return False

def test_smart_recommendations():
    """Test smart recommendations"""
    print("Testing smart recommendations...")
    try:
        context = {
            "mood": 6,
            "energy": 5,
            "weather": "sunny",
            "time_of_day": "afternoon"
        }
        
        response = requests.post(
            f"{BASE_URL}/api/ai/smart-recommendations",
            json={"current_context": context},
            headers={"Authorization": "Bearer demo_token"}
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Smart recommendations passed: {result}")
            return True
        else:
            print(f"❌ Smart recommendations failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Smart recommendations error: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting Moodscape API Tests")
    print("=" * 50)
    
    tests = [
        test_health_check,
        test_mood_entry_creation,
        test_ai_prediction,
        test_sentiment_analysis,
        test_smart_recommendations
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The API is working correctly.")
    else:
        print("⚠️  Some tests failed. Please check the API server.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
