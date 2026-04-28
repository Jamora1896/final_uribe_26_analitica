# FINAL URIBE 26 - ANALÍTICA DE DATOS

Proyecto de simulación, limpieza, análisis y visualización de datos de ventas y empleados en Python.

---

## Descripción

Este proyecto implementa un flujo completo de ingeniería de datos:

- Generación de datos simulados (ventas y empleados)
- Inyección de errores para crear datos sucios
- Limpieza y normalización de datos
- Exportación en CSV y JSON
- Análisis de datos con Pandas
- Generación de gráficas con Matplotlib
- Creación de reportes visuales



## Estructura del proyecto
FINAL_URIBE_26_ANALITICA/
│
├── data/
│ ├── empleados.xlsx
│ ├── empleados_limpios.csv
│ ├── empleados_sucios.csv
│ ├── ventas_limpias.csv
│ ├── ventas_sucias.csv
│
├── reportes/
│ ├── graficas/
│ │ ├── ventas_por_vendedor.png
│ │ ├── ventas_por_talla.png
│ │ ├── ventas_por_mes.png
│ │ ├── ventas_por_vendedor_pie.png
│ ├── reporte_analitica.html
│
├── utils/
│ ├── generarCSV.py
│ ├── generarJSON.py
│ ├── limpieza_data.py
│
├── data/
│ ├── simuladorVentas.py
│ ├── simuladorEmpleados.py
│
├── generadorReportes.py
├── main.py
├── transformaciones.py
├── requirements.txt
└── README.md

## Tecnologías utilizadas

- Python 3.x
- Pandas 🐼
- Matplotlib 📊
- OpenPyXL (Excel)
- Random (simulación de datos)
- OS (manejo de archivos)
- Datetime ⏰

---
## Flujo del proyecto

### 1. Simulación de datos
Se generan datos ficticios de:
- Ventas
- Empleados

---

### 2. Inyección de errores
Se agregan errores como:
- Valores nulos
- Fechas incorrectas
- Texto inconsistente
- Duplicados

---

### 3. Limpieza de datos
Se corrigen:
- Tipos de datos
- Fechas
- Formatos de texto
- Valores inválidos
- Duplicados

---

### 4. Exportación
Los datos se exportan en:
- CSV
- JSON

---

### 5. Análisis de datos
Se generan métricas como:
- Ventas por vendedor
- Ventas por talla
- Ventas por mes

---

### 6. Visualización
Se generan gráficas:

- Ventas por vendedor
- Ventas por talla
- Ventas por mes
- Participación de ventas

---

## ▶️ Ejecución del proyecto

Ejecutar el flujo completo desde el `main.py`:

```bash
python main.py

