import pandas as pd
from utils import replace_missing_values, boxplot_column, cov_analysis, histogram_column, categorize_calories_col, scatter_category, bar_column

def main():
    df = pd.read_csv("./Datos1.csv", usecols=['Grasas_sat','Alcohol','Calorías','Sexo'])
    method = "mean"


    df["Calorías"] = df["Calorías"].str.replace(",", "").astype(int)

    # df["Sexo"] = df["Sexo"].replace("F","0").replace("M","1").astype(int)

    df = replace_missing_values(df, "Alcohol", 999.99, method)
    df = replace_missing_values(df, "Grasas_sat", 999.99, method)

    # boxplot de todas las variables
    boxplot_column(df, "Alcohol", method)
    boxplot_column(df, "Grasas_sat", method)
    boxplot_column(df, "Calorías", method)
    # histogram_column(df, "Sexo")
    bar_column(df, "Sexo")

    # analisis de covarianza
    input_df = df.loc[:,df.columns != "Sexo"]

    normalized_df=(input_df-input_df.mean())/input_df.std()

    normalized_df["Sexo"] = df["Sexo"]
    cov_analysis(normalized_df)

    # categorizando calorias
    categorized_df = categorize_calories_col(df)
    scatter_category(categorized_df, "Alcohol", "Categorías")
    


if __name__ == "__main__":
    main()