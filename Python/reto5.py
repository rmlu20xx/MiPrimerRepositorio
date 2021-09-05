from os import system
import math
import csv
import pandas as pd
from io import open

#Declaro variables Globales
#Se define una lista con las opciones que tendrán ajustes constantes (RF01 - Reto2)
Lista_menu=["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo"]
j=False
Password=None
numero_coordenadas=3  #Define la cantidad de coordenas
matriz=[]
lista_Dist=[]
CoordPredef=[[6.124,-75.946,1035],[6.125,-75.966,109],[6.135,-75.976,31],[6.144,-75.836,151]] #Coordenadas predefinidas (RF01 - Reto4)
lat1=0
lon1=0
zona_wifi1=[]
recorrido=[]


#Mensaje de bienvenida (RF01 - Reto1)
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
#Usuario y contraseña predefinidos (RF02 - Reto1)
Usuario=str(51717)
Password=Usuario[::-1] #Código para invertir una cadena. Con esto generamos el Password. (RF02 - Reto1)

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


#Con esta función organizamos la contraseña (RF01 - Reto3)
def CambiaContrasena():
    global Password
    print("Usted ha elegido la opción Cambiar Contraseña")
    Password_Acceso=input("Ingrese su contraseña actual : ")
    if  Password_Acceso==Password:
        while True:
            NewPassword=input ("Ingrese la nueva contraseña : ")
            if NewPassword==Password:
                print("La contraseña no debe ser igual a la anterior, ingrese otro valor ")
            else:
                ConfirmPassword=input("Confirme su nueva contraseña : ")
                if ConfirmPassword==NewPassword:
                    Password = NewPassword
                    print("Su contraseña ha sido camnbiada satisfactoriamente ")
                    break
                else: 
                    exit(print("Error"))
    else:
       exit(print("Error"))               

#Con esta función ingresamos las coordenadas actuales (RF02 - Reto3)
def IngresaCoordenada():
    global matriz, numero_coordenadas
    actualizar=0
    print("Usted ha elegido la opción Ingresar coordenadas actuales")
          
    if matriz==[]:       
        
        for i in range(numero_coordenadas):
            matriz.append([])
            try:
                latitud=float(input(f"ingrese la latitud de la coordenada {i+1} : "))
            except: print("Error")
            if latitud<6.077 or latitud>6.284:
                exit(print("Error coordenada"))
            else:
                matriz[i].append(latitud)
            try:
                longitud=float(input(f"ingrese la longitud de la coordenada {i+1} : "))
            except: print("Error")
            if longitud<-76.049 or longitud>-75.841:
                exit(print("Error coordenada"))
            else:
                matriz[i].append(longitud)
        print(matriz)
        
    else:
        #El sistema debe mostrar informacion clave sobre las coordenadas ((RF03 - Reto3))
        print("coordenada [latitud,longitud] 1 :",matriz[0])
        print("coordenada [latitud,longitud] 2 :",matriz[1])
        print("coordenada [latitud,longitud] 3 :",matriz[2])
        #Lista_Latitud=[matriz[0][0],matriz[1][0],matriz[2][0]]
        Lista_Longitud=[matriz[0][1],matriz[1][1],matriz[2][1]]
        #Lista_Latitud_min=min(Lista_Latitud)
        #Lista_Latitud_max=max(Lista_Latitud)
        Lista_Longitud_min=min(Lista_Longitud)
        Lista_Longitud_max=max(Lista_Longitud)
        print("la coordenada ",Lista_Longitud.index(Lista_Longitud_max)+1,"es la que está más al oriente")
        print("la coordenada ",Lista_Longitud.index(Lista_Longitud_min)+1,"es la que está más al occidente")

        #El programa permite actualizar las coordenadas de los tres sitios mas frecuentados ((RF03 - Reto3))
        actualizar=int(input("Presiona 1,2 o 3 para actualizar la respectiva coordenada\npresiona 0 para regresar al menu "))
        if actualizar in [1,2,3]:
            numero_coordenadas=1
            try:
                latitud=float(input(f"ingrese la latitud de la coordenada {actualizar} : "))
            except: print("Error")
            if latitud<6.077 or latitud>6.284:
                exit(print("Error coordenada"))
            else:                
                try:
                    longitud=float(input(f"ingrese la longitud de la coordenada {actualizar} : "))
                except: print("Error")
                if longitud<-76.049 or longitud>-75.841:
                    exit(print("Error coordenada"))
                else:
                    del matriz[actualizar-1]
                    matriz.insert(actualizar-1,[latitud,longitud])
                    print(matriz)
        elif actualizar==0: return
        else:exit(print("Error actualización"))


