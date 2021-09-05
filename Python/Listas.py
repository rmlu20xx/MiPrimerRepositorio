#Practica cadenas, diccionarios, listas
quesos=['chedar','edam','gouda']
print(quesos[0])
numeros=[0,1,2,3,4,5,6,7,8,9,10]
print(numeros[-1])
print(5 in numeros)

for i in quesos:
    print(i)
"""chedar
   edam
   gouda"""

for i in range(len(quesos)):
    print(i)
"""0
   1
   2"""

print("la lista numeros inicial es =",numeros)

for i in range(len(numeros)):
    numeros[i]=numeros[i]*10
print("La lista numeros multiplicada x 10 es = ",numeros) 
#[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#imprimir una lista de atras hacia adelante
numeros1=[]

for i in range(len(numeros)-1,-1,-1):
    numeros1.append(numeros[i])
print("La lista numeros alrevés es = ",numeros1)

numeros.extend(numeros1)
print("La lista extendida es =", numeros)

#***************************************************************************************************************************************************
#***************************************************************************************************************************************************

t=['a','b','c','d','e','f']
print("La lista original es ",t)
#['a', 'b', 'c', 'd', 'e', 'f']
t[1:3]=['x','y']
print("Cambiamos parametros en la lista original ",t)
#['a', 'x', 'y', 'd', 'e', 'f']

#append agrega un nuevo elemento al final de una lista
t.append('g')
print('Se agrega un elemento a la lista usando función "append"',t)
#['a', 'x', 'y', 'd', 'e', 'f', 'g']

#extend toma una lista como argumento y agrega todos los elementos
t2=["p","q"]
t.extend(t2)
print('Se agrega un elemento a la lista usando función "extend"',t)
#['a', 'x', 'y', 'd', 'e', 'f', 'g', 'p', 'q']

#insert adiciona un elemento en una posicion determinada
t.insert(1,"h")
print('Se adiciona un elemento en una poscion determinada con la función "insert"',t)
#['a', 'h', 'x', 'y', 'd', 'e', 'f', 'g', 'p', 'q']

#sort ordena los elementos de la lista de menor a mayor
t.sort()
print('Se organiza la lista usando función "sort"',t)
#['a', 'd', 'e', 'f', 'g', 'h', 'p', 'q', 'x', 'y']
t.sort(reverse=True)
print('Se organiza la lista de menor a mayor usando función "sort con reverse"',t)
#['y', 'x', 'q', 'p', 'h', 'g', 'f', 'e', 'd', 'a']
t.reverse
print('Invierte la lista con la función "reverse"',t)
#['y', 'x', 'q', 'p', 'h', 'g', 'f', 'e', 'd', 'a']

#Elimina  elementos y los guarda en otra variable
x=t.pop(0) 
print('Se elimina un elemento de la lista usando función "pop"',t)
#['x', 'q', 'p', 'h', 'g', 'f', 'e', 'd', 'a']
print('El elemento eliminado con la función "pop" se guarda en una variable',x)
#y

#Si no necesitas el valor removido, puedes usar el operador del
del t[0]
print('Se elimina un elemento de la lista por siempre usando función "del"',t)
#['q', 'p', 'h', 'g', 'f', 'e', 'd', 'a']

#Si sabes qué elemento quieres remover (pero no sabes el índice), puedes usar remove
t.remove('p')
print('Se elimina un elemento especifico (Cuando desconozco el indice) usando función "remove"',t)
#['q', 'h', 'g', 'f', 'e', 'd', 'a']

#Para remover más de un elemento, puedes usar del con un índice de rebanado
del t[1:5]
print('Se elimina varios elementos de la lista por siempre con indice rebanado usando función "del e indicando indice rebanado"',t)
#['q', 'd', 'a']

#Funciones
nums=[3,41,12,9,74,15]
print(len(nums)) #6
print(max(nums)) #74
print(min(nums)) #3
print(sum(nums)) #154

#Listas y cadenas
s='spam'
t=list(s)
print(t)
#['s', 'p', 'a', 'm']

s='rafael luna uribe'
t=s.split()
print(t)
#['rafael', 'luna', 'uribe']

s='rafa-luna-uribe'
delimiter='-'
s=s.split(delimiter)
print(s)
#['rafa', 'luna', 'uribe']

t=['rafael','luna','uribe']
delimiter=' '
t=delimiter.join(t)
print(t)
#rafael luna uribe





