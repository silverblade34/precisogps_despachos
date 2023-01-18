from flask import Flask, request, render_template, redirect, url_for, session
from flask_cors import CORS, cross_origin
from src.puntos.infrastructure.controller import PuntosController
from src.rutas.infrastructure.controller import RutasController
import json
import ast
from __main__ import app
app.secret_key = "hhyy526//--"
CORS(app)

@app.route('/mostrar_puntos', methods = ['GET'])
def mostrar_puntos():
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
        if request.args['ruta'] != "null":
            _puntosCL = PuntosController()
            datapuntos = _puntosCL.listarPuntos(dataempresa['token'], dataempresa['depot'], dataempresa['ruc'], request.args['ruta'])
            datamostrar = str(datapuntos)
            data = datamostrar.replace("'",'"')
            session['datapuntos'] = datapuntos
            return render_template('mostrar_puntos.html', dataruta = dataruta, dataempresa = dataempresa, ruta= request.args['ruta'], datapuntos = datapuntos, data = data)
        else:
            return render_template('mostrar_puntos.html', dataruta = dataruta, dataempresa = dataempresa)
    else:
        return redirect(url_for('login'))

@app.route('/enviar_puntos', methods = ['GET'])
def enviar_puntos():
    if 'user' in session:
        dataempresa = session['dataempresa']
        _puntosCL = PuntosController()
        resp = _puntosCL.enviarPuntos(session['datapuntos'])
        result = resp[1:-1]
        message = ast.literal_eval(result)
        print(json.dumps(session['datapuntos']))
        codruta = session['datapuntos'][0]['SM_CODIGO_RUTA']
        return render_template('mostrar_puntos.html', dataruta = session['dataruta'], dataempresa = dataempresa, message = message, codruta = codruta)
    else:
        return redirect(url_for('login'))