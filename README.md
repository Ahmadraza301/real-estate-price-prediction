# 🏠 Bangalore House Price Prediction Web Application

A full-stack machine learning web application that predicts house prices in Bangalore using real estate data. Built with Flask, scikit-learn, and modern web technologies.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

- **Real-time Price Prediction**: Get instant house price estimates based on area, bedrooms, bathrooms, and location
- **240+ Bangalore Locations**: Comprehensive coverage of Bangalore neighborhoods and areas
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Input Validation**: Client and server-side validation for accurate predictions
- **RESTful API**: Clean API endpoints for integration with other applications
- **Error Handling**: Graceful error handling with user-friendly messages
- **Testing Suite**: Comprehensive unit tests and frontend testing utilities

## 🚀 Live Demo

🔗 **[Try the Live Application](https://your-app-name.onrender.com)** *(Replace with your actual Render URL)*

## 📸 Screenshots

### Main Interface
![Main Interface](https://via.placeholder.com/800x400/4CAF50/FFFFFF?text=House+Price+Prediction+Interface)

### Price Prediction Result
![Prediction Result](https://via.placeholder.com/800x400/2196F3/FFFFFF?text=Price+Prediction+Result)

## 🛠️ Technology Stack

- **Backend**: Python 3.7+, Flask 2.0+
- **Frontend**: HTML5, CSS3, JavaScript (ES5), jQuery 3.6
- **Machine Learning**: scikit-learn, NumPy, Pandas
- **Model**: Linear Regression trained on Bangalore housing data
- **Deployment**: Render (Production), Flask Development Server (Local)

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## ⚡ Quick Start

### Option 1: Using Startup Scripts (Recommended)

**Windows:**
```bash
git clone https://github.com/Ahmadraza301/real-estate-price-prediction.git
cd real-estate-price-prediction
start_app.bat
```

**Linux/Mac:**
```bash
git clone https://github.com/Ahmadraza301/real-estate-price-prediction.git
cd real-estate-price-prediction
chmod +x start_app.sh
./start_app.sh
```

### Option 2: Manual Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ahmadraza301/real-estate-price-prediction.git
   cd real-estate-price-prediction
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   Navigate to: `http://localhost:5000`

## 📁 Project Structure

```
├── app.py                 # Main Flask application
├── util.py               # Model loading and prediction utilities
├── requirements.txt      # Python dependencies
├── Procfile             # Deployment configuration
├── runtime.txt          # Python version specification
├── start_app.bat        # Windows startup script
├── start_app.sh         # Linux/Mac startup script
├── test_app.py          # Backend unit tests
├── .gitignore           # Git ignore rules
├── artifacts/           # Model and data files
│   ├── columns.json
│   └── banglore_home_prices_model.pickle
├── templates/           # HTML templates
│   └── index.html
├── static/              # Static files (CSS, JS)
│   ├── app.css
│   ├── app.js
│   └── test.html       # Frontend testing page
└── docs/               # Documentation
    ├── README_APP.md
    └── DEPLOYMENT_GUIDE.md
```

## 🎯 Usage Guide

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

## 🔌 API Documentation

### Get Available Locations

```http
GET /get_location_names
```

**Response:**
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

```http
POST /predict_home_price
```

**Request Body (form-data):**
```
total_sqft: 1000
bhk: 2
bath: 2
location: electronic city
```

**Response:**
```json
{
  "estimated_price": 158.4
}
```

## 🧪 Testing

### Run Backend Tests
```bash
python test_app.py
```

### Run Frontend Tests
1. Start the application
2. Navigate to: `http://localhost:5000/test`
3. Click "Run All Tests"

### Test Coverage
- ✅ API endpoints (location retrieval, price prediction)
- ✅ Input validation and error handling
- ✅ UI components and user feedback
- ✅ Error scenarios and edge cases

## 🚀 Deployment

### Deploy to Render (Free)

1. **Fork this repository**
2. **Go to [render.com](https://render.com)**
3. **Create new Web Service**
4. **Connect your GitHub repository**
5. **Configure:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
6. **Deploy!**

For detailed deployment instructions, see [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

### Other Deployment Options
- Railway
- Vercel
- Heroku
- DigitalOcean App Platform
- AWS Elastic Beanstalk

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Dataset: Bangalore housing data from Kaggle
- Machine Learning: scikit-learn library
- Web Framework: Flask
- Frontend: jQuery and modern CSS
- Deployment: Render platform

## 📞 Contact

**Ahmad Raza** - [GitHub Profile](https://github.com/Ahmadraza301)

Project Link: [https://github.com/Ahmadraza301/real-estate-price-prediction](https://github.com/Ahmadraza301/real-estate-price-prediction)

---

⭐ **Star this repository if you found it helpful!**

## 🔄 Recent Updates

- ✅ Added comprehensive testing suite
- ✅ Improved error handling and validation
- ✅ Enhanced responsive design
- ✅ Added deployment configurations
- ✅ Created detailed documentation

---

*Built with ❤️ for the real estate and machine learning community*