from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

lasso_model = pickle.load(open('models/lasso_model.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict_datapoint', methods=['POST', 'GET'])
def predict_datapoint():
    if request.method == 'POST':
        Tempreature = float(request.form['Temperature'])
        RH = float(request.form['RH'])
        Ws= float(request.form['Ws'])
        Rain= float(request.form['Rain'])
        FFMC= float(request.form['FFMC'])
        DMC= float(request.form['DMC'])
        ISI= float(request.form['ISI'])
        Classes= float(request.form['Classes'])
        Region= float(request.form['Region'])
        scaler_data = scaler.transform([[Tempreature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        prediction = lasso_model.predict(scaler_data)
        return render_template('home.html', result=prediction[0])
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run("0.0.0.0")
