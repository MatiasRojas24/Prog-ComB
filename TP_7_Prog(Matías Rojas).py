# 1.	Escribe un programa que tome una lista de números como entrada y la ordene en orden ascendente 
# utilizando el método de ordenamiento de burbuja.
array = []
print("Ingrese los números que contendrá el array: ")
for i in range(0,10):
    print(i+1,"-",end=" ") 
    array.append(int(input()))
print("El array es:")
print(array)

for i in range(len(array)+1):
    for current_index in range(len(array) - 1):
        next_element_index = current_index + 1
        if array[current_index] > array[next_element_index]:
            array[next_element_index], array[current_index] = array[current_index], array[next_element_index]

print("El array ordenado de forma ascendente es: ")
print(array)

# 2.	Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en 
# orden ascendente utilizando el método de ordenamiento de selección.
array = []
print("Ingrese las palabras que contendrá el array: ")
for i in range(0,10):
    print(i+1,"-",end=" ") 
    array.append(input())
print("El array es:")
print(array)


for i in range(len(array)-1):
    for j in range(i+1, len(array)):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]

print("El array ordenado de alfabéticamente es: ")
print(array)

# 3.	Crea una lista de diccionarios, donde cada diccionario contiene información sobre un libro 
# (título, autor, año de publicación, etc.). Luego, escribe un programa que ordene la lista de libros en 
# función de un campo específico, como el año de publicación o el autor.
book_info = {1:{'titulo':'Fahrenheit 451', 'autor':'Ray Bradbury', 'año de publicación':1953}, 2:{'titulo':'Harry Potter y la piedra filosofal', 'autor':'J. K. Rowling', 'año de publicación':1997}, 3:{'titulo':'El corazón delator', 'autor':'Edgar Allan Poe', 'año de publicación':1834}, 4:{'titulo':'Martín Fierro', 'autor':'José Hernández', 'año de publicación':1872}, 5:{'titulo':'Rayuela', 'autor':'Julio Cortázar', 'año de publicación':1963}}

for i in range (1,5+1):
    print(book_info[i])
print("")
length = len(book_info)
for i in range(1,length+1):
    for j in range(i+1, length+1):
        if book_info[i]['año de publicación'] > book_info[j]['año de publicación']:
            book_info[i], book_info[j] = book_info[j], book_info[i]

for i in range (1,5+1):
    print(book_info[i])

# 4.	Escribe un programa que tome una lista de cadenas como entrada y las 
# ordene en orden ascendente según su longitud. Puedes utilizar el método de 
# ordenamiento de inserción.
strings_list = ["avion", "auto", "ave", "electrodómestico", "Ferrocarril", "celular", "camión", "telescopio"]
print(strings_list)

for i in range(len(strings_list)):
    aux = strings_list[i]
    j = i -1
    while j >= 0 and len(aux) < len(strings_list[j]):
        strings_list[j+1] = strings_list[j]
        j -= 1
    strings_list[j + 1] = aux

print(strings_list)

# 5.	Modifica uno de los ejercicios anteriores para ordenar la lista de números en orden 
# descendente en lugar de ascendente.
array = []
print("Ingrese los números que contendrá el array: ")
for i in range(0,10):
    print(i+1,"-",end=" ") 
    array.append(int(input()))
print("El array es:")
print(array)

for i in range(len(array)-1):
    for j in range(i+1, len(array)):
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]

print("El array ordenado de alfabéticamente es: ")
print(array)

# 6.	Escribe un programa que tome una lista de números enteros y ordene la lista utilizando 
# el algoritmo de ordenamiento por conteo.

# 7.	Crea una lista que contenga tanto números como cadenas de caracteres. Escribe un programa 
# que ordene esta lista de manera que primero estén los números ordenados de menor a mayor y luego 
# las cadenas de caracteres ordenadas alfabéticamente.

# 8.	Implementa el algoritmo de ordenamiento Merge Sort y úsalo para ordenar una lista de números.
