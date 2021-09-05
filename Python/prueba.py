import math
Dist=0
#matriz=[[5,4],[3,20],[8,2]]

#oriente=(max(matriz[0][1],matriz[1][1],matriz[2][1]))
#occidente=(min(matriz[0][1],matriz[1][1],matriz[2][1]))
#j=0

CoordPredef=[[6.124,-75.946,1035],[6.125,-75.966,109],[6.135,-75.976,31],[6.144,-75.836,151]]
print(CoordPredef)
#print(CoordPredef)
#print(CoordPredef[0])
#print(CoordPredef[1])
#print(CoordPredef[2])
#print(CoordPredef[3])

def Distancia(lat1,lat2,lon1,lon2):
    R=6372.795477598 #radio de la tierra
    Dist=2*R*math.asin(math.sqrt((math.sin(lat2-lat1))**2+math.cos(lat1)*math.cos(lat2)*(math.sin(lon2-lon1))**2))
    return round(Dist,3) #Limita el resultado a 3 decimales

"""
a=CoordPredef[0][0]
b=CoordPredef[1][0]
c=CoordPredef[0][1]
d=CoordPredef[1][1]

print("La distancia es ",Distancia(a,b,c,d))
"""

lat1=6.284
lon1=-75.841
lista_Dist=[]
for i in range(len(CoordPredef)):                
    lat2=CoordPredef[i][0]
    lon2=CoordPredef[i][1]
    Dist=Distancia(lat1,lat2,lon1,lon2)
    lista_Dist.append(Dist)
print("Las distancias son ", lista_Dist )
#lista_Dist.sort()
#print(lista_Dist)
lista_Dist_Backup=list(lista_Dist)
lista_Dist_Backup.sort()
#print("Zonas cercanas ",lista_Dist.index(lista_Dist_Backup[0])+1,lista_Dist.index(lista_Dist_Backup[1])+1)
zona_cercana1=lista_Dist.index(lista_Dist_Backup[0])+1
zona_cercana2=lista_Dist.index(lista_Dist_Backup[1])+1
print("Zonas wifi cercanas con menos usuarios")
if CoordPredef[zona_cercana1-1][2]<CoordPredef[zona_cercana2-1][2]:
    print("La zona wifi 1: ubicada en",[CoordPredef[zona_cercana1-1][0],CoordPredef[zona_cercana1-1][1]],"a",lista_Dist_Backup[0],"metros, tiene en promedio",CoordPredef[zona_cercana1-1][2],"usuarios")
    print("La zona wifi 2: ubicada en",[CoordPredef[zona_cercana2-1][0],CoordPredef[zona_cercana2-1][1]],"a",lista_Dist_Backup[1],"metros, tiene en promedio",CoordPredef[zona_cercana2-1][2],"usuarios")
    zona_wifi=[[CoordPredef[zona_cercana1-1][0],CoordPredef[zona_cercana1-1][1],lista_Dist_Backup[0]],[CoordPredef[zona_cercana2-1][0],CoordPredef[zona_cercana2-1][1],lista_Dist_Backup[1]]]
else:
    print("La zona wifi 2: ubicada en",[CoordPredef[zona_cercana2-1][0],CoordPredef[zona_cercana2-1][1]],"a",lista_Dist_Backup[1],"metros, tiene en promedio",CoordPredef[zona_cercana2-1][2],"usuarios")
    print("La zona wifi 1: ubicada en",[CoordPredef[zona_cercana1-1][0],CoordPredef[zona_cercana1-1][1]],"a",lista_Dist_Backup[0],"metros, tiene en promedio",CoordPredef[zona_cercana1-1][2],"usuarios")
    zona_wifi=[[CoordPredef[zona_cercana2-1][0],CoordPredef[zona_cercana2-1][1],lista_Dist_Backup[1]],[CoordPredef[zona_cercana1-1][0],CoordPredef[zona_cercana1-1][1],lista_Dist_Backup[0]]]
IndicacionLlegada=int(input("Elija 1 o 2 para recibir indicaciones de llegada "))
velocidad_pie=0.483 #m/s
velocidad_auto=20.83 #m/s
if IndicacionLlegada in [1,2]:
    if IndicacionLlegada==1:
        tiempo_pie=round((zona_wifi[0][2])/velocidad_pie,3)
        tiempo_auto=round((zona_wifi[0][2])/velocidad_auto,3)
        if (lat1<zona_wifi[0][0])and(lon1<zona_wifi[0][1]):
            print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia al norte")
        elif (lat1<zona_wifi[0][0])and(lon1>zona_wifi[0][1]):
            print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia al norte")
        elif (lat1>zona_wifi[0][0])and(lon1>zona_wifi[0][1]):
            print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia al sur")
        elif (lat1>zona_wifi[0][0])and(lon1<zona_wifi[0][1]):
            print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia al sur")  
        print("El tiempo a pie es :",tiempo_pie,"El tiempo auto es :",tiempo_auto)
    else:
        tiempo_pie=round((zona_wifi[1][2])/velocidad_pie,3)
        tiempo_auto=round((zona_wifi[1][2])/velocidad_auto,3)
        if (lat1<zona_wifi[1][0])and(lon1<zona_wifi[1][1]):
            print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia al norte")
        elif (lat1<zona_wifi[1][0])and(lon1>zona_wifi[1][1]):
            print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia al norte")
        elif (lat1>zona_wifi[1][0])and(lon1>zona_wifi[1][1]):
            print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia al sur")
        elif (lat1>zona_wifi[1][0])and(lon1<zona_wifi[1][1]):
            print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia al sur")
        print("El tiempo a pie es :",tiempo_pie,"El tiempo auto es :",tiempo_auto)
    salida=int(input("Presione 0 para salir "))
    if salida==0:
        print("retornar al menu principal")
else:exit(print("Error zona wifi"))




"""
datos=enumerate(matriz)
print("La posicion",(list(datos)[0])[0])
#a=list(datos)[0]
#print(list(a))
"""