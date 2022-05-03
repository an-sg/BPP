# coding=utf-8

# LISTAS
# Compresión listas
# [x for x in insertable (if condicional)]
from unittest import result


frutas = ["manzana", "kiwi", "naranja"]
new = []

for x in frutas:
    if "a" in x:
        new.append(x)

# Condición simple
new = [x for x in frutas if "a" in x]

# Condicion if else se pone delante
new = [x if "a" in x else "" for x in frutas]

print(new)

# Devolver el precio
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
def get_price(price):
    return price if price > 0 else 0

new = [get_price(i) for i in original_prices]
new = [get_price(i) for i in original_prices]

# Pruebas de rendimiento
def bucle_for(n):
    result=[]
    for i in range(n):
        result.append(n**2)
    return result

def listas_com(n):
    return[i**2 for i in range(n)]

"""
begin = time.time()
bucle_for(100000)
end = time.time()

print("Tiempo ejecución sin comprimir {round(end-begin,2)}")

begin = time.time()
listas_com(100000)
end = time.time()

print("Tiempo ejecución con compresión {round(end-begin,2)}")
"""

# MAPS
# map(funcion, iterable)
#s[]
def reverse(s):
    return s[::-1]
cadena = "Hola mundo" 
print(reverse(cadena))

frutas = ["manzana", "kiwi", "naranja"]

result = list(map(reverse, frutas))
print(result)

# Lo miso con lambda
result = list(map(lambda s : s[::-1], frutas))
print(result)

# Utilizar MAP con multiples iterables
def f(a, b, c):
    return a + b + c

list(map(f,[1,2],[3,4],[5,6]))
list(map((lambda a, b, c : a + b + c),[1,2],[3,4],[5,6]))

# FILTER
def is_even(x):
    return x % 2 == 0

list(filter(is_even, range(10)))
list(filter(lambda x : x % 2 == 0 , range(10)))

def greater_than_100(x):
    return x > 100

list(filter(greater_than_100, [1, 111, 2, 222, 3, 333]))
list(filter(lambda x : x > 100, [1, 111, 2, 222, 3, 333]))

# REDUCE
# Aplia los iterables e 2 en 2, es una acumulación
# reduce(f, iterable)
from functools import reduce

def f(x, y):
    return x + y

reduce(f, [1, 2, 3, 4, 5])
sum([1, 2, 3, 4, 5])

reduce(lambda x, y: x +y, [1, 2, 3, 4, 5], 100)

print(reduce(f, ["cat", "dog", "hedgehog", "gecko"]))

print("".join(["cat", "dog", "hedgehog", "gecko"]))

# Comparativa para tiempos de ejecución
import random
import timeit
TAX_RATE = .08
txns = [random.randrange(100) for _ in range(100000)]
# Coge cada uno de los numeros y los multiplica por el taxt rate + 1
def get_price(txn):
    return txn * (1 + TAX_RATE)

# Funcion con MAP
def get_prices_with_map():
    return list(map(get_price, txns))

# Comprension con listas
def get_prices_with_comprehension():
    return [get_price(txn) for txn in txns]

# Bucle
def get_prices_with_loop():
    prices = []
    for txn in txns:
        prices.append(get_price(txn))
    return prices

# Ver cuanto tarda en ejecutarse cada una de ellas
print(timeit.timeit(get_prices_with_map, number=100))
print(timeit.timeit(get_prices_with_comprehension, number=100))
print(timeit.timeit(get_prices_with_loop, number=100))