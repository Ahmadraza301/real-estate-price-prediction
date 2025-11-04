from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import util
import os
import logging

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)  # Enable CORS for all routes

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    """Serve the main HTML page"""
    return render_template('index.html')

@app.route('/test')
def test_page():
    """Serve the frontend test page"""
    return send_from_directory('static', 'test.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    """Serve static files (CSS, JS)"""
    return send_from_directory('static', filename)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    """API endpoint to get all available locations"""
    try:
        locations = util.get_location_names()
        if not locations:
            logger.warning("No locations available")
            return jsonify({'error': 'No locations available'}), 500
        
        response = jsonify({
            'locations': locations
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        logger.info(f"Returned {len(locations)} locations")
        return response
    except Exception as e:
        logger.error(f"Error getting locations: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    """API endpoint to predict house price"""
    try:
        # Input validation
        if 'total_sqft' not in request.form:
            return jsonify({'error': 'Missing total_sqft parameter'}), 400
        if 'location' not in request.form:
            return jsonify({'error': 'Missing location parameter'}), 400
        if 'bhk' not in request.form:
            return jsonify({'error': 'Missing bhk parameter'}), 400
        if 'bath' not in request.form:
            return jsonify({'error': 'Missing bath parameter'}), 400

        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        # Validate ranges
        if total_sqft <= 0:
            return jsonify({'error': 'Area must be positive'}), 400
        if bhk < 1 or bhk > 10:
            return jsonify({'error': 'BHK must be between 1 and 10'}), 400
        if bath < 1 or bath > 10:
            return jsonify({'error': 'Bathrooms must be between 1 and 10'}), 400

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        
        if estimated_price is None:
            return jsonify({'error': 'Unable to predict price. Model not loaded properly.'}), 500
        
        response = jsonify({
            'estimated_price': estimated_price
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        logger.info(f"Predicted price: {estimated_price} for {location}, {total_sqft}sqft, {bhk}BHK, {bath}bath")
        return response
    except ValueError as e:
        logger.error(f"Invalid input: {e}")
        return jsonify({'error': 'Invalid input parameters'}), 400
    except Exception as e:
        logger.error(f"Error predicting price: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    try:
        util.load_saved_artifacts()
        print("Model and artifacts loaded successfully!")
        
        # Get port from environment variable for deployment platforms
        import os
        port = int(os.environ.get('PORT', 5000))
        
        app.run(debug=False, host='0.0.0.0', port=port)
    except Exception as e:
        print(f"Error starting server: {e}")