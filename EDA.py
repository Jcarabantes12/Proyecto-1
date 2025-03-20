"""
1. Análisis Exploratorio de Datos (EDA)
"""

import pandas as pd
from fpdf import FPDF
from datetime import datetime
import chardet
import locale

# Configurar el idioma local para fechas en español
locale.setlocale(locale.LC_ALL, "es_SV.UTF-8")

# ..:::Análisis Exploratorio de Datos:::..
def eda(csv_path: str):
    with open(csv_path, "rb") as detFormat:
        csv_format = chardet.detect(detFormat.read())

    # Cargar el archivo CSV a un dataframe
    dframe = pd.read_csv(csv_path)

    # Nombres de las columnas
    col_name = dframe.columns.tolist()
    
    # Dimensiones del dataframe
    num_row, num_column = dframe.shape

    # Valores nulos
    null_values = dframe.isnull().sum().to_string()

    # Valores duplicados
    dupl_values = dframe.duplicated().sum()

    # Tipos de datos
    data_types = dframe.dtypes.to_string()

    # Estadísticas descriptivas
    desc_stats = dframe.describe().to_string()

    # Correlación de las variables
    dframe_numeric = dframe.select_dtypes(include=["number"])
    correlation = dframe_numeric.corr().to_string()

    # Visualización de las primeras filas del dataframe
    dframe_preview_first = dframe.head(40).to_string()

    # Visualización de las ultimas filas del dataframe
    dframe_preview_last = dframe.tail(40).to_string()

    return report_eda(csv_format, col_name, num_row, num_column,
               null_values, dupl_values, data_types,
               desc_stats, correlation, dframe_preview_first,
               dframe_preview_last)


