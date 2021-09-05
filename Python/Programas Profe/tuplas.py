'''
#crear tupla vacia
t=tuple()
#crear una tupla a partir de una cadena
t=tuple('1232143')
print(t)
#crear tupla con datos predeterminados
t1=(1,3,4,7,8)
print(t1)
#creación de tupla con un elemento
t2=('b',)
print(t2)
#mostrar contenido particular de la tupla y de un rango
print(t[0])
print(t[1:3])
#reemplazar una tupla
t1=('a',)+t1[3:]
print(t1)

#print((0,10,2000)<(0,3,4)) # abde > abce
txt="Pero qué luz se deja Ver allí"
palabras=txt.split() #Es una lista
print("palabra=",palabras)
t=list() # lista de tuplas
for palabra in palabras:
    t.append((len(palabra),palabra)) #adiciono los elementos de la lista (tupla)
print("t=",t)
t.sort()
print("T ordenada de mayor a menor",t)
res=list()
for longitud, palabra in t:
    res.append(palabra)
print("rest=",res)

a=10 #necesito que a=15
b=15 #necesito que b=10
c = a
a = b
b = c
a,b=b,a
print(a,b)

#pasar un diccionario a una lista de tuplas
diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'} 
lvalor=list()
lclaves=list()
for clave,valor in diccionario.items():
    lvalor.append((valor,clave))
    lclaves.append((clave,valor))
print(lvalor)
print(lclaves)
lvalor.sort()
print(lvalor)
'''
directorio=dict() #defino la variable directorio como un diccionario
nombre='Piedad'
apellido='Marchena'
telefono='3008426262'
directorio[nombre,apellido]=telefono
nombre='Maria'
apellido='Arias'
telefono='3000026262'
directorio[nombre,apellido]=telefono

for nombre,apellido in directorio:
    print(nombre, apellido, directorio[nombre, apellido])

#limpiar consola
#from os import system
#system("cls")