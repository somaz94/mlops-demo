// JavaScript functions for MLOps Demo API

const API_BASE_URL = 'http://localhost:8000';

// Display result in the result div
function displayResult(title, data, isError = false) {
    const resultDiv = document.getElementById('result');
    const timestamp = new Date().toLocaleTimeString();
    const status = isError ? 'ERROR' : 'SUCCESS';
    
    resultDiv.innerHTML += `\n[${timestamp}] ${status}: ${title}\n`;
    resultDiv.innerHTML += JSON.stringify(data, null, 2) + '\n\n';
    resultDiv.scrollTop = resultDiv.scrollHeight;
}

// Check API health
async function checkHealth() {
    const resultDiv = document.getElementById('healthResult');
    
    try {
        const response = await fetch(`${API_BASE_URL}/`);
        const data = await response.json();
        
        resultDiv.innerHTML = `<div class="status success">API is running: ${data.message}</div>`;
        displayResult('Health Check', data);
    } catch (error) {
        resultDiv.innerHTML = `<div class="status error">API not available: ${error.message}</div>`;
        displayResult('Health Check Error', { error: error.message }, true);
    }
}

// Predict with CSV file
async function predictCSV() {
    const fileInput = document.getElementById('fileInput');
    const resultDiv = document.getElementById('csvResult');
    
    if (!fileInput.files[0]) {
        resultDiv.innerHTML = '<div class="status error">Please select a CSV file first</div>';
        return;
    }
    
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    
    try {
        const response = await fetch(`${API_BASE_URL}/predict`, {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        resultDiv.innerHTML = '<div class="status success">CSV prediction successful</div>';
        displayResult('CSV Prediction', data);
    } catch (error) {
        resultDiv.innerHTML = `<div class="status error">CSV prediction failed: ${error.message}</div>`;
        displayResult('CSV Prediction Error', { error: error.message }, true);
    }
}

// Predict with JSON data
async function predictJSON() {
    const resultDiv = document.getElementById('jsonResult');
    
    const testData = [
        {
            "session_duration": 130,
            "page_views": 6,
            "clicks": 9,
            "scroll_depth": 80,
            "time_on_site": 190
        },
        {
            "session_duration": 50,
            "page_views": 2,
            "clicks": 3,
            "scroll_depth": 35,
            "time_on_site": 65
        },
        {
            "session_duration": 170,
            "page_views": 7,
            "clicks": 11,
            "scroll_depth": 85,
            "time_on_site": 210
        }
    ];
    
    try {
        const response = await fetch(`${API_BASE_URL}/predict_batch`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(testData)
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        resultDiv.innerHTML = '<div class="status success">JSON prediction successful</div>';
        displayResult('JSON Prediction', data);
    } catch (error) {
        resultDiv.innerHTML = `<div class="status error">JSON prediction failed: ${error.message}</div>`;
        displayResult('JSON Prediction Error', { error: error.message }, true);
    }
}

// Auto-check health when page loads
document.addEventListener('DOMContentLoaded', function() {
    checkHealth();
}); 