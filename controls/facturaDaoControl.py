from models.factura import Factura, EnumRuc
from controls.dao.daoAdapter import DaoAdapter

class FacturaDaoControl(DaoAdapter):
    
    def __init__(self):
        super().__init__(Factura)
        self.__factura = None

    @property
    def _factura(self):
        if self.__factura is None:
            self.__factura = Factura()
        return self.__factura

    @_factura.setter
    def _factura(self, value):
        self.__factura = value

    def calcularRetencion(self):
        if self.__factura._ruc == 'EDUCATIVO':
            self.__factura._porcentajeRetencion = 0.08 
        elif self.__factura._ruc == 'PROFECIONAL':
            self.__factura._porcentajeRetencion = 0.10
        else:
            print("Error: Tipo de RUC no válido")
            self.__factura._porcentajeRetencion = 0.0
        self.__factura._retencion = self.__factura._valor * self.__factura._porcentajeRetencion
        return self.__factura._retencion
    
    def totalPago(self):
        self.__factura._total = self.__factura._valor - self.__factura._retencion 
        return self.__factura._total
    
    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self._factura._id = self._lista._length + 1
        self._save(self._factura)
