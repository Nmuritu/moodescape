#!/usr/bin/env python3
"""
Cross-platform test script for Moodscape application
Tests the application on Windows, macOS, and Linux
"""

import os
import sys
import platform
import subprocess
import requests
import time
import json
from datetime import datetime

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

class CrossPlatformTester:
    def __init__(self):
        self.os_name = platform.system().lower()
        self.arch = platform.machine().lower()
        self.test_results = []
        
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
            'os': self.os_name,
            'arch': self.arch,
            'timestamp': datetime.now().isoformat()
        })
        
        if success:
            self.print_success(f"{test_name}: {message}")
        else:
            self.print_error(f"{test_name}: {message}")
    
    def detect_os(self):
        """Detect the current operating system"""
        self.print_header("DETECTING OPERATING SYSTEM")
        
        os_info = {
            'system': platform.system(),
            'release': platform.release(),
            'version': platform.version(),
            'machine': platform.machine(),
            'processor': platform.processor(),
            'python_version': platform.python_version()
        }
        
        self.print_info(f"Operating System: {os_info['system']} {os_info['release']}")
        self.print_info(f"Architecture: {os_info['machine']}")
        self.print_info(f"Python Version: {os_info['python_version']}")
        
        self.log_result("OS Detection", True, f"Running on {os_info['system']} {os_info['release']}")
        return os_info
    
    def check_dependencies(self):
        """Check if required dependencies are installed"""
        self.print_header("CHECKING DEPENDENCIES")
        
        # Check Python
        try:
            result = subprocess.run(['python3', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                self.log_result("Python Check", True, f"Python {result.stdout.strip()}")
            else:
                # Try python command on Windows
                result = subprocess.run(['python', '--version'], capture_output=True, text=True)
                if result.returncode == 0:
                    self.log_result("Python Check", True, f"Python {result.stdout.strip()}")
                else:
                    self.log_result("Python Check", False, "Python not found")
                    return False
        except FileNotFoundError:
            self.log_result("Python Check", False, "Python not found")
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
        
        # Check npm
        try:
            result = subprocess.run(['npm', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                self.log_result("npm Check", True, f"npm {result.stdout.strip()}")
            else:
                self.log_result("npm Check", False, "npm not found")
                return False
        except FileNotFoundError:
            self.log_result("npm Check", False, "npm not found")
            return False
        
        return True
    
    def test_backend_setup(self):
        """Test backend setup on current OS"""
        self.print_header("TESTING BACKEND SETUP")
        
        try:
            # Navigate to backend directory
            os.chdir('backend')
            
            # Test Python virtual environment creation
            if self.os_name == 'windows':
                venv_cmd = ['python', '-m', 'venv', 'venv']
                activate_cmd = 'venv\\Scripts\\activate.bat'
                pip_cmd = 'venv\\Scripts\\pip'
                python_cmd = 'venv\\Scripts\\python'
            else:
                venv_cmd = ['python3', '-m', 'venv', 'venv']
                activate_cmd = 'source venv/bin/activate'
                pip_cmd = 'venv/bin/pip'
                python_cmd = 'venv/bin/python'
            
            # Create virtual environment
            if not os.path.exists('venv'):
                result = subprocess.run(venv_cmd, capture_output=True, text=True)
                if result.returncode == 0:
                    self.log_result("Virtual Environment", True, "Created successfully")
                else:
                    self.log_result("Virtual Environment", False, f"Creation failed: {result.stderr}")
                    return False
            else:
                self.log_result("Virtual Environment", True, "Already exists")
            
            # Test pip installation
            result = subprocess.run([pip_cmd, 'install', 'fastapi', 'uvicorn'], capture_output=True, text=True)
            if result.returncode == 0:
                self.log_result("Dependencies Installation", True, "FastAPI and Uvicorn installed")
            else:
                self.log_result("Dependencies Installation", False, f"Installation failed: {result.stderr}")
                return False
            
            # Test Python import
            result = subprocess.run([python_cmd, '-c', 'import fastapi; print("FastAPI imported successfully")'], capture_output=True, text=True)
            if result.returncode == 0:
                self.log_result("Python Import Test", True, "FastAPI can be imported")
            else:
                self.log_result("Python Import Test", False, f"Import failed: {result.stderr}")
                return False
            
            os.chdir('..')
            return True
            
        except Exception as e:
            self.log_result("Backend Setup", False, f"Error: {e}")
            os.chdir('..')
            return False
    
    def test_mobile_setup(self):
        """Test mobile app setup on current OS"""
        self.print_header("TESTING MOBILE APP SETUP")
        
        try:
            # Navigate to mobile app directory
            os.chdir('MoodscapeApp')
            
            # Test npm install
            result = subprocess.run(['npm', 'install'], capture_output=True, text=True)
            if result.returncode == 0:
                self.log_result("npm Install", True, "Dependencies installed successfully")
            else:
                self.log_result("npm Install", False, f"Installation failed: {result.stderr}")
                return False
            
            # Test Expo CLI installation
            result = subprocess.run(['npx', 'expo', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                self.log_result("Expo CLI", True, f"Expo CLI available: {result.stdout.strip()}")
            else:
                self.log_result("Expo CLI", False, "Expo CLI not available")
                return False
            
            # Test TypeScript compilation
            result = subprocess.run(['npx', 'tsc', '--noEmit'], capture_output=True, text=True)
            if result.returncode == 0:
                self.log_result("TypeScript Compilation", True, "No compilation errors")
            else:
                self.log_result("TypeScript Compilation", False, f"Compilation errors: {result.stderr}")
            
            os.chdir('..')
            return True
            
        except Exception as e:
            self.log_result("Mobile Setup", False, f"Error: {e}")
            os.chdir('..')
            return False
    
    def test_preview_mode(self):
        """Test preview mode functionality"""
        self.print_header("TESTING PREVIEW MODE")
        
        try:
            # Test preview session creation
            response = requests.post('http://localhost:8000/api/preview/session', timeout=5)
            if response.status_code == 200:
                data = response.json()
                if 'session_id' in data:
                    self.log_result("Preview Session Creation", True, "Session created successfully")
                    session_id = data['session_id']
                    
                    # Test mood entry creation
                    mood_data = {
                        'session_id': session_id,
                        'mood': 8,
                        'energy': 7,
                        'stress': 3,
                        'sleep_hours': 8.5,
                        'notes': 'Feeling great!',
                        'activities': '["exercise", "socializing"]'
                    }
                    
                    response = requests.post('http://localhost:8000/api/preview/mood-entries', data=mood_data, timeout=5)
                    if response.status_code == 200:
                        self.log_result("Preview Mood Entry", True, "Mood entry created successfully")
                    else:
                        self.log_result("Preview Mood Entry", False, f"Status code: {response.status_code}")
                    
                    # Test AI analysis
                    ai_data = {'session_id': session_id, 'text': 'I am feeling happy today!'}
                    response = requests.post('http://localhost:8000/api/preview/analyze-mood', json=ai_data, timeout=5)
                    if response.status_code == 200:
                        self.log_result("Preview AI Analysis", True, "AI analysis working")
                    else:
                        self.log_result("Preview AI Analysis", False, f"Status code: {response.status_code}")
                    
                    # Test insights
                    response = requests.get(f'http://localhost:8000/api/preview/insights?session_id={session_id}', timeout=5)
                    if response.status_code == 200:
                        self.log_result("Preview Insights", True, "Insights generated successfully")
                    else:
                        self.log_result("Preview Insights", False, f"Status code: {response.status_code}")
                    
                else:
                    self.log_result("Preview Session Creation", False, "Invalid response format")
            else:
                self.log_result("Preview Session Creation", False, f"Status code: {response.status_code}")
            
            return True
            
        except requests.exceptions.ConnectionError:
            self.log_result("Preview Mode Test", False, "Backend server not running")
            return False
        except Exception as e:
            self.log_result("Preview Mode Test", False, f"Error: {e}")
            return False
    
    def test_os_specific_features(self):
        """Test OS-specific features"""
        self.print_header("TESTING OS-SPECIFIC FEATURES")
        
        if self.os_name == 'windows':
            # Test Windows batch files
            if os.path.exists('start_backend_windows.bat'):
                self.log_result("Windows Batch Files", True, "Backend batch file exists")
            else:
                self.log_result("Windows Batch Files", False, "Backend batch file missing")
            
            if os.path.exists('start_mobile_windows.bat'):
                self.log_result("Windows Batch Files", True, "Mobile batch file exists")
            else:
                self.log_result("Windows Batch Files", False, "Mobile batch file missing")
        
        elif self.os_name == 'darwin':  # macOS
            # Test macOS shell scripts
            if os.path.exists('start_backend_macos.sh'):
                self.log_result("macOS Shell Scripts", True, "Backend shell script exists")
            else:
                self.log_result("macOS Shell Scripts", False, "Backend shell script missing")
            
            if os.path.exists('start_mobile_macos.sh'):
                self.log_result("macOS Shell Scripts", True, "Mobile shell script exists")
            else:
                self.log_result("macOS Shell Scripts", False, "Mobile shell script missing")
        
        elif self.os_name == 'linux':
            # Test Linux shell scripts
            if os.path.exists('start_backend.sh'):
                self.log_result("Linux Shell Scripts", True, "Backend shell script exists")
            else:
                self.log_result("Linux Shell Scripts", False, "Backend shell script missing")
            
            if os.path.exists('start_mobile.sh'):
                self.log_result("Linux Shell Scripts", True, "Mobile shell script exists")
            else:
                self.log_result("Linux Shell Scripts", False, "Mobile shell script missing")
        
        return True
    
    def generate_report(self):
        """Generate cross-platform test report"""
        self.print_header("CROSS-PLATFORM TEST REPORT")
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result['success'])
        failed_tests = total_tests - passed_tests
        
        print(f"\n{Colors.BOLD}SUMMARY FOR {self.os_name.upper()}:{Colors.END}")
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
        report_file = f"test_report_{self.os_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w') as f:
            json.dump(self.test_results, f, indent=2)
        
        print(f"\n{Colors.CYAN}Detailed report saved to: {report_file}{Colors.END}")
        
        return failed_tests == 0
    
    def run_all_tests(self):
        """Run all cross-platform tests"""
        try:
            self.print_header("MOODSCAPE CROSS-PLATFORM TEST SUITE")
            self.print_info(f"Testing on: {platform.system()} {platform.release()}")
            
            # Detect OS
            self.detect_os()
            
            # Check dependencies
            if not self.check_dependencies():
                self.print_error("Dependency check failed. Please install required dependencies.")
                return False
            
            # Test backend setup
            if not self.test_backend_setup():
                self.print_error("Backend setup failed.")
                return False
            
            # Test mobile setup
            if not self.test_mobile_setup():
                self.print_error("Mobile setup failed.")
                return False
            
            # Test OS-specific features
            self.test_os_specific_features()
            
            # Test preview mode (if backend is running)
            self.test_preview_mode()
            
            # Generate report
            success = self.generate_report()
            
            if success:
                self.print_success("All tests passed! Application is ready to use on this platform.")
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
    print("🌙 MOODSCAPE CROSS-PLATFORM TESTER 🌙")
    print("Testing mood tracking app on different operating systems")
    print(f"{Colors.END}")
    
    tester = CrossPlatformTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
