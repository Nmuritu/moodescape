#!/bin/bash

# Script to automatically update the app's IP address configuration
echo "🔍 Detecting machine IP address..."

# Get the primary IP address
IP=$(hostname -I | awk '{print $1}')

if [ -z "$IP" ]; then
    echo "❌ Could not detect IP address"
    exit 1
fi

echo "✅ Found IP address: $IP"

# Update the API configuration
echo "📝 Updating API configuration..."
sed -i "s/192.168.0.102/$IP/g" MoodscapeApp/src/config/api.ts

# Update the find_ip.sh script
echo "📝 Updating helper script..."
sed -i "s/192.168.0.102/$IP/g" find_ip.sh

# Create/update .env file for Expo
echo "📝 Creating .env file..."
cat > MoodscapeApp/.env << EOF
EXPO_PUBLIC_MACHINE_IP=$IP
EOF

echo "✅ Configuration updated successfully!"
echo ""
echo "📱 Your app is now configured to use: http://$IP:8000"
echo ""
echo "🚀 You can now:"
echo "   1. Start the backend: cd backend && python3 app/simple_main.py"
echo "   2. Start the mobile app: cd MoodscapeApp && npx expo start"
echo "   3. Scan the QR code with Expo Go"
echo ""
echo "🌐 Make sure your phone and computer are on the same WiFi network!"
