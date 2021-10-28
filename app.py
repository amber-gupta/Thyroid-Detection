from flask import Flask,request,render_template,redirect,url_for
import pickle,gzip
import joblib
import numpy as np
from pymongo import MongoClient
from flask_pymongo import PyMongo


#model = joblib.load('Thyroid_model.pkl')

app=Flask(__name__)

#app.config['MONGO_DBNAME']='mydb'
#app.config["MONGO_URI"]='mongodb+srv://kalpuG:12345@mydb.ydqwp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

mongo=PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")

# def home():
#     online_uses=mongo.db.users.find({"online":True})
#     return render_template('index.html',online_uses=online_uses)

@app.route('/predict',methods=['POST','GET'])

def predict():
    #db = mongo.db.Results_app
 
    Age=float(request.form['age'])
    Thyroid_Stimulating_Hormone_Level= float(request.form.get['TSH'])
    Pregnant=float(request.form['pregnant'])
    Triiodothyronine_T3=float(request.form['T3'])
    Total_Thyroxine_TT4=float(request.form['TT4'])
    On_thyroxine_Medication=float(request.form['on_thyroxine'])
    T4U_Measure=float(request.form['T4U'])
    FTI_Measured=float(request.form['FTI_measured'])
    Tumor= float(request.form['tumor'])
    Free_Thyroxine_Index_FTI= float(request.form['FTI'])

    values=({"age":Age,"TSH":Thyroid_Stimulating_Hormone_Level,"preganant":Pregnant
             "T3":Triiodothyronine_T3,"TT4":Total_Thyroxine_TT4,
            "on_thyroxine":On_thyroxine_Medication,"T4U":T4U Measure,FTI_measured":FTI_Measured,
            "tumor":Tumor,"FTI":Free_Thyroxine_Index_FTI})
    my_data=db.insert_one(values)

    arr=np.array([[Age,Thyroid_Stimulating_Hormone_Level,Pregnant,Triiodothyronine_T3,Total_Thyroxine_TT4,
    On_thyroxine_Medication,T4U_Measure,FTI_Measured,Tumor,Free_Thyroxine_Index_FTI ]])
    pred=model.predict(arr)



    if pred==0:
        res_Val="Compensated hypothyroid"
    elif pred==1:
        res_Val="No thyroid"
    elif pred==2:
        res_Val='Primary hypothyroid'
    elif pred==3:
        res_Val='Secondary hypothyroid'


    return render_template('index.html',prediction_text='Patient has {}'.format(res_Val),my_data=my_data)


if __name__=='__main__':
    app.run(debug=True)