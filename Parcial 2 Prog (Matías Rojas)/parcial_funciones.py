# Definimos función que permitirá al usuario ingresar los datos
def input_dna(dna):
    dna_string_input = ""
    print("--------------------------------")
    print("Has seleccionado: Ingresar ADN")
    print("--------------------------------")
    print()
    print("Las estructuras de ADN están compiladas en una matriz de 6x6")
    print("Para ingresar los datos, ingrese una cadena de 6 letras que representaran cada base nitrogenada del ADN. Al ingresar dicha cadena, presione enter e ingrese la siguiente")
    print("Las letras permitidas son: A, T, C, G")
    print()
    print("Ingrese los datos del ADN del sujeto: ")
    # Defino contador que indica el número de la fila en la que el usuario está ingresando un valor
    i = 0
    # Bucle while que finalizará cuando la variable adn contenga 6 elementos dentro, es decir, que el usuario llené la matriz
    while len(dna) != 6:
        # Limpia la variable dna_string_input
        dna_string_input = ""
        i += 1
        # Bucle while que finalizará cuando el usuario ingrese una cadena válida
        while True:
            print(f"{i}- ",end= "")
            dna_string_input = input().upper()
            if valid_user_input(dna_string_input):
                dna.append(dna_string_input)
                print("Se ha agregado la cadena a la matriz")
                print("")
                break


# Definimos función que comprobará si la cadena ingresada por el usuario en la función "input_dna" es válida
def valid_user_input(user_string_input):
    # Definimos variable que nos indica las letras permitidas a ingresar
    valid_dna_inputs = ["A","T","C","G"]
    # Condicional que verifica que la cadena ingresada por el usuario tenga un largo de 6 letras
    if len(user_string_input) != 6:
                print("Debe ingresar 6 letras, porfavor, intentelo de nuevo")
                print("")
                return False
    # Definimos variable valid_dna_input que nos informará si el usuario ingresó una cadena válida
    valid_dna_input = True
    for letra in user_string_input:
        # Condicional if que nos indica si hay una letra inválida en la cadena ingresada
        if letra not in valid_dna_inputs:
            valid_dna_input = False
    if valid_dna_input:
        return True
    else:
        print("Se ha encontrado una letra inválida en la cadena, porfavor, intentelo de nuevo")
        print("")
        return False


# Definimos función que nos mostrará la "matriz" adn llenada por el usuario
def show_dna(dna):
    print("La estructura de ADN del sujeto es: ")
    # Itera las listas dentro de la lista dna:
    for dna_string in dna:
        # Itera los elementos de las listas dentro de la lista dna:
        for element in dna_string:
            print(element, end= "  ")
        print("")
    print("")

# Definimos función que nos informará si el sujeto es o no mutante
def is_mutant(dna):
    # Definimos la variable que guardará las ocurrencias totales
    mutant_dna_ocurrences = 0
    # Sumamos los retornos de las funciones de validación creadas a la variable
    mutant_dna_ocurrences += validate_rows(dna)
    mutant_dna_ocurrences += validate_colums(dna)
    mutant_dna_ocurrences += validate_main_diagonals(dna)
    mutant_dna_ocurrences += validate_secondary_diagonals(dna)
    # OPCIONAL: print(mutant_dna_ocurrences) para ver la cantidad de ocurrencias totales
    # Si la variable es mayor a 1, devolvemos un True indicando que el usuario es mutante. De otra forma, devolvemos un False
    if mutant_dna_ocurrences > 1:
        return True
    else:
        return False


# Función que cuenta las ocurrencias en las filas
def validate_rows(dna):
    # definimos variable que nos dirá cuantas ocurrencias se producen en las filas
    repeated_element_in_rows = 0
    # Iteramos los strings de la lista "dna"
    for row in range (0,len(dna)):
        # Definimos variable que contará las repeticiones de los elementos
        same_element_count = 1
        # Definimos la variable que guardará al elemento que utilizaremos para comparar
        comparative_element = ''
        # Iteramos cada caracter del string
        for letter in range (0,len(dna)):
            # Si un elemento se repite 4 veces seguidas, le sumamos una ocurrencia a la variable repeated_elements_in_rows
            if same_element_count == 4:
                repeated_element_in_rows +=1
            # Si el elemento de la posición [row][letter] es igual al elemento guardado en la variable comparative_element
            # Sumamos 1 a la variable same_element_count
            if dna[row][letter] == comparative_element:
                same_element_count += 1
            # De otra forma, reiniciamos el contador y asignamos a la variable de comparación el valor actual dna[row][letter]
            else:
                same_element_count = 1
                comparative_element = dna[row][letter]
        # Confirmamos si un elemento se repitio 4 veces al final del string
        # El if dentro del for corrobora los elementos repetidos en los casos: "TTTTAA", "ATTTTA"
        # Este if lo comprueba en el caso: "AATTTT"
        if same_element_count == 4:
            repeated_element_in_rows +=1
    return repeated_element_in_rows

