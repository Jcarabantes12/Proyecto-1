"""
3. Análisis de Datos
"""

import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

# ..:::Análisis de Datos:::..
def analisis(csv_path: str):
    # Cargar el archivo CSV a un dataframe
    df = pd.read_csv(csv_path)

    # Configuración
    bar_color = "#DDBDB6"
    line_color = "#B47656"
    text_color = "#8a6e69"
    alpha = 0.5
    dpi = 300

    # Ventas por país
    sales_country = df.groupby("Country")["Amount"].sum().reset_index()
    sales_country = sales_country.sort_values("Amount", ascending=True)
    sales_country.plot(x="Country", y="Amount", kind="barh", color=bar_color, figsize=(10, 4))
    plt.title("Mayores ventas por país", fontsize=16)
    plt.xlabel("Ventas ($)", fontsize=14)
    plt.ylabel("País", fontsize=14)
    plt.grid(axis="x", linestyle="--", alpha=alpha, color=line_color)
    plt.ticklabel_format(style="plain", axis="x")
    for i, v in enumerate(sales_country["Amount"]):
        plt.text(v, i, f"${v:,.0f}", color=text_color, va="center")
    plt.tight_layout()
    plt.savefig(r"graficos\mayores_ventas_pais.png", bbox_inches="tight", dpi=dpi)
    plt.close()

    # Productos con mayores ventas
    sales_product = df.groupby("Product")["Amount"].sum().reset_index()
    sales_product = sales_product.sort_values("Amount", ascending=True)
    sales_product.plot(x="Product", y="Amount", kind="barh", color=bar_color, figsize=(10, 6))
    plt.title("Productos con mayores ventas", fontsize=16)
    plt.xlabel("Ventas ($)", fontsize=14)
    plt.ylabel("Producto", fontsize=14)
    plt.grid(axis="x", linestyle="--", alpha=alpha, color=line_color)
    plt.ticklabel_format(style="plain", axis="x")
    for i, v in enumerate(sales_product["Amount"]):
        plt.text(v, i, f"${v:,.0f}", color=text_color, va="center")
    plt.tight_layout()
    plt.savefig(r"graficos\mayores_ventas_producto.png", bbox_inches="tight", dpi=dpi)
    plt.close()

    # Vendedores con mayores ventas
    sales_salesperson = df.groupby("Sales Person")["Amount"].sum().reset_index()
    sales_salesperson = sales_salesperson.sort_values("Amount", ascending=True)
    sales_salesperson.plot(x="Sales Person", y="Amount", kind="barh", color=bar_color, figsize=(10, 8))
    plt.title("Vendedores con mayores ventas", fontsize=16)
    plt.xlabel("Ventas ($)", fontsize=14)
    plt.ylabel("Vendedor", fontsize=14)
    plt.grid(axis="x", linestyle="--", alpha=alpha, color=line_color)
    plt.ticklabel_format(style="plain", axis="x")
    for i, v in enumerate(sales_salesperson["Amount"]):
        plt.text(v, i, f"${v:,.0f}", color=text_color, va="center")
    plt.tight_layout()
    plt.savefig(r"graficos\mayores_ventas_vendedor.png", bbox_inches="tight", dpi=dpi)
    plt.close()

    # Días de la semana con mayores ventas
    sales_weekday = df.groupby("Weekday")["Amount"].sum().reset_index()
    sales_weekday = sales_weekday.sort_values("Amount", ascending=False)
    sales_weekday.plot(x="Weekday", y="Amount", kind="bar", color=bar_color)
    plt.xlabel("Día de la semana", fontsize=14)
    plt.ylabel("Ventas ($)", fontsize=14)
    plt.title("Días de la semana con mayores ventas", fontsize=16)
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=alpha, color=line_color)
    plt.ticklabel_format(style="plain", axis="y")
    for i, v in enumerate(sales_weekday["Amount"]):
        plt.text(i, v, f"${v:,.0f}", color=text_color, ha="center")
    plt.tight_layout()
    plt.savefig(r"graficos\mayores_ventas_dias_semana.png", bbox_inches="tight", dpi=dpi)
    plt.close()

    # Meses con mayores ventas
    sales_month = df.groupby("Month")["Amount"].sum().reset_index()
    sales_month = sales_month.sort_values("Amount", ascending=False)
    sales_month.plot(x="Month", y="Amount", kind="bar", color=bar_color)
    plt.xlabel("Mes", fontsize=14)
    plt.ylabel("Ventas ($)", fontsize=14)
    plt.title("Meses con mayores ventas", fontsize=16)
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=alpha, color=line_color)
    plt.ticklabel_format(style="plain", axis="y")
    for i, v in enumerate(sales_month["Amount"]):
        plt.text(i, v, f"${v:,.0f}", color=text_color, ha="center")
    plt.tight_layout()
    plt.savefig(r"graficos\mayores_ventas_meses.png", bbox_inches="tight", dpi=dpi)
    plt.close()

    # ..:::Reporte PDF:::..
    font_family = "Arial"
    font_size_title = 16
    font_size_content = 14

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()
    pdf.set_font(font_family, "B", font_size_title)
    pdf.cell(0, 10, "Reporte de Ventas", 0, 1, "C")
    pdf.set_font(font_family, "B", font_size_content)
    pdf.cell(0, 10, "Ventas por País", 0, 1, "L")
    pdf.image(r"graficos\mayores_ventas_pais.png", x=10, w=190)
    pdf.ln(10)

    pdf.add_page()
    pdf.set_font(font_family, "B", font_size_content)
    pdf.cell(0, 10, "Productos con Mayor Ventas", 0, 1, "L")
    pdf.image(r"graficos\mayores_ventas_producto.png", x=10, w=190)
    pdf.ln(10)

    pdf.add_page()
    pdf.set_font(font_family, "B", font_size_content)
    pdf.cell(0, 10, "Ventas por Vendedor", 0, 1, "L")
    pdf.image(r"graficos\mayores_ventas_vendedor.png", x=10, w=190)
    pdf.ln(10)

    pdf.add_page()
    pdf.set_font(font_family, "B", font_size_content)
    pdf.cell(0, 10, "Días de la Semana con Mayor Ventas", 0, 1, "L")
    pdf.image(r"graficos\mayores_ventas_dias_semana.png", x=10, w=190)
    pdf.ln(10)

    pdf.add_page()
    pdf.set_font(font_family, "B", font_size_content)
    pdf.cell(0, 10, "Meses con Mayores Ventas", 0, 1, "L")
    pdf.image(r"graficos\mayores_ventas_meses.png", x=10, w=190)

    pdf.output(fr"reportes\ReporteVentas_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.pdf")