#Funcion que permite calcular la distancia entre dos puntos (RF02 - Reto4)
def Distancia(lat1,lat2,lon1,lon2):
    R=6372.795477598 #radio de la tierra
    Dist=2*R*math.asin(math.sqrt((math.sin(math.radians(lat2-lat1)))**2+math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*(math.sin(math.radians(lon2-lon1)))**2))
    return round(Dist,3) #Limita el resultado a 3 decimales

#Con esta función ubicamos la zona mas cercana (RF02 - Reto4)
def UbicarZona():
    global matriz, lista_Dist,lat1,lon1,zona_wifi1,recorrido
    if matriz!=[]:
        print("Usted ha elegido la opción ubicar zona wifi más cercana")
        print("coordenada [latitud,longitud] 1 :",matriz[0])
        print("coordenada [latitud,longitud] 2 :",matriz[1])
        print("coordenada [latitud,longitud] 3 :",matriz[2])
                
        UbicActual=int(input("Por favor elija su ubicación actual (1,2 o 3) para calcular la distancia a los puntos de conexión "))
        if UbicActual in [1,2,3]:
            #print("La ubicacion actual es", matriz[UbicActual-1])
            lat1=matriz[UbicActual-1][0]
            lon1=matriz[UbicActual-1][1]
            lista_Dist=[]
            for i in range(len(CoordPredef)):                
                lat2=CoordPredef[i][0]
                lon2=CoordPredef[i][1]
                Dist=Distancia(lat1,lat2,lon1,lon2)
                lista_Dist.append(Dist) #Organizo la lista con las cuatro distancias calculadas
            #print("Las distancias son ", lista_Dist )
            lista_Dist_Backup=list(lista_Dist)  #Guardo una copia de la lista de las distancias
            lista_Dist.sort() #Organizo las distnacias de menor a mayor y asi saber las 2 de menor de distancia
            zona_cercana1=lista_Dist.index(lista_Dist_Backup[0])+1
            zona_cercana2=lista_Dist.index(lista_Dist_Backup[1])+1
            print("Zonas wifi cercanas con menos usuarios")
            if CoordPredef[zona_cercana1-1][2]<CoordPredef[zona_cercana2-1][2]:
                print("La zona wifi 1: ubicada en",[CoordPredef[zona_cercana1-1][0],CoordPredef[zona_cercana1-1][1]],"a",lista_Dist_Backup[0],"metros, tiene en promedio",CoordPredef[zona_cercana1-1][2],"usuarios")
                print("La zona wifi 2: ubicada en",[CoordPredef[zona_cercana2-1][0],CoordPredef[zona_cercana2-1][1]],"a",lista_Dist_Backup[1],"metros, tiene en promedio",CoordPredef[zona_cercana2-1][2],"usuarios")
                zona_wifi=[[CoordPredef[zona_cercana1-1][0],CoordPredef[zona_cercana1-1][1],CoordPredef[zona_cercana1-1][2],lista_Dist_Backup[0]],[CoordPredef[zona_cercana2-1][0],CoordPredef[zona_cercana2-1][1],CoordPredef[zona_cercana2-1][2],lista_Dist_Backup[1]]]
            else:
                print("La zona wifi 2: ubicada en",[CoordPredef[zona_cercana2-1][0],CoordPredef[zona_cercana2-1][1]],"a",lista_Dist_Backup[1],"metros, tiene en promedio",CoordPredef[zona_cercana2-1][2],"usuarios")
                print("La zona wifi 1: ubicada en",[CoordPredef[zona_cercana1-1][0],CoordPredef[zona_cercana1-1][1]],"a",lista_Dist_Backup[0],"metros, tiene en promedio",CoordPredef[zona_cercana1-1][2],"usuarios")
                zona_wifi=[[CoordPredef[zona_cercana2-1][0],CoordPredef[zona_cercana2-1][1],CoordPredef[zona_cercana2-1][2],lista_Dist_Backup[1]],[CoordPredef[zona_cercana1-1][0],CoordPredef[zona_cercana1-1][1],CoordPredef[zona_cercana1-1][2],lista_Dist_Backup[0]]]
            IndicacionLlegada=int(input("Elija 1 o 2 para recibir indicaciones de llegada "))
            velocidad_pie=0.483 #m/s
            velocidad_auto=20.83 #m/s
            if IndicacionLlegada in [1,2]:
               if IndicacionLlegada==1:
                tiempo_pie=round((zona_wifi[0][3])/velocidad_pie,3)
                tiempo_auto=round((zona_wifi[0][3])/velocidad_auto,3)
                zona_wifi1=[zona_wifi[0][0],zona_wifi[0][1],zona_wifi[0][2],zona_wifi[0][3]] #[latiud, longitud, usuarios]
                if (lat1<zona_wifi[0][0])and(lon1<zona_wifi[0][1]):
                    print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia al norte")
                elif (lat1<zona_wifi[0][0])and(lon1>zona_wifi[0][1]):
                    print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia al norte")
                elif (lat1>zona_wifi[0][0])and(lon1>zona_wifi[0][1]):
                    print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia al sur")
                elif (lat1>zona_wifi[0][0])and(lon1<zona_wifi[0][1]):
                    print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia al sur")  
                print("El tiempo a pie es :",tiempo_pie,"El tiempo auto es :",tiempo_auto)
                recorrido=[zona_wifi[0][3],'a pie',tiempo_pie,'en auto',tiempo_auto] #[distancia,pie,tiempo pie,auto,tiempo auto]
                salida=int(input("Presione 0 para salir "))
                if salida==0:
                    return
            if IndicacionLlegada==2:
                tiempo_pie=round((zona_wifi[1][3])/velocidad_pie,3)
                tiempo_auto=round((zona_wifi[1][3])/velocidad_auto,3)
                zona_wifi1=[zona_wifi[1][0],zona_wifi[1][1],zona_wifi[1][2],zona_wifi[1][3]] #[latiud, longitud, usuarios]
                if (lat1<zona_wifi[1][0])and(lon1<zona_wifi[1][1]):
                    print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia al norte")
                elif (lat1<zona_wifi[1][0])and(lon1>zona_wifi[1][1]):
                    print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia al norte")
                elif (lat1>zona_wifi[1][0])and(lon1>zona_wifi[1][1]):
                    print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia al sur")
                elif (lat1>zona_wifi[1][0])and(lon1<zona_wifi[1][1]):
                    print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia al sur")
                print("El tiempo a pie es :",tiempo_pie,"El tiempo auto es :",tiempo_auto) 
                recorrido=[zona_wifi[1][3],'a pie',tiempo_pie,'en auto',tiempo_auto] #[distancia,pie,tiempo pie,auto,tiempo auto]               
                salida=int(input("Presione 0 para salir "))
                if salida==0:
                    return
            else:exit(print("Error zona wifi"))           
        else:exit(print("Error ubicación"))
    else:
        exit(print("Error sin registro de coordenadas"))

