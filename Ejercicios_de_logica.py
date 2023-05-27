#EJERCICIOS PYTHON

# Escribir un programa que pida al usuario dos números y los sume.

# Escribir un programa que pida al usuario dos números y calcule su multiplicación, pero sin utilizar el operador de multiplicación (*).

# Escribir un programa que pida al usuario un número y muestre su tabla de multiplicar hasta el 10.

# Escribir un programa que pida al usuario un número y determine si es primo o no.

# Escribir un programa que pida al usuario una cadena de caracteres y determine si es un palíndromo o no (es decir, si se lee igual de izquierda a derecha que de derecha a izquierda).

# Escribir un programa que pida al usuario una cadena de caracteres y determine cuántas veces aparece una letra específica en ella.

# Escribir un programa que pida al usuario una lista de números y calcule su media aritmética.

# Escribir un programa que pida al usuario una lista de números y determine cuál es el número más grande y cuál es el número más pequeño.

# Escribir un programa que pida al usuario una lista de números y los ordene de menor a mayor utilizando el algoritmo de burbuja.  (complicado se necesita aprender algoritmos y estructuras de datos)

# Escribir un programa que pida al usuario una cadena de caracteres y la convierta a mayúsculas.



#1) Escribir un programa que pida al usuario dos números y los sume.

# a = input("pasame el primer numero: ")

# b = input("pasame el segundo numero: ")

# resultado = int(a) + int(b)  #integer = entero

# print(resultado)

#2) Escribir un programa que pida al usuario dos números y calcule su multiplicación, pero sin utilizar el operador de multiplicación

# a = input("primer numero: ")

# b = input("segundo numero: ")

# a = int(a)
# b = int(b)

# resultado = 0
# contador = 0

# while contador < b:
#     resultado += a
#     contador += 1
    
# print(resultado)

#3) Escribir un programa que pida al usuario un número y muestre su tabla de multiplicar hasta el 10.

# num = input("pasame un numero: ")

# num = int(num)

# contador = 0

# while contador <= 10:
#     resultado = num*contador
#     contador += 1
#     print(resultado)
    

#4) Escribir un programa que pida al usuario un número y determine si es par o no.

# numero = input("pasame un numero: ")

# numero = int(numero)

# if numero % 2 == 0:
#     print("el numero es par")
    
# else:
#     print("el numero es impar")
    
#5) Escribir un programa que pida al usuario un número y determine si es primo o no.(no funciona bien, contraejemplo = 25)

# numero = input("pasame un numero: ")

# numero = int(numero)

# if numero > 1 and numero % 2 != 0 and numero % 3 != 0:
#     print("numero es primo")
# else:
#     print("numero no es primo")
    

#6) Escribir un programa que pida al usuario una cadena de caracteres y determine si es un palíndromo o no (es decir, si se lee igual de izquierda a derecha que de derecha a izquierda).

# palabra = input("pasame una palabra para saber si es un políndromo: ")

# palabra_inversa = palabra[::-1]  #para invertir la palabra

# if palabra == palabra_inversa:
#     print("la palabra es un políndromo")

# else:
#     print("la palabra no es un políndromo")
    

#7) Escribir un programa que pida al usuario una lista de números y calcule su media aritmética.


# serie_de_numeros = input("pasame una serie de numeros, separa cada numero con una coma: ")

# ordenado = serie_de_numeros.split(",")  #es para separar cuando en este caso hay una coma en una lista

# cantidad = len(ordenado) #para saber la cantidad de elementos que hay en una lista

# resultado = 0

# for numero in ordenado:
#     numero = int(numero)
#     resultado += numero

# promedio = resultado / cantidad


# print(promedio)


        
#8) Escribir un programa que pida al usuario una lista de números y determine cuál es el número más grande y cuál es el número más pequeño.

# lista_de_numeros = input("pasame una lista de numeros: ")

# numeros = lista_de_numeros.split(",")

# lista = [] 


# for numero in numeros:
#     numero = int(numero)
#     lista.append(numero)
    

# numero_mayor = max(lista)
# numero_menor = min(lista)

# print(f"el numero mas grande es {numero_mayor} y el numero mas chico es {numero_menor}")


#9) 

#10)  # Escribir un programa que pida al usuario una cadena de caracteres y la convierta a mayúsculas.


# cadena = input("pasame una cadena de caracteres: ")

