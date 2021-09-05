#lista = [2, 5, 'DevCode', 1.2,5,4]
lista = [2, 5, 3, 1.2, 56,7,5,82,4,32.6,5,14]
print("El elemento está repetido",lista.count(5)," veces")
#print("lista=",lista[0:14:3])
r=lista.index(5) # index(elemento_a_buscar)
print("elemento en la posición ",r)
r=lista.index(5,7,14) # index(elemento_a_buscar,posicion_inicial,posicion_final)
print("el segundo 5 está en la posición ",r)
if (1 in lista):
    print("El elemento está en la lista")
else:
    print("El elemento no está en la lista")
'''
lista=["oscar","alejandro","paula","nubia","johan"]
#elemento=lista.pop(2)
#lista.pop(2)
#print("elemento=",elemento)
#del lista[2]
#lista.remove(15)
#del lista[:8]
print("lista=",lista)
print("Máximo=",max(lista))
print("Mínimo=",min(lista))
print("Suma=",sum(lista))
#print("Promedio=",sum(lista)/len(lista))

#Mostrar los elementos de una lista
for element in lista:
    print (element)

#Imprimir una lista de atrás hacia delante
#j=0
lista1=[]
lista2=[7,8]
lista.extend(lista2)
longitud=len(lista)
print("La longitud de la lista es",longitud)
for i in range(longitud-1,-1,-1):
    #lista[i]=lista[i]*2
    lista1.append(lista[i])
    #j+=1
    #print (lista[i])

#ordenar lista
print(len(lista1))
lista=lista.sort() #Devuelve None
#print(lista1)
#lista1=lista[:]
print("Lista=",lista)
print(lista1)

#for i in range(valorinicial,valorfinal,iteraciones)


# Lista vacía
lista1=[]
for i in range(5):
    valor=int(input("ingrese valor: "))
    #agrega elementos al final de la lista
    lista1.append(valor)
print(lista1)

# adiciona todos los datos listados al final de la lista
lista1.extend([2,5,0,7])
print("lista con valores agregados ",lista1)
lista1=[3,5,6,8,5,5]

#elimina el dato en la posición designada y me muestra el valor eliminado
t=lista1.pop(2)
print(t)

#para remover un elemento que se le pase como parámentro de la lista 
#lista1.remove(5)

total=0
contador=len(lista)
for i in range(contador):
    total=total+lista[i]
print("suma=",total)
promedio=total/contador
print("promedio=",promedio)

print("lista con valor eliminado ",lista1)
'''
#Index devuelve el número de indice del elemento que le pasemos por parámetro.
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
'''
#Une las listas
lista2=[3,5,7]
listar=lista1+lista2
print("union lista ",listar)

#Operaciones con cadenas
s="Esto es una cadena"
t=list(s)
print("esta es ahora una lista ",t)

t=s.split()
print("esta es ahora una lista separada por palabras ",t)

separador=' '
print("nuevamente juntas ",separador.join(t))

lista2=[7,3,5]
print("lista ordenada ",lista2.sort())


lista2=[7,3,5]
lista2.sort()
print("lista ordenada ",lista2)

contadores={1:'maria',2:'jose',3:'pedro'} # Este es un diccionario
for clave in contadores:
    print(clave,contadores[clave])
'''