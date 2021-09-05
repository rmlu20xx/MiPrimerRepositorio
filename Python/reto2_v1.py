#Mensaje de bienvenida (RF01 - Reto1)
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
#Usuario y contraseña predefinidos (RF02 - Reto1)
Usuario=51717

#Con estas variables se determinará la acción a realizar
a=len("Cambiar contraseña")
b=len("Ingresar coordenadas actuales")
c=len("Ubicar zona wifi más cercana")
d=len("Guardar archivo con ubicación cercana")
e=len("Actualizar registros de zonas wifi desde archivo")
f=len("Elegir opción de menú favorita")

#Función que define el menu de opciones (RF01 - Reto2)
def Menu():
    print("xxxxxxxxxx Menu de opciones xxxxxxxxxxx")
    print("1.",Lista_menu[0])
    print("2.",Lista_menu[1])
    print("3.",Lista_menu[2])
    print("4.",Lista_menu[3])
    print("5.",Lista_menu[4])
    print("6. Elegir opción de menú favorita")
    print("7. Cerrar sesión")

def CambiaContrasena():
    return "Cambia Contraseña"

def IngresaCoordenada():
    return "Ingresa Coordenada"

def UbicarZona():
    return "Ubicar Zona"

def GuardarArchivo():
    return "Guardar Archivo"

def ActualizarRegistro():
    return "Actualizar Registro"

#Con esta función organizamos la opcion favorita (RF02 - Reto2)
def OpcionFavorita():
    if opcion==6:
        print("1.",Lista_menu[0])
        print("2.",Lista_menu[1])
        print("3.",Lista_menu[2])
        print("4.",Lista_menu[3])
        print("5.",Lista_menu[4])
        
        opcion1=int(input("Elija tu opción favorita = "))
  
#Funcion que me indica Opción invalida (RF01 - Reto2)
def default():
    return "Opción Invalida" 

def tarea():
    if len(Lista_menu[opcion-1])==a:
        CambiaContrasena(),
    elif len(Lista_menu[opcion-1])==b:
        IngresaCoordenada(),
    elif len(Lista_menu[opcion-1])==c:
        UbicarZona(),
    elif len(Lista_menu[opcion-1])==d:
         GuardarArchivo(),
    elif len(Lista_menu[opcion-1])==e:
        ActualizarRegistro(),
    elif len(Lista_menu[opcion-1])==f:
        OpcionFavorita(),
    "Salir"
    return 

"""
    switcher={
        1: CambiaContraseña(),
        2: IngresaCoordenada(),
        3: UbicarZona(),
        4: GuardarArchivo(),
        5: ActualizarRegistro(),
        6: OpcionFavorita(),
        7: "Salida"
    }
"""
      

#Código para invertir un numero. Con esto generamos el Password. (RF02 - Reto1)
invertir = 0
valor = int(Usuario)
while valor > 0:
    residuo = valor % 10
    invertir = (invertir * 10) + residuo
    valor //= 10
Password=invertir
#**********************************************************************************

#Se definien 2 terminos numericos para el captcha (RF03)
Termino1_Captcha=717 #Ultimos tres digitos del Usuario (RF03)
Termino2_Captcha=((7%5)*5-5-5+1 ) #Calcula el penultimo numero del usuario (RF03 - Reto1)
Suma_Captcha = Termino1_Captcha+Termino2_Captcha #Calculo del resultado de los 2 terminos de captcha (RF03 - Reto1)

try:  #Se usa captura de excepciones para indicarf al usuario el error que se produce al ingresar los datos
    Usuario1=int(input("Ingrese su usuario = "))
    if(Usuario1 != Usuario):
        print("Error") #Error al ingresar el usuario
    else:
        Password1=int(input("Ingrese el password = "))
        if(Password1 != Password):
            print("Error") #Error al ingresar al password
        else:
            #Se hace el calculo del captcha (RF03 - Reto1)  
            print("No eres un Robot Resuelve el Captcha ","( ",Termino1_Captcha," + ",Termino2_Captcha," )") #Mensaje para indicarle al usuario que ejecute el captcha
            Resultado_Captcha=int(input("El resultado del Captcha es = "))
            if (Resultado_Captcha != Suma_Captcha):
                print("Error") #Error al calcular el captcha (RF03 - Reto1)
            else:
                print("Sesión iniciada") #Mensaje de confirmación de inicio de sesión (RF04 - Reto1)
                
                #Se define una lista con las opciones que tendrán ajustes constantes (RF01 - Reto2)
                Lista_menu=["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo"]
                Menu()
                opcion=int(input("Elija una opción = "))
                print(tarea())
                
except:
    print("Error, El valor ingresado debe ser un valor numerico")

    
