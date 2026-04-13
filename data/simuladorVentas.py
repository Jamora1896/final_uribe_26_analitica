
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
    #inyectando errores de calidad en los datos 
        probabilidad_error=random.random()
    
    #Rutina para espacios extras
        if probabilidad_error<0.15:
            venta["producto"]=venta["producto"]+" "
        #mayusuculas     
        elif probabilidad_error<0.30:
            venta["vendedor"]=venta["vendedor"].upper()
        #Formato de la talla  
        elif probabilidad_error<0.40:
            venta["talla"]="medio"
       #Cantidades invalidas
        elif probabilidad_error<0.50:
            venta["cantidad"]=random.choice([-0,-1,None])
        #inyectar nulos 
        elif probabilidad_error<0.60:
            venta["precioUnitario"]=None
        #cambiar el formato de la fecha   
        elif probabilidad_error<0.70: 
            venta["fecha"]=fecha.strftime("%d/%m/%Y")
        #total inconsistente
        elif probabilidad_error<0.80:
            venta["total"]=random.randint(1000,500000)
        elif probabilidad_error<0.90:
            venta["producto"]=venta["producto"].lower()
            
        ventas.append(venta)
        
        #inyectar duplicados 
        if len(ventas)>=50: 
            ventas.append(ventas[0].copy())
            ventas.append(ventas[1].copy())
    return ventas