# Función que cuenta las ocurrencias en las columnas
# Esta función funciona y sigue la misma estructura que la función validate_rows
# Pero en esta función recorremos las columnas en lugar de las filas.
# Esto lo hacemos llamando a dna[letter][column] al contrario de la función validate_rows: dna[row][letter]
# El resto de la estructura es la misma que la función anterior ya mencionada
def validate_colums(dna):
    repeated_element_in_columns = 0
    for column in range (0,len(dna)):
        same_element_count = 1
        comparative_element = ''
        for letter in range (0,len(dna)):
            if same_element_count == 4:
                repeated_element_in_columns +=1
            if dna[letter][column] == comparative_element:
                same_element_count += 1
            else:
                same_element_count = 1
                comparative_element = dna[letter][column]
        if same_element_count == 4:
            repeated_element_in_columns +=1
    return repeated_element_in_columns

# Función que cuenta las ocurrencias de las diagonales "principales" (Todas las diagonales que van de arriba a abajo, de izquierda a derecha)
def validate_main_diagonals(dna):
    # Definimos variable que nos indicará cuantas ocurrencias existen en las diagonales
    repeated_elements_in_main_diagonals = 0
    
    # Diagonal [0][0] a [5][5]
    # La variable dna se itera con el mismo valor en fila y columna para conseguir la diagonal principal [fila][fila] / [columna][columna]
    same_element_count = 1
    comparative_element = ''
    for row_column in range(0,len(dna)):
        if same_element_count == 4:
            repeated_elements_in_main_diagonals +=1
        if dna[row_column][row_column] == comparative_element:
            same_element_count += 1
        else:
            same_element_count = 1
            comparative_element = dna[row_column][row_column]
    if same_element_count == 4:
        repeated_elements_in_main_diagonals +=1
    
    # Diagonal [1,0] a [5,4]
    # La variable dna se itera con el valor de la fila y el valor de la fila -1 [fila][fila-1]
    # Empezando desde el valor 1 hasta el largo del arreglo dna
    same_element_count = 1
    comparative_element = ''
    for row in range(1,len(dna)):
        if same_element_count == 4:
            repeated_elements_in_main_diagonals +=1
        if dna[row][row-1] == comparative_element:
            same_element_count += 1
        else:
            same_element_count = 1
            comparative_element = dna[row][row-1]
    if same_element_count == 4:
        repeated_elements_in_main_diagonals +=1
    
    # Diagonal [0,1] a [4,5]
    # La variable dna se itera con el valor de la columna y el valor de la columna-1 [columna-1][columna]
    # Empezando desde el valor 1 hasta el largo del arreglo dna
    same_element_count = 1
    comparative_element = ''
    for column in range(1,len(dna)):
        if same_element_count == 4:
            repeated_elements_in_main_diagonals +=1
        if dna[column-1][column] == comparative_element:
            same_element_count += 1
        else:
            same_element_count = 1
            comparative_element = dna[column-1][column]
    if same_element_count == 4:
        repeated_elements_in_main_diagonals +=1
    
    # Diagonal [2,0] a [5,3]
    # La variable dna se itera con el valor de la fila y el valor de la fila -2 [fila][fila-2]
    # Empezando desde el valor 2 hasta el largo del arreglo 
    # Este bucle es distinto debido a que la diagonal solo posee 4 elementos, por lo que no necesitamos comprobaciones extra para distintos casos
    # debido a que si un solo valor es distinto ya no hay posibilidades de que la diagonal contenga una ocurrencia
    
    # Definimos variable que informará si los 4 elementos de la diagonal son iguales
    same_elements = True
    # Tomamos el primer elemento de la diagonal y lo almacenamos en una variable
    comparative_element = dna[2][0]
    # Recorremos la diagonal
    for row in range(2,len(dna)):
        # Si un elemento de la diagonal es distinto al primero, la variable same_elements será falsa
        if dna[row][row-2] != comparative_element:
            same_elements = False
    # Si todos los elementos de la diagonal son iguales, sumará una ocurrencia a la variable repeated_elements_in_main_diagonals
    if same_elements:
        repeated_elements_in_main_diagonals +=1
    
    # Diagonal [0,2] a [3,5]
    # La variable dna se itera con el valor de la columna y el valor de la columna-2 [columna][columna-2]
    # Empezando desde el valor 2 hasta el largo del arreglo 
    # sigue la estructura de la diagonal anterior
    
    same_elements = True
    comparative_element = dna[0][2]
    for columna in range(2,len(dna)):
        if dna[columna-2][columna] != comparative_element:
            same_elements = False
    if same_elements:
        repeated_elements_in_main_diagonals +=1
    return repeated_elements_in_main_diagonals