# ..:::Informe en PDF:::..
def report_eda(csv_format, col_name, num_row, num_column,
               null_values, dupl_values, data_types,
               desc_stats, correlation, dframe_preview_first,
               dframe_preview_last):
    # Crear el objeto PDF
    eda_pdf = FPDF()
    
    # Configuración de la página
    f_family = "helvetica"
    f_size_title = 14 # font-size de los titulos
    f_size_content = 10 # font-size del contenido/texto

    eda_pdf.set_auto_page_break(auto=True, margin=15)

    # Página 1
    eda_pdf.add_page()

    # 1.1.1 Titulo: Titulo del documento
    eda_pdf.set_font(f_family, "B", f_size_title) # Negrita
    eda_pdf.cell(0, 5, "Análisis Exploratorio de Datos (EDA)", ln=True, align="C") # Centrado
    eda_pdf.ln(7)

    # 1.2.1 Titulo: Resumen del dataframe
    # No tiene set_font porque obtiene el mismo del titulo del reporte
    eda_pdf.cell(0, 5, "Resumen de los datos:", ln=True, align="L") # izquierda

    # 1.2.2 Texto: Resumen del dataframe
    eda_pdf.set_font(f_family, "", f_size_content) # Normal
    eda_pdf.multi_cell(0, 5, "Los datos representan información estructurada proveniente"
        "del archivo CSV, incluyendo número de columnas, números de filas, valores nulos,"
        "duplicados, tipos de datos, estadísticas descriptivas y correlaciones"
        "entre variables."
        "\n\n"
        "Además, se presenta una visualización de los primeros y últimos registros"
        "del dataframe para tener una idea de la estructura de los datos.", # Fecha actual (lunes 01 de enero 2021 | 12:00:00 AM)
        align="J" # Justificado
    )
    eda_pdf.ln(7)

    # 1.2.3 Texto: Fecha de creacion del documento
    eda_pdf.set_font(f_family, "I", 10) # Italica
    eda_pdf.set_text_color(64) # Gris oscuro
    eda_pdf.cell(0, 5, "Fecha de creación del informe: "
        f"{datetime.now().strftime("%A %d de %B de %Y %I:%M:%S %p")}",
        ln=True, align="L" # Izquierda
    )
    
    # Página 2
    eda_pdf.add_page()

    # 2.1.1 Titulo: Codificación del CSV
    eda_pdf.set_font(f_family, "B", f_size_title) # Negrita
    eda_pdf.cell(0, 5, "Codificación del archivo CSV:", ln=True, align="L") # Izquierda
    
    # 2.1.2 Texto: Codificación del CSV
    eda_pdf.set_font(f_family, "", f_size_content) # Normal
    eda_pdf.multi_cell(0, 5, f"Codificación: {csv_format["encoding"]}\n"
        f"Confianza: {csv_format["confidence"]}\n"
        f"Idioma: {csv_format["language"]}",
        align="L") # Izquierda
    eda_pdf.ln(7)

    # 2.2.1 Titulo: Dimenciones del dataframe
    eda_pdf.set_font(f_family, "B", f_size_title) # Negrita
    eda_pdf.cell(0, 5, "Dimenciones del dataframe:", ln=True, align="L") # Izquierda

    # 2.2.2 Texto: Dimenciones del dataframe
    eda_pdf.set_font(f_family, "", f_size_content) # Normal
    eda_pdf.multi_cell(0, 5, f"Número de filas: {num_row}"
        f"\nNúmero de columnas: {num_column}"
        f"\n({num_row}x{num_column})",
                       align="L"  # Izquierda
                       )
    eda_pdf.ln(7)

    # 2.3.1 Titulo: Número de columnsa del dataframe
    eda_pdf.set_font(f_family, "B", f_size_title) # Negrita
    eda_pdf.cell(0, 5, "Columnas del dataframe:", ln=True, align="L") # Izquierda

    # 2.3.2 Texto: número de columas del dataframe
    eda_pdf.set_font(f_family, "", f_size_content) # Normal
    # Numera el número de columnas
    for index, column in enumerate(col_name):
        eda_pdf.cell(0, 5, f"{index+1}- {column}", ln=True, align="L") # Izquierda
    eda_pdf.ln(7)

    # 2.4.1 Titulo: Valores nulos del dataframe
    eda_pdf.set_font(f_family, "B", f_size_title) # Negrita
    eda_pdf.cell(0, 5, "Valores nulos en el dataframe:", ln=True, align="L") # Izquierda

    # 2.4.2 Texto: Valores nulos del dataframe
    eda_pdf.set_font(f_family, "", f_size_content) # Normal
    eda_pdf.multi_cell(0, 5, null_values, align="L") # Izquierda
    eda_pdf.ln(7)

    # 2.5.1 Titulo: Valores duplicados
    eda_pdf.set_font(f_family, "B", f_size_title) # Negrita
    eda_pdf.cell(0, 5, "Valores duplicados en el dataframe:", ln=True, align="L") # Izquierda

    # 2.5.2 Texto: Valores duplicados
    eda_pdf.set_font(f_family, "", f_size_content) # Normal
    eda_pdf.cell(0, 5, f"{dupl_values} valores duplicados", ln=True, align="L") # Izquierda
    eda_pdf.ln(7)

    # 2.6.1 Titulo: Tipos de datos
    eda_pdf.set_font(f_family, "B", f_size_title) # Negrita
    eda_pdf.cell(0, 5, "Tipos de datos de las columnas:", ln=True, align="L") # Izquierda

    # 2.6.2 Texto: Tipos de datos
    eda_pdf.set_font(f_family, "", f_size_content) # Normal
    eda_pdf.multi_cell(0, 5, data_types, align="L") # Izquierda
    eda_pdf.ln(7)

    # 2.7.1 Titulo: Estadistica descriptiva
    eda_pdf.set_font(f_family, "B", f_size_title) # Negrita
    eda_pdf.cell(0, 5, "Estadísticas descriptivas del dataframe:", ln=True, align="L") # Izquierda

    # 2.7.2 Texto: Estadistica descriptiva
    eda_pdf.set_font(f_family, "", f_size_content) # Normal
    eda_pdf.multi_cell(0, 5, desc_stats, align="L") # Izquierda
    eda_pdf.ln(7)

    # 2.8.1 Titulo: Correlación
    eda_pdf.set_font(f_family, "B", f_size_title) # Negrita
    eda_pdf.cell(0, 5, "Correlación de las variables del dataframe:", ln=True, align="L") # Izquierda

    # 2.8.2 Texto: Correlación
    eda_pdf.set_font(f_family, "", f_size_content) # Normal
    eda_pdf.multi_cell(0, 5, correlation, align="L") # Izquierda
    eda_pdf.ln(7)

    # Página 3
    eda_pdf.add_page()

    # 3.1.1 Titulo: Visualización de los primeros registros del dataframe
    eda_pdf.set_font(f_family, "B", f_size_title) # Negrita
    eda_pdf.cell(0, 5, f"Visualización de los primeros registros del dataframe:", ln=True, align="L") # Izquierda
    eda_pdf.ln(4)

    # 3.1.2 Titulo: Visualización de los primeros registros del dataframe
    eda_pdf.set_font(f_family, "", f_size_content - 2) # Normal
    eda_pdf.multi_cell(0, 5, dframe_preview_first, align="L", border=1) # Izquierda

    # Página 4
    eda_pdf.add_page()

    # 4.1.1 Titulo: Visualización de los ultimos registros del dataframe
    eda_pdf.set_font(f_family, "B", f_size_title) # Negrita
    eda_pdf.cell(0, 5, f"Visualización de los últimos registros del dataframe:", ln=True, align="L") # Izquierda
    eda_pdf.ln(4)

    # 4.1.2 Texto: Visualización de los ultimos registros del dataframe
    eda_pdf.set_font(f_family, "", f_size_content - 2) # Normal
    eda_pdf.multi_cell(0, 5, dframe_preview_last, align="L", border=1) # Izquierda

    # Guardar el informe en un archivo PDF
    eda_pdf.output(fr"reportes\ReporteEDA_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.pdf")
