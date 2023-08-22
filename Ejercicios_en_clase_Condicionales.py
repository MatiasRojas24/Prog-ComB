print("Bienvenido")
print("Ingrese la fecha actual en formato: [día, DD/MM].")
print("Siendo día un día de la semana, DD el número del día y MM el número del mes")
fecha = input()
fecha = fecha.lower()
dia = fecha[0:fecha.find(",")]
dia_n = int(fecha[fecha.find(" ")+1:fecha.find("/")])
mes = int(fecha[fecha.find("/")+1:])
boolean = False

if dia == "lunes":
    boolean = True
if dia == "martes":
    boolean = True
if dia == "miercoles":
    boolean = True
if dia == "miércoles":
    boolean = True
if dia == "jueves":
    boolean = True
if dia == "viernes":
    boolean = True
    
if boolean == False:
    print(f"{dia} no es un día válido.")
    exit()
if dia_n > 32:
    print(f"{dia_n} no es un día válido.")
    
if mes > 12:
    print(f"{mes} no es un mes válido.")
