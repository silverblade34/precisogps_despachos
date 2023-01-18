import requests

class ApiConnectionPreciso:
    @staticmethod
    def consumirValidarCliente(ruc):
        response = requests.get(f'http://192.168.1.37:3222/api/v1/clientes/validar?ruc={ruc}')
        raw = response.json()
        return raw

    @staticmethod
    def consumirRutas(token, depot, ruc):
        response = requests.get(f'http://192.168.1.37:3222/api/v1/rutas/listar?token={token}&depot={depot}&ruc={ruc}')
        raw = response.json()
        return raw['data']

    @staticmethod 
    def enviarRuta():
        response = requests.post(f'http://192.168.1.37:3222/api/v1/ruta/enviar', )
        raw = response.json()
        return raw