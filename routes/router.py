from flask import Flask, Blueprint, jsonify, abort, request, render_template, redirect
from controls.PersonaDaoControl import PersonaDaoControl
from controls.facturaDaoControl import FacturaDaoControl
import json

app = Flask(__name__)

# Archivo donde se guardarán las facturas
FACTURAS_FILE = "data/historial.json"

# Crear una lista global para almacenar las facturas
facturas_emitidas = []

def cargar_facturas():
    global facturas_emitidas
    try:
        with open(FACTURAS_FILE, 'r') as file:
            facturas_emitidas = json.load(file)
    except FileNotFoundError:
        facturas_emitidas = []

def guardar_facturas():
    with open(FACTURAS_FILE, 'w') as file:
        json.dump(facturas_emitidas, file)

# Cargar facturas al iniciar la aplicación
cargar_facturas()

router = Blueprint('router', __name__)

@router.route('/')
def home():
    return render_template("template.html")

@router.route('/emitir')
def ver_factura():
    return render_template("interfaz/emitirFactura.html")

@router.route('/idea')
def ver_general():
    return render_template("interfaz/general.html")

@router.route('/factura/guardar', methods=['POST'])
def guardar_factura():
    pd = PersonaDaoControl()
    fdc = FacturaDaoControl()
    data = request.form
    
    if not "nombre" in data.keys():
        abort(400)
    
    pd._persona._nombre = data['nombre']
    pd._persona._apellido = data['apellido']
    pd._persona._cedula = data['cedula']
    fdc._factura._valor = float(data['valor'])
    fdc._factura._numRuc = data['numRuc']
    fdc._factura._ruc = data['tipoRuc']
    retencion = fdc.calcularRetencion()
    total = fdc.totalPago()
    
    fdc.save
    pd.save
    
    factura = {
        'id': len(facturas_emitidas) + 1,  # Asignar un ID único
        'nombre': data['nombre'],
        'apellido': data['apellido'],
        'cedula': data['cedula'],
        'numRuc': data['numRuc'],
        'valor': float(data['valor']),
        'tipoRuc': data['tipoRuc'],
        'retencion': retencion,
        'total': total
    }
    facturas_emitidas.append(factura)
    guardar_facturas()
    
    return redirect("/historial", code=302)


@router.route('/historial')
def ver_historial():
    return render_template("interfaz/historial.html", lista=facturas_emitidas)

@router.route('/historial/eliminar/<int:factura_id>', methods=['POST'])
def eliminar_factura(factura_id):
    global facturas_emitidas
    factura_encontrada = False
    for factura in facturas_emitidas:
        if factura['id'] == factura_id:
            facturas_emitidas.remove(factura)
            factura_encontrada = True
            break
    
    if not factura_encontrada:
        abort(404, description="Factura no encontrada")

    guardar_facturas()
    return redirect("/historial", code=302)


app.register_blueprint(router)

if __name__ == "__main__":
    app.run(debug=True)
