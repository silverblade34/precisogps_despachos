from src.despachos.application.response import ResponseDespachos

class DespachosController:
    def __init__(self):
        self.response = ResponseDespachos()

    def listarEstrDespachos(self, file, datapuntos, codruta, dataempresa, codigodespacho):
        coddatapuntos = self.response.listarCodPuntos(datapuntos)
        data = self.response.responseEstructura(file, coddatapuntos, codruta, dataempresa, codigodespacho)
        return data
        