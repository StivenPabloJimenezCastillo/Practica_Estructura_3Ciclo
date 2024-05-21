from models.ruc import EnumRuc
class Factura:
    def __init__(self):
        self.__id = 0
        self.__valor = 0.0
        self.__fecha = ""
        self.__porcentajeRetencion = 0.0
        self.__total = 0.0
        self.__retencion = 0.0
        self.__ruc = EnumRuc
        self.__numRuc = ""

    @property
    def _numRuc(self):
        return self.__numRuc

    @_numRuc.setter
    def _numRuc(self, value):
        self.__numRuc = value

    @property
    def _ruc(self):
        return self.__ruc

    @_ruc.setter
    def _ruc(self, value):
        self.__ruc = value


    @property
    def _retencion(self):
        return self.__retencion

    @_retencion.setter
    def _retencion(self, value):
        self.__retencion = value

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _valor(self):
        return self.__valor

    @_valor.setter
    def _valor(self, value):
        self.__valor = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def _porcentajeRetencion(self):
        return self.__porcentajeRetencion

    @_porcentajeRetencion.setter
    def _porcentajeRetencion(self, value):
        self.__porcentajeRetencion = value

    @property
    def _total(self):
        return self.__total

    @_total.setter
    def _total(self, value):
        self.__total = value
        
    @property
    def serializable(self):
        return {
            "id": self.__id,
            "valor": self.__valor,
            "fecha": self.__fecha,
            "porcentajeRetencion": self.__porcentajeRetencion,
            "total": self.__total,
            "retencion": self.__retencion,
            "ruc": str(self.__ruc),
            "numRuc": self.__numRuc,
        }
    
        
    def deserializar(data):
 
        fatura = Factura()
        fatura._id = data["id"]
        fatura._valor = data["valor"]
        fatura._fecha = data["fecha"]
        fatura._porcentajeRetencion = data["porcentajeRetencion"]
        fatura._total = data["total"]
        fatura._retencion = data["retencion"]
        fatura._ruc = data["ruc"]
        fatura._numRuc = data["numRuc"]
        return fatura