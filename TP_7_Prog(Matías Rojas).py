# 1.	Escribe un programa que tome una lista de números como entrada y la ordene en orden ascendente 
# utilizando el método de ordenamiento de burbuja.
array = []
print("Ingrese los valores del array: ")
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