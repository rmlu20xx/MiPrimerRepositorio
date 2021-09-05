lista=[2,5,6,7,8]
#contenido de la primera posición de la lista
print(lista[0])
print(len(lista))
#Multiplicar listas tantas veces se indique
lista=lista*2
print(lista)
#Rebanado de listas desde una posición hasta antes de la posición final
print(lista[2:3])
#Rebanado de listas desde inicio hasta antes de la posición final
print(lista[:2])
#Rebanado de listas desde una posición hasta el final
print(lista[2:])
#Un operador de rebanado al lado izquierdo de 
# una asignación puede actualizar múltiples elementos
lista[1:3]=[10,22]
print(lista)
#sort ordena los elementos de la lista de menor a mayor
lista.sort()
print(lista)
#almacena el valor eliminado y elimina el ultimo valor
print("Valor eliminado",lista.pop())
print("eliminado ultimo valor",lista)
#Si no necesitas el valor removido, puedes usar el operador del
del lista[4]
print(lista)
#Para remover más de un elemento, puedes usar del con un índice de rebanado
del lista[3:5]
print(lista)
#cantidad de elementos de la lista
print(len(lista))
#Mayor del listado
print(max(lista))
#Menor del listado
print(min(lista))
#Sumar los valores de la lista
print(sum(lista))
lista1=['h','y','a','p','y','g','y']
lista1.sort()
print(lista1)
#ordena de mayor a menor
lista1.sort(reverse=True)
print(lista1)
#Contar cantidad de apariciones elementos
print("Aparece la y ",lista1.count()," veces")