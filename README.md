# 🔥 Fire Weather Index (FWI) Prediction System

A complete end-to-end machine learning application that predicts fire risk using meteorological and fuel condition data. Built with Flask and deployed as a scalable web application.

## 📋 Table of Contents

- [Overview](#overview)
- [The Problem](#the-problem)
- [The Solution](#the-solution)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Input Variables](#input-variables)
- [Requirements](#requirements)
- [Contributing](#contributing)
- 

## 🎯 Overview

The Fire Weather Index (FWI) Prediction System is an advanced machine learning application that forecasts fire risk by analyzing weather conditions and fuel characteristics. The system uses **Lasso Regression** to predict the FWI, enabling firefighters, forestry professionals, and emergency responders to make data-driven decisions.

## 🚨 The Problem

Wildfires are a growing threat to forests, communities, and ecosystems worldwide. Traditional fire risk assessment methods are:

- ❌ Manual and time-consuming
- ❌ Prone to human error
- ❌ Unable to process complex weather interactions
- ❌ Not scalable across multiple regions
- ❌ Slow to provide actionable insights

This necessitates an **automated, data-driven solution** that can quickly and accurately assess fire risk in real-time.

## 💡 The Solution

Our FWI Prediction System leverages machine learning to:

✅ **Analyze Complex Relationships** - Captures non-linear interactions between weather and fuel variables  
✅ **Provide Real-Time Predictions** - Instant fire risk assessments  
✅ **Scale Across Regions** - Deployable for different geographic areas  
✅ **Enable Data-Driven Decisions** - Supports emergency planning and prevention  
✅ **Maintain Accuracy** - Consistently reliable predictions using Lasso Regression

## ✨ Features

- 🎯 **Accurate FWI Predictions** - Machine learning-based fire risk forecasting
- ⚡ **Real-Time Analysis** - Instant predictions with input submission
- 🌍 **Regional Support** - Location-specific assessments
- 📱 **User-Friendly Web Interface** - Modern, responsive design
- 🔬 **Production-Ready** - Complete ML pipeline from training to deployment
- 📊 **Comprehensive Analytics** - Based on 7 critical weather and fuel variables
- 🚀 **Scalable Architecture** - Easy to deploy and extend

## 📁 Project Structure

```
fwi-prediction-system/
│
├── application.py              # Main Flask application
├── main.py                     # Supporting utilities
├── requirements.txt            # Python dependencies
├── pyproject.toml             # Project configuration
│
├── models/                     # Machine learning models (pickled)
│   ├── lasso_model.pkl        # Trained Lasso regression model
│   └── scaler.pkl             # Data scaler for feature normalization
│
├── notebook/                   # Jupyter notebooks
│   └── lasso_Ridge_Regression.ipynb  # Model training & analysis
│
├── templates/                  # HTML templates
│   ├── index.html             # Welcome/home page
│   └── home.html              # Prediction input page
│
└── README.md                   # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (optional)

### Step 1: Clone or Download the Repository

```bash
git clone <repository-url>
cd fwi-prediction-system
```

### Step 2: Create a Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Verify Model Files

Ensure the following files exist in the `models/` directory:

- `lasso_model.pkl` - Trained model
- `scaler.pkl` - Feature scaler

## 💻 Usage

### Running the Application

```bash
python application.py
```

The application will start on `http://0.0.0.0:5000` by default.

### Accessing the Web Interface

1. Open your browser and navigate to `http://localhost:5000`
2. You'll see the welcome page with information about the model
3. Click "Start Prediction" to go to the prediction form
4. Fill in the required meteorological and fuel condition variables
5. Click "Predict" to get the FWI value

### Example Prediction Request

```
Temperature: 25°C
Relative Humidity: 45%
Wind Speed: 15 km/h
Rainfall: 0 mm
FFMC Index: 85
DMC Index: 120
ISI Index: 6
Classes: High
Region: Forest_Region_A
```

## 📊 Model Details

### Algorithm: Lasso Regression

**Lasso (Least Absolute Shrinkage and Selection Operator)** is a linear regression technique with L1 regularization that:

- Performs feature selection automatically
- Prevents overfitting
- Handles multicollinearity well
- Provides interpretable coefficients
- Scales efficiently to multiple features

### Model Performance

- **Training Approach**: Supervised learning on labeled wildfire data
- **Features**: 7 meteorological and fuel condition variables
- **Output**: Fire Weather Index (FWI) value
- **Deployment**: Serialized using pickle for easy loading

### Training Process

The model was trained using:

1. Historical wildfire and weather data
2. Feature engineering and normalization
3. Train-test split validation
4. Lasso regression with optimal regularization
5. Model persistence for production deployment

## 📝 Input Variables

| Variable                   | Unit     | Description                                                 |
| -------------------------- | -------- | ----------------------------------------------------------- |
| **Temperature**            | °C       | Air temperature - affects fuel moisture and combustion rate |
| **RH (Relative Humidity)** | %        | Atmospheric humidity - lower values increase fire risk      |
| **Ws (Wind Speed)**        | km/h     | Wind velocity - critical factor in fire spread              |
| **Rain (Rainfall)**        | mm       | Precipitation amount - increases fuel moisture              |
| **FFMC**                   | Index    | Fine Fuel Moisture Code - surface litter moisture           |
| **DMC**                    | Index    | Duff Moisture Code - organic layer moisture                 |
| **ISI**                    | Index    | Initial Spread Index - fast-burning fuel moisture           |
| **Classes**                | Category | Fire danger classification                                  |
| **Region**                 | Location | Geographic region for localized predictions                 |

## 📦 Requirements

All dependencies are listed in `requirements.txt`:

```
Flask==2.3.0
scikit-learn==1.2.0
numpy==1.24.0
pandas==1.5.0
pickle
```

Install them with:

```bash
pip install -r requirements.txt
```

## 🔧 Configuration

### Flask Configuration

The application runs with the following default configuration:

```python
HOST: 0.0.0.0  # Listen on all network interfaces
PORT: 5000     # Default Flask port
DEBUG: False   # Set to True for development
```

### Model Configuration

Models are loaded from the `models/` directory:

- `lasso_model.pkl` - Regression model
- `scaler.pkl` - StandardScaler for feature normalization

## 🧪 Testing Predictions

### Manual Test Case

```
Input:
- Temperature: 20°C
- RH: 50%
- Ws: 10 km/h
- Rain: 0 mm
- FFMC: 80
- DMC: 100
- ISI: 5

Expected Output: Fire Weather Index value
```

## 📚 Additional Resources

- **Notebook**: Check `notebook/lasso_Ridge_Regression.ipynb` for model training details
- **Application Logic**: See `application.py` for Flask route handlers
- **Predictions**: Visit `templates/home.html` for the prediction interface

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Submit a pull request

## 📈 Future Enhancements

- [ ] Add user authentication and logging
- [ ] Implement prediction history tracking
- [ ] Create API endpoints for programmatic access
- [ ] Add advanced visualization charts
- [ ] Deploy to cloud platform (AWS, Azure, GCP)
- [ ] Implement model versioning and A/B testing
- [ ] Add real-time data integration
- [ ] Create mobile application


**Last Updated**: March 2026  
**Version**: 1.0.0  
**Status**: Production Ready ✅
