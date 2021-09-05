from os import system
#Declaro variables Globales
#Se define una lista con las opciones que tendrán ajustes constantes (RF01 - Reto2)
Lista_menu=["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo"]
j=False

#Mensaje de bienvenida (RF01 - Reto1)
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
#Usuario y contraseña predefinidos (RF02 - Reto1)
Usuario=str(51717)

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

"""
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
"""
#Con esta función organizamos la opcion favorita (RF02 - Reto2)
def OpcionFavorita():
    global j,Lista_menu
    if opcion==6:
        print("1.",Lista_menu[0])
        print("2.",Lista_menu[1])
        print("3.",Lista_menu[2])
        print("4.",Lista_menu[3])
        print("5.",Lista_menu[4])
        opcion1=int(input("Seleccione opción favorita = "))        
        if opcion1>5: #El programa deberá mostrar el mensaje “Error” si el usuario elige una opción incorrecta (número diferente entre 1 y 5) y finalizar la ejecución del programa.(RF02 - Reto2)
            print("Error")
            j=True
            return            
        else: #Confirmación deberá ser diseñada con dos adivinanzas en pantalla que tengan como respuesta las últimas dos cifras del Usuario (RF02 - Reto2)
            adivinanza1=input("Para confirmar por favor responda: Estoy entre el 2 y el 0, la respuesta es : ")
            if adivinanza1==Usuario[len(Usuario)-2]:
                adivinanza2=input("Para confirmar por favor responda: Estoy entre el 8 y el 6, la respuesta es : = ")
                if adivinanza2==Usuario[len(Usuario)-1]:
                    a=Lista_menu.pop(opcion1-1)
                    Lista_menu.insert(0,a)
                    system("cls")
                    return
                print("Error")
                return
            print("Error")
            return
        

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
    Usuario1=(input("Ingrese su usuario = "))
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
                
                i=0 #Esta variable permite llevar el conteo de errores consecutivos al escojer la opción (RF03 - Reto2)
                while i!=3: #El programa genera una alerta si el usuario elige una opción incorrecta. (RF03 - Reto2)
                    if j==True: #El programa deberá mostrar el mensaje “Error” si el usuario elige una opción incorrecta (número diferente entre 1 y 5) y finalizar la ejecución del programa.(RF02 - Reto2)
                        break
                    else:
                        Menu()
                        opcion=int(input("Elija una opción = "))
                        if opcion<=0 or opcion > 7:
                            i+=1
                            print("Error")
                        if 0<opcion<=5: #El programa permite acceder a las opciones del menú (RF04 - Reto2)
                            i=0
                            if len(Lista_menu[opcion-1])==len("Cambiar contraseña"):
                                print("Usted ha elegido la opción",opcion)
                                break     
                            elif len(Lista_menu[opcion-1])==len("Ingresar coordenadas actuales"):
                                print("Usted ha elegido la opción",opcion)
                                break  
                            elif len(Lista_menu[opcion-1])==len("Ubicar zona wifi más cercana"):
                                print("Usted ha elegido la opción",opcion)
                                break  
                            elif len(Lista_menu[opcion-1])==len("Guardar archivo con ubicación cercana"):
                                print("Usted ha elegido la opción",opcion)
                                break  
                            elif len(Lista_menu[opcion-1])==len("Actualizar registros de zonas wifi desde archivo"):
                                print("Usted ha elegido la opción",opcion)
                                break  
                        elif (opcion == 6):
                            i=0
                            OpcionFavorita()
                        elif (opcion == 7): #El programa permite al usuario salir del menú. (RF05 - Reto2)
                            print("Hasta pronto")
                            break
            
except:
    print("Error, El valor ingresado debe ser un valor numerico")

    
