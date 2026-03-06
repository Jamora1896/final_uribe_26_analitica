
import random
from datetime import datetime,timedelta
from data.simuladorEmpleados import leer_empleados

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
    ventas=[]
    for venta_id in range(numeroVentas):
        productos_seleccionados = random.sample(productos, random.randint(1,3))
        for producto in productos_seleccionados:
            cantidad=random.randint(1,5)
            fecha=fechaInicio+timedelta(days=random.randint(0,60))
            vendedor = random.choice(vendedores)
            ventas.append(
            {
                "venta_id":venta_id,
                "producto":producto["nombre"],
                "precioUnitario":producto["precio"],
                "talla":random.choice(tallas),
                "cantidad":cantidad,
                "vendedor":vendedor["id"],
                "fecha":fecha,
                "total":cantidad*producto["precio"]
            }
        )
    return ventas