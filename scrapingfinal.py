# -*- coding: utf-8 -*-
"""ScrapingFinal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AnwPmPWSa46N44CLmHAgElQ72x8A0S2s
"""

!pip install requests_html
! pip install panda

from requests_html import HTMLSession
import pprint

session = HTMLSession()

r = session.get('https://www.datos.gov.py/conjunto-de-datos-m-s-conusltados')

scrapear = r.html.find('tbody tr td')

contenido = scrapear

num_columna = 1
lista = []


for posicion in range(len(contenido)):#scrapea el contenido de adentro 

  if num_columna == 1: 
    conj_datos = contenido[posicion].text



  if num_columna == 2:
    total = contenido[posicion].text

 
  num_columna += 1

  if num_columna == 3:
    info ={ 'Conjunto de datos':conj_datos ,'Total de visitas':total}

    lista.append(info)
    num_columna = 1

pprint.pprint(lista)

import pandas as pd
df= pd.DataFrame(lista)
df

from requests_html import HTMLSession
import pprint

session = HTMLSession()

r = session.get('https://www.datos.gov.py/conjunto-de-datos-m-s-conusltados')

scrapear = r.html.find('tbody tr td')

contenido = scrapear

num_columna = 0
lista = []
for posicion in range(len(contenido)):

  if num_columna == 1:
    total = contenido[posicion].text

  num_columna += 1

  if num_columna == 2:
    tipo_info ={ 'Total de visitas':total}

    lista.append(tipo_info)
    num_columna = 0

pprint.pprint(lista)

