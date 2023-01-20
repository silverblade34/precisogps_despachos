from src.despachos.application.response import ResponseDespachos

class DespachosController:
    def __init__(self):
        self.response = ResponseDespachos()

    def listarEstrDespachos(self, file, datapuntos, codruta, dataempresa):
        coddatapuntos = self.response.listarCodPuntos(datapuntos)
        data = self.response.responseEstructura(file, coddatapuntos, codruta, dataempresa)
        return data
    
    def validarPlacas(self, file, dataempresa, datapuntos):
        resp = self.response.parsedValidarPlacas(file, dataempresa, datapuntos)
        return resp
    
    def enviarDespachosSMQ(self):
        resp = self.response.responseEnviarDespachos()
        return resp
        