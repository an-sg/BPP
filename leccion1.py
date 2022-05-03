# EXCEPCIONES
"""try:
    #numero = 10
    #divisor = int(input("Introduzca un divisor"))
    #resultado = numero/divisor
    file = open("myfile.txt",'w')
except ZeroDivisionError as error:
    print("Se ha producido una division entre 0", error)
except ValueError:
    print("Introduzca un numero")
except IOError:
    print("Error obteniendo el fichero")
except Exception as error:  #las engloba todas
    print(f"Ha ocurrido una excepcion {error}")
else: #Se ejecutara siempre y cunado no se ejecute el except
    print("No ha habido ninguna excepción")
finally:
    file.close()
"""

"""# RAISE
raise ZeroDivisionError("Información de la excepción")

# Podemos crear nuestras propias excepciones (excepciones personalizadas)
class MiExcepcion(Exception):
    pass

raise MiExcepcion"""

"""# Le damos contenido y la personalizamos más
class MiExcepcion(Exception):
    def __init__(self, param1, param2):
        self.param1=param2
        self.param2=param2
try:
    raise MiExcepcion("Valor parametro 1", "Valor parametro 2")
except MiExcepcion as error:
    p1,p2 = error.args
    print(p1)
    print(p2)"""

"""#ASSERT

#assert(1==2) # Lanza una excepcion de tipo AssertionError

#if condicion:
    #raise AssertionError()
# Assert en testing
#def suma(num1, num2):
    #return num1 + num2
#assert(suma(2, 2) == 4)
#print("**************")
#assert(suma(2, 2) == 3)

# Comprobar que el tipo de dato que estamos pasando
# Assert en funciones
def suma(num1, num2):
    assert(type(num1) == int)
    assert(type(num2) == int)
    return num1 + num2

assert(suma(3,1))

# Assert con clases
class MiClase():
    pass

class OtraClase():
    pass

obj1 = MiClase()
obj2 = OtraClase()

assert(isinstance(obj1, MiClase))
assert(isinstance(obj2, MiClase))

# Deshabilitar el assert cuando estamos ejecutando (curiosidad)
# python -O main.py"""