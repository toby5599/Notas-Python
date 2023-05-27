#int = numero entero
#float = numero decimal -> 40.3

#los valores booleanos deben empezar con mayuscula: True - False

#convertir un dato a texto (f strings):

saludo = 5

saludo2 = f"hola como estas {saludo}"

print(saludo2)


#borrado de datos con del:

saludo = "matias"

saludo2 = f"hola como estas {saludo}"

del saludo2

print(saludo2)


#Para saber si una palabra esta en una variable ponemos in, si esta nos tira true. Podemos poner (in not).

saludo = "matias"

saludo2 = f"hola como estas {saludo}"

print("como" in saludo2)

#true

#¡IMPORTANTE! LAS PALABRAS CON MAYUSCULAS CON LAS MISMAS PALABRAS PERO EN MINUSCULA SON DIFERENTES

#¡IMPORTANTE! UTILIZAR SNAKE_CASE PARA DEFINIR CADA VARIABLE: QUE ES SEPARAR CADA PALABRA CON UN GUION BAJO




#DATOS COMPUESTOS

#LISTA (se puede modificar)

lista = ["matias","tobias",True,5]

print(lista[0])

#TUPLA (no se puede modificar)

datos = ("matias","tobias",True,5)

print(datos[0])

#la diferencia entre lista y tupla que es la tupla no se puede modificar:

datos = ["matias","tobias",True,5]

datos[0] = "pedro"

print(datos[0])


#SET: es como los anteriores pero desordenado por eso si queremos elegir por el indice un elemento en especifico no se puede y no se pueden repetir elementos:

conjunto = {"matias","tobias",True,5}

print(conjunto[0])

#error


#DICCIONARIO(KEY : VALUE): definimos el indice de cada elemento eliminando los numeros por defecto

diccionario = {
    'nombre' : "tobias",
    'edad' : "24"
}

print(diccionario['edad'])


#OPERADORES ARITMETICOS

    #DIVISION: siempre devuelve un dato float, lo podemos saber con type(dato)

    #DIVISION BAJA (//): devuelve un entero, redondeando para abajo

    #RESTO (%)


#OPERADORES DE COMPARACION

    # == (es igual que)
    # != (es distinto de)
    
#CONDICIONALES

edad = 17

if edad >=18: 
    print("podes pasar")

else: 
    print("no podes pasar")
    
    
# else if (elif)

ingreso_mensual = 5000

if ingreso_mensual > 100000:
    print("esta bien economicamente")
    
elif ingreso_mensual > 100:  #si se ejecuta el primero no se ejecuta el elif, pero si el primero el falso se va al elif
    print("esta bien")
    
else:
    print("sos pobre")
    

#OPERADORES LOGICOS

#AND (&) - las dos tienen que ser verdaderas

#OR (|) - solamentente es falso cuando las dos son falsas

#NOT (not) - cambia el valor

#True and not False - esto nos tira verdadero



#METODOS DE CADENA

#DIR (es una funcion): devuelve una lista de los atributos y metodos disponibles para un un objeto determinado o esa cadena.

cadena1 = "hola que ace"
cadena2 = "como andas"

print(dir(cadena1))


#upper (convierte el texto en mayuscula, es un metodo porque esta asociada a un objeto, tambien es una funcion)

# objeto.nombre_del_metodo(argumentos)

resultado = cadena1.upper()

print(resultado)


#lower() : hace lo contrario a upper

#find(argumento) : devuelve si esta en la cadena la posicion de la letra

#index(argumento) : lo mismo que find pero devuelve una excepcion sino encuentra la letra

#isnumeric() : si es numerico, devuelve true, sino devuelve false

#isalpha() : si es alfanumerico(si son palabras de la A a la Z) devuelve true, sino devuelve false, si hay numeros o caracteres especiales


#count(argumento) : encuentra la cantidad de veces que se repite una letra

cadena1 = "hola como estas"
cadena2 = "como andas"

resultado = cadena1.count("a")

print(resultado)

#startswith(argumento) : si una cadena empieza con una letra o conjuto de caracteres que le pongamos y nos tira true o false
#endswith(argumento) : lo mismo que el anterior pero con el final

#replace(argumento1(lo que queremos cambiar), argumento2(lo que vamos a poner))

cadena1 = "hola como estas"
cadena2 = "como andas"

