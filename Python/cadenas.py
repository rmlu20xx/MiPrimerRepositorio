#***************************************************************************************************************************************************
#***************************************************************************************************************************************************
# ANALIZANDO CADENAS
#***************************************************************************************************************************************************

cadena ="Esto es una prueba"
lista=list(cadena)
print('Convierte una cadena en una lista de caracteres con la funcion "list"',lista)
#['E', 's', 't', 'o', ' ', 'e', 's', ' ', 'u', 'n', 'a', ' ', 'p', 'r', 'u', 'e', 'b', 'a']
lista=cadena.split()
print('Convierte una cadena en una lista de palabras con la funcion "split"',lista)
#['Esto', 'es', 'una', 'prueba']
limite='-'
lista=limite.join(lista)
print('Convierte una cadena en otra cadena y le agrega un delimitador con la funcion "join" ',lista)
#Esto-es-una-prueba
cadena=cadena.upper()
print("Imprime la cadena toda en mayuscula",cadena)


# capturar el nombre de usuario de una direccion de internet
dato='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
espacio=dato.find(' ')

arroba_pos = dato.find('@')

nombre_usuario=dato[espacio+1:arroba_pos]
print(nombre_usuario)