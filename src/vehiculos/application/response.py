import requests

class VehiculosResponse:
    def responselistarVehiculosSMQ(self):
        response = requests.get(f'http://smmonitoreo.quito.gob.ec:444/api/vehiculos/?token=A1B8B0F9-490A-4E3B-BEC3-56FC54901AFA')
        raw = response.json()
        return raw