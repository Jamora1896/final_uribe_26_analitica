#crear un funcion que crea n empleados con: id, nombre y apellidos, salario base, documento, fechaIngreso
import random
import pandas as pd

def leer_empleados():
    
    empleados_excel= pd.read_excel("data/empleados.xlsx")
    empleados=[]
    for _, fila in empleados_excel.iterrows():
        empleado = {
            "id": fila["id"],
            "nombre": fila["nombre_apellidos"],
            "salario_base": fila["salario_base"],
            "documento": fila["documento"],
            "fechaIngreso": fila["fechaIngreso"]
        }

        empleados.append(empleado)
        
    return empleados

import random
from datetime import datetime

def inyectar_errores_en_empleados(lista_empleados):
    empleados_con_errores = []

    for empleado in lista_empleados:
        empleado_modificado = empleado.copy()
        probabilidad_error = random.random()

        if probabilidad_error < 0.20:
            empleado_modificado["nombre"] = empleado_modificado["nombre"] + " "

        elif probabilidad_error < 0.40:
            empleado_modificado["nombre"] = empleado_modificado["nombre"].upper()

        elif probabilidad_error < 0.60:
            empleado_modificado["salario_base"] = random.choice([0, -1000, None])

        elif probabilidad_error < 0.75:
            empleado_modificado["documento"] = None

        elif probabilidad_error < 0.90:
            if isinstance(empleado_modificado["fechaIngreso"], datetime):
                empleado_modificado["fechaIngreso"] = empleado_modificado["fechaIngreso"].strftime("%d/%m/%Y")

        empleados_con_errores.append(empleado_modificado)

    # Duplicados
    if len(empleados_con_errores) >= 2:
        empleados_con_errores.append(empleados_con_errores[0].copy())

    return empleados_con_errores
    
def limpiar_datos_empleados(lista_empleados):
    empleados_limpios = []
    registros_vistos = set()

    for empleado in lista_empleados:
        empleado_limpio = empleado.copy()

        # Normalizar nombre
        if empleado_limpio.get("nombre"):
            empleado_limpio["nombre"] = empleado_limpio["nombre"].strip().title()

        # Validar salario
        if not isinstance(empleado_limpio.get("salario_base"), (int, float)) or empleado_limpio["salario_base"] <= 0:
            continue

        # Validar documento
        if not empleado_limpio.get("documento"):
            continue

        # Normalizar fecha
        if isinstance(empleado_limpio.get("fechaIngreso"), str):
            try:
                empleado_limpio["fechaIngreso"] = datetime.strptime(empleado_limpio["fechaIngreso"], "%d/%m/%Y")
            except:
                continue

        # Convertir fecha a string
        if isinstance(empleado_limpio.get("fechaIngreso"), datetime):
            empleado_limpio["fechaIngreso"] = empleado_limpio["fechaIngreso"].strftime("%Y-%m-%d")

        # Eliminar duplicados
        clave_unica = (empleado_limpio["id"], empleado_limpio["documento"])
        if clave_unica in registros_vistos:
            continue

        registros_vistos.add(clave_unica)
        empleados_limpios.append(empleado_limpio)

    return empleados_limpios
  

    