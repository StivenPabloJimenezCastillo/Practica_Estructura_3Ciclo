import sys
sys.path.append('../')

from controls.facturaDaoControl import FacturaDaoControl
from controls.PersonaDaoControl import PersonaDaoControl

pdc = PersonaDaoControl()
ftra = FacturaDaoControl()
try:
    pdc._persona._nombre = "Joel"
    pdc._persona._
    pdc._persona._apellido = "Jimenez"
    pdc._persona._cedula = "123456789"
    pdc.save
    
    pdc._persona._nombre = "Stiven"
    pdc._persona._apellido = "Jimenez"
    pdc._persona._cedula = "1150096681"
    pdc.save
    
    pdc._persona._nombre = "Troya"
    pdc._persona._apellido = "Torres"
    pdc._persona._cedula = "1950089372"
    pdc.save
    
    '''
    ftra._factura._fecha = "20/05/2025"
    ftra._factura._valor = 1000
    ftra._factura._ruc = ftra._factura._ruc.PROFECIONAL
    #ftra._factura._cliente._nombre = "Joel"
    #ftra._factura._cliente._apellido = "Jimenez"
    ftra.calcularRetencion()
    ftra.totalPago()
    ftra.save()
    '''
    
except Exception as error:
    print("error")
    print(error)