# cadena_en_mayuscula = cadena.upper()
# cadena_en_minuscula = cadena.lower()

# print(cadena_en_mayuscula)
# print(cadena_en_minuscula)



#11) definir una funcion max_de_tres(), que tome tres numeros como argumentos y devuelva el mayor de ellos

# def max_de_tres(num1,num2,num3):
#     if num1 > num2 and num1 > num3:
#         print(f"el argumento uno es el mayor y el numero es {num1}")
        
#     elif num2 > num3:
#         print(f"el segundo argumento es el mayor y el numero es {num2}")
    
#     elif num3 > num2 and num3 > num2:
#         print(f"el argumento tres es el mayor y el numero es {num3}")
    
#     else:
#         print("son iguales")
    
# max_de_tres(100,200,12872)

#12) escribir una funcion que tome un caracter y devuelva true si es una vocal, de lo contrario devuelve false

# def caracter(carac):
#     if carac == "a" or carac == "e"  or carac == "i" or carac == "o"  or carac == "u":
#         print("es una vocal")
#     else:
#         print("no es una vocal")
        
# caracter("b")

#otra forma

# def is_vocal(caracter):
#     lista_vocales = ["a","e","i","o","u"]
    
#     if caracter in lista_vocales:
#         return True
#     else:
#         return False
    
# print(is_vocal("a"))


#PARTE 2

# Suma de los dígitos de un número:
# Escribir una función que tome un número como argumento y devuelva la suma de sus dígitos. Por ejemplo, si el número es 123, la función debería devolver 6 (1 + 2 + 3).

# Número inverso:
# Escribir una función que tome un número como argumento y devuelva su inverso. Por ejemplo, si el número es 123, la función debería devolver 321.

# Factorial:
# Escribir una función que calcule el factorial de un número dado. El factorial de un número es el producto de todos los enteros positivos desde 1 hasta el número en cuestión. Por ejemplo, el factorial de 5 es 120 (1 x 2 x 3 x 4 x 5).

# Suma de los cuadrados de una lista de números:
# Escribir una función que tome una lista de números como argumento y devuelva la suma de los cuadrados de todos los números de la lista. Por ejemplo, si la lista es [1, 2, 3], la función debería devolver 14 (1^2 + 2^2 + 3^2 = 14).


#13) # Suma de los dígitos de un número:
    # Escribir una función que tome un número como argumento y devuelva la suma de sus dígitos. Por ejemplo, si el número es 123, la función debería devolver 6 (1 + 2 + 3).
   
# def suma_digitos(numero):
#     suma = 0
#     while numero != 0:
#         suma += numero % 10
#         numero //= 10
#     return suma

# numero = int(input("Ingrese un número entero: "))
# resultado = suma_digitos(numero)
# print("La suma de los dígitos de", numero, "es:", resultado)


#mi manera

# def suma_cifras(numeros):
#     numeros = str(numeros)
#     resultado = 0
    
#     for numero in numeros:
#         numero = int(numero)
#         resultado += numero
#     print(resultado)
        
# suma_cifras(12345)    


#14) 

# # Número inverso:
# Escribir una función que tome un número como argumento y devuelva su inverso. Por ejemplo, si el número es 123, la función debería devolver 321.

# def numero_inverso(numeros):
#     numeros = str(numeros)
#     numeros = numeros[::-1] #solamente se puede en strings no en enteros
#     numeros = int(numeros)
#     return numeros

# print(numero_inverso(1234))


#15) 

# Factorial:
# Escribir una función que calcule el factorial de un número dado. El factorial de un número es el producto de todos los enteros positivos desde 1 hasta el número en cuestión. Por ejemplo, el factorial de 5 es 120 (1 x 2 x 3 x 4 x 5).

# def numero_factorial(numero):
#     contador = 1
#     resultado = 1
#     while 1 <= contador <= numero:
#         resultado = resultado * contador
#         contador += 1
#     print(resultado)
    
# numero_factorial(5)
        

#16)

# Suma de los cuadrados de una lista de números:
# Escribir una función que tome una lista de números como argumento y devuelva la suma de los cuadrados de todos los números de la lista. Por ejemplo, si la lista es [1, 2, 3], la función debería devolver 14 (1^2 + 2^2 + 3^2 = 14).

