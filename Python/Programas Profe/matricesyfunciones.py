# Procedimiento para llenar la matriz de notas
def leermatriz():
    for i in range(num_filas):
        matriz.append([])
        nombre=input("Nombre del estudiante: ")
        matriz[i].append(nombre)
        j=0
        for j in range(1,columnas,1):
            nota=float(input(f"Nota {j} de {nombre}: "))
            matriz[i].append(nota)
    print(matriz)

# Procedimiento para llenar la lista de notas definitivas
def calculo_nota():
    for i in range(num_filas):
        suma=0
        for j in range(1,columnas,1):
            #sumo todas las notas del estudiante
            suma+=matriz[i][j]  #suma=suma+matriz[i][j]
        #Calculo el promedio
        prom=suma/num_col
        #agregar a la lista de notas definitivas
        notadef.append(prom)
    print(" Lista de Notas definitivas")
    print(notadef)

#Menu
def menu():
    print("MENU")
    print("1- La persona con mayor nota de las notas definitivas de los estudiantes")
    print("2- La persona con menor nota de las notas definitivas de los estudiantes")
    print("3- El promedio del grupo de las notas definitivas de los estudiantes")
    print("4- La cantidad de personas con nota superior al promedio.")
    print("5- SALIR")

# Procedimiento para calcular la nota mayor
def nota_mayor():
    mayor=max(notadef)
    pos=notadef.index(mayor)
    print(matriz[pos][0]," Tiene la nota más alta. Su nota es ",mayor)

# Procedimiento para calcular la nota menor
def nota_menor():
    menor=min(notadef)
    pos=notadef.index(menor)
    print(matriz[pos][0]," Tiene la nota más baja. Su nota es ",menor)

# Función para calcular el promedio de notas definitivas
def promedio():
    prom=sum(notadef)/len(notadef)
    return prom

# Función calcular cantidad de estudiantes con notas mayores al promedio
def cantidad():
    p=promedio()
    cantidad=0
    for i in range(len(notadef)):
        if notadef[i]>p:
            cantidad+=1 # cantidad=cantidad+1
    return cantidad

# Procedimiento principal
matriz=[]
notadef=[]

# pedir datos para la matriz
num_filas=int(input("Digite la cantidad de estudiantes: "))
num_col=int(input("Digite la cantidad de notas por estudiantes: "))
columnas=num_col+1
# llamar la procedimiento para llenar la matriz
leermatriz()
# llamar el procedimiento para llenar la lista de notas definitivas
calculo_nota()

while True:
    menu()
    opcion=int(input("Seleccione la opción a utilizar: "))
    if opcion==1: #calcular la mayor nota definitiva
        nota_mayor()
    elif opcion==2:#calcular la menor nota definitiva
        nota_menor()
    elif opcion==3: #Calcular promedio de notas definitivas
        print("El promedio de notas definitivas del grupo es ",promedio())
    elif opcion==4: # Cantidad de estudiantes con notas mayores al promedio
        print("Hay ",cantidad()," de estudiantes con notas definitivas por encima del promedio",promedio())
    elif opcion==5: # opcion de salida
        print("Fin del menu")
        break
    else:
        print("Opción incorrecta")
print("Fin del programa")
