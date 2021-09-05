import csv
import pandas as pd
from io import open

print('Guarda el contenido de una archivo en una matriz')
matriz=list()
archivo=open('matriz.txt') # abrirlo en modo lectura
datos=archivo.readlines()
print('\nEste es el valor de datos:')
print(datos)
#['Hugo Lobo,1.70,75.3,45\n', 'Maria Caro,1.55,55.7,50\n', 'Paco Gutierrez,1.86,86.9,35']

temp=list()
i=0
for linea in datos:
    matriz.append([])
    temp=linea.split(',')
    print('\nEste es el valor de temp')
    print(temp)
    #['Hugo Lobo', '1.70', '75.3', '45\n']
    #['Maria Caro', '1.55', '55.7', '50\n']
    #['Paco Gutierrez', '1.86', '86.9', '35']
    matriz[i].append(temp[0])
    matriz[i].append(float(temp[1]))
    matriz[i].append(float(temp[2]))
    matriz[i].append(int(temp[3]))
    i+=1
print('\nLa matriz sería')
print(matriz)
#[['Hugo Lobo', 1.7, 75.3, 45], ['Maria Caro', 1.55, 55.7, 50], ['Paco Gutierrez', 1.86, 86.9, 35]]


# procedimiento para guardar datos en el archivo
def guardar_telefonos(n_archivo,directorio):
    archivo=open(n_archivo,'a')
    for nombre,apellido,telefono,email in directorio:
        cad=nombre+','+apellido+','+telefono+','+email+'\n'
        archivo.write(cad)

# procedimiento para mostrar los datos del archivo dir_telefonico.txt
def mostrar_telefonos(n_archivo):
    telefonos=list()
    archivo=open(n_archivo,'r')
    for linea in archivo:
        print('\n Resultado de linea.strip ')
        print(linea.split(','))
        #['Alejandro', 'Restrepo', '3007654321', 'pedro@upb.com\n']
        #['Ramon', 'Zapata', '3001234567', 'ramon@upb.com\n']
        #['Oscar', 'Aguilar', '3207654321', 'oscar@upb.com\n']
        nombre,apellido,telefono,email=linea.rstrip().split(',')
        telefonos.append((nombre,apellido,telefono,email))
    archivo.close()
    return telefonos

print('\n guardar un conjuntas de tuplas como archivo de texto con formato .csv')
directorio=[('Alejandro','Restrepo','3007654321','pedro@upb.com'),('Ramon','Zapata','3001234567','ramon@upb.com'),('Oscar','Aguilar','3207654321','oscar@upb.com')]
n_archivo='dir_telefonico.txt'
guardar_telefonos(n_archivo,directorio) # guardar los datos en el archivo
agenda=mostrar_telefonos(n_archivo)
print(agenda)
#[('Alejandro', 'Restrepo', '3007654321', 'pedro@upb.com'), ('Ramon', 'Zapata', '3001234567', 'ramon@upb.com'), ('Oscar', 'Aguilar', '3207654321', 'oscar@upb.com')]

print('guardar el contenido de un directorio en un archivo.txt')
datos_dir={'edad':45,'Cargo':'ingeniero','area':'sistemas'}
with open('base_datos1.txt','w') as archivo1:
    archivo1.write(str(datos_dir))
with open('base_datos1.txt','r') as archivo1:
    print(archivo1.read())
    #{'edad': 45, 'Cargo': 'ingeniero', 'area': 'sistemas'}

print('guardar el contenido de un directorio en un archivo.csv')
datos_dir={'edad':60,'Cargo':'tecnico','area':'produccion'}
with open('base_datos2.csv','w') as archivo2:
    almacenar=csv.writer(archivo2)
    almacenar.writerow(datos_dir.items())
with open('base_datos2.csv','r') as archivo3:
    print(archivo3.read())
    #"('edad', 60)","('Cargo', 'tecnico')","('area', 'produccion')"

