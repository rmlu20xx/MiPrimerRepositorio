import math
#import codecs
# Librería necesaria para el manejo de archivos
from io import open

# Ingresar datos en un archivo
def abrir_archivo():
    while True:
        radio=float(input('\nDigite el valor del radio: '))
        # abrir archivo para adicionar datos
        archivo=open('nuevo.txt','a')
        
        perimetro=math.pi*2*radio
        cad1="Perimetro del circulo es "+str('{0:.2f}').format(perimetro)+'\n'
        archivo.write(cad1)
        area=math.pi*radio**2
        cad2="Area del circulo es "+str('{0:.2f}').format(area)+'\n'
        archivo.write(cad2)

        op=int(input("Digite 1 si desea continuar ingresando datos. de lo contrario, digite cualquier número "))
        if op!=1:
            break

# Mostrar los datos de un archivo
def mostrar_archivo():
    archivo=open('nuevo.txt','r')
    contenido=archivo.readlines()
    print('El contenido del archivo es:')
    print(contenido)
    archivo.close()

# Adicionar datos en un archivo
def adicionar_archivo():
    archivo=open('nuevo.txt','a')
    nuevo_dato=['Perimetro del circulo es 10\n','Area del circulo es 10\n','Perimetro del circulo es 15\n','Area del circulo es 15\n']
    archivo.writelines(nuevo_dato)

#Modificar una linea dada, teniendo en cuenta el índice
def modificar_linea():
    archivo=open('nuevo.txt','r+') #modo lectura y escritura
    contenido=archivo.readlines() #descargando el contenido del archivo en la variable contenido
    contenido[2]='Esto debe aparecer en la linea 3\n'
    archivo.seek(0) # colocar el puntero del archivo al inicio del archivo
    archivo.writelines(contenido) #cargar los datos modificados de nuevo al archivo
    archivo.close

# Contar líneas de un archivo
def contar_linea():
    archivo=open('nuevo.txt')
    cantidad_lineas=0
    for linea in archivo:
        cantidad_lineas+=1
    return cantidad_lineas

#mostrar las líneas que inician con Area
def buscar_palabra():
    archivo=open('nuevo.txt')
    for linea in archivo:
        if linea.startswith('Area'):
            print(linea)

#mostrar las líneas que inician con Area sin fin de línea
def buscar_palabra_sin_fin():
    archivo=open('nuevo.txt')
    for linea in archivo:
        linea=linea.rstrip() # quitar los fin de línea
        if not linea.endswith('5'):
            continue
        print(linea)

#mostrar las líneas que inician con Area sin fin de línea
def buscar_palabra_linea():
    archivo=open('nuevo.txt')
    for linea in archivo:
        linea=linea.rstrip() # quitar los fin de línea
        if linea.find('metro')==-1: # esa línea no inlcuye metro
            continue
        print(linea)

# secuencia principal
print("Ingresar datos en un archivo")
abrir_archivo()

print("\nMostrar los datos de un archivo")
mostrar_archivo()

print("\nAdicionar datos de un archivo")
adicionar_archivo()
mostrar_archivo()

print('\nModificar una linea dada, teniendo en cuenta el índice')
modificar_linea()
mostrar_archivo()

print('\nEl archivo tiene ',contar_linea(),' líneas')

print('\nLíneas que empiezan con Area')
buscar_palabra()

print('\nLíneas que terminan con 5 sin espacio')
buscar_palabra_sin_fin()

print('\nLíneas que incluyen metro sin espacio')
buscar_palabra_linea()