# def suma_cuadrados(numeros):
#     numeros = list(numeros)
#     resultado = 0
#     for numero in numeros:
#         numero = numero*numero
#         resultado += numero
#     return resultado
        
    
# print(suma_cuadrados([1,2,3,4,5,6]))


#PARTE 3

# Escribe una función que tome una lista de números como argumento y devuelva una lista de todos los números que son divisibles por 3 o 5.

# Escribe una función que tome una cadena de palabras como argumento y devuelva una lista de todas las palabras que aparecen más de una vez en la cadena.

# Escribe una función que tome dos cadenas como argumentos y devuelva una lista de todas las palabras que aparecen en ambas cadenas.

# Escribe una función que tome una lista de números como argumento y devuelva una lista de todas las combinaciones únicas de dos números en la lista que suman 10.

# Escribe una función que tome una cadena como argumento y devuelva una lista de todas las subcadenas que contienen una cantidad igual de vocales y consonantes.

# Escribe una función que tome una lista de palabras como argumento y devuelva una lista de todas las palabras que son anagramas de al menos otra palabra en la lista.

# Escribe una función que tome una lista de números como argumento y devuelva una lista de las longitudes de las secuencias más largas de números consecutivos en la lista.

# Escribe una función que tome una lista de números como argumento y devuelva una lista de las diferencias entre cada número y el número siguiente en la lista.

# Escribe una función que tome dos listas de números como argumentos y devuelva una lista que contenga solo los números que aparecen en ambas listas.



#17) # Escribe una función que tome una lista de números como argumento y devuelva una lista de todos los números que son divisibles por 3 o 5.


# def numeros_divisibles(numeros):
#     divisores = []
    
#     for numero in numeros:
#         if numero % 3 == 0 or numero %5 == 0:
#             divisores.append(numero)
        
#     print(divisores)
    

# numeros_divisibles([1,2,4,5,6,7,8,9,10,11])


#18) # Escribe una función que tome dos cadenas como argumentos y devuelva una lista de todas las palabras que aparecen en ambas cadenas.

# def palabras(cadena1,cadena2):
#         conjunto1 = set(cadena1)
#         conjunto2 = set(cadena2)
#         interseccion = conjunto1.intersection(conjunto2)
#         print(interseccion)

    
# palabras(["hola","como","estas","pepe"],["hola","estas","como","3","pepe"])


#otra manera

# def palabras_comunes(cadena1, cadena2):
#     # Dividir ambas cadenas en palabras y convertirlas en conjuntos
#     set_cadena1 = set(cadena1.split())
#     set_cadena2 = set(cadena2.split())
#     # Realizar una intersección entre ambos conjuntos
#     palabras_comunes = set_cadena1 & set_cadena2
#     # Convertir el conjunto resultante en una lista y devolverla
#     return list(palabras_comunes)
    
    
# print(palabras_comunes("Esta es 2 hola una cadena de prueba 3 4", "Otra cadena para probar hola 2"))



#ejercicios de conjuntos


# conjunto1 = {1,2,3,4,5,6}
# conjunto2 = set([1,2,3,4,5,6,4,7])

# conjunto_interseccion = conjunto1.intersection(conjunto2)

# print(conjunto_interseccion)

# conjunto1 = set(["hola","tobias"])
# conjunto2 = set(["matias"])

# conjunto_interseccion = conjunto1.union(conjunto2)

# print(conjunto_interseccion)


#19) # Escribe una función que tome una cadena de palabras como argumento y devuelva una lista de todas las palabras que aparecen más de una vez en la cadena.

#mi manera muy complicado y esta mal hecha la funcion

# def palabras(cadena):
#     cantidad = len(cadena)
#     palabras_repetidas = []
#     contador = 1
#     for palabra in cadena:
#         while contador < cantidad:
#             if cadena[contador] == palabra:
#                 palabras_repetidas.append(palabra)
#             contador += 1
#     palabras_repetidas = set(palabras_repetidas)
#     return palabras_repetidas


# print(palabras(["hola","estas","estas","hola","estas"]))


# def palabras_repetidas(lista):
#     palabras_repetidas = []
#     for palabra in lista:
#         if lista.count(palabra) > 1:  #el mayor a 1 nos verifica que hay dos palabras repetidas porque count() nos devuelve un numero
#             palabras_repetidas.append(palabra)
#     return set(palabras_repetidas)

# print(palabras_repetidas(["hola","estas","tobias","hola","estas","tobias"]))