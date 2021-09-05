'''#crea un diccionario vacío
palabras=dict()
print(palabras)
#agrega elementos al diccionaro en esa clave
palabras['one']='uno'
print(palabras)
'''
#creando diccionario de varios elementos
palabra1={'one':'uno','two':'dos','three':'tres'}
'''print(palabra1)
#cantidad de claves del diccionario
print(len(palabra1))
print(palabra1['three'])
#si se encuentra una clave en el diccionario
f='dos' in palabra1
print(f)
#método values, el cual retorna los valores 
# como una lista, y después puedes usar el operador in
vals=list(palabra1.values())
print("Lista de valores ",vals)
t='tres' in vals
print(t)

#mostrar la clave y contenido del diccionario recorriendolo
for p in palabra1:
    print(p,palabra1[p])

#ordenar claves alfabeticamente y luego buscar su valor y mostrarlo
pala={'one':'uno','two':'dos','three':'tres'}
lst=list(pala.keys())
print("Lista de claves ",lst)
lst.sort()
for clave in lst:
    print(clave,pala[clave])

#copia de un diccionario
pala2=pala.copy()
print(pala2)

#vaciar el diccionario
pala2.clear()
print(pala2)
'''
#Crear un nuevo diccionario desde las claves de una secuencia 
secuencia={"1","2","3"}
palab=dict.fromkeys(secuencia)
#sin colocar ningun valor a las claves
print(palab)
#colocar el mismo valor a cada secuencia
palab1=dict.fromkeys(secuencia,'valor por defecto')
print(palab1)
#Establecer una clave y valor por defecto
clave=palab1.setdefault("6","Hoy")
print(clave)
print(palab1)
clave1=palab1.setdefault("5")
print(clave1)
'''print(palab1.get("7","Nuevo"))
print(palab1)
clave=palab1.setdefault("4","Maria")
print(clave)
print(palab1)
#Concatenar diccionarios
pala.update(palab1)
print(pala)
#Obtener el valor de una clave
print("Valor de la clave",pala.get("2"))
#Saber si una clave existe en el diccionario
existe = "two" in pala 
print(existe)
#Obtener las claves y valores de un diccionario
diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'} 
for clave, valor in diccionario.items(): 
    print ("El valor de la clave %s es %s" % (clave, valor))
#Obtener los valores de un diccionario 
claves = diccionario.keys()
print(claves)
#Obtener los valores de un diccionario 
valores = diccionario.values()
print(valores)
'''