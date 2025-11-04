# Design Document

## Overview

The House Price Prediction Web Application is a full-stack solution that combines a machine learning model with a web interface to provide real-time property price estimates for Bangalore. The system uses a client-server architecture with a Flask backend serving a trained scikit-learn model and an HTML/CSS/JavaScript frontend for user interaction.

## Architecture

### System Architecture
```
┌─────────────────┐    HTTP Requests    ┌─────────────────┐
│   Web Browser   │ ◄─────────────────► │  Flask Server   │
│  (Client Side)  │                     │  (Backend API)  │
└─────────────────┘                     └─────────────────┘
         │                                        │
         │                                        │
    ┌─────────┐                              ┌─────────┐
    │ Static  │                              │ ML Model│
    │ Files   │                              │ & Data  │
    │(HTML/CSS│                              │ Files   │
    │   /JS)  │                              │         │
    └─────────┘                              └─────────┘
```

### Technology Stack
- **Frontend**: HTML5, CSS3, JavaScript (ES5), jQuery
- **Backend**: Python Flask framework
- **Machine Learning**: Scikit-learn (Linear Regression model)
- **Data Format**: JSON for API communication, Pickle for model serialization
- **Server**: Development server (Flask built-in)

## Components and Interfaces

### 1. Flask Server Component (`server.py`)
**Purpose**: Serves as the main application server and API gateway

**Key Functions**:
- `get_location_names()`: Returns list of available Bangalore locations
- `predict_home_price()`: Processes prediction requests and returns estimated prices

**API Endpoints**:
- `GET /get_location_names`: Returns JSON array of location names
- `POST /predict_home_price`: Accepts form data and returns price prediction

**Dependencies**: Flask, util module for model operations

### 2. Utility Module (`util.py`)
**Purpose**: Handles model loading and prediction logic

**Key Functions**:
- `load_saved_artifacts()`: Loads model and location data on server startup
- `get_estimated_price()`: Performs price prediction using loaded model
- `get_location_names()`: Returns available locations from loaded data

**Data Management**:
- Loads `banglore_home_prices_model.pickle` (trained model)
- Loads `columns.json` (feature columns and location names)
- Maintains global state for model and data

### 3. Client Interface Components

#### HTML Structure (`app.html`)
- Form inputs for area (text field)
- Radio button groups for BHK and bathroom selection
- Dropdown for location selection
- Submit button and result display area

#### JavaScript Logic (`app.js`)
- Form data collection and validation
- AJAX communication with Flask server
- Dynamic location dropdown population
- Result display and error handling

#### CSS Styling (`app.css`)
- Responsive form layout
- Switch-style radio buttons
- Background image with blur effect
- Modern, clean visual design

## Data Models

### Input Data Model
```javascript
{
  total_sqft: Number,    // House area in square feet
  bhk: Integer,          // Number of bedrooms (1-5)
  bath: Integer,         // Number of bathrooms (1-5)
  location: String       // Selected Bangalore location
}
```

### API Response Model
```javascript
{
  estimated_price: Number,  // Predicted price in lakhs
  locations: Array<String>  // Available location names
}
```

### Model Feature Vector
The ML model expects a numpy array with:
- Index 0: total_sqft (float)
- Index 1: bath (integer)
- Index 2: bhk (integer)
- Index 3+: One-hot encoded location features

## Error Handling

### Server-Side Error Handling
1. **File Not Found Errors**: Graceful handling when model or data files are missing
2. **Model Loading Errors**: Proper error messages and fallback behavior
3. **Invalid Input Handling**: Validation of form data before processing
4. **CORS Configuration**: Headers added for cross-origin requests

### Client-Side Error Handling
1. **Network Failures**: AJAX error callbacks for server communication issues
2. **Invalid Responses**: Validation of server response format
3. **Form Validation**: Client-side validation before submission
4. **User Feedback**: Clear error messages displayed to users

### Error Recovery Strategies
- Default values for missing form fields
- Fallback behavior when locations fail to load
- Graceful degradation when model is unavailable
- User-friendly error messages instead of technical details

## Testing Strategy

### Unit Testing Approach
1. **Backend Testing**:
   - Test model loading functionality
   - Validate prediction accuracy with known inputs
   - Test API endpoint responses
   - Verify error handling for edge cases

2. **Frontend Testing**:
   - Test form data collection functions
   - Validate AJAX request formatting
   - Test UI state management
   - Verify error display mechanisms

### Integration Testing
1. **End-to-End Workflow**:
   - Complete user journey from form input to result display
   - API communication between frontend and backend
   - Model prediction pipeline validation

2. **Cross-Browser Compatibility**:
   - Test in major browsers (Chrome, Firefox, Safari, Edge)
   - Validate responsive design on different screen sizes
   - Ensure JavaScript compatibility across browser versions

### Performance Testing
1. **Response Time**: Ensure predictions complete within 3 seconds
2. **Concurrent Users**: Test server stability under multiple simultaneous requests
3. **Resource Usage**: Monitor memory and CPU usage during operation

## Deployment Configuration

### Development Setup
1. **Dependencies**: Install required Python packages from requirements.txt
2. **File Structure**: Ensure proper placement of model and data files
3. **Server Configuration**: Flask development server on localhost:5000
4. **Static File Serving**: Configure Flask to serve HTML/CSS/JS files

### Production Considerations
1. **WSGI Server**: Replace Flask development server with production WSGI server
2. **Reverse Proxy**: Configure nginx for static file serving and load balancing
3. **Security**: Implement proper input validation and sanitization
4. **Monitoring**: Add logging and error tracking capabilities

## Security Considerations

### Input Validation
- Sanitize all user inputs before processing
- Validate numeric ranges for area, BHK, and bathroom counts
- Whitelist location names against known valid locations

### API Security
- Implement rate limiting for API endpoints
- Add request size limits to prevent abuse
- Consider authentication for production deployment

### Data Protection
- Secure model files and prevent unauthorized access
- Implement proper error messages that don't expose system details
- Use HTTPS in production environments