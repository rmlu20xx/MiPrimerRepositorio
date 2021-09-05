import time
tiempo=time.strftime("%H:%M:%S",time.localtime())
print("La hora actual en (Horas, minutos y segundos) es: ",tiempo)

tiempoh=int(input("Introduce la hora en formato militar: "))


if tiempoh < 12:
    print("Buenos dias")
if 12<=tiempoh<18:
    print("Buenas tardes")
if tiempoh>18:
    print("Buenas noches")
