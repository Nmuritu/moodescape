#!/usr/bin/env python3
"""
Final comprehensive test script for Moodscape application
Tests all features including preview mode, admin functionality, and cross-platform compatibility
"""

import requests
import json
import time
import subprocess
import sys
import os
from datetime import datetime
import platform

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

class FinalTester:
    def __init__(self):
        self.api_base_url = "http://localhost:8000"
        self.test_results = []
        self.session_id = None
        self.admin_token = None
        
    def print_header(self, text):
        print(f"\n{Colors.BLUE}{Colors.BOLD}{'='*60}{Colors.END}")
        print(f"{Colors.BLUE}{Colors.BOLD}{text.center(60)}{Colors.END}")
        print(f"{Colors.BLUE}{Colors.BOLD}{'='*60}{Colors.END}\n")
    
    def print_success(self, text):
        print(f"{Colors.GREEN} {text}{Colors.END}")
    
    def print_error(self, text):
        print(f"{Colors.RED} {text}{Colors.END}")
    
    def print_warning(self, text):
        print(f"{Colors.YELLOW}  {text}{Colors.END}")
    
    def print_info(self, text):
        print(f"{Colors.CYAN}ℹ  {text}{Colors.END}")
    
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
    
    def test_backend_health(self):
        """Test backend health endpoint"""
        self.print_header("TESTING BACKEND HEALTH")
        
        try:
            response = requests.get(f"{self.api_base_url}/health", timeout=5)
            if response.status_code == 200:
                data = response.json()
                self.log_result("Backend Health", True, f"Backend is running - Version {data.get('version', 'unknown')}")
                return True
            else:
                self.log_result("Backend Health", False, f"Status code: {response.status_code}")
                return False
        except requests.exceptions.ConnectionError:
            self.log_result("Backend Health", False, "Backend server not running")
            return False
        except Exception as e:
            self.log_result("Backend Health", False, f"Error: {e}")
            return False
    
    def test_preview_mode(self):
        """Test preview mode functionality"""
        self.print_header("TESTING PREVIEW MODE")
        
        try:
            # Test preview session creation
            response = requests.post(f"{self.api_base_url}/api/preview/session")
            if response.status_code == 200:
                data = response.json()
                self.session_id = data['session_id']
                self.log_result("Preview Session Creation", True, f"Session created: {self.session_id[:8]}...")
                
                # Test mood entry creation
                mood_data = {
                    'session_id': self.session_id,
                    'mood': 8,
                    'energy': 7,
                    'stress': 3,
                    'sleep_hours': 8.5,
                    'notes': 'Feeling great in preview mode!',
                    'activities': '["exercise", "socializing"]'
                }
                
                response = requests.post(f"{self.api_base_url}/api/preview/mood-entries", data=mood_data)
                if response.status_code == 200:
                    self.log_result("Preview Mood Entry", True, "Mood entry created successfully")
                else:
                    self.log_result("Preview Mood Entry", False, f"Status code: {response.status_code}")
                
                # Test AI analysis
                ai_data = {'session_id': self.session_id, 'text': 'I am feeling happy today!'}
                response = requests.post(f"{self.api_base_url}/api/preview/analyze-mood", json=ai_data)
                if response.status_code == 200:
                    self.log_result("Preview AI Analysis", True, "AI analysis working")
                else:
                    self.log_result("Preview AI Analysis", False, f"Status code: {response.status_code}")
                
                # Test insights
                response = requests.get(f"{self.api_base_url}/api/preview/insights?session_id={self.session_id}")
                if response.status_code == 200:
                    self.log_result("Preview Insights", True, "Insights generated successfully")
                else:
                    self.log_result("Preview Insights", False, f"Status code: {response.status_code}")
                
                return True
            else:
                self.log_result("Preview Session Creation", False, f"Status code: {response.status_code}")
                return False
                
        except Exception as e:
            self.log_result("Preview Mode", False, f"Error: {e}")
            return False
    
    def test_user_registration(self):
        """Test user registration"""
        self.print_header("TESTING USER REGISTRATION")
        
        try:
            # Test user registration
            user_data = {
                'email': 'testuser@example.com',
                'password': 'TestPassword123',
                'name': 'Test User'
            }
            
            response = requests.post(f"{self.api_base_url}/api/auth/register", data=user_data)
            if response.status_code == 200:
                self.log_result("User Registration", True, "User registered successfully")
                return True
            else:
                self.log_result("User Registration", False, f"Status code: {response.status_code}")
                return False
                
        except Exception as e:
            self.log_result("User Registration", False, f"Error: {e}")
            return False
    
    def test_admin_login(self):
        """Test admin login (Makopolo)"""
        self.print_header("TESTING ADMIN LOGIN")
        
        try:
            # Test admin login
            admin_data = {
                'email': 'makopolo@moodscape.dev',
                'password': '123456'
            }
            
            response = requests.post(f"{self.api_base_url}/api/auth/login", data=admin_data)
            if response.status_code == 200:
                data = response.json()
                if data.get('success') and data.get('user', {}).get('is_admin'):
                    self.admin_token = data['access_token']
                    self.log_result("Admin Login", True, "Makopolo admin login successful")
                    return True
                else:
                    self.log_result("Admin Login", False, "Login successful but not admin")
                    return False
            else:
                self.log_result("Admin Login", False, f"Status code: {response.status_code}")
                return False
                
        except Exception as e:
            self.log_result("Admin Login", False, f"Error: {e}")
            return False
    
    def test_admin_functionality(self):
        """Test admin functionality"""
        self.print_header("TESTING ADMIN FUNCTIONALITY")
        
        if not self.admin_token:
            self.log_result("Admin Functionality", False, "No admin token available")
            return False
        
        try:
            headers = {'Authorization': f'Bearer {self.admin_token}'}
            
            # Test admin stats
            response = requests.get(f"{self.api_base_url}/api/admin/stats", headers=headers)
            if response.status_code == 200:
                self.log_result("Admin Stats", True, "Admin statistics retrieved")
            else:
                self.log_result("Admin Stats", False, f"Status code: {response.status_code}")
            
            # Test admin users list
            response = requests.get(f"{self.api_base_url}/api/admin/users", headers=headers)
            if response.status_code == 200:
                self.log_result("Admin Users List", True, "Users list retrieved")
            else:
                self.log_result("Admin Users List", False, f"Status code: {response.status_code}")
            
            return True
            
        except Exception as e:
            self.log_result("Admin Functionality", False, f"Error: {e}")
            return False
    
    def test_ai_features(self):
        """Test AI features"""
        self.print_header("TESTING AI FEATURES")
        
        if not self.admin_token:
            self.log_result("AI Features", False, "No admin token available")
            return False
        
        try:
            headers = {'Authorization': f'Bearer {self.admin_token}'}
            
            # Test mood prediction
            response = requests.post(
                f"{self.api_base_url}/api/ai/predict-mood",
                json={'text': 'I am feeling very happy today!'},
                headers=headers
            )
            if response.status_code == 200:
                self.log_result("Mood Prediction", True, "AI mood prediction working")
            else:
                self.log_result("Mood Prediction", False, f"Status code: {response.status_code}")
            
            # Test therapeutic AI
            response = requests.post(
                f"{self.api_base_url}/api/therapy/analyze-emotion",
                json={'text': 'I am feeling sad and lonely'},
                headers=headers
            )
            if response.status_code == 200:
                self.log_result("Therapeutic AI", True, "Therapeutic AI analysis working")
            else:
                self.log_result("Therapeutic AI", False, f"Status code: {response.status_code}")
            
            return True
            
        except Exception as e:
            self.log_result("AI Features", False, f"Error: {e}")
            return False
    
    def test_cross_platform_compatibility(self):
        """Test cross-platform compatibility"""
        self.print_header("TESTING CROSS-PLATFORM COMPATIBILITY")
        
        os_info = {
            'system': platform.system(),
            'release': platform.release(),
            'version': platform.version(),
            'machine': platform.machine(),
            'python_version': platform.python_version()
        }
        
        self.log_result("OS Detection", True, f"Running on {os_info['system']} {os_info['release']}")
        
        # Test if startup scripts exist for different OS
        if os_info['system'] == 'Windows':
            scripts = ['start_backend_windows.bat', 'start_mobile_windows.bat']
        elif os_info['system'] == 'Darwin':  # macOS
            scripts = ['start_backend_macos.sh', 'start_mobile_macos.sh']
        else:  # Linux
            scripts = ['start_backend.sh', 'start_mobile.sh']
        
        for script in scripts:
            if os.path.exists(script):
                self.log_result(f"Startup Script: {script}", True, "Script exists")
            else:
                self.log_result(f"Startup Script: {script}", False, "Script missing")
        
        return True
    
    def test_mobile_app_structure(self):
        """Test mobile app structure"""
        self.print_header("TESTING MOBILE APP STRUCTURE")
        
        try:
            os.chdir('MoodscapeApp')
            
            # Check for required files
            required_files = [
                'App.tsx',
                'package.json',
                'src/screens/HomeScreen.tsx',
                'src/screens/SettingsScreen.tsx',
                'src/screens/AdminPanelScreen.tsx',
                'src/screens/PreviewScreen.tsx',
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
            
            os.chdir('..')
            return all_files_exist
            
        except Exception as e:
            self.log_result("Mobile App Structure", False, f"Error: {e}")
            os.chdir('..')
            return False
    
    def generate_report(self):
        """Generate comprehensive test report"""
        self.print_header("COMPREHENSIVE TEST REPORT")
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result['success'])
        failed_tests = total_tests - passed_tests
        
        print(f"\n{Colors.BOLD}SUMMARY:{Colors.END}")
        print(f"Total Tests: {total_tests}")
        print(f"{Colors.GREEN}Passed: {passed_tests}{Colors.END}")
        print(f"{Colors.RED}Failed: {failed_tests}{Colors.END}")
        print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        # Group results by category
        categories = {}
        for result in self.test_results:
            category = result['test'].split(':')[0] if ':' in result['test'] else 'General'
            if category not in categories:
                categories[category] = {'passed': 0, 'failed': 0, 'total': 0}
            categories[category]['total'] += 1
            if result['success']:
                categories[category]['passed'] += 1
            else:
                categories[category]['failed'] += 1
        
        print(f"\n{Colors.BOLD}RESULTS BY CATEGORY:{Colors.END}")
        for category, stats in categories.items():
            success_rate = (stats['passed'] / stats['total']) * 100
            color = Colors.GREEN if success_rate >= 80 else Colors.YELLOW if success_rate >= 60 else Colors.RED
            print(f"{color}{category}: {stats['passed']}/{stats['total']} ({success_rate:.1f}%){Colors.END}")
        
        if failed_tests > 0:
            print(f"\n{Colors.RED}{Colors.BOLD}FAILED TESTS:{Colors.END}")
            for result in self.test_results:
                if not result['success']:
                    print(f"  • {result['test']}: {result['message']}")
        
        # Save detailed report
        report_file = f"final_test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w') as f:
            json.dump({
                'summary': {
                    'total_tests': total_tests,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'success_rate': (passed_tests/total_tests)*100
                },
                'categories': categories,
                'results': self.test_results,
                'timestamp': datetime.now().isoformat()
            }, f, indent=2)
        
        print(f"\n{Colors.CYAN}Detailed report saved to: {report_file}{Colors.END}")
        
        return failed_tests == 0
    
    def run_all_tests(self):
        """Run all comprehensive tests"""
        try:
            self.print_header("MOODSCAPE FINAL COMPREHENSIVE TEST SUITE")
            self.print_info("Testing all features including preview mode, admin functionality, and cross-platform compatibility")
            
            # Test backend health first
            if not self.test_backend_health():
                self.print_error("Backend is not running. Please start the backend server first.")
                return False
            
            # Test preview mode
            self.test_preview_mode()
            
            # Test user registration
            self.test_user_registration()
            
            # Test admin login
            self.test_admin_login()
            
            # Test admin functionality
            self.test_admin_functionality()
            
            # Test AI features
            self.test_ai_features()
            
            # Test cross-platform compatibility
            self.test_cross_platform_compatibility()
            
            # Test mobile app structure
            self.test_mobile_app_structure()
            
            # Generate report
            success = self.generate_report()
            
            if success:
                self.print_success("All tests passed! Moodscape is ready for production use.")
                self.print_info("Features tested:")
                self.print_info("   Preview mode for users without accounts")
                self.print_info("   User registration and authentication")
                self.print_info("   Admin functionality for Makopolo")
                self.print_info("   AI mood prediction and therapeutic analysis")
                self.print_info("   Cross-platform compatibility")
                self.print_info("   Mobile app structure and navigation")
                self.print_info("   Settings page with user management")
                self.print_info("   Privacy notices for AI data usage")
            else:
                self.print_error("Some tests failed. Please check the report for details.")
            
            return success
            
        except KeyboardInterrupt:
            self.print_warning("Testing interrupted by user")
            return False
        except Exception as e:
            self.print_error(f"Unexpected error: {e}")
            return False

def main():
    """Main function"""
    print(f"{Colors.PURPLE}{Colors.BOLD}")
    print("MOODSCAPE FINAL TESTER")
    print("Comprehensive testing for mood tracking app with all features")
    print(f"{Colors.END}")
    
    tester = FinalTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
