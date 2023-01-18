from src.clientes.infrastructure.api import ApiBotConnection

class ClientReponse:
    def __init__(self):
        self.connect = ApiBotConnection

    def responseTodoRutas(self, datosclient):
        listaRutasClientes = []
        for cliente in datosclient:
            dataRucRuta = {}
            estr_ruta = self.connect.apiListRoutes(cliente['token'], cliente['depot'], cliente['ruc'])
            dataRucRuta['ruc'] = cliente['ruc']
            dataRucRuta['rutas'] = estr_ruta
            listaRutasClientes.append(dataRucRuta)
        print(listaRutasClientes)
        return listaRutasClientes
