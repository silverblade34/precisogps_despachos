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
                print("---------------------0")
                dataruta = _rutasCL.rutasCliente(dataempresa['token'], dataempresa['depot'], dataempresa['ruc'])
                session['dataempresa'] = dataempresa
                session['dataruta'] = dataruta
                return render_template('mostrar_rutas.html', dataempresa = session['dataempresa'], rutas = dataruta, ubic= "home")
            except Exception as err:
                return render_template('index.html', datosclient = session['dataclientes'], message = err)
    else:
        return redirect(url_for('login')) 

@app.route('/modal_ruta', methods = ['GET'])
def modal_ruta():
    if 'user' in session:
        session.pop('rutaestr', None)
        _rutasCL = RutasController()
        dataempresa = session['dataempresa']
        rutaestr = _rutasCL.rutaEstructura(dataempresa['token'], dataempresa['depot'], dataempresa['ruc'], request.args['rutacodigo'])
        session['rutaestr'] = rutaestr
        rutamostrar = str(rutaestr)
        data = rutamostrar.replace("'",'"')
        return render_template('modal_rutas.html', rutas = session['dataruta'], rutacodigo = request.args['rutacodigo'], dataempresa = dataempresa, rutaestr = data) 
    else:
        return redirect(url_for('login'))

@app.route('/enviar_ruta_smq', methods = ['GET', 'POST'])
def enviar_ruta_smq():
    if 'user' in session:
        _rutasCL = RutasController()
        if 'rutaeditar' in session:
            datosclient = session['dataclientes']
            dataresumen = _rutasCL.resumenRutasSMQ(datosclient)
            resp = _rutasCL.editarRutaSMQ(session['rutaeditar'], request.form['nombre-ruta'], request.form['textarea-coordenadas'])
            result = resp[1:-1]
            message = ast.literal_eval(result)
            session.pop('rutaeditar', None)
            return render_template('rutas.html',  dataresumen = dataresumen, datosclient = datosclient, message = message)
        else:
            resp = _rutasCL.enviarRutaSMQ(session['rutaestr'])
            result = resp[1:-1]
            message = ast.literal_eval(result)
            print(message)
            return render_template('mostrar_rutas.html', dataempresa = session['dataempresa'], rutas = session['dataruta'], message = message)       
    else:
        return redirect(url_for('login'))
    

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