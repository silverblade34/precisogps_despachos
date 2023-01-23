from src.rutas.infrastructure.api import ApiConnectionPreciso
from src.rutas.application.reponse import RutasResponse
import json

class RutasController:
    def validarCliente(self, ruc):
        conexion = ApiConnectionPreciso()
        data = conexion.consumirValidarCliente(ruc)
        return data['data']

    def rutasCliente(self, token, depot, ruc):
        conexion = ApiConnectionPreciso()
        response = RutasResponse()
        datarutas = conexion.consumirRutas(token, depot, ruc)
        resp = response.responseListarRuta(datarutas)  
        return resp

    def rutaEstructura(self, token, depot, ruc, rutacodigo):
        conexion = ApiConnectionPreciso()
        response = RutasResponse()
        datarutas = conexion.consumirRutas(token, depot, ruc)
        resp = response.responseEstrRuta(datarutas, rutacodigo)     
        return resp

    def enviarRutaSMQ(self, rutaestr):
        enviarsmq = RutasResponse()
        resp = enviarsmq.responseEnviarRuta(rutaestr)
        return resp

    def setDataEmpresa(self, dataclientes, ruc):
        dataempresa = {}
        for d in dataclientes:
            if d['ruc'] == ruc:
                dataempresa['token'] = d['token']
                dataempresa['depot'] = d['depot']
                dataempresa['ruc'] = d['ruc']
                dataempresa['empresa'] = d['empresa']
        return dataempresa
    
    def resumenRutasSMQ(self, dataclientes):
        resp = RutasResponse()
        data = resp.resumenRutasSMQ(dataclientes)
        return data
    
    def filtroRutasSMQ(self, ruta, empresa, dataresumen):
        resp = RutasResponse()
        data = resp.responseFiltrosRutas(ruta, empresa, dataresumen)
        return data
        