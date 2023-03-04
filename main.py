import pandas as pd
import numpy as np
from utils import replace_missing_values, boxplot_column

def main():
    df = pd.read_csv("./Datos1.csv", usecols=['Grasas_sat','Alcohol','Calorías','Sexo'])
    method = "median"


    df["Calorías"] = df["Calorías"].str.replace(",", "").astype(int)
    print(df["Calorías"].head())    

    df["Sexo"] = df["Sexo"].replace("F","0").replace("M","1").astype(int)

    df = replace_missing_values(df, "Alcohol", 999.99, method)
    df = replace_missing_values(df, "Grasas_sat", 999.99, method)

    boxplot_column(df, "Alcohol", method)
    boxplot_column(df, "Grasas_sat", method)
    boxplot_column(df, "Calorías", method)
    boxplot_column(df, "Sexo", method)

    


if __name__ == "__main__":
    main()