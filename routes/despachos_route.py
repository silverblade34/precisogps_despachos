from flask import Flask, request, render_template, redirect, url_for, session
from flask_cors import CORS, cross_origin
from src.despachos.infrastructure.controller import DespachosController
from src.puntos.infrastructure.controller import PuntosController
from src.rutas.infrastructure.controller import RutasController
import json
import ast
import pandas as pd
from __main__ import app
app.secret_key = "hhyy526//--"
CORS(app)

@app.route('/cargar_despachos', methods = ['GET'])
def cargar_despachos():
    if 'user' in session:
        _rutasCL = RutasController()
        if 'dataempresa' in session:
            dataempresa = session['dataempresa']
            dataruta = session['dataruta']
        else:
            dataempresa = _rutasCL.setDataEmpresa(session['dataclientes'], request.args['ruc']) 
            dataruta = _rutasCL.rutasCliente(dataempresa['token'], dataempresa['depot'], dataempresa['ruc'])
            session['dataempresa'] = dataempresa
            session['dataruta'] = dataruta

        session.pop('datapuntos', None)
        if request.args['codruta'] == "null":
            return render_template('cargar_despachos.html', dataruta = session['dataruta'], dataempresa = session['dataempresa'])
        else:
            return render_template('cargar_despachos.html', dataruta = session['dataruta'], dataempresa = session['dataempresa'], codruta = request.args['codruta'])
    else:
        return redirect(url_for('login'))

@app.route('/enviar_despachos', methods = ['POST', 'GET'])
def enviar_despachos():
        if 'user' in session:
            dataempresa = session['dataempresa']
            _puntosCL = PuntosController()
            datapuntos = _puntosCL.listarPuntos(dataempresa['token'], dataempresa['depot'], dataempresa['ruc'], request.args['codruta'])
            file = request.files.get('file')
            _despachosCL = DespachosController()
            codigodespacho = 9510024
            resp = _despachosCL.listarEstrDespachos(file, datapuntos, request.args['codruta'], session['dataempresa'], codigodespacho)
            print(resp)
            return render_template('cargar_despachos.html', dataruta = session['dataruta'], dataempresa = session['dataempresa'])
        else:
            return redirect(url_for('login'))
        