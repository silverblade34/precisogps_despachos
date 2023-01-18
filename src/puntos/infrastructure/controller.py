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