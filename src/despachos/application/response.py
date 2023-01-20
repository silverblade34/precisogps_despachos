import requests
import pandas as pd
from datetime import datetime
import json
from flask import Flask, request, render_template, redirect, url_for, session

class ResponseDespachos:
    def listarCodPuntos(self, datapuntos):
        list = []
        for d in datapuntos:
           list.append(d['SM_CODIGO_PC'])
        return list
    
    def responseEstructura(self, file, coddatapuntos, codruta, dataempresa):
        try:
            if file and file.filename.endswith('.xlsx'):
                codigodespacho = self.codigoDespachoMostrar()
                print("Anterior orden despacho: "+ str(codigodespacho)) 
                df = pd.read_excel(file, sheet_name=1)
                cantdesp=0
                tramaspuntos = len(coddatapuntos) + 1
                fechaf= ""
                counter = 0
                totalestrdespachos = []
                for i in range(0, df.shape[0], tramaspuntos): 
                    # if counter >= limit:
                    #     break
                    despachos={}
                    despachos["SM_RUC_OTT"]= dataempresa['ruc']
                    despachos["SM_CODIGO_RUTA"] = codruta
                    despachos["SM_CI_CONDUCTOR"] = ""
                    despachos["SM_RUC_PROVEEDOR"] = "1716024474001"
                    despachos["SM_CODIGO_DESPACHO"] = str(int(codigodespacho) + cantdesp)
                    despachos["SM_ESTADO_DESPACHO"] = "A"
                    despachos["SM_DESCRIPCION_DESPACHO"] = ""
                    despachos["SM_OBSERVACION_DESPACHO"] = ""
                    SM_PC = []    
                    n = 0 
                    p = 1
                    for i, row in df.iloc[i:i + tramaspuntos].iterrows():
                        if i == 0 or i%tramaspuntos == 0:
                            placai= str(row[0])
                            #Convertimos la fecha para poder tratarla
                            fecha= str(row[1])
                            fecha1=fecha.replace('.','/')
                            fecha_dt = datetime.strptime(fecha1, '%d/%m/%Y')
                            dater=str(fecha_dt)
                            fechaf=dater[:10]
                            despachos["SM_PLACA"]=placai[:7]
                            counter += 1             
                        else:              
                            dic_pc={}
                            dic_pc['SM_CODIGO_PC']=str(coddatapuntos[n])                
                            horadespacho= str(fechaf)+"T"+ str(row[2])+":00"                
                            dic_pc["SM_HORA_DESPACHO"]=horadespacho
                            SM_PC.append(dic_pc)
                            n += 1
                            counter += 1
                            p += 1
                    cantdesp=cantdesp+1
                    despachos["SM_PC"]=SM_PC
                    # despachosEnviar= json.dumps(despachos)
                    # resp = self.parsedEnviarDespachos(despachosEnviar)
                    # -------------------------------------------------------------
                    #GUARDAR LA ESTRUCTURA FINAL DEL DESPACHO EN UNA ARCHIVO JSON
                    totalestrdespachos.append(despachos)
                despachosEnviar = json.dumps(totalestrdespachos)
                with open('datos.json', 'w') as f:
                    f.write(despachosEnviar)
                    # -------------------------------------------------------------
                    # if len(respuesta)<= 1:
                    #     print(despachos["SM_PLACA"])
                    # else:
                    #     r=r+1
                    #     print("Despachos correctos: "+str(r))
                    # lista.append(respuesta)
                    # cantdesp=cantdesp+1
                    # print("Despachos enviados: "+ str(cantdesp))
                    # #time.sleep(1)
            #listaf=json.dumps(lista)
                valor_orden = cantdesp + int(codigodespacho) + 1
                actualizar = self.codigoDespachoActualizar("SM_DESPACHOS", valor_orden)
                print("Nuevo orden despacho: "+ str(valor_orden))   
                return "Completo"
        except Exception as err:
            print(err)
    
    def parsedValidarPlacas(self, file, dataempresa, datapuntos):
        if file and file.filename.endswith('.xlsx'):
            listplacas_empresa = self.parsedListarPlacasSMQ(dataempresa)
            df = pd.read_excel(file, sheet_name=1)
            tramaspuntos = len(datapuntos) + 1
            placasexcel = []
            resultestado = {}
            for i in range(0, df.shape[0], tramaspuntos): 
                for i, row in df.iloc[i:i + tramaspuntos].iterrows():
                    if i == 0 or i%tramaspuntos == 0:
                        placai= str(row[0])
                        placaf=placai[:7]
                        placasexcel.append(placaf)
            print("Placas que pertenecen a Quitumbe: "+ str(len(listplacas_empresa)))
            placas_unicas_excel = list(set(placasexcel))
            print("Placas unicas en el excel: "+ str(len(placas_unicas_excel)))
            if all(item in listplacas_empresa for item in placas_unicas_excel):
                resultestado['status'] = True
            else:
                resultestado['status'] = False
                placas_excel_set = set(placas_unicas_excel)
                placas_faltantes = list( placas_excel_set.difference(listplacas_empresa) )
                resultestado['placas'] = placas_faltantes
            return resultestado

    def parsedVehiculosCargadosSMQ(self): 
        response = requests.get(f'http://smmonitoreo.quito.gob.ec:444/api/vehiculos/?token=A1B8B0F9-490A-4E3B-BEC3-56FC54901AFA')
        raw = response.json()
        return raw
        
    def parsedListarPlacasSMQ(self, dataempresa):
        vehiculos = self.parsedVehiculosCargadosSMQ()
        listplacas = []
        for v in vehiculos:
            if v['RUC_OTT'] == dataempresa['ruc']:
                listplacas.append(v['PLACA'])
        return listplacas
    
    def codigoDespachoMostrar(self):
        response = requests.get(f'http://192.168.1.37:3222/api/v1/orden/mostrar')
        raw = response.json()
        ndespachos = raw['data']['SM_DESPACHOS']
        return ndespachos
    
    def codigoDespachoActualizar(self, nameorden, valor):
        response = requests.get(f'http://192.168.1.37:3222/api/v1/orden/actualizar?nameorden={nameorden}&valorden={valor}')
        raw = response.json()
        return raw['data']
    
    def responseConnectDespachos(self):
        headers={
            "Content-Type":"application/json"
            }
        response = requests.post(f'http://smmonitoreo.quito.gob.ec:444/api/despachar/?token=A1B8B0F9-490A-4E3B-BEC3-56FC54901AFA', despachosEnviar , headers=headers )
        raw = response.json()
        return raw

    def responseEnviarDespachos(self):
        with open('datos.json', 'r') as file:
            # carga el json en un objeto python
            data = json.load(file)
        # recorre el objeto python
        cont = 0
        for item in data:
            cont += 1
        print(cont)
        print(data[0])
        print(data[-1])
        return "Enviado"

   
