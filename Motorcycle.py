class Motorcycle:
    condition = "nuevas"
    engine = False

    def __init__(self, color="", license_plate="", fuel_liters=0, wheels_number=0, brand="", model="", fabrication_date="", max_speed_km=0, weight_kg=""):
        self.color = color
        self.license_plate = license_plate
        self.fuel_liters = fuel_liters
        self.__wheels_number = wheels_number
        self.brand = brand
        self.model = model
        self.fabrication_date = fabrication_date
        self.max_speed_km = max_speed_km
        self.weight_kg = weight_kg
    
    def start_up_engine(self):
        if self.engine:
            print("El motor ya está encendido")
        else:
            self.engine = True
            print("Se ha encendido el motor")
    
    def stop_engine(self):
        if self.engine:
            self.engine = False
            print("Se ha detenido el motor")
        else:
            print("El motor ya está detenido")
    
    def getPrice (self,motorcycle):
        return motorcycle.price