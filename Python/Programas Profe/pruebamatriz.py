
matriz = []
nd=list() #Lista de notas definitivas de cada estudiante

#lectura de datos para una matriz entera
numero_filas=int(input("ingrese la cantidad de estudiantes: "))
numero_columnas=int(input("ingrese la cantidad de notas que tomo al grupo: "))
notas=numero_columnas+1
for i in range(numero_filas):
    j=0
    matriz.append([])
    nombre=input("ingrese el nombre ")
    matriz[i].append(nombre)
    for j in range(1,notas,1):
        nota=float(input("ingrese la nota "))
        matriz[i].append(nota)
print(matriz)

#Menu
def menu():
    print("MENU")
    print("1- La persona con mayor nota de las notas definitivas de los estudiantes")
    print("2- La persona con menor nota de las notas definitivas de los estudiantes")
    print("3- El promedio del grupo de las notas definitivas de los estudiantes")
    print("4- La cantidad de personas con nota superior al promedio.")
    print("5- SALIR")

#Calculo de notas definitivas por estudiante (promedio)
for i in range(numero_filas):
    suma=0
    for j in range(1,notas,1):
        suma+=matriz[i][j]
    p=suma/numero_columnas
    nd.append(p)
print(nd)

while 6:
    menu()
    op=int(input("Por favor digite la opción deseada..."))
    if op==1:
        #nombre y nota de estudiante con mayor nota definitiva
        mayor=max(nd)
        pos=nd.index(mayor)
        print("El estudiante con mayor nota definitiva es ",matriz[pos][0], "su nota es ",mayor)
    elif op==2:
        #nombre y nota de estudiante con menor nota definitiva
        menor=min(nd)
        pos=nd.index(menor)
        print("El estudiante con menor nota definitiva es ",matriz[pos][0], "su nota es ",menor)
    elif op==3:
        #Promedio de notas definitivas de los estudiantes
        prom=float(sum(nd)/len(nd))
        print(prom)
    elif op==4:
        #cantidad de estudiantes con notas definitivas por encima del promedio
        prom=float(sum(nd)/len(nd))
        c=0
        for i in range(len(nd)):
            if nd[i]>prom:
                c+=1
        print("Hay ",c," estudiantes con notas por encima de ",prom)
    elif op==5:
        print("Fin del Programa.")
        break
        #exit()
    else:
        print("Opción incorrecta")
print("Gracias por utilizar el programa")