resultado = cadena1.replace("hola", "chau")

print(resultado)

#len(objeto) : contamos cuantos caracteres tiene una cadena, es una funcion no un metodo

#split(argumento) : separar cadenas con la cadena que le pasemos, nos devuelve una lista

cadena1 = "hola como estas"
cadena2 = "como andas"

resultado = cadena1.split(" ")

print(resultado)



#METODOS DE LISTAS


#list : para crear una lista

lista = list(["hola","dalto",34])

print(lista)

#len : nos devuelve las cantidad de elementos de una lista

lista = list(["hola","dalto",34])

cantidad_de_elementos = len(lista)

print(cantidad_de_elementos)

#append(argumento) : agrega un elemento a la lista

lista = list(["hola","dalto",34])

resultado = lista.append("tobias")

print(lista)

#insert(dos argumentos) : como el append pero nosotros podemos elegir la posicion que queremos cambiar

lista = list(["hola","dalto",34])

resultado = lista.insert(0, "benitez")

print(lista)

#extend(dos argumentos) : si queremos agregar una lista (si o si, tiene que ser una lista) a la lista origina

lista = list(["hola","dalto",34])

resultado = lista.extend([0, "benitez"])

print(lista)

#pop(argumento) : si queremos eliminar un elemento especifico de la lista, si queremos eliminar el ultimo elemento hay que poner como argumento -1

lista = list(["hola","dalto",34])

resultado = lista.pop(1)

print(lista)

#remove(argumento) : elimina un elemento de la lista por su valor

lista = list(["hola","dalto",34])

resultado = lista.remove("hola")

print(lista)

#clear() : nos elimina todos los elementos de la lista

#sort() : ordena todos los elementos de una lista de menor a mayor, si ponemos reverse hace lo contrario, no tiene que haber cadenas de texto

lista = list([34,1])

resultado = lista.sort()

print(lista)



#TUPLA : NO LA PODEMOS MODIFICAR, PERO SI VER LA CANTIDAD DE ELEMENTOS QUE TIENE, ETC


#METODOS DE DICCIONARIO

#keys() : es para iterar

diccionario = {
    "nombre" : 'tobias',
    "edad" : '24',
    "profesion" : 'programador'
}

claves = diccionario.keys()

print(claves)

#get(argumento) : para poner el indice y nos da el elemento. si no lo encuentra nos tira none

#clear() : elimina todos los elementos del diccionario

#pop(argumento) : elimina un elemento del diccionario, si agregamos la coma podemos eliminar mas elementos

#items() : es para poder iterar(recorrer) los elementos del diccinario



#INPUT: pedirle un dato al usuario, simpre nos devuelve texto

nombre = input("pasame tu nombre:")

print("hola como estas " + nombre)

#ya que nos devuelve texto si queremos hacer cuentas aritmeticas podemos hacer esto:

numero = input("pasame un numero: ")

resultado = int(numero) * 2

print(resultado)



#VARIABLES 2.0

#DESEMPAQUETADO:

datos = ("tobias","benitez") #los elementos se almacenan en una tupla, es decir, que estan ordenados

nombre,apellido = datos

print(apellido)

#esta es una forma de covertir una lista en una tupla

datos = tuple(["dato1","dato2"])

print(datos)

#otra forma de crear una tupla, si queremos que sea solamente un elemento vamos a poner una coma: 

tupla = "tobias","benitez"

print(tupla)


#convertir una lista en un conjunto, que no se puede modificar y esta desordenado

conjunto = set(["dato1","dato2"])

print(conjunto)


#meter un conjunto dentro de otro conjunto con frozenset

conjunto1 = frozenset(["dato1","dato2"])

conjunto2 = {conjunto1,"dato3"}

print(conjunto2)


#TEORIA DE CONJUNTOS

#crear un conjunto vacio:
conjunto_vacio = set()

#crear un conjunto con elementos:
conjunto1 = {1,2,3,4,5,6}
conjunto2 = set([1,2,3,4,5,6])

# Unión
conjunto_union = conjunto1.union(conjunto2)

# Intersección
conjunto_interseccion = conjunto1.intersection(conjunto2)

# Diferencia
conjunto_diferencia = conjunto1.difference(conjunto2)


