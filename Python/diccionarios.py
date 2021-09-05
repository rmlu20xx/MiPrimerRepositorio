# DICCIONARIOS

#La función "dict" crea un nuevo diccionario sin elementos

diccionario=dict()
print(diccionario)
#{}

#Para agregar elementos a un diccionario, puedes utilizar corchetes

diccionario['one']='uno'
print(diccionario)
#{'one': 'uno'}

#Crear diccionario completo
diccionario={'one':'uno','two':'dos','three':'tres'}
print(diccionario)
#{'one': 'uno', 'two': 'dos', 'three': 'tres'}

#utilizas las claves para encontrar los valores correspondientes
print("Two = ",diccionario['two'])
#Two =  dos

#Longitud del diccionario
print("La longitud del diccionario es ",len(diccionario))
#La longitud del diccionario es  3


#El operador in funciona en diccionarios éste te dice si algo aparece como una clave en el diccionario (aparecer como valor no es suficiente)

print('one'in diccionario)
#True
print('uno'in diccionario)
#False

#Para ver si algo aparece como valor en un diccionario, puedes usar el método values, el cual retorna los valores como una lista, y después puedes usar el operador in

vals=list(diccionario.values())
print(vals)
#['uno', 'dos', 'tres']
print('uno'in vals)
#True


"""Si
utilizas un diccionario como una secuencia para una sentencia for esta recorre las claves del diccionario Este bucle
imprime cada clave y su valor correspondiente
"""

contadores={'sofia':1,'rafa':3,"yuri":5}
for i in contadores:
    print(i, contadores[i])
#sofia 1
#rafa 3
#yuri 5


"""
Si quieres imprimir las claves en orden alfabético,
primero haces una lista de las claves en el diccionario utilizando el método keys disponible en los objetos de diccionario,
y después ordenar esa lista e iterar a través de la lista ordenada, buscando cada clave e imprimiendo pares clave valor
ordenados
"""

contadores={'sofia':1,'rafa':3,"yuri":5}
lst=list(contadores.keys())
print(lst)
#['sofia', 'rafa', 'yuri']
lst.sort()
for i in lst:
    print(i, contadores[i])
#rafa 3
#sofia 1
#yuri 5


#Vaciar un diccionario
contadores={'sofia':1,'rafa':3,"yuri":5}
contadores.clear()
print(contadores)
#{}


#Crear un nuevo diccionario desde las claves de una secuencia o lista
secuencia=["color","talle","marca"]
diccionario1=dict.fromkeys(secuencia)
print(diccionario1)
#{'color': None, 'talle': None, 'marca': None}

diccionario2=dict.fromkeys(secuencia,'valor x defecto')
print(diccionario2)
#{'color': 'valor x defecto', 'talle': 'valor x defecto', 'marca': 'valor x defecto'}

#Copiar un diccionario
diccionario3=diccionario1.copy()
print(diccionario3)
#{'color': None, 'talle': None, 'marca': None}

#Concatenar diccionarios
diccionario1={"color":"verde","precio":"45"}
diccioanrio2={"talla":"M","marca":"Lacoste"}
diccionario1.update(diccioanrio2)
print(diccionario1)
#{'color': 'verde', 'precio': '45', 'talla': 'M', 'marca': 'Lacoste'}

#Obtener el valor de una clave
print(diccionario1.get("color"))
#verde

#Adicionar elementos al diccionario
clave=diccionario1.setdefault("Genero","Masculino")
print(diccionario1)
#{'color': 'verde', 'precio': '45', 'talla': 'M', 'marca': 'Lacoste', 'Genero': 'Masculino'}


#Obtener las claves de un diccionario
clave=diccionario1.keys()
print(clave)
#dict_keys(['color', 'precio', 'talla', 'marca', 'Genero'])

#Obtener los valores de un diccionario
valores=diccionario1.values()
print(valores)
#dict_values(['verde', '45', 'M', 'Lacoste', 'Masculino'])

