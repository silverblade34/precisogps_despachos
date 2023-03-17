from src.vehiculos.application.response import VehiculosResponse

class VehiculosController:
    def listarVehiculos(self):
        response = VehiculosResponse()
        data = response.responselistarVehiculosSMQ()
        return data