from flask import Flask, request, json
import requests

class ApiBotConnection:
    @staticmethod
    def apiListClient():
        url = 'http://192.168.1.37:3222/api/v1/clientes/listar'
        clientes = requests.get(url)
        rawData =clientes.json()
        return rawData["data"]

    @staticmethod
    def apiListRoutes(token, depot, ruc):
        url = f'http://192.168.1.37:3222/api/v1/rutas/listar?token={token}&depot={depot}&ruc={ruc}'
        estr_ruta = requests.get(url)
        rawData = estr_ruta.json()
        print(json.dumps(rawData))
        if rawData['status'] == True:
            return rawData["data"]
        else:
            return {}

