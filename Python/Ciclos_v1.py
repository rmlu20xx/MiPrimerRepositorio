""" Reescriba el código de ejercicios previos en el mismo programa, para: Saludar, Calcular si un número es par, Calcular el promedio de 5 notas, 
Calcular el módulo, Calcular el porcentaje y elevar a una potencia.
"""
#Definicion de Funciones
def Menu():
    print("1. SALUDAR")
    print("2. NUMERO PAR")
    print("3. PROMEDIO")
    print("4. MODULO")
    print("5. PORCENTAJE")
    print("6. ELEVAR POTENCIA")
    print("0. SALIR")

def Saludar(): #Función Saludar
    return "Hola a este maravilloso programa"
     

def Numero_Par(): #Función calcular si un numero es par
    a=int(input("Ingrese un numero "))
    Calculo = a%2
    if Calculo ==0:
        return "El numero ",a," ingresado es par"   
    return "El numero ",a," ingresado es impar"

def Promedio(): #Función Calcular el promedio de cinco notas
    a=int(input("Ingresa Nota 1 = "))
    b=int(input("Ingresa Nota 2 = "))
    c=int(input("Ingresa Nota 3 = "))
    d=int(input("Ingresa Nota 4 = "))
    e=int(input("Ingresa Nota 5 = "))
    resultado = (a+b+c+d+e)/5
    return "El promedio de los cincos numeros ingresados es = ", resultado

def Modulo(): #Función Calcular el modulo
    a=int(input("Ingresa Numero 1 = "))
    b=int(input("Ingresa Numero 2 = "))
    resultado = a%b
    return "El modulo entre",a,"y",b,"es =",resultado

def Porcentaje(): #Función Sacar porcentaje
    a=int(input("Ingresa Numero 1 = "))
    b=int(input("Ingresa Numero 2 = "))
    resultado = (a*b)/100
    return "El ",b," % 'de'",a, "es = ", resultado

def Elevar_Potencia(): #Función Elevar potencia
    a=int(input("Ingresa Numero 1 = "))
    b=int(input("Ingresa Numero 2 = "))
    resultado = a**b
    return "El resultado de la potencia es = ", resultado

def Salir():
    return "Has salido del sistema"

def default():
    return "Opción Invalida"


def switch(case):      
    switcher={
        1: Saludar,
        2: Numero_Par,
        3: Promedio,
        4: Modulo,
        5: Porcentaje,
        6: Elevar_Potencia,
        0: Salir, 
    }
    return switcher.get(case,default())()


# Inicio Programa Principal
i=True
try:
    while i==True:
        Menu()
        opcion=int(input("Seleccione la opción: "))
        print(switch(opcion))
        if opcion==0:
            break
except:
    print("Error, debes ingresar un valor numérico entre 0 y 6")