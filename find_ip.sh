#!/bin/bash

# Script to find your computer's IP address for mobile development
echo "Finding your computer's IP address..."
echo ""

# Get the IP address
IP=$(hostname -I | awk '{print $1}')

echo "Your computer's IP address is: $IP"
echo ""
echo "To use this with Expo Go:"
echo "1. Make sure your phone and computer are on the same WiFi network"
echo "2. Update the IP address in MoodscapeApp/src/config/api.ts"
echo "3. Replace '192.168.0.102' with '$IP'"
echo ""
echo "Current API configuration:"
echo "API_BASE_URL = 'http://$IP:8000'"
echo ""
echo "You can also run this command to update it automatically:"
echo "sed -i \"s/192.168.0.102/$IP/g\" MoodscapeApp/src/config/api.ts"
