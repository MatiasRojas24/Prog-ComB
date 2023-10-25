from Motorcycle import Motorcycle

motorcycle1 = Motorcycle(
    color="Rojo", 
    license_plate="QRS 431", 
    fuel_liters=10, 
    wheels_number=2, 
    brand="Yamaha", 
    model="XTZ 250", 
    fabrication_date="2022", 
    max_speed_km=120, 
    weight_kg=152
)
motorcycle2 = Motorcycle(
    color="Blanca", 
    license_plate="XPQ241", 
    fuel_liters=10, 
    wheels_number=2, 
    brand="Suzuki", 
    model="GSX-R1000", 
    fabrication_date="2017", 
    max_speed_km=140, 
    weight_kg=201
)

print("Pruebas primera moto: ")
motorcycle1.start_up_engine()
motorcycle1.stop_engine()
motorcycle1.stop_engine()

print()

print("Pruebas segunda moto: ")
motorcycle2.start_up_engine()
motorcycle2.start_up_engine()
motorcycle2.stop_engine()

print()
Motorcycle.price = 'Aun sin precio'
motorcycle1.price = 4320000
print("El precio de la moto",motorcycle1.brand, motorcycle1.model,"es de $",motorcycle1.price)

print()

print("La primer moto cuesta: ")
print(motorcycle1.getPrice(motorcycle1))

print("La segunda moto cuesta: ")
print(motorcycle2.getPrice(motorcycle2))