#crear un funcion que crea n empleados con: id, nombre y apellidos, salario base, documento, fechaIngreso
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
    
    
    