import pandas as pd
from data.simuladorVentas import generar_ventas

#TRANSFORMANDO LOS DATOS EN FUNCION DE DECISIONES UTILES PARA EL NEGOCIO 

#PANDAS ==> QUERIES: PERMITEN EXTRAER INFORMACION DE UN SET DE DATOS 
datos=generar_ventas(50) #datos sucios 
datosOrdenados= pd.DataFrame(datos)

#1. QUERY SIMPLES
# CUALES SON LAS VENTAS SUPERIORES A 500.000 PESOS
ventas_mayores_500=datosOrdenados.query("total > 500000").head(5)



#2. QUERY CON DOS CONDICIONES
# FILTRAR FILAS QUE EL TOTAL SEA MAYOR A 300.000 PESOS Y LA TALLA SEA "M"
ventas_mayores_300_talla_m=datosOrdenados.query("total > 300000 and talla == 'M'")
#print(ventas_mayores_300_talla_m)

#3. QUERY CON VALORES ESPECIFICOS DE UNA COLUMNA
# FILTRAR FILAS DONDE EL VENDEDOR SEA "LAURA MORA" O "JESSICA MORA"
ventas_laura_jessica=datosOrdenados.query("vendedor == 'LAURA MORA' or vendedor == 'JESSICA MORA'")
#print(ventas_laura_jessica)

#4. OTRAS QUERIES DEPENDIENDO DEL NEGOCIO QUE ESTOY ANALIZANDO 
#FILTRAR FILAS CUYO VALOR DE LA COLUMNA MES SEA IGUAL A 2 
datosOrdenados['fecha'] = pd.to_datetime(datosOrdenados['fecha'], errors='coerce',dayfirst=False)
datosOrdenados['mes'] = datosOrdenados['fecha'].dt.month
datosOrdenados['nombreDia'] = datosOrdenados['fecha'].dt.day_name()
#datosOrdenados['dia'] = datosOrdenados['fecha'].dt.day
#datosOrdenados['año'] = datosOrdenados['fecha'].dt.year
ventas_febrero=datosOrdenados.query("mes == 2")
#print(ventas_febrero)

#QUERIES USANDO VARIABLES EXTERNAS
vendedor_buscado="LAURA MORA"
ventas_laura_mora=datosOrdenados.query("vendedor == @vendedor_buscado")
#print(ventas_laura_mora)



#AGRUPANDO DATOS CON PYTHON Y PANDAS : (REUNIR DOS O MAS COLUMNAS PARA EXTRAER INFORMACION GROUP BY)
#1. AGRUPACIONES SIMPLES 
#AGRUPAR TODAS LAS FILAS QUE TENGAN EL MISMO VENDEDOR 
ventas_agrupadas=datosOrdenados.groupby("vendedor")["total"].sum().sort_values(ascending=False)
print(ventas_agrupadas)

#AGRUPAR Y MOSTRAR VENTAS POR TALLA 
ventas_agrupadas_tallas=datosOrdenados.groupby("talla")["total"].sum().sort_values(ascending=False)
print(ventas_agrupadas_tallas)
