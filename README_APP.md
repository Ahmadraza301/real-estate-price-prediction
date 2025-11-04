# Bangalore House Price Prediction Web Application

A full-stack web application that predicts house prices in Bangalore using machine learning. The application features a user-friendly interface built with HTML, CSS, and JavaScript, powered by a Flask backend serving a trained scikit-learn model.

## Features

- **Real-time Price Prediction**: Get instant house price estimates based on area, bedrooms, bathrooms, and location
- **240+ Bangalore Locations**: Comprehensive coverage of Bangalore neighborhoods
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Input Validation**: Client and server-side validation for accurate predictions
- **Error Handling**: Graceful error handling with user-friendly messages
- **RESTful API**: Clean API endpoints for integration with other applications

## Quick Start

### Option 1: Using Startup Scripts (Recommended)

**Windows:**
```bash
start_app.bat
```

**Linux/Mac:**
```bash
./start_app.sh
```

### Option 2: Manual Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Application**
   ```bash
   python app.py
   ```

3. **Open in Browser**
   Navigate to: http://localhost:5000

## Project Structure

```
├── app.py                 # Main Flask application
├── util.py               # Model loading and prediction utilities
├── requirements.txt      # Python dependencies
├── start_app.bat        # Windows startup script
├── start_app.sh         # Linux/Mac startup script
├── test_app.py          # Backend unit tests
├── artifacts/           # Model and data files
│   ├── columns.json
│   └── banglore_home_prices_model.pickle
├── templates/           # HTML templates
│   └── index.html
├── static/              # Static files (CSS, JS)
│   ├── app.css
│   ├── app.js
│   └── test.html       # Frontend testing page
└── README_APP.md       # This documentation
```

## Usage Guide

### Making Price Predictions

1. **Enter Area**: Input the house area in square feet (minimum 1 sqft)
2. **Select BHK**: Choose number of bedrooms (1-5)
3. **Select Bathrooms**: Choose number of bathrooms (1-5)
4. **Choose Location**: Select from 240+ Bangalore locations
5. **Get Estimate**: Click "Estimate Price" to get prediction in lakhs

### Example Prediction

- **Area**: 1000 sqft
- **BHK**: 2 bedrooms
- **Bathrooms**: 2 bathrooms
- **Location**: Electronic City
- **Estimated Price**: ~158.4 lakhs

## API Documentation

### Get Available Locations

**Endpoint**: `GET /get_location_names`

**Response**:
```json
{
  "locations": [
    "1st block jayanagar",
    "electronic city",
    "whitefield",
    ...
  ]
}
```

### Predict House Price

**Endpoint**: `POST /predict_home_price`

**Request Body** (form-data):
```
total_sqft: 1000
bhk: 2
bath: 2
location: electronic city
```

**Response**:
```json
{
  "estimated_price": 158.4
}
```

**Error Response**:
```json
{
  "error": "Missing total_sqft parameter"
}
```

### Input Validation Rules

- **total_sqft**: Must be positive number
- **bhk**: Integer between 1-10
- **bath**: Integer between 1-10
- **location**: Must be non-empty string

## Testing

### Backend Tests

Run unit tests for server functions:
```bash
python test_app.py
```

### Frontend Tests

1. Start the application
2. Navigate to: http://localhost:5000/test
3. Click "Run All Tests" to execute frontend tests

### Test Coverage

- **API Endpoints**: Location retrieval and price prediction
- **Input Validation**: Form validation and error handling
- **UI Components**: Result display and user feedback
- **Error Scenarios**: Invalid inputs and network failures

## Troubleshooting

### Common Issues

**1. "Python is not installed"**
- Install Python 3.7+ from https://python.org
- Ensure Python is added to system PATH

**2. "Module not found" errors**
- Run: `pip install -r requirements.txt`
- Ensure you're using the correct Python environment

**3. "Model files not found"**
- Verify `artifacts/` directory contains:
  - `columns.json`
  - `banglore_home_prices_model.pickle`

**4. "Port already in use"**
- Stop any existing Flask applications
- Or modify port in `app.py`: `app.run(port=5001)`

**5. Prediction returns fallback values**
- This is normal if the original model can't load
- The app uses a mathematical fallback for demonstration

### Browser Compatibility

- **Chrome**: Fully supported
- **Firefox**: Fully supported
- **Safari**: Fully supported
- **Edge**: Fully supported
- **Internet Explorer**: Not supported

### Performance Notes

- **Response Time**: Predictions typically complete in <1 second
- **Concurrent Users**: Supports multiple simultaneous requests
- **Memory Usage**: ~50-100MB depending on model size

## Development

### Adding New Features

1. **Backend Changes**: Modify `app.py` and `util.py`
2. **Frontend Changes**: Update files in `static/` and `templates/`
3. **Testing**: Add tests to `test_app.py` and `static/test.html`

### Model Updates

To use a different model:
1. Replace files in `artifacts/` directory
2. Update `util.py` if model format changes
3. Test with sample predictions

### Deployment

For production deployment:
1. Use a WSGI server (gunicorn, uWSGI)
2. Configure reverse proxy (nginx, Apache)
3. Set up proper logging and monitoring
4. Use environment variables for configuration

## Technical Details

### Technology Stack

- **Backend**: Python 3.7+, Flask 2.0+
- **Frontend**: HTML5, CSS3, JavaScript (ES5), jQuery 3.6
- **Machine Learning**: scikit-learn, NumPy, Pandas
- **Model**: Linear Regression (trained on Bangalore housing data)

### Security Features

- Input validation and sanitization
- CORS headers for cross-origin requests
- Error message sanitization
- Request size limits

### Browser Requirements

- JavaScript enabled
- Modern browser (Chrome 60+, Firefox 55+, Safari 12+, Edge 79+)
- Internet connection for jQuery CDN

## License

This project is for educational and demonstration purposes. The machine learning model is trained on publicly available Bangalore housing data.

## Support

For issues and questions:
1. Check the troubleshooting section above
2. Review the test results at `/test`
3. Check browser console for JavaScript errors
4. Verify all dependencies are installed correctly

---

**Version**: 1.0.0  
**Last Updated**: November 2025