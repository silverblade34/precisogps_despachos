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

    def responseMostrarRutasSMQ(self):
        response = requests.get("http://192.168.1.37:3222/api/v1/ruta/smq")
        data = response.json()
        return data['data']
    
    def resumenRutasSMQ(self, dataclientes):
        dataSMQ = self.responseMostrarRutasSMQ()
        listarutasresumen = []
        for ruta in dataSMQ:
            for cliente in dataclientes:
                if ruta['RUC_OTT'] == cliente['ruc']:
                    datosrutasmq = {}
                    datosrutasmq['CODIGO_RUTA'] = ruta['CODIGO_RUTA']
                    datosrutasmq['GISROU_NOMBRE'] = ruta['GISROU_NOMBRE']
                    datosrutasmq['RUC_OTT'] = ruta['RUC_OTT']
                    datosrutasmq['NOMBRE_EMPRESA'] = cliente['empresa']
                    listarutasresumen.append(datosrutasmq)
        return listarutasresumen
    
    def responseFiltrosRutas(self, codruta, empresa, dataresumen):
        datafiltro = []
        cont = 0
        for ruta in dataresumen:
            codruta2 = codruta.replace(" ","").upper()
            if ruta['CODIGO_RUTA'] == codruta2 or ruta['RUC_OTT'] == empresa:
                datafiltro.append(ruta)
                cont += 1
        if cont == 0:
            datafiltro = dataresumen
        
        return datafiltro





