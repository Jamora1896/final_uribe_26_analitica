
import random
from datetime import datetime,timedelta
from data.simuladorEmpleados import  leer_empleados
import csv


# Construir una funcion generadora de N ventas, que permita crear MOCKS o datos semillas para la rutina de analisis
def generar_ventas(numeroVentas):
    
    # simular una lista de productos, leer un excel y cargar esta lista con la info de excel
    #consumir una api
    productos=[
        {"nombre":"Mono largo combinado","precio":150000,"descuento":False},
        {"nombre":"Vestido corto evasé","precio":120000,"descuento":False},
        {"nombre":"Mono palabra de honor estampado","precio":250000,"descuento":False},
        {"nombre":"Vestido cuello barco fruncidos","precio":185000,"descuento":False},
        {"nombre":"Mono largo asimétrico drapeado","precio":289000,"descuento":True},
        {"nombre":"Vestido maxi volante","precio":199000,"descuento":False},
        {"nombre":"Mono largo cuello drapeado cinturón","precio":210000,"descuento":True},
        {"nombre":"Vestido punto cuello perkins","precio":110000,"descuento":False},
        {"nombre":"Mono raya diplomática combinado","precio":350000,"descuento":False},
        {"nombre":"Vestido asimétrico fruncido","precio":170000,"descuento":True},
    ]
    #simular lista de tallas
    tallas=[ "XS","S","M","L","XL","XXL","XXXL"]
    
    #simular vendedor asociado 
    #TAREAS
    vendedores= leer_empleados()
    
    #simular fecha
    fechaInicio=datetime(2026,1,2) 
    
    #generar las N ventas pedidas 
    ventas = []
    for _ in range(numeroVentas):
        producto = random.choice(productos) 
        cantidad = random.randint(1, 5)
        fecha = fechaInicio + timedelta(days=random.randint(0, 60))
        vendedor = random.choice(vendedores)

        venta={
        "producto": producto["nombre"],
        "precioUnitario": producto["precio"],
        "talla": random.choice(tallas),
        "cantidad": cantidad,
        "vendedor": vendedor["nombre"],
        "fecha": fecha,
        "total": cantidad * producto["precio"]
    }
        ventas.append(venta)
    return ventas

def inyectar_errores_y_exportar(ventas):
    
    ventas_con_errores = []

    for venta in ventas:
        venta = venta.copy()  # evitar modificar el original
        probabilidad_error = random.random()

        # Espacios extras
        if probabilidad_error < 0.15:
            venta["producto"] = venta["producto"] + " "

        # Mayúsculas en vendedor
        elif probabilidad_error < 0.30:
            venta["vendedor"] = venta["vendedor"].upper()

        # Talla inválida
        elif probabilidad_error < 0.40:
            venta["talla"] = "medio"

        # Cantidades inválidas
        elif probabilidad_error < 0.50:
            venta["cantidad"] = random.choice([0, -1, None])

        # Precio nulo
        elif probabilidad_error < 0.60:
            venta["precioUnitario"] = None

        # Formato de fecha incorrecto
        elif probabilidad_error < 0.70:
            if isinstance(venta["fecha"], datetime):
                venta["fecha"] = venta["fecha"].strftime("%d/%m/%Y")

        # Total inconsistente
        elif probabilidad_error < 0.80:
            venta["total"] = random.randint(1000, 500000)

        # Producto en minúsculas
        elif probabilidad_error < 0.90:
            venta["producto"] = venta["producto"].lower()

        ventas_con_errores.append(venta)

    # Inyectar duplicados
    if len(ventas_con_errores) >= 2:
        ventas_con_errores.append(ventas_con_errores[0].copy())
        ventas_con_errores.append(ventas_con_errores[1].copy())

    return ventas_con_errores

def limpiar_ventas(ventas):
    ventas_limpias = []
    vistos = set()

    for v in ventas:
        v = v.copy()  # ✅ no dañar el original

        # 1. Normalizar producto
        if v.get("producto"):
            v["producto"] = v["producto"].strip().title()

        # 2. Normalizar vendedor
        if v.get("vendedor"):
            v["vendedor"] = v["vendedor"].strip().title()

        # 3. Normalizar talla
        tallas_validas = ["XS","S","M","L","XL","XXL","XXXL"]
        if v.get("talla") not in tallas_validas:
            v["talla"] = "M"

        # 4. Validar cantidad
        if not isinstance(v.get("cantidad"), int) or v["cantidad"] <= 0:
            v["cantidad"] = 1

        # 5. Validar precio
        if not isinstance(v.get("precioUnitario"), (int, float)) or v["precioUnitario"] is None:
            continue

        # 6. Normalizar fecha
        if isinstance(v.get("fecha"), str):
            try:
                v["fecha"] = datetime.strptime(v["fecha"], "%d/%m/%Y")
            except ValueError:
                continue

        # 👉 Convertir fecha a string (para CSV)
        if isinstance(v.get("fecha"), datetime):
            v["fecha"] = v["fecha"].strftime("%Y-%m-%d")

        # 7. Recalcular total
        v["total"] = v["cantidad"] * v["precioUnitario"]

        # 8. Eliminar duplicados
        clave = (v["producto"], v["vendedor"], v["fecha"], v["total"])
        if clave in vistos:
            continue

        vistos.add(clave)
        ventas_limpias.append(v)

    return ventas_limpias