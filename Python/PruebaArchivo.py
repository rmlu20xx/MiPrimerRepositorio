import csv
import pandas as pd
from io import open

print('Guarda el contenido de una archivo en una matriz')

CoordPredef=[6.124,-75.946,1035],[6.125,-75.966,109],[6.135,-75.976,31],[6.144,-75.836,151]
with open('CoordenadaPredefinida.txt','w') as archivo1:
    archivo1.write(str(CoordPredef))


archivo=open('CoordenadaPredefinida.txt') # abrirlo en modo lectura
datos=archivo.readlines()
print('\nEste es el valor de datos:')
print(datos)
#['6.130,-75.936,350\n', '6.143,-75.976,245\n', '6.094,-75.966,43\n', '6.244,-75.846,867']

"""
temp=list()
i=0
CoordPredef.clear()
for linea in datos:
    CoordPredef.append([])
    temp=linea.split(',')
    print('\nEste es el valor de temp')
    print(temp)
    #['6.130', '-75.936', '350\n']
    #['6.143', '-75.976', '245\n']
    #['6.094', '-75.966', '43\n']
    #['6.244', '-75.846', '867']
    CoordPredef[i].append(float(temp[0]))
    CoordPredef[i].append(float(temp[1]))
    CoordPredef[i].append(float(temp[2]))    
    i+=1
print('\nLa matriz sería')
print(CoordPredef)
#[[6.13, -75.936, 350.0], [6.143, -75.976, 245.0], [6.094, -75.966, 43.0], [6.244, -75.846, 867.0]]


"""