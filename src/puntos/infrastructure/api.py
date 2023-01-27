import requests

class ApiConnectionPreciso:
    @staticmethod
    def consumirPuntos(token, depot, ruc, ruta):
        response = requests.get(f'http://159.203.177.210:3020/api/v1/puntos/listar?depot={depot}&token={token}&ruta={ruta}&ruc={ruc}')
        raw = response.json()
        return raw['data']
    