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
    
    def responseEstructura(self, file, coddatapuntos, codruta, dataempresa, codigodespacho):
        #pc = [359376, 359375, 359360, 359358, 359373, 359367, 359371, 359363, 359378, 359359, 359380, 359357, 525519] : coddatapuntos
        try:
            if file and file.filename.endswith('.xlsx'):
                df = pd.read_excel(file, sheet_name=1)
                cantdesp=0
                limit = 99
                tramaspuntos = len(coddatapuntos) + 1
                fechaf= ""
                counter = 0
                for i in range(0, df.shape[0], tramaspuntos): 
                    if counter >= limit:
                        break
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
                    despachosEnviar= json.dumps(despachos)
                    print(despachosEnviar)
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
                return "Completo"
        except Exception as err:
            print(err)

    def parsedEnviarDespachos(self, despachosEnviar): 
        headers={
            "Content-Type":"application/json"
            }
        response = requests.post(f'http://smmonitoreo.quito.gob.ec:444/api/despachar/?token=A1B8B0F9-490A-4E3B-BEC3-56FC54901AFA', despachosEnviar , headers=headers )
        raw = response.json()
        return raw

   
