# Diabetes-Prediction-Application
This project is a web-based application for predicting diabetes using patient data. The application uses a pre-trained machine learning model to analyze the input data and determine whether a patient is likely to have diabetes. It is built using Flask for the backend and HTML for the frontend.

# Features
Accepts input for 8 health-related parameters:
Pregnancies,
Glucose,
Blood Pressure,
Skin Thickness,
Insulin,
BMI,
Diabetes Pedigree Function,
Age.

  Processes the inputs using a pre-trained ML model.
  
  Returns a prediction: "Diabetes Positive" or "Diabetes Negative".
  
  User-friendly interface styled with Bootstrap.

# Requirements
Before running the application, ensure you have the following installed:
Python,
Flask,
Numpy,
Scikit-learn.

# Files Overview
app.py: Main Python script for the Flask application. Includes routes for handling form submissions and making predictions using the ML model.

diabetes.pkl: Pre-trained machine learning model.

scaler.pkl: Scaler for preprocessing input data.

index.html: Frontend HTML form for user input.

# How the Prediction Works
The user provides input values for the 8 health parameters in the HTML form.

These values are sent to the Flask backend upon submission

The app.py script:
                    >Preprocesses the input data using the scaler.
                    >Feeds the data into the pre-trained model for prediction.

The model predicts whether the user is likely to have diabetes.

The prediction result is displayed on the webpage.

# Acknowledgments
This project uses machine learning techniques to predict diabetes.

Thanks to the authors of the dataset used for training the model.
