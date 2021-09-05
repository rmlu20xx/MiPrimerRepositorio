
matriz = []
notadef=list() #Lista de notas definitivas de cada estudiante

#*************************************************************************************************
#Funciones
#*************************************************************************************************

# Menu de opciones

def menu():
    print("MENU")
    print("1- La persona con mayor nota de las notas definitivas de los estudiantes")
    print("2- La persona con menor nota de las notas definitivas de los estudiantes")
    print("3- El promedio del grupo de las notas definitivas de los estudiantes")
    print("4- La cantidad de personas con nota superior al promedio.")
    print("5- SALIR")

# Procedimiento para construri la matriz

def OrganizarMatriz(estudiantes,notas):
    for i in range(estudiantes):
        j=0
        matriz.append([])
        nombre=input("ingrese el nombre del estudiante ")
        matriz[i].append(nombre)
        for j in range(1,notas,1):
            nota=float(input(f"Nota {j} de {nombre} : "))
            matriz[i].append(nota)
    print(matriz)


# Procedimiento para llenar la lista de notas definitivas

def CalculoNota(estudiantes,notas):
    for i in range(estudiantes):
        suma=0
        for j in range(1,notas,1):
            suma+=matriz[i][j]
        p=suma/numero_columnas
        notadef.append(p)
    print(notadef)

#lectura de datos para una matriz entera
numero_filas=int(input("ingrese la cantidad de estudiantes: "))
numero_columnas=int(input("ingrese la cantidad de notas que tomo al grupo: "))
notas=numero_columnas+1

OrganizarMatriz(numero_filas,notas) #Llamo la funcion para organizar la matriz
CalculoNota(numero_filas,notas) #Llamo la funcion Calculo de notas definitivas por estudiante (promedio)

while True:
    menu()
    op=int(input("Por favor digite la opción deseada..."))
    if op==1:
        #nombre y nota de estudiante con mayor nota definitiva
        mayor=max(notadef)
        pos=notadef.index(mayor)
        print("El estudiante con mayor nota definitiva es ",matriz[pos][0], "su nota es ",mayor)
    elif op==2:
        #nombre y nota de estudiante con menor nota definitiva
        menor=min(notadef)
        pos=notadef.index(menor)
        print("El estudiante con menor nota definitiva es ",matriz[pos][0], "su nota es ",menor)
    elif op==3:
        #Promedio de notas definitivas de los estudiantes
        prom=float(sum(notadef)/len(notadef))
        print(prom)
    elif op==4:
        #cantidad de estudiantes con notas definitivas por encima del promedio
        prom=float(sum(notadef)/len(notadef))
        c=0
        for i in range(len(notadef)):
            if notadef[i]>prom:
                c+=1
        print("Hay ",c," estudiantes con notas por encima de ",prom)
    elif op==5:
        print("Fin del Programa.")
        break
        #exit()
    else:
        print("Opción incorrecta")
print("Gracias por utilizar el programa")
