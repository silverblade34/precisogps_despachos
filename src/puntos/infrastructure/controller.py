from src.puntos.infrastructure.api import ApiConnectionPreciso
from src.puntos.application.response import PuntosResponse

class PuntosController:

    def listarPuntos(self, token, depot, ruc, ruta):
        connApi = ApiConnectionPreciso()
        data = connApi.consumirPuntos(token, depot, ruc, ruta)
        return data

    def enviarPuntos(self, puntosestr):
        enviarsmq = PuntosResponse()
        resp = enviarsmq.responseEnviarPuntos(puntosestr) 
        return resp
    
    def statusRutasSMQ(self, codruta, ruc):
        validarRutas = PuntosResponse()
        resp = validarRutas.responseValidarRutas(codruta, ruc) 
        return resp
    
    def resumenPuntosSMQ(self, dataclientes):
        response = PuntosResponse()
        resp = response.resumenPuntosSMQ(dataclientes)
        return resp

    def filtroPuntosSMQ(self, parada, empresa, dataresumen):
        resp = PuntosResponse()
        data = resp.responseFiltrosPuntos(parada, empresa, dataresumen)
        return data
    
    