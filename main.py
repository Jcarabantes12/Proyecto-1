import os

from EDA import eda
from Limpieza import data_cleansing
from Analisis import analisis

def create_files():
    os.makedirs("reportes", exist_ok=True) # Carpeta de reportes
    os.makedirs("graficos", exist_ok=True) # Carpeta de graficos

if __name__ == "__main__":
    dframe = r"data/ChocolateSales.csv"
    create_files()
    eda(dframe)
    dframe_clean = data_cleansing(dframe)
    analisis(dframe_clean)