from os import system
'''
# Muestra una letra de la cadena
fruta="banana"
letra=fruta[0]
print(letra)

# longitud de la cadena
longitud=len(fruta)
print(longitud)

#Última letra
ultima=fruta[longitud-1]
print(ultima)

# Recorrer una cadena
indice=0
while indice<longitud:
    letra=fruta[indice]
    print(letra)
    indice+=1

for caracter in fruta:
    print(caracter)

# Dividir una cadena
nombre="Piedad Marchena"
print(nombre[0:5])
print(nombre[7:15])
inicio=nombre[:5]
print(inicio)
final=nombre[7:]
print(final)

saludo="Hola chicos"
nuevosaludo="J"+saludo[1:]
print(nuevosaludo)

# número de veces que aparece  un caracter
palabra='banana'
contador=0
for letra in palabra:
    if letra == "a":
        contador+=1
print(contador)

esta='a' in palabra
print(esta)
esta='ena' in palabra
print(esta)

quesos=["chedar",'edam','gouda']
print(quesos[0])
numeros=[1,3,5,7]
print(numeros[-1])
print(5 in numeros)

for queso in quesos:
    print(queso)

a=len(numeros)
for indice in range(a):
    print(indice)
    numeros[indice]=numeros[indice]*10
print(numeros)

vacia=[]
print(len(vacia))
for i in vacia:
    print("Hola")
print("fin")
'''
t=["a",'b',"c","d","e","f"]
print(t)
t[1:3]=["x","y"]
print(t)
t.append("g")
print(t)
system("cls")
t2=["p","q"]
t.extend(t2)
print(t)
t.sort()
print(t)
x=t.pop(3)
