import os

import requests
from flask import Flask, jsonify, request



app = Flask(__name__)

@app.route("/")
def read_root():
    return jsonify({"message": "Welcome to AlogMed APIs"})

@app.route("/egfr1")
def egfr():
    creat = float(request.args.get('creat'))
    female = bool(request.args.get('female'))
    age = int(request.args.get('age'))
    
    if female == True:
        g= 1.012
        if creat <= 0.7:
            a = 0.7
            b = -0.241
        else:
            a = 0.7
            b = -1.2
    else:
        g= 1.0
        if creat <= 0.9:
            a = 0.9
            b = -0.302
        else:
            a = 0.9
            b = -1.2
    p1 = creat/a
    p2 = p1**b
    p3 = 0.9938**age
    p4 = 142*p2*p3*g
    egfr1 = round(p4, 0)
    if egfr1 >= 90:
        cat = "G1"
        info = "This falls in category of normal/high eGFR"
    elif egfr1 >=60 and egfr1 <90:
        cat = "G2"
        info = "This falls in category of mildly decreased eGFR"
    elif egfr1 >=45 and egfr1 <60:
        cat = "G3a"
        info = "This falls in category of mildly to moderately decreased eGFR"
    elif egfr1 >=30 and egfr1 <45:
        cat = "G3b"
        info = "This falls in category of Moderately to Severely decreased eGFR"
    elif egfr1 >15 and egfr1 <30:
        cat = "G4"
        info = "This falls in category of Severely decreased eGFR"
    elif egfr1 <15:
        cat = "G5"
        info = "This falls in category of Kidney failure"
    units = "mL/min/1.73m2"
    return jsonify({"egfr": egfr1, "units":units, "CKD category": cat, "details":info})
