from flask import Flask, render_template, request
import numpy as np
import pickle

# Initialize Flask application
app = Flask(__name__)

# Load the pre-trained model from the file 'diabetes.pkl'
classifier = pickle.load(open("diabetes.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route('/')
def index():
    return render_template('index.html')  # Render the index.html template when the user visits the root URL

@app.route('/predict', methods=['GET','POST'])
def predict():
    try:
        Pregnancies = int(request.form["Pregnancies"])
        Glucose = int(request.form["Glucose"])
        BloodPressure = int(request.form["BloodPressure"])
        SkinThickness = int(request.form["SkinThickness"])
        Insulin = int(request.form["Insulin"])
        BMI = float(request.form["BMI"])
        DiabetesPedigreeFunction = float(request.form["DiabetesPedigreeFunction"])
        Age = int(request.form["Age"])


        input_data = (Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        std_data = scaler.transform(input_data_reshaped)

        # Make prediction using the loaded model
        prediction = classifier.predict(std_data)

        # Since prediction is an array, get the first element for comparison
        result = "Diabetes Positive" if prediction[0] == 1 else "Diabetes Negative"

    except Exception as e:
        result = f"Error in prediction: {str(e)}"
    
    # Render the HTML template and pass the result to it
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
