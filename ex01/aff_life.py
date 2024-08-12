import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from load_csv import load



def main()->None:
    """main function"""
    df = load("../life_expectancy_years.csv")
    if df is None:
        return
    try:
        numeric_df = df.select_dtypes(include=['number'])
        mean_data = numeric_df.mean()
        years = mean_data.index.to_list()
        life = mean_data.to_list()

        fig, axis = plt.subplots()
        axis.plot(years, life)
        axis.xaxis.set_major_locator(MaxNLocator(integer=True))
        axis.set_xlabel("Year")
        axis.set_ylabel("Life expectancy")
        axis.set_title("Life expectancy over the years")
        plt.show()
    except Exception:
        print("Dataset is modified")
        return


if __name__ == "__main__":
    main()