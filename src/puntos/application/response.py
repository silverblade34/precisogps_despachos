import json
import requests
import Levenshtein

class PuntosResponse:
    def __init__(self):
        pass
    
    def responseEnviarPuntos(self, puntosestr):
        ordenenvio = int(puntosestr[-1]['SM_ORDEN']) + 1
        headers={
            "Content-Type":"application/json"
            }
        puntos = json.dumps(puntosestr)
        response = requests.post(f'http://smmonitoreo.quito.gob.ec:444/api/cargapc/?token=A1B8B0F9-490A-4E3B-BEC3-56FC54901AFA', puntos , headers=headers)
        resp = response.json()
        actualizar = self.codigoEnvioActualizar("SM_ORDEN_PC", ordenenvio)
        return resp
    
    def responseValidarRutas(self, codruta, ruc):
        response = requests.get(f"http://159.203.177.210:3020/api/v1/smq/rutas/validar?codruta={codruta}&ruc={ruc}")
        raw = response.json()
        return raw['status']
    
    def resumenPuntosSMQ(self, dataclientes):
        dataSMQ = self.responseMostrarPuntosSMQ()
        listarutasresumen = []
        for parada in dataSMQ:
            for cliente in dataclientes:
                if parada['RUC_OTT'] == cliente['ruc']:
                    datosrutasmq = {}
                    datosrutasmq['CODIGO_RUTA'] = parada['CODIGO_RUTA']
                    datosrutasmq['NOMBRE_PC'] = parada['NOMBRE_PC']
                    datosrutasmq['RUC_OTT'] = parada['RUC_OTT']
                    datosrutasmq['NOMBRE_EMPRESA'] = cliente['empresa']
                    listarutasresumen.append(datosrutasmq)
        return listarutasresumen
    
    def responseMostrarPuntosSMQ(self):
        response = requests.get("http://159.203.177.210:3020/api/v1/puntos/mostrar/smq")
        data = response.json()
        return data['data']
    
    def responseFiltrosPuntos(self, nameparada, ruta, empresa, dataresumen):
        print(nameparada)
        print(ruta)
        print(empresa)
        datafiltro = []
        cont = 0
        for parada in dataresumen:
            nameparada2 = nameparada.replace(" ","").lower()
            puntodata = parada['NOMBRE_PC'].replace(" ","").lower()
            distance1 = Levenshtein.distance(puntodata, nameparada2)
            rutaname = ruta.replace(" ","").lower()
            rutadata = parada['CODIGO_RUTA'].replace(" ","").lower()
            # distance2 = Levenshtein.distance(rutadata, rutaname)
            if distance1 < 3 or parada['RUC_OTT'] == empresa or rutaname == rutadata:
                datafiltro.append(parada)
                cont += 1
        if cont == 0:
            datafiltro = dataresumen
        return datafiltro
    
    def codigoEnvioActualizar(self, nameorden, valor):
        response = requests.get(f'http://159.203.177.210:3020/api/v1/orden/actualizar?nameorden={nameorden}&valorden={valor}')
        raw = response.json()
        return raw['data']


    
    
    