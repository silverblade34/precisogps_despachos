from flask import Flask, request, render_template, redirect, url_for, session
from flask_cors import CORS, cross_origin
from src.rutas.infrastructure.controller import RutasController
import json
import ast
from __main__ import app
app.secret_key = "hhyy526//--"
CORS(app)

@app.route('/mostrar_rutas', methods = ['GET'])
def mostrar_rutas():
    if 'user' in session:
        _rutasCL = RutasController()
        if 'dataempresa' in session:
            return render_template('mostrar_rutas.html', dataempresa = session['dataempresa'], rutas = session['dataruta'], ubic= "home") 
        else:
            try:
                dataempresa = _rutasCL.setDataEmpresa(session['dataclientes'], request.args['ruc'])
                dataruta = _rutasCL.rutasCliente(dataempresa['token'], dataempresa['depot'], dataempresa['ruc'])
                session['dataempresa'] = dataempresa
                session['dataruta'] = dataruta
                return render_template('mostrar_rutas.html', dataempresa = session['dataempresa'], rutas = dataruta, ubic= "home")
            except Exception as err:
                return render_template('index.html', datosclient = session['dataclientes'], message = err)
    else:
        return redirect(url_for('login')) 

@app.route('/enviar_ruta_smq', methods=['POST'])
def enviar_ruta_smq():
    try:
        data = request.json  # Aquí obtienes los datos enviados desde el frontend como un diccionario Python
        _rutasCL = RutasController()
        resp = _rutasCL.enviarRutaSMQ(data)
        result = resp[1:-1]
        message = ast.literal_eval(result)
        print(message)
        return {"message": message}  # Por ejemplo, devolviendo un diccionario con un mensaje de éxito
    except Exception as e:
        return {"error": str(e)}, 400 


@app.route('/data_ruta_nimbus', methods = ['POST'])
def data_ruta_nimbus():
    _rutasCL = RutasController()
    dataempresa = session['dataempresa']
    rutaestr = _rutasCL.rutaEstructura(dataempresa['token'], dataempresa['depot'], dataempresa['ruc'], request.json['rutacodigo'])
    rutamostrar = str(rutaestr)
    data = rutamostrar.replace("'",'"')
    resp = {"data": data, "codruta": request.json['rutacodigo']}
    return resp


@app.route('/buscar_ruta_smq', methods = ['GET'])
def buscar_ruta_smq():
    _rutasCL = RutasController()
    codruta = request.args['codruta']
    dataruta = _rutasCL.mostrarRutaSMQ(codruta)
    return dataruta

@app.route('/actualizar_ruta_smq', methods = ['POST'])
def actualizar_ruta_smq():
    _rutasCL = RutasController()
    resp = _rutasCL.editarRutaSMQ(request.json['dataanterior'], request.json['data'])
    result = resp[1:-1]
    message = ast.literal_eval(result)
    print(dict(message))
    return message