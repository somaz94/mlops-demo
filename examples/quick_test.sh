#!/bin/bash

# MLOps Demo API Quick Test
echo "MLOps Demo API Quick Test"
echo "========================"

# Check if API is running
echo "1. Checking API health..."
curl -s http://localhost:8000/ > /dev/null || { echo "Error: API not running. Please start with: python predict_api.py"; exit 1; }

echo "2. Creating test file and running prediction..."
echo "session_duration,page_views,clicks,scroll_depth,time_on_site
130,6,9,80,190" > test.csv && \
curl -X POST "http://localhost:8000/predict" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@test.csv"

echo -e "\n3. Testing JSON prediction..."
curl -X POST "http://localhost:8000/predict_batch" \
     -H "accept: application/json" \
     -H "Content-Type: application/json" \
     -d '[{"session_duration": 130, "page_views": 6, "clicks": 9, "scroll_depth": 80, "time_on_site": 190}]'

echo -e "\n4. Cleaning up..."
rm -f test.csv

echo -e "\nDone!" 