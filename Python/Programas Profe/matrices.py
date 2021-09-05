matriz = []   # matriz [[5,4],[5,20],[10,1]]
matriz1 = []

#lectura de datos para una matriz entera
numero_filas=int(input("ingrese la cantidad de filas: ")) # 3 filas - Cuántas sublistas se van a crear
numero_columnas=int(input("ingrese la cantidad de columnas: ")) # 2 columnas - Cuántos elementos tiene cada sublistas

# Creación de la lista de listas (matriz) de datos enteros
for i in range(numero_filas): # i es el índice asociado a las filas
    matriz.append([])
    for j in range(numero_columnas): # j es el índice asociado a las columnas
        #print("Posición (",i,",",j,")")
        dato=int(input(f"ingrese el dato de la posición ({i},{j})"))
        matriz[i].append(dato)
print(matriz)

print('El máximo es ',max(matriz))

'''
# En cada sublista de las listas puedo tener distintos tipos de datos
for i in range(numero_filas):
    print("Fila :",i)
    matriz1.append([])
    nombre=input("ingrese el nombre ")
    matriz1[i].append(nombre)
    edad=int(input("ingrese la edad "))
    matriz1[i].append(edad)
    saldo=float(input("Ingrese su saldo "))
    matriz1[i].append(saldo)
print(matriz1)

# Menos intuitiva pero mas eficiente llenadola de none
matriz = [None] * numero_filas
for i in range(numero_filas):
    matriz[i] = [None] * numero_columnas
print(matriz)

# Versión mas compacta
matriz = [[None] * numero_columnas for i in range(numero_filas)]
print(matriz)
'''
# Calcular el mayor de la matriz
mayor=None
for i in range(numero_filas):
    for j in range(numero_columnas):
        if mayor==None or matriz[i][j]>mayor:
          mayor=matriz[i][j]
          col=j
          fil=i
print("elemento mayor= ",mayor," en la posición ",fil,",",col)

m=[["maria",24,30000],["Pedro",35,100000],["Martha",40,250457]]
print(m)