# Función que cuenta las ocurrencias de las diagonales "secundarias" (Todas las diagonales que van de abajo a arriba, de izquierda a derecha)
def validate_secondary_diagonals(dna):
    # Definimos variable que nos indicará cuantas ocurrencias existen en las diagonales
    repeated_elements_in_secondary_diagonals = 0
    
    # Diagonal [5][0] a [0][5]
    # La variable dna se itera con el valor de la fila empezando en 5 y el valor de la columna empezando en 0, con cada paso el valor de
    # la fila baja y el de la columna sube
    same_element_count = 1
    comparative_element = ''
    column = 0
    # indicamos que row irá desde el largo del arreglo-1, hasta 0-1, con un paso de -1 
    # len(dna) = 6 - 1 = 5
    for row in range(len(dna)-1,0-1,-1):
        if same_element_count == 4:
            repeated_elements_in_secondary_diagonals +=1
        if dna[row][column] == comparative_element:
            same_element_count += 1
        else:
            same_element_count = 1
            comparative_element = dna[row][column]
        # Sumamos 1 a column a modo de contador para usarlo como iterador
        column += 1
    if same_element_count == 4:
        repeated_elements_in_secondary_diagonals +=1
    
    # Diagonal [4,0] a [0,4]
    # La variable dna se itera con el valor de la fila empezando en 4 y el valor de la columna empezando en 0, con cada paso el valor de
    # la fila baja y el de la columna sube
    same_element_count = 1
    comparative_element = ''
    column = 0
    # len(dna) = 6 - 2 = 4
    for row in range(len(dna)-2,0-1,-1):
        if same_element_count == 4:
            repeated_elements_in_secondary_diagonals +=1
        if dna[row][column] == comparative_element:
            same_element_count += 1
        else:
            same_element_count = 1
            comparative_element = dna[row][column]
        column += 1
    if same_element_count == 4:
        repeated_elements_in_secondary_diagonals +=1
    
    # Diagonal [5,1] a [1,5]
    # La variable dna se itera con el valor de la fila empezando en 5 y el valor de la columna empezando en 1, con cada paso el valor de
    # la fila baja y el de la columna sube
    same_element_count = 1
    comparative_element = ''
    column = 1
    # len(dna) = 6 - 1 = 5
    for row in range(len(dna)-1,1-1,-1):
        if same_element_count == 4:
            repeated_elements_in_secondary_diagonals +=1
        if dna[row][column] == comparative_element:
            same_element_count += 1
        else:
            same_element_count = 1
            comparative_element = dna[row][column]
        column += 1
    if same_element_count == 4:
        repeated_elements_in_secondary_diagonals +=1
    
    # Diagonal [3,0] a [0,3]
    # La variable dna se itera con el valor de la fila empezando en 3 y el valor de la columna empezando en 0, con cada paso el valor de
    # la fila baja y el de la columna sube
    # Este bucle es distinto debido a que la diagonal solo posee 4 elementos, por lo que no necesitamos comprobaciones extra para distintos casos
    # debido a que si un solo valor es distinto ya no hay posibilidades de que la diagonal contenga una ocurrencia
    
    # Definimos variable que informará si los 4 elementos de la diagonal son iguales
    same_elements = True
    column = 0
    # Tomamos el primer elemento de la diagonal y lo almacenamos en una variable
    comparative_element = dna[3][0]
    # len(dna) = 6 - 3 = 3
    for row in range(len(dna)-3,0-1,-1):
        # Si un elemento de la diagonal es distinto al primero, la variable same_elements será falsa
        if dna[row][column] != comparative_element:
            same_elements = False
        column +=1
    # Si todos los elementos de la diagonal son iguales, sumará una ocurrencia a la variable repeated_elements_in_main_diagonals
    if same_elements:
        repeated_elements_in_secondary_diagonals +=1
    
    # Diagonal [5,2] a [2,5]
    # La variable dna se itera con el valor de la fila empezando en 5 y el valor de la columna empezando en 2, con cada paso el valor de
    # la fila baja y el de la columna sube
    # sigue la estructura de la diagonal anterior
    same_elements = True
    column = 2
    comparative_element = dna[5][2]
    # len(dna) = 6 - 1 = 5
    for row in range(len(dna)-1,2-1,-1):
        if dna[row][column] != comparative_element:
            same_elements = False
        column +=1
    if same_elements:
        repeated_elements_in_secondary_diagonals +=1
    return repeated_elements_in_secondary_diagonals