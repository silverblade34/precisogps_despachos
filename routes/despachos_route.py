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
        try:
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
        except Exception as err:
                return render_template('index.html', datosclient = session['dataclientes'], message = err)
    else:
        return redirect(url_for('login'))

@app.route('/enviar_despachos', methods = ['GET'])
def enviar_despachos():
        if 'user' in session:
            _despachosCL = DespachosController()
            resp = _despachosCL.enviarDespachosSMQ()
            return render_template('cargar_despachos.html', dataruta = session['dataruta'], dataempresa = session['dataempresa'], messageconfirm = resp)
        else:
            return redirect(url_for('login'))
        
@app.route('/validar_placas', methods = ['POST', 'GET'])
def validar_placas():
    if 'user' in session:
        dataempresa = session['dataempresa']
        _puntosCL = PuntosController()
        statusRutaSMQ = _puntosCL.statusRutasSMQ(request.args['codruta'], dataempresa['ruc'])
        codruta = request.args['codruta']
        if statusRutaSMQ == True:
            file = request.files.get('file')
            _despachosCL = DespachosController()
            datapuntos = _puntosCL.listarPuntos(dataempresa['token'], dataempresa['depot'], dataempresa['ruc'], request.args['codruta'])
            validarPlacas = _despachosCL.validarPlacas(file, dataempresa, datapuntos)
            resp = _despachosCL.listarEstrDespachos(file, datapuntos, request.args['codruta'], session['dataempresa'])
            print(validarPlacas)
            if validarPlacas['status'] == True:
                print(resp)
                redirect(url_for('enviar_despachos'))
            else:
                return render_template('cargar_despachos.html', dataruta = session['dataruta'], dataempresa = session['dataempresa'], messageplacas = validarPlacas['placas'])
        else:
                messagevalidar = f"La {codruta} no se ha cargado a SMQ"
                return render_template('cargar_despachos.html', dataruta = session['dataruta'], dataempresa = session['dataempresa'], messagevalidar = messagevalidar)

        