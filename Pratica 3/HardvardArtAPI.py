##Codigo desenvolvido por Lucas Vinicio Maldonado
##Modulo de Infraestrutura computacional da Pos Graduação em DSDB


import requests
import json
import pprint
import webbrowser
from PIL import Image


import random
nr_rd = (random.randint(45000,500000))

#Exibe uma imagem aleatoria da galeria
pp = pprint.PrettyPrinter(indent=4)
r = requests.get(f"https://api.harvardartmuseums.org/image/{nr_rd}?apikey=afa59bb3-6290-44eb-be59-f38a63038dcc")
#print(r.text)
j = r.json()
try:   
    img = j['baseimageurl']
except:
  print("Imagem inválida, tente novamente")
name = j['renditionnumber']
date = j['date']

caption = j['caption']
if caption == None:
    caption = "Sem descrição"
#pp.pprint(j)
#print(img)
#Detalhes da obra
print(f"Obra:{name}")
print(f"Descrição:{caption}")
print(f"Data de criação da imagem ou da entrada na coleção:{date}")

#Abre a imagem
im = Image.open(requests.get(img, stream=True).raw)
im.show()