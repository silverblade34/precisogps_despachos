import json
import requests

class PuntosResponse:
    def __init__(self):
        pass
    
    def responseEnviarPuntos(self, puntosestr):
        headers={
            "Content-Type":"application/json"
            }
        puntos = json.dumps(puntosestr)
        response = requests.post(f'http://smmonitoreo.quito.gob.ec:444/api/cargapc/?token=A1B8B0F9-490A-4E3B-BEC3-56FC54901AFA', puntos , headers=headers)
        resp = response.json()
        return resp