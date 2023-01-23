from flask import Flask, request, render_template, redirect, url_for, session
from flask_cors import CORS, cross_origin
from src.clientes.infrastructure.controller import ClientController
from src.rutas.infrastructure.controller import RutasController
from src.puntos.infrastructure.controller import PuntosController

from __main__ import app
app.secret_key = "hhyy526//--"
CORS(app)

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('menu'))
    else:
        return redirect(url_for('login'))

@app.route('/menu')
def menu():
    if 'user' in session:
        if 'dataclientes' in session:
            session.pop('dataruta', None)
            session.pop('dataempresa', None)
            datosclient = session['dataclientes']
            return render_template('index.html', datosclient = datosclient)
        else:
            _clientCL = ClientController()
            datosclient = _clientCL.listarClientes()
            session['dataclientes'] = datosclient
            return render_template('index.html', datosclient = datosclient)
    else:
        return redirect(url_for('login'))

@app.route('/rutas', methods = ['POST', 'GET'])
def rutas():
    if 'user' in session:
        datosclient = session['dataclientes']
        _rutasCL = RutasController()
        if request.method == 'POST':
            dataresumen = _rutasCL.resumenRutasSMQ(datosclient)
            datafiltro = _rutasCL.filtroRutasSMQ(request.form['codruta'], request.form['select-ruc'], dataresumen)
            return render_template('rutas.html', dataresumen = datafiltro, datosclient = datosclient)
        else:
            dataresumen = _rutasCL.resumenRutasSMQ(datosclient)
            return render_template('rutas.html', dataresumen = dataresumen, datosclient = datosclient)
    else:
        return redirect(url_for('login'))
    
@app.route('/paradas', methods = ['POST', 'GET'])
def paradas():
    if 'user' in session:
        datosclient = session['dataclientes']
        _rutasCL = PuntosController()
        if request.method == 'POST':
            dataresumen = _rutasCL.resumenPuntosSMQ(datosclient) 
            datafiltro = _rutasCL.filtroPuntosSMQ(request.form['parada'], request.form['select-ruc'], dataresumen)  
            return render_template('paradas.html', dataresumen = datafiltro, datosclient = datosclient)
        else:
            dataresumen = _rutasCL.resumenPuntosSMQ(datosclient)
            return render_template('paradas.html', dataresumen = dataresumen, datosclient = datosclient)
    else:
        return redirect(url_for('login'))  

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

def pagina_no_encontrada(error):
    return render_template('404.html'), 404