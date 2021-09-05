import numpy as np
a = np.array([1, 3, 5, 7, 9])
b =np.array([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])
print("Vector a:\n", a)
#print()
print("Matrix b:\n", b)
print(b.sum())

print(b[1,1]) # muestra los elementos de una fila 1 columna 1

print(b[0,::-1]) # muestra los elementos de una fila alrevés
print(b[::-1,1]) # muestra los elementos de una columna 1 alrevés