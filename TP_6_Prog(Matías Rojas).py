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
num_frequency_list = []
counter = 0
for i in num_list:
    num_frequency_list.append((i,num_list.count(i)))
num_frequency_list_aux = num_frequency_list
while counter != len(num_frequency_list_aux):
    i = num_frequency_list_aux[counter]
    if num_frequency_list.count(i) != 1:
        num_frequency_list.remove(i)
    counter += 1
print("Se ha creado una lista que incluye (num, cantidad de veces que se repite el número)")
print("La listas resultante es: ",num_frequency_list)

# 6.	Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar ‘x’. 
# A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar ‘x’.
# a.	Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.
# b.	Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
# c.	Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
elementary_school_names = []
middle_school_names = []
school_names = []
print("Ingrese uno a uno el nombre de pila de los alumnos de primaria (para finalizar ingrese x): ")
name = ""
while name != "x" or name != "X":
    name = input().capitalize()
    if name == "x" or name == "X":
        break
    elementary_school_names.append(name)
print("Ingrese uno a uno el nombre de pila de los alumnos de secundaria (para finalizar ingrese x): ")
name = ""
while name != "x" or name != "X":
    name = input().capitalize()
    if name == "x" or name == "X":
        break
    if name != "" or name != " ":
        middle_school_names.append(name)

for i in elementary_school_names:
    school_names.append(i)
for i in middle_school_names:
    school_names.append(i)

aux_school_names = school_names.copy()

for i in school_names:
    if school_names.count(i) != 1:
        school_names.remove(i)

print("Los nombres de todos los alumnos de primaria y secundaria son: ")
for i in school_names:
    print("-", i)

print("Los nombres que se repiten entre los alumnos son: ")
for i in school_names:
    if aux_school_names.count(i) > 1:
        print("-",i)

print("Los nombres de primaria que no se repiten en secundaria son: ")
for i in elementary_school_names:
    if aux_school_names.count(i) == 1:
        print("-",i)
        
# 7.	Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings. 
# Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. Ejemplo:
# ‘r’:5
# ‘%’:3
# ‘a’:8
# ‘9’:1
counter = 0
strings = []
caracters = []
caracter_frequency = []
while counter != 50:
    string = input("Ingrese un string: ")
    strings.append(string)
    counter += 1

for element in strings:
    for letter in element:
        caracters.append(letter)
aux_caracters = caracters.copy()

for i in aux_caracters:
    if caracters.count(i) != 1:
        caracters.remove(i)

for i in caracters:
    caracter_frequency.append((f"'{i}':{aux_caracters.count(i)}"))

print("La lista de ocurrencias por caracter en los strings ingresados es la siguiente:")
for i in caracter_frequency:
    print(i)

# 8.	Diez equipos de la liga inter-barrial identificados con los números 1, 2, 3, 4, …, 10, participaron en un campeonato de fútbol 
# con modalidad todos contra todos. 
# Escriba un programa que:
#  Lea el cuadro de goles en un arreglo de dos dimensiones.
#  Muestre para cada equipo la cantidad de triunfos, empates y derrotas.
#  Muestre la diferencia entre el total de goles marcados y el total de goles recibidos.
#  Determine la cantidad de puntos obtenidos por cada equipo.
import random
def dif_scored_and_received_goals (team):
        team = team-1
        scored_goals = 0
        received_goals = 0
        for j in range(0,10):
            if team != j:
                scored_goals += goals[j][team]
        for j in range(0,10):
            if team != j:
                received_goals += goals[team][j]
        print(f"El equipo {team+1} ha hecho {scored_goals} goles y ha recibido {received_goals} teniendo una diferencia de {abs(scored_goals-received_goals)} goles entre anotados y recibidos")

def wins_draws_defeats (team):
    team = team -1
    wins = 0
    draws = 0
    defeats = 0
    for j in range(0,10):
        if team != j:
            if goals[j][team] > goals[team][j]:
                wins += 1
            if goals[team][j] > goals[j][team]:
                defeats += 1
            if goals[j][team] == goals[team][j]:
                draws += 1
    print(f"Las estadísticas del equipo {team+1} son las siguientes:")
    print("Victorias: ",wins)
    print("Derrotas: ",defeats)
    print("Empates: ",draws)

def points_per_team (team):
    team = team -1
    wins = 0
    draws = 0
    points = 0
    for j in range(0,10):
        if team != j:
            if goals[j][team] > goals[team][j]:
                wins += 1
            if goals[j][team] == goals[team][j]:
                draws += 1
    points += wins * 3
    points += draws 
    print(f"El equipo {team+1} tiene {points} puntos")

goals = []
goals_aux = []

for i in range(0,10):
    for j in range(0,10):
        if i == j:
            goals_aux.append(0)
            continue
        goals_aux.append(random.randint(0,5))
    goals.append(goals_aux.copy())
    goals_aux.clear()
team = 1

print("La tabla con los goles hechos por los equipos es la siguiente (siendo las columnas el equipo que hizo los goles y las filas el equipo que recibió los goles):")
print(end='    ')
for i in range(1,11):
        print(team, end = '   ')
        team += 1
print("")
team = 1
for i in goals:
        print(team, end='   ')
        for j in i:
            print(j, end = '   ')
        team +=1
        print("")
print("")

#  Muestre para cada equipo la cantidad de triunfos, empates y derrotas.
for i in range(1,11):
    wins_draws_defeats(i)
print("")
#  Muestre la diferencia entre el total de goles marcados y el total de goles recibidos.
for i in range(1,11):
    dif_scored_and_received_goals(i)
print("")

