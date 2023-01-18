from src.credential.infrastructure.api import ApiBotConnection

class CredentialController:
    def __init__(self):
        self.connect = ApiBotConnection
    
    def validarUsuario(self, user, pasw):
        datastatus = self.connect.connectionApi(user, pasw)
        return datastatus