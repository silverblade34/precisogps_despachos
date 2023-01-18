from src.clientes.infrastructure.api import ApiBotConnection
from src.clientes.application.reponse import ClientReponse

class ClientController:
    def __init__(self):
        self.connect = ApiBotConnection
    
    def listarClientes(self):
        dataclient = self.connect.apiListClient()
        return dataclient

    def listarRutas(self, datosclient):
        clientResponse = ClientReponse()
        dataRutasClientes = clientResponse.responseTodoRutas(datosclient)
        return dataRutasClientes