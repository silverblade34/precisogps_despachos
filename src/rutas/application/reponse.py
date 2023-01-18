import json
import requests

class RutasResponse:
    def __init__(self):
        pass
    
    def responseEnviarRuta(self, rutaestr):
        headers={
            "Content-Type":"application/json"
            }
        rutaenviar = []
        rutaenviar.append(rutaestr)
        rutae = json.dumps(rutaenviar)
        response = requests.post(f'http://smmonitoreo.quito.gob.ec:444/api/cargaruta/?token=A1B8B0F9-490A-4E3B-BEC3-56FC54901AFA', rutae , headers=headers )
        resp = response.json()
        return resp

    def responseListarRuta(self, datarutas):
        rutasmostrar = []
        for ruta in datarutas:
            rutal = {}
            rutal['SM_RUC_EMPRESA'] = ruta['SM_RUC_EMPRESA']
            rutal['SM_CODIGO_RUTA'] = ruta['SM_CODIGO_RUTA']
            rutal['SM_NOMBRE'] = ruta['SM_NOMBRE']
            rutasmostrar.append(rutal)
        return rutasmostrar

    def responseEstrRuta(self, datarutas, rutacodigo):
        for ruta in datarutas:
            if ruta['SM_CODIGO_RUTA'] == rutacodigo:
                return ruta


