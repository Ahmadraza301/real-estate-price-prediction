#!/bin/bash

echo "========================================"
echo "Bangalore House Price Prediction App"
echo "========================================"
echo

echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "ERROR: Python is not installed or not in PATH"
        echo "Please install Python 3.7 or higher"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo "Python found!"
echo

echo "Checking required packages..."
$PYTHON_CMD -c "import flask, numpy, sklearn" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing required packages..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to install packages"
        exit 1
    fi
else
    echo "All packages are installed!"
fi

echo
echo "Checking model files..."
if [ ! -f "artifacts/columns.json" ]; then
    echo "ERROR: Model files not found in artifacts directory"
    echo "Please ensure the following files exist:"
    echo "- artifacts/columns.json"
    echo "- artifacts/banglore_home_prices_model.pickle"
    exit 1
fi

if [ ! -f "artifacts/banglore_home_prices_model.pickle" ]; then
    echo "ERROR: Model files not found in artifacts directory"
    echo "Please ensure the following files exist:"
    echo "- artifacts/columns.json"
    echo "- artifacts/banglore_home_prices_model.pickle"
    exit 1
fi

echo "Model files found!"
echo

echo "Starting the application..."
echo
echo "The application will be available at:"
echo "http://localhost:5000"
echo
echo "Press Ctrl+C to stop the server"
echo "========================================"
echo

$PYTHON_CMD app.py