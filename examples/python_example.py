#!/usr/bin/env python3
"""
Python example for MLOps Demo API usage
"""

import requests
import json

def predict_with_csv():
    """Predict using CSV file"""
    try:
        with open('data/test.csv', 'rb') as f:
            files = {'file': f}
            response = requests.post('http://localhost:8000/predict', files=files)
            print("CSV Prediction Result:")
            print(json.dumps(response.json(), indent=2))
    except FileNotFoundError:
        print("Error: data/test.csv not found. Please run from project root directory.")
    except Exception as e:
        print(f"Error: {e}")

def predict_with_json():
    """Predict using JSON data"""
    try:
        data = [
            {"session_duration": 130, "page_views": 6, "clicks": 9, "scroll_depth": 80, "time_on_site": 190},
            {"session_duration": 50, "page_views": 2, "clicks": 3, "scroll_depth": 35, "time_on_site": 65},
            {"session_duration": 170, "page_views": 7, "clicks": 11, "scroll_depth": 85, "time_on_site": 210}
        ]
        response = requests.post('http://localhost:8000/predict_batch', json=data)
        print("JSON Prediction Result:")
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print(f"Error: {e}")

def check_api_health():
    """Check if API is running"""
    try:
        response = requests.get('http://localhost:8000/')
        print("API Health Check:")
        print(response.json())
        return True
    except Exception as e:
        print(f"API not available: {e}")
        return False

if __name__ == "__main__":
    print("MLOps Demo API Python Examples")
    print("=" * 40)
    
    # Check API health first
    if check_api_health():
        print("\n" + "=" * 40)
        
        # Test JSON prediction (works without files)
        predict_with_json()
        
        print("\n" + "=" * 40)
        
        # Test CSV prediction (requires data/test.csv)
        predict_with_csv()
    else:
        print("Please start the API server first:")
        print("python predict_api.py") 