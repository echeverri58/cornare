#Enviar los PDF separados al grupo de telegram VigilanteCornare

import requests
import os

def enviar_archivos_telegram():
  path3 = r"/content/separados"
  archivos = os.listdir(path3)
  for sendfiletele in archivos:
    requests.post('https://api.telegram.org/bot5105284062:AAHV2kCTc3ElARnk3uQbWWSQbB5Sjp0OiGM/sendDocument',
    files={'document': (path3+'/'+sendfiletele, open(path3+'/'+sendfiletele, 'rb'))},
    data={'chat_id': "-734037324", 'caption': "El siguiente archivo contiene la palabra "})