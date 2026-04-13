import pandas as pd
import os


def generar_archivo_json(listaVentas,nombreArchivo):
     dataFramePandas = pd.DataFrame(listaVentas)
     dataFramePandas.to_json(nombreArchivo, orient='records', indent=4)
     print(f"Archivo '{nombreArchivo}' generado exitosamente.")