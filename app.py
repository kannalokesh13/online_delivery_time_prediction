from sklearn.metrics import r2_score
from src.exception import CustomException
from src.logger import logging
import os
import pandas as pd
import sys
from flask import Flask,request,render_template,url_for
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline
from flask_cors import CORS,cross_origin


app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/review',methods=['POST','GET'])
def calculate():
    if request.method=='POST':
        return render_template('index.html')
    else:
        try:
            results=request.form
            # age1=float(request.form['age'])
            # rating1=float(request.form.get('ratings'))
            # rlatitude=float(request.form.get('rlat'))
            # rlongitude=float(request.form.get('rlon'))
            # dlatitude=float(request.form.get('dlat'))
            # dlongitude=float(request.form.get('dlon'))
            # timeorder=pd.to_datetime(request.form.get('torder'))
            # timepicked=pd.to_datetime(request.form.get('tpicked'))
            # weather1=request.form.get('weather')
            # traffic=request.form.get('road_traffic')
            # vcond=int(request.form.get('vehicle_cond'))
            # typorder=request.form.get('top')
            # typvehicle=request.form.get('tov')
            # md=float(request.form.get('multi_deli'))
            # city1=request.form.get('city')

            # results=[age1,rating1,rlatitude,rlongitude,dlatitude,dlongitude,timeorder,timepicked,weather1,traffic,vcond,typorder,typvehicle,md,city1]


            return render_template('results.html',final_result=results)
        
        except Exception as e:
            logging.info("some where the error occured")
            raise CustomException(e,sys)






if __name__=="__main__":
    app.run(debug=True)
