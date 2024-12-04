"""
VARIABLES
En python las variables deben iniciar con una letra o con un guion bajo.
Los nombres solo pueden contener caracteres alfanumericos.
Python es camel sensitive, las mayusculas influyen en los nombres.
"""
num = 5
string = 'hola que mas'


"""
TIPOS DE DATOS
-  <class 'int'> => Integer => Entero numero.
- <class 'str'> => String => Letras.
- <class 'float'> => Decimales => Su nombre se debe a como se representar los numeros en memoria
- <class 'bool'> => Valores true o false -> Empiezan en mayusculas.

"""

# Funcion TYPE
type(num)

# Funcion LENT
# para saber la longitud de una cadena de catacteres.
print(len(string))

# Indexacion
# Permite acceder a caracteres individuales de la cadena.
print(string[3])

# Slicing
# Cortar una cadena de caracteres.
# <cadena>[ inicio : fin ]
# El ultimo no es incluido.
print(string[ 0:3 ]) # hol
# El parametro paso, el tercer valor antes de cerrar el paso, como se va
# saltar al siguiente 
print(string[0:3:2]) # se salto el 2 , hl