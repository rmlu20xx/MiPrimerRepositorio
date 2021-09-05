#Matrices: es una lista de listas que nosotros interpretamos desde el punto de vista matemático
import numpy as np

matriz1=[[1,4,5],[-5,8,9]]
print(matriz1)
#[[1, 4, 5], [-5, 8, 9]]

matriz = []
matriz1 = []

#lectura de datos para un amatriz entera
numero_filas=int(input("ingrese la cantidad ee filas : "))
numero_columnas=int(input("ingrese la cantidad de columnas : "))

""" vamos a ingresa la siguiente matriz 3x4
     [0 1 2 5
     3 4 5 7
     6 7 8 9]
"""

#**************************************************************************************************
#Creacion de la lista de listas (matriz) de datos enteros (No se usa la libreria numpy)
#**************************************************************************************************

for i in range(numero_filas): # i es el indice asociado a las filas
    matriz.append([])
    for j in range(numero_columnas): # j es el indice asociado a las colminas
        dato=int(input(f"ingrese el dato de la posicion  ({i},{j})"))
        matriz[i].append(dato)
print(matriz)
#[[0, 1, 2, 5], [3, 4, 5, 7], [6, 7, 8, 9]]
print("El maximo es ",max(matriz))
#El maximo es  [6, 7, 8, 9]

"""
#**************************************************************************************************
#En cada sublista de las listas puedo tener distintos tipos de datos (No se usa la libreria numpy)
#**************************************************************************************************

for i in range(numero_filas):
    matriz1.append([])
    nombre=input("ingrese el nombre ")
    matriz1[i].append(nombre)
    edad=int(input("ingrese la edad "))
    matriz1[i].append(edad)
    saldo=int(input("Ingrese el saldo "))
    matriz1[i].append(saldo)
print(matriz1)
#[['rafael', 43, 456], ['carlos', 45, 567]]


#**************************************************************************************************
# Menos intuitiva pero mas eficiente llenandola de None 3 x 4
#**************************************************************************************************
matriz =[None]*numero_filas
for i in range(numero_filas):
    matriz[i]=[None]*numero_columnas
print(matriz)
#[[None, None, None, None], [None, None, None, None], [None, None, None, None]]


#**************************************************************************************************
# Verion mas compacta 3 x 4
#**************************************************************************************************
matriz=[[None]*numero_columnas for i in range(numero_filas)]
print(matriz)
#[[None, None, None, None], [None, None, None, None], [None, None, None, None]]

"""

#**************************************************************************************************
# Calcular el valor mayor de la matriz
#**************************************************************************************************

mayor=None
for i in range(numero_filas):
    for j in range(numero_columnas):
        if mayor==None or matriz[i][j]>mayor:
          mayor=matriz[i][j]
          col=j
          fil=i
print("elemento mayor= ",mayor," en la posición ",fil,",",col)





#**************************************************************************************************
# Ejemplo matriz con numpy
#**************************************************************************************************

a=np.array([1,3,5,7,9])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])

print("Vector a:\n", a)
#[1 3 5 7 9]
print()
print("Matriz b:\n", b)
#[[1 2 3]
#[4 5 6]
#[7 8 9]
print(b.sum())
print(b[1,1]) #muestra los elemntos de la fila 1, columna 1
print(b[0,::-1]) #muestra los elementos de una fila alreves

