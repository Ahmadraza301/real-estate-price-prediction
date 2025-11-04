import unittest
import json
from app import app
import util

class TestHousePricePredictionApp(unittest.TestCase):
    
    def setUp(self):
        """Set up test client and load artifacts"""
        self.app = app.test_client()
        self.app.testing = True
        util.load_saved_artifacts()
    
    def test_index_page_loads(self):
        """Test that the main page loads successfully"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bangalore Home Price Prediction', response.data)
    
    def test_get_location_names_endpoint(self):
        """Test the get_location_names API endpoint"""
        response = self.app.get('/get_location_names')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIn('locations', data)
        self.assertIsInstance(data['locations'], list)
        self.assertGreater(len(data['locations']), 0)
    
    def test_predict_home_price_valid_input(self):
        """Test price prediction with valid input"""
        response = self.app.post('/predict_home_price', data={
            'total_sqft': '1000',
            'bhk': '2',
            'bath': '2',
            'location': 'electronic city'
        })
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('estimated_price', data)
        self.assertIsInstance(data['estimated_price'], (int, float))
        self.assertGreater(data['estimated_price'], 0)
    
    def test_predict_home_price_missing_parameters(self):
        """Test price prediction with missing parameters"""
        response = self.app.post('/predict_home_price', data={
            'total_sqft': '1000',
            'bhk': '2'
            # Missing bath and location
        })
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
    
    def test_predict_home_price_invalid_sqft(self):
        """Test price prediction with invalid square feet"""
        response = self.app.post('/predict_home_price', data={
            'total_sqft': '-100',
            'bhk': '2',
            'bath': '2',
            'location': 'electronic city'
        })
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
    
    def test_predict_home_price_invalid_bhk(self):
        """Test price prediction with invalid BHK"""
        response = self.app.post('/predict_home_price', data={
            'total_sqft': '1000',
            'bhk': '15',  # Too high
            'bath': '2',
            'location': 'electronic city'
        })
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
    
    def test_predict_home_price_unknown_location(self):
        """Test price prediction with unknown location"""
        response = self.app.post('/predict_home_price', data={
            'total_sqft': '1000',
            'bhk': '2',
            'bath': '2',
            'location': 'unknown_location_xyz'
        })
        
        # Should still work but with different pricing
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('estimated_price', data)


class TestUtilFunctions(unittest.TestCase):
    
    def setUp(self):
        """Load artifacts before each test"""
        util.load_saved_artifacts()
    
    def test_get_location_names(self):
        """Test getting location names"""
        locations = util.get_location_names()
        self.assertIsInstance(locations, list)
        self.assertGreater(len(locations), 0)
        self.assertIn('electronic city', locations)
    
    def test_get_data_columns(self):
        """Test getting data columns"""
        columns = util.get_data_columns()
        self.assertIsInstance(columns, list)
        self.assertGreater(len(columns), 3)  # Should have at least sqft, bath, bhk + locations
    
    def test_get_estimated_price_valid_location(self):
        """Test price estimation with valid location"""
        price = util.get_estimated_price('electronic city', 1000, 2, 2)
        self.assertIsInstance(price, (int, float))
        self.assertGreater(price, 0)
    
    def test_get_estimated_price_unknown_location(self):
        """Test price estimation with unknown location"""
        price = util.get_estimated_price('unknown_location', 1000, 2, 2)
        self.assertIsInstance(price, (int, float))
        self.assertGreater(price, 0)
    
    def test_get_estimated_price_different_sizes(self):
        """Test price estimation with different house sizes"""
        price_small = util.get_estimated_price('electronic city', 500, 1, 1)
        price_large = util.get_estimated_price('electronic city', 2000, 4, 3)
        
        self.assertIsInstance(price_small, (int, float))
        self.assertIsInstance(price_large, (int, float))
        self.assertGreater(price_large, price_small)  # Larger house should cost more


if __name__ == '__main__':
    unittest.main()