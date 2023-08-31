# Ejercicios en clase for-while
# 1- 
print("Bienvenido.")
mensaje1 = input("Ingrese el primer mensaje: ")
mensaje1 = mensaje1.lower()
encrip1 =  ""
mens_final1 = ""

mensaje2 = input("Ingrese el segundo mensaje: ")
mensaje2 = mensaje2.lower()
encrip2 =  ""
mens_final2 = ""

mensaje3 = input("Ingrese el tercer mensaje: ")
mensaje3 = mensaje3.lower()
encrip3 =  ""
mens_final3 = ""

mensaje4 = input("Ingrese el cuarto mensaje: ")
mensaje4 = mensaje4.lower()
encrip4 =  ""
mens_final4 = ""

mensaje5 = input("Ingrese el quinto mensaje: ")
mensaje5 = mensaje5.lower()
encrip5 =  ""
mens_final5 = ""

corrimiento = int(input("Ingrese cuantas letras se tienen que correr para los mensajes: "))
abc = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'ñ': 15, 
    'o': 16, 'p': 17, 'q': 18, 'r': 19, 's': 20, 't': 21, 'u': 22, 'v': 23, 'w': 24, 'x': 25, 'y': 26, 'z': 27}
cba = {"1" : 'a', "2" : 'b', "3" : 'c', "4" : 'd', "5" : 'e', "6" : 'f', "7" : 'g', "8" : 'h', "9" : 'i', "10" : 'j', 
    "11" : 'k', "12" : 'l', "13": 'm', "14" : 'n', "15" : 'ñ', "16": 'o', "17": 'p', "18": 'q', "19": 'r', "20": 's', "21": 't', 
    "22": 'u', "23": 'v', "24": 'w', "25": 'x', "26": 'y', "27" : 'z',}

for letra in mensaje1:
        if letra in abc:
            encrip1 += str((abc[letra] + corrimiento)%27) + " "
        else:
            encrip1 += letra + " "
encrip1 = encrip1.split()
for n in encrip1:
    if  n in cba:
        mens_final1 += cba[n]
    else:
        mens_final1 += n

for letra in mensaje2:
        if letra in abc:
            encrip2 += str((abc[letra] + corrimiento)%27) + " "
        else:
            encrip2 += letra + " "
encrip2 = encrip2.split()
for n in encrip2:
    if  n in cba:
        mens_final2 += cba[n]
    else:
        mens_final2 += n

for letra in mensaje3:
        if letra in abc:
            encrip3 += str((abc[letra] + corrimiento)%27) + " "
        else:
            encrip3 += letra + " "
encrip3 = encrip3.split()
for n in encrip3:
    if  n in cba:
        mens_final3 += cba[n]
    else:
        mens_final3 += n

for letra in mensaje4:
        if letra in abc:
            encrip4 += str((abc[letra] + corrimiento)%27) + " "
        else:
            encrip4 += letra + " "
encrip4 = encrip4.split()
for n in encrip4:
    if  n in cba:
        mens_final4 += cba[n]
    else:
        mens_final4 += n

for letra in mensaje5:
        if letra in abc:
            encrip5 += str((abc[letra] + corrimiento)%27) + " "
        else:
            encrip5 += letra + " "
encrip5 = encrip5.split()
for n in encrip5:
    if  n in cba:
        mens_final5 += cba[n]
    else:
        mens_final5 += n
print("primer mensaje: ")
print(mens_final1)
print("segundo mensaje: ")
print(mens_final2)
print("tercer mensaje: ")
print(mens_final3)
print("cuarto mensaje: ")
print(mens_final4)
print("quinto mensaje: ")
print(mens_final5)

# 2- 
num = ""
num_i = ""
dig_par = 0
dig_impar = 0
dig_par_t = 0
dig_impar_t = 0
while num != "0":
    dig_impar = 0
    dig_par = 0
    num = input("Ingrese un número: ")
    if num != "0":
        for x in num:
            if ( int(x) % 2) == 00:
                dig_par +=1
                dig_par_t +=1
            else:
                dig_impar +=1
                dig_impar_t +=1
    else:
        break
    print(f"El número {num} tiene {dig_par} digitos pares y {dig_impar} digitos impares")
    print("Para finalizar, ingrese el número 0.")
print(f"Cantidad de digitos pares totales: {dig_par_t}")
print(f"Cantidad de digitos impares totales: {dig_impar_t}")