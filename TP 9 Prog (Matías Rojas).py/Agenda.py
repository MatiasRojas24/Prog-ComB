# 4.	Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. 
# Además deberá mostrar un menú con las siguientes opciones:
# •	Añadir contacto
# •	Lista de contactos
# •	Buscar contacto
# •	Editar contacto
# •	Cerrar agenda
class Agenda():
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email
    
    def setName(self, new_value):
        self.__name = new_value
    def setPhone(self, new_value):
        self.__phone = new_value
    def setEmail(self, new_value):
        self.__email = new_value
    
    def getName(self):
        return self.__name
    def getPhone(self):
        return self.__phone
    def getEmail(self):
        return self.__email

    def showContact(self):
        contact_info = f"Nombre: {self.__name}\nNúmero telefónico: {self.__phone}\nEmail: {self.__email}"
        return contact_info


