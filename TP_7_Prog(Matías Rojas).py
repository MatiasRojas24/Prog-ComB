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
def counting_sort(numbers):
    if not numbers:
        return numbers
    
    max_value = max(numbers)
    count = [0] * (max_value + 1)

    for num in numbers:
        count[num] += 1

    sorted_numbers = []
    for i in range(max_value + 1):
        sorted_numbers.extend([i] * count[i])
    
    return sorted_numbers

list = [3, 1, 4, 5, 2, 7, 10, 6, 9, 8]
sorted_numbers = counting_sort(list)
print(sorted_numbers)
# 7.	Crea una lista que contenga tanto números como cadenas de caracteres. Escribe un programa 
# que ordene esta lista de manera que primero estén los números ordenados de menor a mayor y luego 
# las cadenas de caracteres ordenadas alfabéticamente.
def order_numbers_strings(list):
    numbers = []
    strings = []

    for i in list:
        if isinstance(i, (int, float)):
            numbers.append(i)
        elif isinstance(i, str):
            strings.append(i)
        
    numbers.sort()
    strings.sort()

    sorted_list = numbers + strings
    return sorted_list

mixed_list = ["Lionel Messi", 10, "Cristiano Ronaldo", 7, "Erling Haaland", 9]
sorted_mixed_list = order_numbers_strings(mixed_list)
print(sorted_mixed_list)

# 8.	Implementa el algoritmo de ordenamiento Merge Sort y úsalo para ordenar una lista de números.
def merge_sort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2  
        left_half = numbers[:mid]
        right_half = numbers[mid:]

        merge_sort(left_half)  
        merge_sort(right_half)  

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                numbers[k] = left_half[i]
                i += 1
            else:
                numbers[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            numbers[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            numbers[k] = right_half[j]
            j += 1
            k += 1

list = [3, 1, 4, 5, 2, 7, 10, 6, 9, 8]
print("Lista Desordenada:")
print(list)

merge_sort(list)
print("Lista Ordenada:")
print(list)