#Con esta función guardamos el archivo del resultado del reto 4 (RF01 - Reto5)
def GuardarArchivo():
    global matriz,lista_Dist,zona_wifi1
    if matriz!=[] and lista_Dist!=[]:
        print("Usted ha elegido la opción ubicar zona wifi más cercana")
        informacion={'actual':[['latitud',lat1],['longitud',lon1]],'Zonawifi1':[['latitud',zona_wifi1[0]],['longitud',zona_wifi1[1]],['usuarios',zona_wifi1[2]]],'recorrido':[['distancia',recorrido[0]],['medio 1',recorrido[1]],['tiempo (s)',recorrido[2]],['medio 2',recorrido[3]],['tiempo (s)',recorrido[4]]]}
        print(informacion)
        confirmacion=None
        while confirmacion !=1 or confirmacion!=0:
            confirmacion=int(input("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menu principal "))
            if confirmacion==1:
                print("Exportando archivo")
                with open('coordenada.txt','w') as archivo1:
                    archivo1.write(str(informacion))
                exit()
                #with open('coordenada.txt','r') as archivo1:
                    #print(archivo1.read()) 
            if confirmacion==0:
                return           
    else:
        exit(print("Error de alistamiento"))

#Con esta función actualizamos los registros de las zonas definidas en el reto 4 (RF02 - Reto5)   
def ActualizarRegistro():
    global CoordPredef
    print("Actualizar registros de zonas wifi desde archivo")
    
    archivo=open('CoordenadaPredefinida.txt') # abrirlo en modo lectura
    datos=archivo.readlines()
    
    temp=list()
    i=0
    CoordPredef.clear()
    for linea in datos:
        CoordPredef.append([])
        temp=linea.split(',')
        CoordPredef[i].append(float(temp[0]))
        CoordPredef[i].append(float(temp[1]))
        CoordPredef[i].append(float(temp[2]))    
        i+=1
    while True:
        regresar=int(input("Datos de coordenadas para zonas wifi actualizados, presiona 0 para regresar al menu principal "))
        if regresar==0:     
            return  
    
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
        if opcion1<=0 or opcion1 > 5: #El programa deberá mostrar el mensaje “Error” si el usuario elige una opción incorrecta (número diferente entre 1 y 5) y finalizar la ejecución del programa.(RF02 - Reto2)
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
        
