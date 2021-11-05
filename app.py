from flask import Flask, request, render_template, redirect, url_for
import pickle, gzip
import joblib
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.sav', 'rb'))


# HTML File to get user input
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    Age = request.form['age']
    Thyroid_Stimulating_Hormone_Level = request.form['TSH']
    Pregnant = float(request.form['pregnant'])
    Triiodothyronine_T3 = request.form['T3']
    Total_Thyroxine_TT4 = request.form['TT4']
    On_thyroxine_Medication = request.form['on_thyroxine']
    T4U_Measure = request.form['T4U']
    FTI_Measured = request.form['FTI_measured']
    Tumor = float(request.form['tumor'])
    Free_Thyroxine_Index_FTI = float(request.form['FTI'])

    values = ({"age": Age, "TSH": Thyroid_Stimulating_Hormone_Level, "pregnant": Pregnant,
               "T3": Triiodothyronine_T3, "TT4": Total_Thyroxine_TT4,
               "on_thyroxine": On_thyroxine_Medication, "T4U": T4U_Measure, "FTI_measured": FTI_Measured,
               "tumor": Tumor, "FTI": Free_Thyroxine_Index_FTI})

    arr = np.array([[Age, Thyroid_Stimulating_Hormone_Level, Pregnant, Triiodothyronine_T3, Total_Thyroxine_TT4,
                     On_thyroxine_Medication, T4U_Measure, FTI_Measured, Tumor, Free_Thyroxine_Index_FTI]])
    pred = model.predict(arr)

    if pred == 0:
        res_Val = "Compensated hypothyroid"
    elif pred == 1:
        res_Val = "No thyroid"
    elif pred == 2:
        res_Val = 'Primary hypothyroid'
    elif pred == 3:
        res_Val = 'Secondary hypothyroid'

    return render_template('index.html',prediction_text='Patient has {}'.format(res_Val))

#
# return render_template('forest_fire.html',
#                        pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(),
#                        bhai="Your Forest is Safe for now")

if __name__ == '__main__':
    app.run(debug=True)