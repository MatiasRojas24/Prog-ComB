# 1.	Solicitar al usuario que ingrese números, estos deben guardarse en una lista. 
# Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.
num_list = []
num = int(input("Ingrese un número: "))
num_list.append(num)
while num != 0:
    num = int(input("Ingrese otro número (para finalizar ingrese 0): "))
    if num != 0:
        num_list.append(num)
print("Los números ingresados se han guardado en una lista")
print("La lista resultante es: ", num_list)

# 2.	A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, 
# eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
delete = False
num_delete = int(input("Ingrese el número que desea borrar de la lista (tenga en cuenta que solo se eliminará su primera ocurrencia): "))
for i in num_list:
    if i == num_delete:
        delete = True
        num_list.remove(i)
if delete:
    print("Se ha eliminado el número", num_delete)
    print("La lista resultante es: ", num_list)
else:
    print(f"El número {num_delete} no se encuentra en la lista")

# 3.	Imprimir la sumatoria de todos los números de la lista.
list_sum = 0
for i in num_list:
    list_sum += i
print("La suma de los elementos de la lista es: ",list_sum)

# 4.	Solicitar al usuario otro número y crear una lista con los elementos de la lista original, que sean menores 
# que el número dado. Imprimir esta nueva lista, iterando por ella.
less_than = int(input("Ingrese un número: "))
less_than_list = []
for i in num_list:
    if i < less_than:
        less_than_list.append(i)
print(f"Se ha creado una lista con todos los números menores a {less_than} de la lista original")
print("Sus elementos son: ")
for i in less_than_list:
    print(i)

# 5.	Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un 
# número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original 
# es [5,16,2,5,57,5,2], la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]
num_frecuency_list = []
counter = 0
for i in num_list:
    num_frecuency_list.append((i,num_list.count(i)))
num_frecuency_list_aux = num_frecuency_list
while counter != len(num_frecuency_list_aux):
    i = num_frecuency_list_aux[counter]
    if num_frecuency_list.count(i) != 1:
        num_frecuency_list.remove(i)
    counter += 1
print("Se ha creado una lista que incluye (num, cantidad de veces que se repite el número)")
print("La listas resultante es: ",num_frecuency_list)

# 6.	Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar ‘x’. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar ‘x’.
# a.	Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.
# b.	Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
# c.	Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
elementary_school_names = []
middle_school_names = []
print("Ingrese uno a uno el nombre de pila de los alumnos de primaria (para finalizar ingrese x): ")
name = ""
while name != "x" or name != "X":
    if name != "x" or name != "X":
        name = input().capitalize()