#  Determine la cantidad de puntos obtenidos por cada equipo.
for i in range(1,11):
    points_per_team(i)

# 9.	Escribir un programa que simule el juego clásico de Memoria (Memotest) utilizando matrices. 
#El juego consiste en un tablero de cartas boca abajo y el objetivo es encontrar todas las parejas de cartas iguales.
import copy
def showBoard(board):
    pos = 1
    coords2 = {1:'a', 2:'b', 3:'c', 4:'d'}
    print(end='    ')
    for i in range(1,5):
        print(coords2[pos], end = '   ')
        pos += 1
    print("")
    pos = 1
    for i in board:
        print(pos, end='   ')
        for j in i:
            print(j, end = '   ')
        pos +=1
        print("")

def board_state(board):
    board_state_bool = True
    for i in board:
        for j in i:
            if j == 'X':
                return False
    return board_state_bool

def card_input():
    user_coord = input("Ingrese una posición (EJ: b3): ").lower()
    while user_coord[0] not in coords.keys() or int(user_coord[1]) not in coords.values():
        user_coord = input("Ingrese una posición valida: ").lower()
    while current_board[int(user_coord[1])-1][coords[user_coord[0]]] != 'X':
        user_coord = input(f"La carta en las coordenadas {user_coord} ya ha sido revelada: ").lower()
        while user_coord[0] not in coords.keys() or int(user_coord[1]) not in coords.values():
            user_coord = input("Ingrese una posición valida: ").lower()
    while current_board_aux[int(user_coord[1])-1][coords[user_coord[0]]] != 'X':
        user_coord = input(f"Ya has seleccionado esa carta: ").lower()
        while user_coord[0] not in coords.keys() or int(user_coord[1]) not in coords.values():
            user_coord = input("Ingrese una posición valida: ").lower()
    return user_coord

coords = {'a':0, 'b':1, 'c':2, 'd':3}
current_board = [
    ['X','X','X','X'],
    ['X','X','X','X'],
    ['X','X','X','X']]
current_board_aux = copy.deepcopy(current_board)
cards = [
    [1,4,3,2],
    [6,6,5,1],
    [2,5,4,3]]
complete_board = board_state(current_board)

print("Bienvenido a Memotest!")
print("Encuentra todos los pares del tablero para ganar el juego!")
print("El tablero a resolver es el siguiente: ")
print("")
while complete_board == False:
    already_selected = False
    showBoard(current_board)
    print("")
    input_coord = card_input()
    column = input_coord[0]
    column = coords[column]
    row = int(input_coord[1])-1
    current_board_aux[row][column] = cards[row][column]
    first_selected = current_board_aux[row][column]
    showBoard(current_board_aux)
    print("")
    input_coord = card_input()
    column = input_coord[0]
    column = coords[column]
    row = int(input_coord[1])-1
    current_board_aux[row][column] = cards[row][column]
    last_selected = current_board_aux[row][column]
    showBoard(current_board_aux)
    if last_selected == first_selected:
        print("Has encontrado un par!")
        print("")
        current_board = copy.deepcopy(current_board_aux)
    else:
        print("No se ha encontrado un par")
        print("")
        current_board_aux = copy.deepcopy(current_board)
    complete_board = board_state(current_board)

print("Has ganado! Felicidades!")

# 10.	Teniendo una matriz cuadrada de cualquier dimensión, obtener lo siguiente:
# a.	la diagonal principal.
# b.	la diagonal inversa.
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]
principal_diagonal = []
inverse_diagonal = []
counter_i = 0
counter_j = 0
#obtener el largo de las filas de la matriz
last = len(matrix[len(matrix)-1])-1

print("La matriz es: ")
for i in matrix:
    for j in i:
        print(j, end= '   ')
    print("")
#diagonal principal
for i in matrix:
    for j in i:
        if counter_i == counter_j:
            principal_diagonal.append(i[counter_j])
        counter_j +=1
    counter_j = 0
    counter_i += 1
#diagonal inversa
for i in matrix:
    for j in i:
        if last == counter_j:
            inverse_diagonal.append(i[counter_j])
        counter_j +=1
    counter_j = 0
    last -= 1
print("La diagonal principal de la matriz es: ", principal_diagonal)
print("La diagonal inversa de la matriz es: ", inverse_diagonal)

# 11.	Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
currency = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currency_input = input("Ingrese una divisa: ").capitalize()
if currency_input in currency.keys():
    print(currency[currency_input])
else:
    print("La divisa ingresada no se encuentra en el sistema")

# 12.	Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde 
# en un diccionario. Después debe mostrar por pantalla el mensaje ‘<nombre> tiene <edad> años, vive en 
# <dirección> y su número de teléfono es <teléfono>’.
info = {}
info['name'] = input("Ingrese su nombre: ").title()
info['age'] = input("Ingrese su edad: ")
info['adress'] = input("ingrese su dirección: ").capitalize()
info['phone_number'] = input("ingrese su número de teléfono: ")
print(f"{info['name']} tiene {info['age']} años, vive en {info['adress']} y su número de teléfono es {info['phone_number']}")

# 13.	Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al 
# usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
fruit_prices = {'manzana':510, 'frutilla':1300, 'banana':813, 'naranja':559}
fruit = ""
while fruit not in fruit_prices:
    fruit = input("Ingrese la fruta que desea comprar: ").lower()
    if fruit not in fruit_prices:
        print("La fruta ingresada no se encuentra en el mercado.")
fruit_amount = float(input(f"Cuantos kilos de {fruit} desea comprar? "))
print(f"Ha comprado {fruit_amount} kilos de {fruit}, el precio de dichos kilos es de ${fruit_prices[fruit]*fruit_amount}")