#Comprobar si un elemento pertenece a un conjunto:
if 3 in conjunto1:
    print("3 pertenece a conjunto1")







#esto es para saber si el conjunto2 es un subconjunto de conjunto1 con el metodo issubset

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

resultado = conjunto2.issubset(conjunto1)

print(resultado)

#otra manera de saberlo es:

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

resultado = conjunto2 <= conjunto1

print(resultado)

#issuperset() : si queremos saber si es un superconjunto vamos a utilizar issuperset y otra manera es poner > :


#isdisjoint() : si queremos saber si hay valores en comun, si hay valores en comun nos tira false y no lo hay nos tira true:

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)

#DICCIONARIOS

#creando diccionarios con dict()

diccionario = dict(nombre="tobias",apellido="benitez")

print(diccionario)

#¡IMPORTANTE! NO SE PUEDE CREAR LISTAS, CONJUNTOS, DICCIONARIOS VACIOS DE LA MANERA TRADICIONAL HAY QUE UTILIZAR DICT(), SET(), ETC


#fromkeys() : crear un diccionario con todos los valores none, es decir, sin keys

diccionario = dict.fromkeys(["nombre","apellido"])

print(diccionario)

#si lo ponemos de esta forma, va a iterar cada letra y a cada una le va a asignar none, pero si lo ponemos entre corchetes como arriba va a iterar solamente ABCD

diccionario = dict.fromkeys("ABCD")


#y de esta otra forma a los indices nombre y apellido le podemos asignar un elemento:

diccionario = dict.fromkeys(["nombre","apellido"], "cualquier cosa")

print(diccionario)

#nombre = cualquier cosa
#apellido = cualquier cosa





#BUCLES E ITERACION


#Todo lo siguiente funciona para listas, tuplas y la mayoria para conjuntos

#crear un bucle e iterar con for in

animales = ["gato","perro","rata","pajaro"]

for animal in animales:
    print(f"ahora la variable animal es igual a: {animal}")
    
    
#de esta forma podemos iterar dos listas al mismo tiempo

animales = ["gato","perro","rata","pajaro"]
numeros = [15,54,13]

for numero,animal in zip(animales,numeros):
    print(numero)   
    print(animal)

# recorre del 1 al 5, sin tomar el 5

for numero in range(1,5):
    print(numero)
    
    
#forma correcta de recorrer una lista con su indice: primero nos da su indice y luego el valor

numeros = {12,54,64,48}

for num in enumerate(numeros):
    print(num)
    
#si queremos el indice nada mas:
    print(num[0])
#si queremos el valor del indice:
    print(num[1])
    

#usando for else, cuando el bucle termina:

numeros = {12,54,64,48}

for num in enumerate(numeros):
    print(num[0])
else:
    print("el bucle ya termino")



#ITERAR DICCIONARIOS

diccionario = {
    "nombre" : "tobias",
    "apellido" : "benitez",
    "edad" : "24"   
}

for key in diccionario.items():
    print(key)

#si queremos elegir si queremos iterar los keys o los values:

diccionario = {
    "nombre" : "tobias",
    "apellido" : "benitez",
    "edad" : "24"   
}

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(value)
    
#si queremos saltear un elemento del bucle entonces utilizamos la sentencia continue:

frutas = ["manzana","banana","granada","tomate"]

for fruta in frutas:
    if fruta == "granada":
        continue
    print(fruta)
    
#si queremos romper el bucle en un elemento utilizamos break:

frutas = ["manzana","banana","granada","tomate"]

for fruta in frutas:
    if fruta == "granada":
        break
    print(fruta)
    
#recorrer una cadena de texto

saludo = "hola tobias"

for letra in saludo:
    print(letra)
    
    
#for en una sola linea de codigo para multiplicar por dos cada numero

numeros = [2,4,5,8]

numeros_duplicados = [x*2 for x in numeros]

print(numeros_duplicados)


#BUCLE-WHILE (siempre que se cumpla la condicion)

contador = 0

while contador < 10:
    contador += 1
    print(contador)
    


#FUNCIONES

#FUNCIONES INTEGRADAS (build_in)

#max() - encontrar el numero mas alto

numeros = [4,5,7,2,1]

numero_mayor = max(numeros)

print(numero_mayor)

#min() - lo contrario a max

#round() - round es para redondear pero podemos elegir la cantidad de decimales que queremos en el segundo argumento

