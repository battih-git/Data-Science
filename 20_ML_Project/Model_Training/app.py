import pickle
from flask import Flask, jsonify, render_template, request
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# import ridge regressor and standard scaler pickle
ridge_path = r"C:\Users\battih\Desktop\Personal\Data Science\20_ML_Project\Model_Training\models\ridge.pkl"
scaler_path = r"C:\Users\battih\Desktop\Personal\Data Science\20_ML_Project\Model_Training\models\scaler.pkl"

ridge_model = pickle.load(open(ridge_path,'rb'))
standard_scaler = pickle.load(open(scaler_path,'rb'))

"/mode"

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predictdata', methods =['GET','POST'])
def predict_data_point():
    if request.method == 'POST':
        Temprature = float(request.form.get('Temprature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))
        
        new_data_scaled = standard_scaler.transform([[Temprature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        result = ridge_model.predict(new_data_scaled)
        return render_template('home.html',result=result[0])
        
    else:
        return render_template("home.html")

if __name__=='__main__':
    app.run(host='0.0.0.0')