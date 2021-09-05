#***************************************************************
#                  TUPLAS
#**************************************************************


# Sintácticamente, una tupla es una lista de valores separados por comas o es común encerrar las tuplas entre paréntesis

t='a','b','c','d','e','f'
print(t)
#('a', 'b', 'c', 'd', 'e', 'f')


#Para crear una tupla con un solo elemento, es necesario incluir una coma al final

t1=('a',)
print(t1)
print(type(t1))
"""('a',)
<class 'tuple'>
"""

#Crear una tupla vacia
t2=tuple()
print(t2)
#()

#Si el argumento es una secuencia ( lista, o tupla), el resultado de la llamada a tuple es una tupla con los elementos de la secuencia

t3=tuple('Rafael Luna')
print(t3)
#('R', 'a', 'f', 'a', 'e', 'l', ' ', 'L', 'u', 'n', 'a')
print(t3[0])
#R
print(t3[1:3])
#('a', 'f')

#No se puede modificar los elementos de una tupla, pero sí se puede reemplazar una tupla por otra
t3= t3+tuple(' Uribe')
print(t3)
#('R', 'a', 'f', 'a', 'e', 'l', ' ', 'L', 'u', 'n', 'a', ' ', 'U', 'r', 'i', 'b', 'e')

#Ordenando los valores de las tuplas
t4="84 730 62 73 821 73"
palabras=t4.split()
print(palabras)
t=list()
for palabra in palabras:
    t.append((len(palabra),palabra))
print("t=",t)
t.sort()
res=list()
print(res)
for longitud,palabra in t:
    res.append(palabra)
print(res)


#Asignacion de tuplas
m=['pasalo','bien']
(x,y)=m

print("x= ",x)
print("y= ",y)
print(m[0])
print(m[1])

#intercambiar valores en una sola sentencia
x,y=y,x
print("x= ",x)
print("y= ",y)

#Por ejemplo, para dividir una dirección de e mail en nombre de usuario y dominio, se podría escribir
dir='rafael.luna@epm.com.co'
nombre,dominio=dir.split('@')
print("nombre =",nombre)
#nombre = rafael.luna
print("domino =",dominio)
#domino = epm.com.co


#Los diccionarios tienen un método llamado items que retorna una lista de tuplas, donde cada tupla es un par clave valor
diccionario={'color':'rojo','marca':'nike','talla':'40'}
t=list(diccionario.items())
print(t)
#[('color', 'rojo'), ('marca', 'nike'), ('talla', '40')]
t.sort(reverse=True)
print(t)
#[('talla', '40'), ('marca', 'nike'), ('color', 'rojo')]


#Pasar un diccionario a una lista de tuplas
diccionario={'color':'rojo','marca':'nike','talla':'40'}
l=list()
for clave,valor in diccionario.items():
    l.append((clave,valor))
print(l)
#[('color', 'rojo'), ('marca', 'nike'), ('talla', '40')]


#Uso de tuplas como claves en diccionarios
nombre='Rafael'
apellido='Luna'
telefono='3808080'
directorio=dict()
directorio[apellido,nombre]=telefono
nombre='Yuri'
apellido='Monsalve'
telefono='5809854'
directorio[apellido,nombre]=telefono

for nombre, apellido in directorio:
    print(nombre,apellido,directorio[nombre,apellido])








