import os

def limpiar_archivos_generados():
    archivos = [
        "data/ventas_sucias.csv",
        "data/ventas_limpias.csv",
        "data/ventas_sucias.json",
        "data/ventas_limpias.json",
        "data/empleados_sucios.csv",
        "data/empleados_limpios.csv",
        "data/empleados_sucios.json",
        "data/empleados_limpios.json"
    ]

    for archivo in archivos:
        if os.path.exists(archivo):
            os.remove(archivo)
            print(f"🗑️ Eliminado: {archivo}")
            
            
def limpiar_graficas(carpeta="reportes/graficas"):
    if not os.path.exists(carpeta):
        return

    for archivo in os.listdir(carpeta):
        ruta = os.path.join(carpeta, archivo)

        if os.path.isfile(ruta) and archivo.endswith(".png"):
            os.remove(ruta)
            print(f"🗑️ Gráfica eliminada: {ruta}")