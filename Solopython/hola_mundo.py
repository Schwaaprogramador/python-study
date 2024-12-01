#https://www.youtube.com/watch?v=D3IUO0T3fOM&t=7377s&ab_channel=SoloPython


print('Hola Mundo')

# Gestor de Paquetes
# Para hacer un pip install => Hacer un environment.
# Hacerlo sin eso, se instalaria en la computadora en general.
# python -m venv environment => Para crear un env nuevo.
# Activar el ambiente => ./environment/Scripts/activate
#                     => sourve env/bin/acctivate Para MACos

# Cuando esta el env activo ahi si pip install numpy

# PEP8 => es el emacscript de js => normas para formateo

# Creacion de Variables

#Numeros
a = 2
b = 12312312312

#Floats
p = 3.14

#Strins
c = "A"
d = "Solo Python"
f = 'Con single tambien funciona'

#Booleans siempre con mayus inicial
q = False

#null
x = None

"""
Las variables se siempre se aginas de izq a der, no peuden empezar con numeros
ni pueden ser palabras reservadas de python.

import keyword
print(keyword.kwlist)

Este es un comentario de varias líneas.
Se usa comúnmente para documentar funciones o secciones del código.

"""

#Reglas Nombres de Variables: 
    # -> Los nombres de las variables deben empezar por letras o guion bajo.
    # -> Tampoco se pueden usar simbolos.
    
x = 1

# Por convenccion en una funcion, el parametro de uan funcion empieza con guion bajo.
# Variables privadas y publicas -> codigo limpio.
_x = 2

# Despues de la letra inicial si pueden ir numeros.
x2 = 3


"""
Asignacion

"""
# Multipl asignacion
g, h , l = 1, 3 ,5
#El mismo valor a varias => Mismo objeto en memoria.
b = n = m = 1

#Reasignacion
# Las variables no tienen que ser del mismo tipo.
a = 1 
a = "b"


"""
LISTAS
    Los elementos se separan por comas.
    Se pueden poner listas anidadas.
    El index de las listas es igual que es js. Index 0.

"""

z = [ 1, 2, ["a","b","c"]]
#Index
print(z[2][1])


"""
Identacion
    Se abre con dos puntos -> No tiene CIERRES.
    Las funciones siempre tienen que tener algo definido adentro.
    4 Espacios es la identacion recomendada.
    
"""

# No se pueden dejar vacias las funciones
def mi_func():    
    a = 2    
    b = 1    
    if a > b:
        return " a es gay "
    else:
        return " b es gay"

# Pass es un comando que no se hace nada no mas para no dejar espacion en black
def ejem():
    pass



print(mi_func())


"""
TIPOS DE DATOS

"""


#BOOLEANS
#OPERACIONES LOGICAS
# and , or , not
# En python los booleans son INT => 1 OR 0

x = True
y = False

#Las dos tienen que ser True
if x and y:
    print('hola')
    

#Uno solo tiene que ser verdadero
if x or y:
    print('alguno es verdadero')
    

#Si es falso devuelve true
if not x:
    print('x es falso')
    
    
    
#NUMEROS - integer