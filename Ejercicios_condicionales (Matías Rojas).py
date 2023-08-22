#Declaración variables auxiliares
boolean = False
nivel = ""

#Ingresar fecha
print("Bienvenido.")
print("Ingrese la fecha actual en formato: [día, DD/MM].")
print("Siendo día un día de la semana, DD el número del día y MM el número del mes.")
fecha = input()
fecha = fecha.lower()
dia = fecha[0:fecha.find(",")]
dia_n = int(fecha[fecha.find(" ")+1:fecha.find("/")])
mes = int(fecha[fecha.find("/")+1:])


#Comprobación fecha ingresada
if dia == "lunes":
    boolean = True
    nivel = "inicial"

if dia == "martes":
    boolean = True
    nivel = "intermedio"

if dia == "miercoles":
    boolean = True
    nivel = "avanzado"

if dia == "miércoles":
    boolean = True
    nivel = "avanzado"

if dia == "jueves":
    boolean = True
    nivel = "practica"

if dia == "viernes":
    boolean = True
    nivel = "extranjeros"
if boolean == False:

    print(f"{dia} no es un día válido.")
    exit()
if dia_n > 32 or dia_n < 1:
    print(f"{dia_n} no es un día válido.")
    exit()
if mes > 12 or mes < 1:
    print(f"{mes} no es un mes válido.")
    exit()

#Nivel inicial, intermedio y avanzado
if nivel == "inicial" or nivel == "intermedio" or nivel == "avanzado":
    print("¿Se tomaron exámenes? [SI/NO]")
    tom_ex = input()
    tom_ex = tom_ex.lower()
    if tom_ex == "si":
        print("Ingrese la cantidad de aprobados y desaprobados [aprobados, desaprobados]")
        cant = input()
        ap = int(cant[0:cant.find(",")])
        desap = int(cant[cant.find(" ")+1:])
        cantidad = ap + desap
        porcentaje = ap / cantidad
        porcentaje *= 100
        print(f"La cantidad de aprobados es del {porcentaje}%.")

#Prácticas habladas
if nivel == "practica":
    asis = int(input("Ingrese el porcentaje de asistencia a clase [num]: "))
    if asis > 50:
        print("Asistió la mayoría a clases.")
    else:
        print("No asistió la mayoría a clases.")

#Clases extranjeros
if nivel == "extranjeros" and dia_n == 1 and mes == 1 or mes == 7:
    print("Comienzo de nuevo ciclo")
    print("Ingrese la cantidad de alumnos y el arancel en $ por cada alumno [alumnos, $arancel]")
    inf = input()
    cant_a = int(inf[0:inf.find(",")])
    arancel = int(inf[inf.find("$")+1:])
    ing_tot = arancel * cant_a 
    print(f"Los ingresos totales son de ${ing_tot:.2f}")