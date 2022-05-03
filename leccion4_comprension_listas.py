import functools
from hmac import trans_36


numeros = [1,2,3,4,5,6]

pares = []

#Ver si un numero es par o no
# Si lo es, guardarlo en una lista

for num in numeros:
    if num % 2 == 0:
        pares.append(num)

print(pares)

# Estructura de la comprension de listas:
# [ expresion(i) for i in list condition]

pares = [num for num in numeros if num%2 == 0 ]
print(pares)

# Numeros cuadrados del 1 al 10

cuadrados = [num**2 for num in range(10) ]
print(cuadrados)

# Si es mayor a 5 que muestre 0

cuadrados = [num**2 for num in range(10) if num > 5 ]
print(cuadrados)

# Para condiciones if-else

cuadrados = [num**2 if num > 5 else 2 for num in range(10) ]
print(cuadrados)

# Multiplicacion de matrices anidadas

transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

# Codigo optimizado de la multiplicacion de matrices

transpose = [[row[i] for row in matrix] for i in range(2)]

# FUNCIONES LAMBDA - funciones sin nombre
# lambda parametros : expresion

def cuadrado(x):
    return x**2

# Con funcion lambda

cuad = lambda x : x**2

print(cuadrado(2))
print(cuad(5))

# FUNCIONES MAP
# map()
# map(una_funcion, una_lista)

enteros = [1, 2, 4, 7]
cuadrados = []
for e in enteros:
    cuadrados.append(e ** 2)

print(cuadrados)

# Funcion optimizada

cuadra = list(map(lambda x : x**2,enteros))

print(cuadra)

# FUNCIONES FILTER
# filter()
# filter(una_funcion, una_lista)

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = []
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
print(pares)

# Funcion optimizada

pares = list(filter(lambda x : x%2==0,valores))
print(pares)

# FUNCIONES REDUCE

from functools import reduce

valores = [2, 4, 6, 5, 4]
suma = 0
for el in valores:
    suma += el
print(suma)

# Funcion optimizada

suma = reduce(lambda x,y : x+y, valores )
print(suma)