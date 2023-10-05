# 1.    Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
def valid_dni (dni):
    if len(dni) == 7 or len(dni) == 8:
        return True
    else:
        return False

# 2.	Escribir una función que, dado un string, retorne la longitud de la última palabra. 
# Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios 
# al principio o al final del string pasado por parámetro.
def long_word (words):
    words = words.split()
    last_word = words[len(words)-1]
    return len(last_word)

# 3.	Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. 
# Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento 
# mediante el ingreso de un nombre vacio.
# Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, 
# en cuyo caso será: nombre1, nombre2, apellido. Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
# Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario 
# en un bucle hasta que ingrese un DNI correcto.
# Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad 
# de letras del apellido y los 3 primeros dígitos de su DNI. Ejemplo:
# Nombre: María Ines Rosales
# DNI: 25469648
# ID -> Maria7254
def id_club(full_name, id_dni):
    full_name = full_name.split()
    length_lastname = ""
    if len(full_name) == 3:
        length_lastname = len(full_name[2])
    if len(full_name) == 2:
        length_lastname = len(full_name[1])
    club_id = full_name[0]+str(length_lastname)+id_dni[0:3]
    return club_id

# 4.	Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. 
# Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.
def is_multiple_of (num1, multiplenum1):
    if multiplenum1 % num1 == 0:
        return True
    else:
        return False 

# 5.	Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
# Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de 
# cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.
def average_temperature (min_temp, max_temp):
    return (min_temp + max_temp) / 2

# 6.	Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio 
# adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa 
# principal donde se use dicha función.
def extra_space(inp_string):
    final_string = ""
    for i in inp_string:
        final_string += i + " "
    return final_string

# 7.	Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. 
# Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.
def min_max_num(nums_list):
    max = nums_list[0]
    min = nums_list[0]
    for i in nums_list:
        if i < min:
            min = i
        if i > max:
            max = i
    return max,min

# 8.	Diseñar una función que calcule el área y el perímetro de una circunferencia. 
# Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.
def area_perimeter_circumference(rad):
    import math
    area = math.pi * math.pow(rad,2)
    perimeter = 2 * math.pi * rad
    return area,perimeter

# 9.	Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te 
# devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe 
# el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, 
# solamente tenemos tres oportunidades para intentarlo.
def login(username, password, tries):
    if username == "usuario1" and password == "asdasd":
        return True, tries
    else:
        return False, tries-1

# 10.	Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un 
# diccionario con los precios y porcentajes del carrito de compra, aplicar los descuentos a los productos del carrito  
# y devolver el precio final de la compra.
def buy_discount(items_buyed):
    discounted_final_price = 0
    for product, info in items_buyed.items():
        price = info['precio']
        discount = info['descuento']
        discounted_price = price - (price * discount / 100)
        discounted_final_price += discounted_price
    return discounted_final_price

# 11.	Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado 
# de aplicar la función dada a cada uno de los elementos de la lista.
def list_modifier(moded_list):
    counter = 0
    for i in moded_list:
        if type(i) == int or type(i) == float:
            moded_list[counter] = moded_list[counter]*10
        if type(i) == str:
            moded_list[counter] += "!"
        if type(i) == bool:
            if i == True:
                moded_list[counter] = False
            if i == False: 
                moded_list[counter] = True
        counter += 1
    return moded_list

def list_reciever(list_inp):
    list_inp = list_modifier(list_inp)
    return list_inp

# 12.	Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
def dictionary_words_and_length(phrase):
    dictionary = {}
    phrase = phrase.lower()
    phrase = phrase.split()
    counter = 0
    for i in phrase:
        length_word = len(i)
        dictionary[phrase[counter]] = length_word
        counter += 1
    return dictionary

# 13.	Escribir una función que calcule el módulo de un vector.
def vector_module(coord_a, coord_b):
    import math
    vec_mod = math.pow(coord_a, 2) + math.pow(coord_b, 2)
    vec_mod = math.sqrt(vec_mod)
    return vec_mod

# 14.	Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función 
# booleana que lo decida.
def is_prime_num(num):
    if num == 1:
        return False
    else:
        if num == 2 or num == 3 or num == 5:
            return True
        else:
            if num % 1 == 0 and num % num == 0 and num % 2 != 0 and num % 3 != 0 and num % 5 != 0: 
                return True
            else:
                return False
# 15.	Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, la 
# cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.
def factorial(num): 
    if num < 0: 
        print("El factorial de un número negativo no existe")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# 16.	Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito 
# en el número, utilizando para ello una función que calcule la frecuencia.
def digit_in_number(num, digit):
    in_number = 0
    for i in num:
        if digit == i:
            in_number += 1
    return in_number

# 17.	Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que 
# no sea primo. Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e 
# informar la cantidad de veces que aparece en el número (frecuencia). Al finalizar el programa, mostrar el 
# factorial del mayor número ingresado.
def digit_sum(num):
    sum = 0
    for i in num:
        sum += int(i)
    return sum
# reutilizo las funciones:
# digit_in_number
# factorial
# is_prime_num