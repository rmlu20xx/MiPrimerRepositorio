# Programa que calcule la suma, la resta, la multiplicación, la división y la potencia cuadrada

#Definicion de Funciones

def Menu():
    print("xxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("1. SUMAR")
    print("2. RESTAR")
    print("3. MULTIPLICAR")
    print("4. DIVIDIR")
    print("5. ELEVAR A LA POTENCIA")
    print("6. Salir")

def Sumar(a,b): #Función Suma
    resultado = a+b
    return resultado

def Restar(a,b): #Función Resta
    resultado = a-b
    return resultado

def Multiplicar(a,b): #Función Multiplica
    resultado = a*b
    return resultado

def Dividir(a,b): #Función Dividir
    resultado = a/b
    return resultado

def Potencia(a,b): #Función Elevar potencia
    resultado = a**b
    return resultado

def default():
  return "Opción Invalida"


def switch(case,a,b):
    switcher={
        1: Sumar(a,b),
        2: Restar(a,b),
        3: Multiplicar(a,b),
        4: Dividir(a,b),
        5: Potencia(a,b),
        6: "salida",
    }
    return switcher.get(case,default())


# Inicio Programa Calculadora

try:
    a=int(input("Ingrese primer valor: "))
    b=int(input("Ingrese segundo valor: "))
    Menu()
    opcion=int(input("Seleccione la opción: "))
    print(switch(opcion,a,b))
except:
    print("Disión por cero no es posible")


