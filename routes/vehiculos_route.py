from flask import Flask, request, render_template, redirect, url_for, session
from flask_cors import CORS, cross_origin
from src.vehiculos.infrastructure.controller import VehiculosController
import json
import ast
from __main__ import app
app.secret_key = "hhyy526//--"
CORS(app)

@app.route('/vehiculos', methods = ['GET'])
def vehiculos():
    _vehiCL = VehiculosController()
    datavehiculos = _vehiCL.listarVehiculos()
    return render_template('vehiculos.html', ubic= "vehiculos", datavehiculos = datavehiculos) 