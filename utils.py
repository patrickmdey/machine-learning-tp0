from matplotlib import pyplot as plt
def replace_missing_values(df, column, value, method="mean"):
    mean_df = df.copy()
    median_df = df.copy()
    df.drop(df[df[column] >= value].index, inplace=True) # drops the rows that have Alcohol >= value
    df_mean = df[column].mean()
    df_median = df[column].median()

    # print("Removing rows with " + column +" >=", value,"...")
    # print()
    # print("Mean:", df_mean)
    # print("Median:", df_median)

    # print()
    if (method == "mean"):
        # print("Replacing for mean...")
        mean_df.loc[mean_df[column] >= value, column] = df_mean
        # mean_df[column].replace(value, df_mean, inplace=True)
        # print("New " + column +" mean:", mean_df[column].mean())
        # print("New " + column +" median:", mean_df[column].median())
        return mean_df
    elif (method == "median"):
        # print("Replacing for median...")
        median_df.loc[median_df[column] >= value, column] = df_median
        # median_df[column].replace(value, df_median, inplace=True)
        # print("New " + column +" mean:", median_df[column].mean())
        # print("New " + column +" median:", median_df[column].median())
        return median_df

def boxplot_column(df, column_name, method=""):
    plt.clf()
    boxplot = df.boxplot(column=column_name, grid=False)
    boxplot.set_title(column_name+ " boxplot")
    # boxplot.set_xlabel("Variables")
    boxplot.set_ylabel("Valor")
    str = column_name + "_with_" + method if method != "" else column_name
    boxplot.figure.savefig("./out/"+str + "_boxplot.png")