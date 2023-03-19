from flask import Flask, request, render_template, redirect, url_for, session
from flask_cors import CORS, cross_origin
from src.clientes.infrastructure.controller import ClientController
from src.rutas.infrastructure.controller import RutasController
from src.puntos.infrastructure.controller import PuntosController
from src.despachos.infrastructure.controller import DespachosController
import requests

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
            session.pop('datapuntos', None)
            datosclient = session['dataclientes']
            return render_template('index.html', datosclient = datosclient, ubic= "home")
        else:
            _clientCL = ClientController()
            datosclient = _clientCL.listarClientes()
            session['dataclientes'] = datosclient
            return render_template('index.html', datosclient = datosclient,  ubic= "home")
    else:
        return redirect(url_for('login'))

@app.route('/rutas', methods = ['POST', 'GET'])
def rutas():
    if 'user' in session:
        try: 
            datosclient = session['dataclientes']
            _rutasCL = RutasController()
            if request.method == 'POST':
                dataresumen = _rutasCL.resumenRutasSMQ(datosclient)
                datafiltro = _rutasCL.filtroRutasSMQ(request.form['codruta'], request.form['select-ruc'], dataresumen)
                return render_template('rutas.html', dataresumen = datafiltro, datosclient = datosclient, ubic= "rutas")
            else:
                dataresumen = _rutasCL.resumenRutasSMQ(datosclient)
                return render_template('rutas.html', dataresumen = dataresumen, datosclient = datosclient, ubic= "rutas")
        except requests.exceptions.RequestException as e:
            mensaje_error = "Hubo un error al conectarse con la API. Por favor, inténtelo de nuevo más tarde."
            return render_template('notificaciones.html', msgerror = mensaje_error)
    else:
        return redirect(url_for('login'))
    
@app.route('/paradas', methods = ['POST', 'GET'])
def paradas():
    if 'user' in session:
        datosclient = session['dataclientes']
        _rutasCL = PuntosController()
        if request.method == 'POST':
            dataresumen = _rutasCL.resumenPuntosSMQ(datosclient) 
            datafiltro = _rutasCL.filtroPuntosSMQ(request.form['parada'], request.form['ruta'], request.form['select-ruc'], dataresumen)  
            return render_template('paradas.html', dataresumen = datafiltro, datosclient = datosclient, ubic= "paradas")
        else:
            dataresumen = _rutasCL.resumenPuntosSMQ(datosclient)
            return render_template('paradas.html', dataresumen = dataresumen, datosclient = datosclient, ubic= "paradas")
    else:
        return redirect(url_for('login'))

@app.route('/despachos', methods = ['POST', 'GET'])
def despachos():
    if 'user' in session:
        datosclient = session['dataclientes']
        _despachosCL = DespachosController()
        if request.method == 'POST':
            datadespachos = _despachosCL.mostrarDespachosSMQ(request.form['date-filtro'], request.form['select-ruc'])
            return render_template('despachos.html', datosclient = datosclient, datadespachos = datadespachos, ubic= "despachos")
        else:
            return render_template('despachos.html', datosclient = datosclient, ubic= "despachos")
    else:
        return redirect(url_for('login'))    

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

def pagina_no_encontrada(error):
    return render_template('404.html'), 404