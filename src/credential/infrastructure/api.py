from flask import Flask, request, json
import requests

class ApiBotConnection:
    @staticmethod
    def connectionApi(user, pasw):
        body = {"user": user, "pass" : pasw}
        url = 'http://159.203.177.210:3020/api/v1/login'
        hed = {"Content-Type": "application/json"}  
        get_tramas = requests.post(url, data= json.dumps(body), headers= hed)
        rawData = get_tramas.json()
        return rawData["status"]
