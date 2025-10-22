#!/usr/bin/env python3
"""
Comprehensive test script for Moodscape application
Tests both backend API and frontend-backend integration
"""

import requests
import json
import time
import subprocess
import sys
import os
from datetime import datetime
import threading
import signal

# Configuration
API_BASE_URL = "http://localhost:8000"
MOBILE_APP_DIR = "MoodscapeApp"
BACKEND_DIR = "backend"

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

class TestRunner:
    def __init__(self):
        self.backend_process = None
        self.mobile_process = None
        self.test_results = []
        self.api_available = False
        
    def print_header(self, text):
        print(f"\n{Colors.BLUE}{Colors.BOLD}{'='*60}{Colors.END}")
        print(f"{Colors.BLUE}{Colors.BOLD}{text.center(60)}{Colors.END}")
        print(f"{Colors.BLUE}{Colors.BOLD}{'='*60}{Colors.END}\n")
    
    def print_success(self, text):
        print(f"{Colors.GREEN}✅ {text}{Colors.END}")
    
    def print_error(self, text):
        print(f"{Colors.RED}❌ {text}{Colors.END}")
    
    def print_warning(self, text):
        print(f"{Colors.YELLOW}⚠️  {text}{Colors.END}")
    
    def print_info(self, text):
        print(f"{Colors.CYAN}ℹ️  {text}{Colors.END}")
    
    def log_result(self, test_name, success, message):
        self.test_results.append({
            'test': test_name,
            'success': success,
            'message': message,
            'timestamp': datetime.now().isoformat()
        })
        
        if success:
            self.print_success(f"{test_name}: {message}")
        else:
            self.print_error(f"{test_name}: {message}")
    
    def check_dependencies(self):
        """Check if required dependencies are installed"""
        self.print_header("CHECKING DEPENDENCIES")
        
        # Check Python
        try:
            result = subprocess.run(['python3', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                self.log_result("Python Check", True, f"Python {result.stdout.strip()}")
            else:
                self.log_result("Python Check", False, "Python3 not found")
                return False
        except FileNotFoundError:
            self.log_result("Python Check", False, "Python3 not found")
            return False
        
        # Check Node.js
        try:
            result = subprocess.run(['node', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                self.log_result("Node.js Check", True, f"Node.js {result.stdout.strip()}")
            else:
                self.log_result("Node.js Check", False, "Node.js not found")
                return False
        except FileNotFoundError:
            self.log_result("Node.js Check", False, "Node.js not found")
            return False
        
        # Check Expo CLI
        try:
            result = subprocess.run(['expo', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                self.log_result("Expo CLI Check", True, f"Expo CLI {result.stdout.strip()}")
            else:
                self.log_result("Expo CLI Check", False, "Expo CLI not found")
                self.print_info("Installing Expo CLI...")
                subprocess.run(['npm', 'install', '-g', '@expo/cli'], check=True)
                self.log_result("Expo CLI Check", True, "Expo CLI installed")
        except FileNotFoundError:
            self.log_result("Expo CLI Check", False, "Expo CLI not found")
            return False
        
        return True
    
    def install_backend_dependencies(self):
        """Install Python backend dependencies"""
        self.print_header("INSTALLING BACKEND DEPENDENCIES")
        
        try:
            os.chdir(BACKEND_DIR)
            
            # Create virtual environment if it doesn't exist
            if not os.path.exists('venv'):
                self.print_info("Creating virtual environment...")
                subprocess.run(['python3', '-m', 'venv', 'venv'], check=True)
            
            # Activate virtual environment and install dependencies
            if os.name == 'nt':  # Windows
                pip_path = os.path.join('venv', 'Scripts', 'pip')
            else:  # Unix/Linux/macOS
                pip_path = os.path.join('venv', 'bin', 'pip')
            
            self.print_info("Installing Python dependencies...")
            subprocess.run([pip_path, 'install', '-r', 'requirements.txt'], check=True)
            
            self.log_result("Backend Dependencies", True, "All dependencies installed")
            os.chdir('..')
            return True
            
        except subprocess.CalledProcessError as e:
            self.log_result("Backend Dependencies", False, f"Installation failed: {e}")
            os.chdir('..')
            return False
        except Exception as e:
            self.log_result("Backend Dependencies", False, f"Error: {e}")
            os.chdir('..')
            return False
    
    def install_mobile_dependencies(self):
        """Install mobile app dependencies"""
        self.print_header("INSTALLING MOBILE APP DEPENDENCIES")
        
        try:
            os.chdir(MOBILE_APP_DIR)
            
            self.print_info("Installing Node.js dependencies...")
            subprocess.run(['npm', 'install'], check=True)
            
            self.log_result("Mobile Dependencies", True, "All dependencies installed")
            os.chdir('..')
            return True
            
        except subprocess.CalledProcessError as e:
            self.log_result("Mobile Dependencies", False, f"Installation failed: {e}")
            os.chdir('..')
            return False
        except Exception as e:
            self.log_result("Mobile Dependencies", False, f"Error: {e}")
            os.chdir('..')
            return False
    
    def start_backend(self):
        """Start the backend server"""
        self.print_header("STARTING BACKEND SERVER")
        
        try:
            os.chdir(BACKEND_DIR)
            
            # Activate virtual environment and start server
            if os.name == 'nt':  # Windows
                python_path = os.path.join('venv', 'Scripts', 'python')
            else:  # Unix/Linux/macOS
                python_path = os.path.join('venv', 'bin', 'python')
            
            self.print_info("Starting FastAPI server...")
            self.backend_process = subprocess.Popen(
                [python_path, 'app/main.py'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Wait for server to start
            self.print_info("Waiting for server to start...")
            time.sleep(5)
            
            # Check if server is running
            if self.check_api_health():
                self.log_result("Backend Server", True, "Server started successfully")
                os.chdir('..')
                return True
            else:
                self.log_result("Backend Server", False, "Server failed to start")
                self.stop_backend()
                os.chdir('..')
                return False
                
        except Exception as e:
            self.log_result("Backend Server", False, f"Error: {e}")
            os.chdir('..')
            return False
    
    def check_api_health(self):
        """Check if API is responding"""
        try:
            response = requests.get(f"{API_BASE_URL}/health", timeout=5)
            if response.status_code == 200:
                self.api_available = True
                return True
            else:
                return False
        except requests.exceptions.RequestException:
            return False
    
    def stop_backend(self):
        """Stop the backend server"""
        if self.backend_process:
            self.backend_process.terminate()
            self.backend_process.wait()
            self.backend_process = None
    
    def test_api_endpoints(self):
        """Test all API endpoints"""
        self.print_header("TESTING API ENDPOINTS")
        
        if not self.api_available:
            self.log_result("API Health Check", False, "API not available")
            return False
        
        # Test health endpoint
        try:
            response = requests.get(f"{API_BASE_URL}/health")
            if response.status_code == 200:
                self.log_result("Health Endpoint", True, "API is healthy")
            else:
                self.log_result("Health Endpoint", False, f"Status code: {response.status_code}")
        except Exception as e:
            self.log_result("Health Endpoint", False, f"Error: {e}")
        
        # Test authentication endpoints
        self.test_auth_endpoints()
        
        # Test mood tracking endpoints
        self.test_mood_endpoints()
        
        # Test AI endpoints
        self.test_ai_endpoints()
        
        return True
    
    def test_auth_endpoints(self):
        """Test authentication endpoints"""
        self.print_info("Testing authentication endpoints...")
        
        # Test registration
        try:
            response = requests.post(f"{API_BASE_URL}/api/auth/register", data={
                'email': 'test@example.com',
                'password': 'TestPassword123',
                'name': 'Test User'
            })
            if response.status_code in [200, 201]:
                self.log_result("User Registration", True, "Registration endpoint working")
            else:
                self.log_result("User Registration", False, f"Status code: {response.status_code}")
        except Exception as e:
            self.log_result("User Registration", False, f"Error: {e}")
        
        # Test login
        try:
            response = requests.post(f"{API_BASE_URL}/api/auth/login", data={
                'email': 'test@example.com',
                'password': 'TestPassword123'
            })
            if response.status_code == 200:
                data = response.json()
                if data.get('success') and data.get('access_token'):
                    self.log_result("User Login", True, "Login endpoint working")
                    # Store token for other tests
                    self.access_token = data['access_token']
                else:
                    self.log_result("User Login", False, "Invalid response format")
            else:
                self.log_result("User Login", False, f"Status code: {response.status_code}")
        except Exception as e:
            self.log_result("User Login", False, f"Error: {e}")
    
    def test_mood_endpoints(self):
        """Test mood tracking endpoints"""
        self.print_info("Testing mood tracking endpoints...")
        
        if not hasattr(self, 'access_token'):
            self.log_result("Mood Endpoints", False, "No access token available")
            return
        
        headers = {'Authorization': f'Bearer {self.access_token}'}
        
        # Test create mood entry
        try:
            mood_data = {
                'mood': 8,
                'energy': 7,
                'stress': 3,
                'sleep_hours': 8.5,
                'notes': 'Feeling great today!',
                'activities': ['exercise', 'socializing']
            }
            response = requests.post(
                f"{API_BASE_URL}/api/mood-entries",
                json=mood_data,
                headers=headers
            )
            if response.status_code in [200, 201]:
                self.log_result("Create Mood Entry", True, "Mood entry created successfully")
            else:
                self.log_result("Create Mood Entry", False, f"Status code: {response.status_code}")
        except Exception as e:
            self.log_result("Create Mood Entry", False, f"Error: {e}")
        
        # Test get mood entries
        try:
            response = requests.get(f"{API_BASE_URL}/api/mood-entries", headers=headers)
            if response.status_code == 200:
                self.log_result("Get Mood Entries", True, "Mood entries retrieved successfully")
            else:
                self.log_result("Get Mood Entries", False, f"Status code: {response.status_code}")
        except Exception as e:
            self.log_result("Get Mood Entries", False, f"Error: {e}")
    
    def test_ai_endpoints(self):
        """Test AI endpoints"""
        self.print_info("Testing AI endpoints...")
        
        if not hasattr(self, 'access_token'):
            self.log_result("AI Endpoints", False, "No access token available")
            return
        
        headers = {'Authorization': f'Bearer {self.access_token}'}
        
        # Test mood prediction
        try:
            response = requests.post(
                f"{API_BASE_URL}/api/ai/predict-mood",
                json={'text': 'I am feeling very happy today!'},
                headers=headers
            )
            if response.status_code == 200:
                self.log_result("Mood Prediction", True, "AI mood prediction working")
            else:
                self.log_result("Mood Prediction", False, f"Status code: {response.status_code}")
        except Exception as e:
            self.log_result("Mood Prediction", False, f"Error: {e}")
        
        # Test sentiment analysis
        try:
            response = requests.post(
                f"{API_BASE_URL}/api/ai/sentiment-analysis",
                json={'text': 'I am feeling stressed and overwhelmed'},
                headers=headers
            )
            if response.status_code == 200:
                self.log_result("Sentiment Analysis", True, "Sentiment analysis working")
            else:
                self.log_result("Sentiment Analysis", False, f"Status code: {response.status_code}")
        except Exception as e:
            self.log_result("Sentiment Analysis", False, f"Error: {e}")
        
        # Test therapeutic AI
        try:
            response = requests.post(
                f"{API_BASE_URL}/api/therapy/analyze-emotion",
                json={'text': 'I am feeling sad and lonely'},
                headers=headers
            )
            if response.status_code == 200:
                self.log_result("Therapeutic AI", True, "Therapeutic AI analysis working")
            else:
                self.log_result("Therapeutic AI", False, f"Status code: {response.status_code}")
        except Exception as e:
            self.log_result("Therapeutic AI", False, f"Error: {e}")
    
    def test_mobile_app(self):
        """Test mobile app compilation"""
        self.print_header("TESTING MOBILE APP")
        
        try:
            os.chdir(MOBILE_APP_DIR)
            
            # Check if app can be built
            self.print_info("Checking mobile app structure...")
            
            # Check for required files
            required_files = [
                'App.tsx',
                'package.json',
                'src/screens/HomeScreen.tsx',
                'src/services/apiService.ts'
            ]
            
            all_files_exist = True
            for file in required_files:
                if os.path.exists(file):
                    self.log_result(f"File Check: {file}", True, "File exists")
                else:
                    self.log_result(f"File Check: {file}", False, "File missing")
                    all_files_exist = False
            
            if all_files_exist:
                self.log_result("Mobile App Structure", True, "All required files present")
            else:
                self.log_result("Mobile App Structure", False, "Some files missing")
            
            # Test TypeScript compilation
            self.print_info("Testing TypeScript compilation...")
            try:
                subprocess.run(['npx', 'tsc', '--noEmit'], check=True, capture_output=True)
                self.log_result("TypeScript Compilation", True, "No compilation errors")
            except subprocess.CalledProcessError as e:
                self.log_result("TypeScript Compilation", False, f"Compilation errors: {e}")
            
            os.chdir('..')
            return all_files_exist
            
        except Exception as e:
            self.log_result("Mobile App Test", False, f"Error: {e}")
            os.chdir('..')
            return False
    
    def generate_report(self):
        """Generate test report"""
        self.print_header("TEST REPORT")
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result['success'])
        failed_tests = total_tests - passed_tests
        
        print(f"\n{Colors.BOLD}SUMMARY:{Colors.END}")
        print(f"Total Tests: {total_tests}")
        print(f"{Colors.GREEN}Passed: {passed_tests}{Colors.END}")
        print(f"{Colors.RED}Failed: {failed_tests}{Colors.END}")
        print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        if failed_tests > 0:
            print(f"\n{Colors.RED}{Colors.BOLD}FAILED TESTS:{Colors.END}")
            for result in self.test_results:
                if not result['success']:
                    print(f"  • {result['test']}: {result['message']}")
        
        # Save detailed report
        report_file = f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w') as f:
            json.dump(self.test_results, f, indent=2)
        
        print(f"\n{Colors.CYAN}Detailed report saved to: {report_file}{Colors.END}")
        
        return failed_tests == 0
    
    def cleanup(self):
        """Cleanup resources"""
        self.print_info("Cleaning up...")
        self.stop_backend()
    
    def run_all_tests(self):
        """Run all tests"""
        try:
            self.print_header("MOODSCAPE APPLICATION TEST SUITE")
            self.print_info("Starting comprehensive testing...")
            
            # Check dependencies
            if not self.check_dependencies():
                self.print_error("Dependency check failed. Please install required dependencies.")
                return False
            
            # Install dependencies
            if not self.install_backend_dependencies():
                self.print_error("Backend dependency installation failed.")
                return False
            
            if not self.install_mobile_dependencies():
                self.print_error("Mobile dependency installation failed.")
                return False
            
            # Start backend
            if not self.start_backend():
                self.print_error("Backend startup failed.")
                return False
            
            # Test API
            self.test_api_endpoints()
            
            # Test mobile app
            self.test_mobile_app()
            
            # Generate report
            success = self.generate_report()
            
            if success:
                self.print_success("All tests passed! Application is ready to use.")
            else:
                self.print_error("Some tests failed. Please check the report for details.")
            
            return success
            
        except KeyboardInterrupt:
            self.print_warning("Testing interrupted by user")
            return False
        except Exception as e:
            self.print_error(f"Unexpected error: {e}")
            return False
        finally:
            self.cleanup()

def main():
    """Main function"""
    print(f"{Colors.PURPLE}{Colors.BOLD}")
    print("🌙 MOODSCAPE APPLICATION TESTER 🌙")
    print("Comprehensive testing for mood tracking app")
    print(f"{Colors.END}")
    
    runner = TestRunner()
    
    # Handle Ctrl+C gracefully
    def signal_handler(sig, frame):
        print(f"\n{Colors.YELLOW}Test interrupted by user{Colors.END}")
        runner.cleanup()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    
    success = runner.run_all_tests()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
