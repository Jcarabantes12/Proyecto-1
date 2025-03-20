"""
2. Limpieza de datos
"""

import pandas as pd

# ..:::Limpieza de Datos:::..
def data_cleansing(csv_path: str):
    # Cargar el archivo CSV a un dataframe
    df = pd.read_csv(csv_path)

    # Converción de tipos de datos
    df["Sales Person"] = df["Sales Person"].astype("string")
    df["Country"] = df["Country"].astype("string")
    df["Product"] = df["Product"].astype("string")
    df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%y", errors="coerce") # 01-Jan-21
    df["Amount"] = df["Amount"].str.replace("$", "", regex=False).str.replace(",", "", regex=False).astype(float)
    df["Boxes Shipped"] = df["Boxes Shipped"].astype(int)

    # Eliminación de valores nulos
    df.dropna(inplace=True)

    # Eliminación de duplicados
    df.drop_duplicates(inplace=True)

    # Eliminación espacio en blanco
    df["Sales Person"] = df["Sales Person"].str.strip()
    df["Country"] = df["Country"].str.strip()
    df["Product"] = df["Product"].str.strip()

    # Dividir fecha
    df["Weekday"] = df["Date"].dt.day_name() # Día de la semana
    df["Day"] = df["Date"].dt.day # Día
    df["Month"] = df["Date"].dt.month_name() # Mes
    df["Year"] = df["Date"].dt.year # Año

    # Exportar el dataframe en formato CSV
    df.to_csv(fr"{csv_path}_clean.csv", index=False)

    return fr"{csv_path}_clean.csv"