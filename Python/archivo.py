import math
# Libreria necesaria para el manejo de archivos
from io import open

#Ingresar datos en un archivo
def abrir_archivo():
    while True:
        radio=float(input('Digita el valor del radio: '))
        #abrir archivo para adicionar datos
        archivo=open('d:/OneDriveLuna/OneDrive/ESTUDIO/MINTIC/Fundamentos_Programacion/Python/nuevo.txt','a')

        perimetro=math.pi*2*radio
        cad1="Perimetro del circulo es"+str('{0:.2f}').format(perimetro)+'\n'
        archivo.write(cad1)
        area=math.pi*radio**2
        cad2="Area del circulo es"+str('{0:.2f}').format(area)+'\n'
        archivo.write(cad2)

        op=int(input("Digite 1 si desea continuar ingresando datos de lo contrario, digita cualquier numero "))
        if op!=1:
            break

#Mostrar los datos de un archivo
def mostrar_archivo():
    archivo=open('nuevo.txt')

#secuencia principal
print("Ingresar datos en un archivo")
abrir_archivo()
