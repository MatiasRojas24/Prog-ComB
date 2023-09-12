action = 1
cash = 100000
r_dolar = 0
dolar = 51

print("Bienvenido!")

# bucle while seleccion de funciones
while action != 0:
    dolar = 51
    print("Seleccione una acción")
    print("1. Extracción.") 
    print("2. Deposito") 
    print("3. Consulta de Saldo") 
    print("4. Cambio Peso-Dolar") 
    print("5. Inversiones") 
    print("0. Salir")

    action = int(input("Opción: "))
    money_b = int(0)
    
    if action == 1:
        print("-----------------")
        print("Extracciones")
        print("-----------------")
        extration = float(input("Ingrese el saldo que desea retirar: "))
        while extration>cash:
            print("Saldo insuficiente---Retire un saldo correspondiente de acuerdo a sus ahorros---Consulte su saldo")
            option = int(input("Volver al menù(presione 0)--- Extracciòn(presione cualquier nùmero):"))
            if option == 0:
                break
            extration = float(input("Ingrese el saldo que desea retirar: "))
        cash = cash-extration 
        print(" ")
    elif action == 2:
        print("--------------------------")
        print("Ha Seleccionado Deposito")
        print("--------------------------")
        cantidad_deposito = int(input("¿Cúanto Dinero desea Depositar?: $"))
        cash += cantidad_deposito
        print("Su Monto ha sido depostiado Correctamente")
    elif action == 3:
        print("--------------------------")
        print("Usted eligio consulta de saldo")
        print("--------------------------")
        money_f = cash + money_b
        print(f"Su saldo en pesos es de: ${cash}")
        print(f"Su saldo en dolares es de: ${r_dolar}")
    elif action == 4:
            print("-----------")
            print("Usted eligió cambio peso-dólar")
            print("-----------")
            print("Ingrese cuantos dólares desea (Tenga en cuenta que solo puede retirar un máximo de 50 dolares ")
            print("Para volver al menú ingrese 0")
            while dolar != 0:
                dolar = float(input("Dólares a retirar: $"))
                if dolar == 0:
                    break
                if dolar > 50:
                    print("No puede retirar más de 50 dólares")
                    continue
                if cash - (dolar * 700) < 0:
                    print(f"No posee saldo suficiente para retirar {dolar} dólares")
                    continue
                if dolar <= 50 and dolar > 0:
                    cash = cash - dolar*700
                    print(f"Usted a retirado {dolar} dólares")
                    r_dolar += dolar
    
    elif action == 5:
        print("-----------")
        print("Usted eligió Inversiones")
        print("-----------")
        interest=1.15
        money = float(input("Cuanto dinero desea ingresar?: $"))
        total_money=money
        print("*-------------------------------------------------------------------*")
        #IF para verificar que se igrese el monto minimo
        if money<1000:
            print("Debe ingresar un minimo de 1000 pesos")
        else:
            print("Se ingresaron ",money," pesos")
            print("Cuantos años quiere dejar el dinero (minimo de 1 años)")
            years=int(input())
            #IF para verificar que se ingrese por lo menos un año
            if years>0:
                #Ciclo for que muestra el crecimiento del valor del desposito por cada año que pase
                for i in range(years):
                        total_money=total_money*interest
                        print("En",i+1,"año/s tendra:",total_money,"pesos")
            #Si no se ingresa por lo menos un año, se entra en un bucle hasta que se ingrese un año mayor a cero
            else:
                while years<1 :
                    print("Los años deben ser mayores que cero")
                    print("cuantos años quiere dejar el dinero: ")
                    years=int(input())
                for i in range(years):
                        total_money=total_money*interest
                        print("En ",i+1,"año/s tendra: ",total_money," pesos")
    
    elif action == 0:
        print("Hasta luego")
        exit()