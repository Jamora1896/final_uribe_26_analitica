from data.simuladorVentas import generar_ventas
from data.simuladorEmpleados import leer_empleados


print(generar_ventas(10))


empleados = leer_empleados()

print(empleados)
