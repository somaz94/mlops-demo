# MLOps Demo API Examples

This directory contains various examples for testing and using the MLOps Demo API.

## Quick Start

1. **Install example dependencies**:
   ```bash
   pip install -r examples/requirements.txt
   ```

2. **Start the API server** (from project root):
   ```bash
   python predict_api.py
   ```

3. **Run examples**:
   ```bash
   # Python example
   python examples/python_example.py
   
   # Quick test
   ./examples/quick_test.sh
   
   # HTTPie example (requires httpie installation)
   ./examples/httpie_example.sh
   ```

## Available Examples

### 1. Python Example (`python_example.py`)
- Complete Python script with error handling
- Tests both CSV and JSON endpoints
- Includes API health check
- **Usage**: `python examples/python_example.py`

### 2. Web Interface (`web_example.html`, `web_example.js`)
- Interactive web interface for API testing
- File upload for CSV prediction
- JSON data input for batch prediction
- Real-time results display
- **Usage**: Open `examples/web_example.html` in a web browser

### 3. Postman Collection (`postman_collection.json`)
- Import into Postman for API testing
- Pre-configured requests for all endpoints
- Ready-to-use test data
- **Usage**: Import into Postman application

### 4. Shell Scripts
- **`quick_test.sh`**: Fast test with curl commands
- **`httpie_example.sh`**: HTTPie-based testing (requires httpie)

## Installation Requirements

### Required
- Python 3.8+
- requests library: `pip install requests`

### Optional
- **HTTPie**: `pip install httpie` (for httpie_example.sh)
- **Postman**: Download from [postman.com](https://www.postman.com/)
- **Web browser**: For web_example.html

## Test Data

All examples use the same test data structure:
```json
{
  "session_duration": 130,
  "page_views": 6,
  "clicks": 9,
  "scroll_depth": 80,
  "time_on_site": 190
}
```

## Troubleshooting

1. **API not running**: Start with `python predict_api.py`
2. **Port conflicts**: Change port in examples if needed
3. **CORS issues**: Use web_example.html locally
4. **File not found**: Ensure you're running from project root

## Example Output

Successful prediction response:
```json
{
  "predictions": [1],
  "probabilities": [[0.0, 1.0]]
}
``` 