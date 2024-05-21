from models.ruc import EnumRuc
class Persona:
    def __init__(self):
        self.__id = 0
        self.__nombre = ""
        self.__apellido = ""
        self.__cedula = ""


    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _cedula(self):
        return self.__cedula

    @_cedula.setter
    def _cedula(self, value):
        self.__cedula = value        
        
    @property
    def serializable(self):
        return {
            "id": self.__id,
            "apellido": self.__apellido,
            "nombre": self.__nombre,
            "cedula": self.__cedula
        }
        
    def deserializar(data): 
        persona = Persona()
        persona._id = data["id"]
        persona._apellido = data["apellido"]
        persona._nombre = data["nombre"]
        persona._cedula = data["cedula"]
        return persona