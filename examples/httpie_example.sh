#!/bin/bash

# MLOps Demo API HTTPie Examples
# Make sure the API server is running: python predict_api.py
# Install HTTPie: pip install httpie

echo "MLOps Demo API HTTPie Examples"
echo "=============================="

# Check if API is running
echo "1. Checking API health..."
http GET localhost:8000/ || { echo "Error: API not running. Please start with: python predict_api.py"; exit 1; }

echo -e "\n2. Testing JSON prediction..."
# Predict with JSON data (send as raw JSON list via pipe)
echo '[{"session_duration":130,"page_views":6,"clicks":9,"scroll_depth":80,"time_on_site":190}]' | http POST localhost:8000/predict_batch

echo -e "\n3. Testing CSV prediction..."
# Create test CSV file
echo "session_duration,page_views,clicks,scroll_depth,time_on_site
130,6,9,80,190
50,2,3,35,65
170,7,11,85,210" > test.csv

# Predict with CSV file
http -f POST localhost:8000/predict file@test.csv

echo -e "\n4. Testing batch JSON prediction..."
# Multiple records (send as raw JSON list via pipe)
echo '[{"session_duration":130,"page_views":6,"clicks":9,"scroll_depth":80,"time_on_site":190},{"session_duration":50,"page_views":2,"clicks":3,"scroll_depth":35,"time_on_site":65},{"session_duration":170,"page_views":7,"clicks":11,"scroll_depth":85,"time_on_site":210}]' | http POST localhost:8000/predict_batch

echo -e "\n5. Cleaning up..."
rm -f test.csv

echo "Done!"