numero = 12.23484521

numero_redondeado = round(numero,2)

print(numero_redondeado)

#bool() - si es cero o vacio nos tira false, si es 1 o datos no vacios tira true

resultado_bool = bool(0)

print(resultado_bool)

#all() - es igual que bool pero detecta todos los elementos si ninguno es false, 0, vacio nos tira true

resultado_all = all([1,5,10,True])

print(resultado_all)

#sum() - suma todos los numeros

suma = sum([1,2,3,4,5])

print(suma)


#FUNCIONES PROPIAS

def saludar():
    print("hola como estas")
    
saludar()


#utilizando un parametro

def saludar(nombre):
    print(f"hola {nombre} como estas")
    
saludar("pedro")


#otra funcion un poco mas complicada

def saludar(nombre,sexo):
    if (sexo == "hombre"):
        adjetivo = "señor"
    elif (sexo == "mujer"):
        adjetivo = "querida"
    else:
        adjetivo = "crack"
    
    print(f"hola {nombre}, como estas {adjetivo}")
    
saludar("tobias","hombre")
saludar("camila","mujer")
saludar("roberto","otros")


#return

def calculo(num):
    return num*2

print(calculo(5))

#otra forma

def suma(a,b):
    return a + b

resultado = suma(5,3)

print(resultado)

#manera no optima de sumar varios numeros

def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados

resultado = suma([1,2,3,4,5])

print(resultado)


#args una manera mas optima de sumar varios numeros

def suma(*numeros):  #pone a todos los numeros en una lista
    return sum(numeros)

resultado = suma(1,2,3,4,5)

print(resultado)


#FUNCIONES LAMBDA (actua como la funcion flecha de javascript)

multiplicacion = lambda x : x*2

print(multiplicacion(2))


#filter

numeros = [1,2,3,4,5,6,8,9,10,11]

def par(num):
    if(num%2==0): #divide al numero por dos y luego a ese numero le saca el resto, si el resto es cero es par si no es impar
        return True
    
numeros_pares = filter(par,numeros) #usa la funcion par y le pasa cada numero de lista en cada vuelta

print(list(numeros_pares))


#con lambda podemos ahorrar mucho codigo del ejercicio de arriba

numeros = [4,5,6,8,9,10,11,12]

numeros_pares = filter(lambda numero:numero%2 == 0, numeros)

print(list(numeros_pares))



#MODULOS

#primer archivo: holamundo

def saludar(name):
    return f"hola {name} espero que hayas tendio un lindo dia"
    
saludo = saludar("tobias")
print(saludo)

#segundo archivo: modulos

import holamundo  #ponemos el nombre del archivo

saludo = holamundo.saludar("matias") #ahora la funcion saludar funciona como un metodo
print(saludo)


#si queremos renombrar el modulo

import holamundo as archivo_1

saludo = archivo_1.saludar("matias")
print(saludo)

#si queremos importar solamente una funcion de archivo, si queremos importar mas ponemos una coma

from holamundo import saludar  #estamos importando la funcion saludar

saludo = saludar("juan")

print(saludo)


#si queremos importar todo ponemos, pero es poco recomendable *

from holamundo import *

#accedemos al nombre del modulo

print(__name__)


#si el archivo esta en otra carpeta por ejemplo carpeta2:

from carpeta2.modulos import saludar as sal

saludo_2 = sal("jaimico")
print(saludo_2)


#si queremos import nada mas el archivo y llamar la funcion, pero mas abreviado podemos cambiarle el nombre con as

import carpeta2.modulos

print(carpeta2.modulos.saludar("penelope"))  #hay que poner el nombre de la carpeta y del archivo y recien luego el nombre de la funcion


#si el modulo estuviera fuera, utilizar sys que es un modulo integrado en python

import sys

#lo utilizamos asi, de esta manera podemos eligir cualquier carpeta mas facil

import sys

sys.path.append("G:\My Drive\Programacion\curso de python\\carpeta2")

import modulos  #nombre del archivo que esta dentro de la carpeta2

print(modulos.saludar("penelope"))



#PAQUETE: es una carpeta con muchos archivos python, dentro de la carpeta debe tener un archivo python con el nombre "__init__" para que detecte que es un paquete




#str() - para convertir un numero en una cadena de texto