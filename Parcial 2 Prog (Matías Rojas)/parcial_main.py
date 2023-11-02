from parcial_funciones import *

# CASOS EJEMPLO
# NO ES MUTANTE: 
# adn = [
# A T G C T A
# C G A T G C
# T A C G T A
# G C T A G C
# A T G C T A
# C G A T G C
# ]
# adn = [
# A C T G A G
# T C T C G A
# G A T C T T
# C G T G A G
# T A C T G A
# G T C G A C
# ]
#----------------------------------------------------
# ES MUTANTE: 
# adn = [
# A C T G A G
# T C T C G A
# G A T C T T
# C G T G A G
# T A C T G A
# G T C G A C
# ]
# adn = [
# G A G T A G
# C A C T G C
# A C T T A C
# G T C G A A
# T T G C A T
# A A A C A G
# ]

print("Bienvenido al sistema de lectura de ADN")
print("En este programa ingresarás la estructura de ADN del sujeto para comprobar si el mismo es un mutante o no")
print("Para empezar;")
print()

# Menú:
option = 1
while option != 0:
    # Definimos variable en la que se guardara la "matriz" con los datos del ADN
    dna = []
    print("Seleccione una opción: ")
    print("1. Ingresar y comprobar ADN")
    print("0. salir")
    # Ingresar opción:
    option = int(input())
    print()
    if option == 1:
        input_dna(dna)
        show_dna(dna)
        if is_mutant(dna):
            print("el sujeto es un mutante")
            print()
        else:
            print("el sujeto no es un mutante")
            print()


print("Hasta luego!")