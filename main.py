import pandas as pd
from data.simuladorVentas import generar_ventas
from data.simuladorEmpleados import leer_empleados
from utils.generarCSV import generar_archivo_csv
from utils.generarJSON import generar_archivo_json

#print(generar_ventas(10))
#empleados = leer_empleados()
#print(empleados)

lista = generar_ventas(10)
datosOrdenados= pd.DataFrame(lista)

#Generando un dataset en formato CSV 
#generar_archivo_csv(lista, "data/ventas_sucias.csv")

#Generando un dataset en formato JSON
#generar_archivo_json(lista, "data/json_ventas.json")

#print(datosOrdenados)

#pasos para analizar los datos:
#1identificar, insoeccionar, asociar la informacion base de los datos:
#print(datosOrdenados.head(8))
#print(datosOrdenados.tail(3))
#print(datosOrdenados.shape)
#print(datosOrdenados.columns)
#print(datosOrdenados.dtypes)
#print(datosOrdenados.info())
#print(datosOrdenados.describe())

#2limpiar,evaluar calidad de los datos, eliminar duplicados, eliminar nulos, corregir formatos, corregir errores de tipeo
#Que se limpia?
#A nombre de las columnas

#B textos:
#espacios
#mayusculas o minisculas 
#formatos inconsistentes

# VALORES NULOS

# VALORES DUPLICADOS

# VERIFICAR TIPOS DE DATOS

# SE VERIFICAN LAS REGLAS DE NEGOCIO 

#tarea CONVERTIR ESTA RUTINA A UNA FUNCION GENERICA, funcion aparte de la rutina de limipeza se debe crear 

dataFrameCopia = datosOrdenados.copy()
dataFrameCopia.columns = dataFrameCopia.columns.str.strip()
columnas_texto=['producto','talla','vendedor']
for columna in columnas_texto:
    dataFrameCopia[columna] = dataFrameCopia[columna].astype(str).str.strip()

dataFrameCopia['producto'] = dataFrameCopia['producto'].str.title()
dataFrameCopia['vendedor'] = dataFrameCopia['vendedor'].str.title()
dataFrameCopia['talla'] = dataFrameCopia['talla'].str.upper()

dataFrameCopia.replace(['',' ','nan', 'NaN', 'None'], pd.NA, inplace=True)

dataFrameCopia['precioUnitario']=pd.to_numeric(dataFrameCopia['precioUnitario'], errors='coerce')

dataFrameCopia['cantidad']=pd.to_numeric(dataFrameCopia['cantidad'], errors='coerce')
dataFrameCopia['total']=pd.to_numeric(dataFrameCopia['total'], errors='coerce')

dataFrameCopia['fecha']=pd.to_datetime(dataFrameCopia['fecha'], errors='coerce', dayfirst=False)

dataFrameCopia=dataFrameCopia.drop_duplicates()

dataFrameCopia=dataFrameCopia.dropna(subset=['producto','precioUnitario','cantidad','total','fecha'])


# RUTINA PARA LIMPIAR SEGUN LA REGLA DE NEGOCIO: 

#VALIDACION DE CANTIDAD 
dataFrameCopia=dataFrameCopia[dataFrameCopia['cantidad']>0]

#VALIDACION DE PRECIO UNITARIO
dataFrameCopia=dataFrameCopia[dataFrameCopia['precioUnitario']>0]

#VALIDACION DE TOTAL
dataFrameCopia=dataFrameCopia[dataFrameCopia['total']>5000]

#VALIDACION TALLA VALIDA 
tallasValidas=["XS","S","M","L","XL","XXL","XXXL"]
dataFrameCopia=dataFrameCopia[dataFrameCopia['talla'].isin(tallasValidas)]

#VALIDACION RECALCULO DEL TOTAL
dataFrameCopia['total']=dataFrameCopia['precioUnitario']*dataFrameCopia['cantidad']

print(datosOrdenados)
print("-----------------------------")
print(dataFrameCopia)