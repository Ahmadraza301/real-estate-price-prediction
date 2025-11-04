@echo off
echo ========================================
echo Bangalore House Price Prediction App
echo ========================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7 or higher from https://python.org
    pause
    exit /b 1
)

echo Python found!
echo.

echo Checking required packages...
python -c "import flask, numpy, sklearn" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing required packages...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install packages
        pause
        exit /b 1
    )
) else (
    echo All packages are installed!
)

echo.
echo Checking model files...
if not exist "artifacts\columns.json" (
    echo ERROR: Model files not found in artifacts directory
    echo Please ensure the following files exist:
    echo - artifacts\columns.json
    echo - artifacts\banglore_home_prices_model.pickle
    pause
    exit /b 1
)

if not exist "artifacts\banglore_home_prices_model.pickle" (
    echo ERROR: Model files not found in artifacts directory
    echo Please ensure the following files exist:
    echo - artifacts\columns.json
    echo - artifacts\banglore_home_prices_model.pickle
    pause
    exit /b 1
)

echo Model files found!
echo.

echo Starting the application...
echo.
echo The application will be available at:
echo http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python app.py