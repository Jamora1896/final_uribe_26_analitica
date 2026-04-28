import pandas as pd
from data.simuladorVentas import generar_ventas, inyectar_errores_y_exportar, limpiar_ventas
from data.simuladorEmpleados import leer_empleados, inyectar_errores_en_empleados, limpiar_datos_empleados
from utils.generarCSV import generar_archivo_csv
from utils.generarJSON import generar_archivo_json
from utils.limpieza_data import limpiar_archivos_generados, limpiar_graficas
from generadorReportes import generar_graficas



if __name__ == "__main__":

    import os
    os.makedirs("data", exist_ok=True)

    print("🚀 INICIANDO PROCESO...\n")

   
    # LIMPIEZA INICIAL
    print("Limpiando archivos anteriores...")
    limpiar_archivos_generados()
    limpiar_graficas("reportes/graficas")
    print("Limpieza completa\n")

    #PROCESO VENTAS
   
    print("Procesando ventas...")

    ventas = generar_ventas(100)
    ventas_sucias = inyectar_errores_y_exportar(ventas)
    ventas_limpias = limpiar_ventas(ventas_sucias)

    generar_archivo_csv(ventas_sucias, "data/ventas_sucias.csv")
    generar_archivo_csv(ventas_limpias, "data/ventas_limpias.csv")

    generar_archivo_json(ventas_sucias, "data/ventas_sucias.json")
    generar_archivo_json(ventas_limpias, "data/ventas_limpias.json")

    print(f"Ventas Original: {len(ventas)}")
    print(f"Ventas Sucias: {len(ventas_sucias)}")
    print(f"Ventas Limpias: {len(ventas_limpias)}\n")

    
    # PROCESO EMPLEADOS
    
    print("👥 Procesando empleados...")

    empleados = leer_empleados()
    empleados_sucios = inyectar_errores_en_empleados(empleados)
    empleados_limpios = limpiar_datos_empleados(empleados_sucios)

    generar_archivo_csv(empleados_sucios, "data/empleados_sucios.csv")
    generar_archivo_csv(empleados_limpios, "data/empleados_limpios.csv")

    generar_archivo_json(empleados_sucios, "data/empleados_sucios.json")
    generar_archivo_json(empleados_limpios, "data/empleados_limpios.json")

    print(f"Empleados Original: {len(empleados)}")
    print(f"Empleados Sucios: {len(empleados_sucios)}")
    print(f"Empleados Limpios: {len(empleados_limpios)}\n")

    # GENERAR GRÁFICAS
    
    print("📊 Generando gráficas...")
    generar_graficas()
    print("✅ Gráficas generadas")
















