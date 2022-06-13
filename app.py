#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:14:36 2022

@author: abhinav
"""
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import json 
import pickle

app = Flask(__name__,template_folder="template")

model = pickle.load(open("model.pkl","rb"))

@app.route("/",methods=["GET"])
def home():
        return render_template("/index.html")
    
@app.route("/",methods=["POST"])
def predict():
    if request.method=="POST":
        
        type_school =request.form['school_type']
        if (type_school == "Academic"):
            type_school = 0
        else:
            type_school = 1
        
        
        school_accreditation = request.form['school_accreditation']
        if (school_accreditation == "A"):
            school_accreditation = 0
        else:
            school_accreditation = 1
            
        gender = request.form['gender'] 
        if (gender == "male"):
            gender = 1
        else:
            gender= 0
            
        interest = request.form['interest']
        if (interest == "very_interested"):
            interest = 4
        elif interest == "uncertain":
            interest = 3
        elif interest == "less_interested":
            interest = 0
        elif interest == "quiet_intersted":
            interest = 2
        else:
            interest= 1
            
        residence = request.form['residence']
        if (residence == "urban"):
            residence = 1
        else:
            residence = 0
            
        parent_age = int(request.form['parent_age']) 
        parent_salary = int(request.form['parent_salary']) 
        house_area =float(request.form['house_area'])
        average_grades=float(request.form['average_grades'])
        
        parent_was_in_college = request.form['parents_education']
        if (parent_was_in_college =="true") :
            parent_was_in_college = 1
        else:
            parent_was_in_college = 0
            
        features = np.array([type_school, school_accreditation, gender, interest, residence,parent_age, parent_salary, house_area,average_grades, parent_was_in_college])
       
        features = features.reshape(1,-1)
        prediction = model.predict(features)
        
        if(prediction == 1):
            return render_template("/index.html",prediction_text = "CONGRATULATIONS, YOU MIGHT BE IN")
        else:
            return render_template("/index.html",prediction_text = "SORRY, YOU MIGHT NOT BE IN")
        
if __name__ == "__main__":
    app.run(debug=True)