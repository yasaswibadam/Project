# from flask import Flask, render_template, request
# import pickle

# app = Flask(__name__)

# # Load the trained model
# model = pickle.load(open('model.pkl', 'rb'))

# @app.route("/")
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the input values from the form
#     input_values = [
#         float(request.form['nitrogen']),
#         float(request.form['phosphorous']),
#         float(request.form['potassium']),
#         float(request.form['temperature']),
#         float(request.form['humidity']),
#         float(request.form['ph']),
#         float(request.form['rainfall'])
#     ]

#     # Make a prediction using the loaded model
#     recommended_crop = model.predict([input_values])[0]

#     return render_template('result.html', crop=recommended_crop)

# if __name__ == '__main__':
#      app.run(host='0.0.0.0', debug=True)
from flask import Flask, render_template, request
import pickle
import numpy as np  # To convert input into the proper format
app = Flask(__name__)
# Load the trained model
# Ensure model.pkl is present in the correct directory
model = pickle.load(open('model.pkl', 'rb'))


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input values from the form and convert them to floats
        input_values = [float(request.form['nitrogen']),
                        float(request.form['phosphorous']),
                        float(request.form['potassium']),
                        float(request.form['temperature']),
                        float(request.form['humidity']),
                        float(request.form['ph']),
                        float(request.form['rainfall'])]
        input_values = np.array(input_values).reshape(1, -1)
        # Make a prediction using the loaded model
        recommended_crop = model.predict(input_values)[0]
        return render_template('result.html', crop=recommended_crop)
    except Exception as e:
        # In case of errors, return a simple error page or log the error
        return f"An error occurred: {e}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
