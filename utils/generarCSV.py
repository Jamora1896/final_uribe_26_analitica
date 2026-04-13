import pandas as pd
import os

def generar_archivo_csv(listaVentas, nombreArchivo):
    dataFramePandas = pd.DataFrame(listaVentas)
    dataFramePandas.to_csv(nombreArchivo, index=False, encoding='utf-8')
    print(f"Archivo '{nombreArchivo}' generado exitosamente.")
    