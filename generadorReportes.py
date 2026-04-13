import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd


from transformaciones import(
    
    datosOrdenados,
    ventas_mayores_500,
    ventas_mayores_300_talla_m,
    ventas_laura_jessica,
    ventas_febrero,
    ventas_laura_mora,
    ventas_agrupadas,
    ventas_agrupadas_tallas
    
)

#Preparar el espacio donde voy a guardar los reportes graficos, CREAR CARPETAS
CARPETA_REPORTES = "reportes"
CARPETA_GRAFICAS= os.path.join(CARPETA_REPORTES, "graficas")
os.makedirs(CARPETA_GRAFICAS, exist_ok=True)

#Crear el reporte de los datos, un reporte estará confirmado por un documento html que carga graficas
## crear html 
## crear imagenes 

def dataFrame_convertir_html(dataFrame):
    
    if isinstance(dataFrame, pd.Series):
        dataFrame = dataFrame.reset_index()
        
    return dataFrame.to_html(
        classes="table table-striped table-hover table-bordered table-sm",
        border=0
    )
    
#Primera Grafica (graficar comportamiento de ventas_agrupadas)
plt.figure(figsize=(20,6))
ventas_agrupadas.plot(kind="bar", color="#251B75") 
plt.title('Total de ventas por vendedor')       
plt.xlabel('Vendedor')
plt.ylabel('Total de Ventas en pesos')
plt.xticks(rotation=45)
plt.savefig(os.path.join(CARPETA_GRAFICAS, 'ventas_por_vendedor.png'))
plt.close()


#Segunda Grafica (graficar comportamiento de ventas_agrupadas_tallas)
plt.figure(figsize=(10,5))
ventas_agrupadas_tallas.plot(kind="bar", color="#E923AD")
plt.title('Total de ventas por talla') 
plt.xlabel('talla')
plt.ylabel('Total de Vendido en pesos ')
plt.savefig(os.path.join(CARPETA_GRAFICAS, 'ventas_por_talla.png'))
plt.close()    


#Tercera Grafica (graficar comportamiento de ventas por mes) 


##Cuarta grafica de tortas (participacion porcentual de cada vendedor en las ventas de la tienda)
plt.figure(figsize=(10,8))
ventas_agrupadas.plot(
    kind="pie", 
    y="total",
    autopct='%1.1f%%', 
    startangle=90, 
    colors=["#E923AD", "#251B75", "#F2C94C", "#27AE60", "#2F80ED", "#9B51E0", "#EB5757", "#56CCF2", "#6FCF97", "#BDBDBD"])
plt.title('Participación porcentual de cada vendedor en las ventas totales')
plt.savefig(os.path.join(CARPETA_GRAFICAS, 'ventas_por_vendedor_porcentaje.png'))
plt.close() 
           
 

#RUTINA PARA CREAR UN DOCUMENTO HTML QUE GUARDE LAS IMAGENES Y LOS DATOS EN TABLAS HTML
documento_html = f""" 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Reportes de analitica </title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>
<body>



    <section class="container "> 
        <section class="row">
            <section class="col-12">
                <h1> REPORTE DE DATOS ASOCIADOS A LAS VENTAS </h1>
                <hr>
                <p> 
                    Utilizando PANDAS este es el reporte de ventas de la tienda chevignon de la central
                </p>
            </section>
        </section>
    </section>
    
    <section class="container "> 
        <section class="row">
            <section class="col-12">
                <div class="card p-5 shadow border">
                    
                        <h3> Total vendido por cada vendedor</h3>
                        <p>
                            La grafica muestra el total vendido por cada vendedor, lo que permite identificar a los vendedores más exitosos 
                            y aquellos que podrían necesitar apoyo adicional para mejorar sus ventas. Esta información es crucial para la toma de decisiones 
                            estratégicas en la gestión de ventas y recursos humanos.</p>
                            {dataFrame_convertir_html(ventas_agrupadas)}
                            <br>
                            <img src="graficas/ventas_por_vendedor.png" alt="foto" class="img-fluid">
                            <br>
                            <img src="graficas/ventas_por_vendedor_porcentaje.png" alt="foto" class="img-fluid">
                </div>
            </section>
        </section>
    </section>
        
        
</body>
</html>
"""
                               
 # RUTINA PARA ALMACENAR EL HTML GENERADO EN LA RAIZ DE NUESTRO PROYECTO 
RUTA_REPORTE = os.path.join(CARPETA_REPORTES, "reporte_analitica.html")
with open(RUTA_REPORTE, "w", encoding="utf-8") as archivo:
    archivo.write(documento_html)                              