#Se definien 2 terminos numericos para el captcha (RF03)
Termino1_Captcha=717 #Ultimos tres digitos del Usuario (RF03)
Termino2_Captcha=((7%5)*5-5-5+1 ) #Calcula el penultimo numero del usuario (RF03 - Reto1)
Suma_Captcha = Termino1_Captcha+Termino2_Captcha #Calculo del resultado de los 2 terminos de captcha (RF03 - Reto1)


Usuario1=(input("Ingrese su usuario = "))
if(Usuario1 != Usuario):
    print("Error") #Error al ingresar el usuario
else:
    Password1=input("Ingrese el password = ")
    if(Password1 != Password):
        print("Error") #Error al ingresar al password
    else:
        #Se hace el calculo del captcha (RF03 - Reto1)  
        print("No eres un Robot Resuelve el Captcha ","( ",Termino1_Captcha," + ",Termino2_Captcha," )") #Mensaje para indicarle al usuario que ejecute el captcha
        try:
            Resultado_Captcha=int(input("El resultado del Captcha es = "))
        except: print("Error, El valor ingresado debe ser un valor numerico")
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
                    try:
                        opcion=int(input("Elija una opción = "))
                    except: print("Error, El valor ingresado debe ser un valor numerico")
                    if opcion<=0 or opcion > 7:
                        i+=1
                        print("Error")
                    if 0<opcion<=5: #El programa permite acceder a las opciones del menú (RF04 - Reto2)
                        i=0
                        if len(Lista_menu[opcion-1])==len("Cambiar contraseña"):
                            CambiaContrasena()                                    
                        elif len(Lista_menu[opcion-1])==len("Ingresar coordenadas actuales"):
                            IngresaCoordenada()                                 
                        elif len(Lista_menu[opcion-1])==len("Ubicar zona wifi más cercana"):
                            UbicarZona() 
                        elif len(Lista_menu[opcion-1])==len("Guardar archivo con ubicación cercana"):
                            GuardarArchivo()                             
                        elif len(Lista_menu[opcion-1])==len("Actualizar registros de zonas wifi desde archivo"):
                            ActualizarRegistro()                             
                    elif (opcion == 6):
                        i=0
                        OpcionFavorita()
                    elif (opcion == 7): #El programa permite al usuario salir del menú. (RF05 - Reto2)
                        print("Hasta pronto")
                        break
            

    

    
