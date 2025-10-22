# Expo QR Code Troubleshooting Guide

## Common QR Code Issues & Solutions

### Issue 1: QR Code Not Appearing
**Symptoms**: No QR code displayed in terminal
**Solutions**:
1. **Restart Expo with tunnel mode**:
   ```bash
   cd MoodscapeApp
   npx expo start --tunnel
   ```

2. **Clear Expo cache**:
   ```bash
   npx expo r -c
   ```

3. **Check network connectivity**:
   ```bash
   ping google.com
   ```

### Issue 2: QR Code Not Scannable
**Symptoms**: QR code appears but Expo Go can't scan it
**Solutions**:
1. **Use tunnel mode** (recommended):
   ```bash
   npx expo start --tunnel
   ```

2. **Check firewall settings**:
   - Ensure port 19000-19006 are open
   - Disable VPN if active

3. **Try different network**:
   - Switch to mobile hotspot
   - Use same WiFi network for both devices

### Issue 3: "Couldn't connect to development server"
**Symptoms**: Expo Go shows connection error
**Solutions**:
1. **Use tunnel mode**:
   ```bash
   npx expo start --tunnel
   ```

2. **Check backend server**:
   ```bash
   curl http://localhost:8000/health
   ```

3. **Restart both servers**:
   ```bash
   # Stop all processes
   pkill -f expo
   pkill -f python
   
   # Restart backend
   cd backend && source venv/bin/activate && python3 app/simple_main.py &
   
   # Restart mobile app
   cd MoodscapeApp && npx expo start --tunnel
   ```

## Alternative Access Methods

### Method 1: Web Browser (Recommended)
1. **Start the app**:
   ```bash
   cd MoodscapeApp
   npx expo start --web
   ```

2. **Access via browser**:
   - Open http://localhost:19006
   - Works on any device with a browser

### Method 2: Direct URL Access
1. **Get the development URL**:
   ```bash
   npx expo start --tunnel
   ```

2. **Look for output like**:
   ```
   › Metro waiting on exp://192.168.1.100:19000
   › Scan the QR code above with Expo Go (Android) or the Camera app (iOS)
   ```

3. **Use the URL directly**:
   - Copy the `exp://` URL
   - Paste in Expo Go app

### Method 3: Local Network Access
1. **Start with LAN mode**:
   ```bash
   npx expo start --lan
   ```

2. **Find your IP address**:
   ```bash
   ip addr show | grep inet
   ```

3. **Access via IP**:
   - Use the IP address shown in terminal
   - Format: `exp://YOUR_IP:19000`

## Platform-Specific Solutions

### Android
1. **Install Expo Go**:
   - Download from Google Play Store
   - Ensure latest version

2. **Enable developer options**:
   - Go to Settings > About Phone
   - Tap "Build Number" 7 times
   - Enable "USB Debugging"

3. **Check network**:
   - Ensure both devices on same WiFi
   - Disable mobile data

### iOS
1. **Install Expo Go**:
   - Download from App Store
   - Ensure latest version

2. **Use Camera app**:
   - Open Camera app
   - Point at QR code
   - Tap notification when it appears

3. **Check network**:
   - Ensure both devices on same WiFi
   - Disable cellular data

## Network Troubleshooting

### Check Ports
```bash
# Check if ports are open
netstat -tulpn | grep :19000
netstat -tulpn | grep :19006
netstat -tulpn | grep :8000
```

### Firewall Issues
```bash
# Linux - Check firewall status
sudo ufw status

# Linux - Allow Expo ports
sudo ufw allow 19000:19006/tcp
sudo ufw allow 8000/tcp
```

### Network Configuration
```bash
# Check network interfaces
ip addr show

# Test connectivity
ping 8.8.8.8
ping google.com
```

## Development Server Commands

### Start with Different Modes
```bash
# Standard mode
npx expo start

# Tunnel mode (recommended for QR issues)
npx expo start --tunnel

# LAN mode
npx expo start --lan

# Web mode
npx expo start --web

# Clear cache and start
npx expo start -c
```

### Debug Mode
```bash
# Start with debug logs
npx expo start --verbose

# Check Expo CLI version
npx expo --version

# Update Expo CLI
npm install -g @expo/cli@latest
```

## Quick Fixes

### Complete Reset
```bash
# Stop all processes
pkill -f expo
pkill -f python
pkill -f node

# Clear all caches
cd MoodscapeApp
rm -rf node_modules
npm cache clean --force
npm install

# Clear Expo cache
npx expo r -c

# Restart everything
cd ../backend
source venv/bin/activate
python3 app/simple_main.py &

cd ../MoodscapeApp
npx expo start --tunnel
```

### Verify Installation
```bash
# Check Node.js version
node --version

# Check npm version
npm --version

# Check Expo CLI
npx expo --version

# Check React Native
npx react-native --version
```

## Still Having Issues?

### Use Web Version
The web version is the most reliable alternative:
```bash
cd MoodscapeApp
npx expo start --web
```
Then open http://localhost:19006 in your browser.

### Contact Support
If issues persist:
1. Check the terminal output for error messages
2. Try the web version first
3. Ensure all dependencies are installed
4. Check network connectivity

---
*Last Updated: October 2024*
