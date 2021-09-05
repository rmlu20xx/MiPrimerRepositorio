'''
#Convierte la cadena en una lista de caracteres
cadena="Esto es una 4 prueba"
lista=list(cadena)

print(lista)
lista.reverse()
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

#Convierte la cadena en una lista por el separador indicado
lista=cadena.split("es",1)
print(lista)

#cadena="Esto-es una-prueba"
#lista1=cadena.split('-')
#print(lista1)
#junta la lista colocando el separador deseado
limite='*'
lista2=limite.join(lista)
print(lista2)


#compara cadenas (espacios en blanco, numeros, mayusculas, minusculas)
#a="aaa"
#b="Bbb"
cad1="Maria"
cad2=input("Ingrese un texto: ")
if cad2.upper()<cad1.upper():
    print("la palabra ingresada ",cad2," está antes de ",cad1)
elif cad2.upper()>cad1.upper():
    print("la palabra ingresada ",cad2," está después de ",cad1)
else:
    print("son iguales") # cad1==cad2 maria


#Muestra todos los métodos del objeto
#print(dir(cad1))

cad1="Valor de Prueba"
#operdor in para saber si un valor está dentro de la cadena devuelve True o false
f='a' in cad1
print("muestra si el caracter está en la cadena ",f)
#método de cadena llamado find que busca la posición de una cadena dentro de otra:
print("muestra si lo encontró en la posición de la cadena",cad1.find('or'))
#busca la cadena desde el indice indicado
print("muestra si lo encontró a partir del indice",cad1.find('lo',2))

#eliminar los espacios en blanco (espacios, tabs, o nuevas líneas) 
# en el inicio y el final de una cadena usando el método strip
cad3='hola señor 8 es la lala'
print(cad3.strip())
print (cad3.center(30,"*"))
print (cad3.ljust(40,"*"))
print (cad3.rjust(40,"*"))
print (cad3.zfill(30))
print (cad3.count("la"))
print (cad3.find("la"))
print (cad3.find("os",4))
print (cad3.startswith("hola",1))
print (cad3.endswith("ala "))
print (cad3.isalnum())
cad4="cadena"
cad5="1234"
print (cad4.isalpha())
print (cad5.isdigit())
cad6="estimado señor nombre apellido"
buscar="nombre apellido"
reemplazar="Alejandro Rueda"
print(cad6.replace(buscar,reemplazar))
#permite un numero al formato cadena
c=5.3
c1='%d' % c
print(type(c1)," valor de c1=",c1)
#permite una copia de las cadenas convertida las mayusculas en minusculas y viceversa
e="Hola Mundo"
print(e.swapcase())

formato_numero_factura=("N° 0000-0","-0000 (ID:",") Nombre:",")","****")
numero='123'
numero_factura=numero.join(formato_numero_factura)
print('Número de la factura es ',numero_factura)

tupla="http://www.eugeniabahit.com".partition('www.')
print ('La tupla resultante es ',tupla)

protocolo,separador,dominio = tupla
print('Protocolo: {0} \nDominio: {1} \nSeparador: {2}'.format(protocolo,dominio,separador))

datos="Pedro Picapiedra 2000"
t=datos.partition("Picapiedra ")
print(t)
nom,ape,adn=t
print("Nombre: {0} Apellido: {1} Año de nacimiento: {2}".format(nom,ape,adn))
'''
ingredientes='''
carne
papa
yuca
sal
cilantro    
'''
print(ingredientes.splitlines())