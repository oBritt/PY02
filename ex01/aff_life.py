import matplotlib.pyplot as plt
from load_csv import load


def main() -> None:
    """main function"""
    country = "Germany"
    df = load("../life_expectancy_years.csv")
    if df is None:
        return
    try:
        germany = df[df['country'] == country]
        years = germany.columns[1:]
        life = [float(germany[year].values[0]) for year in years]
        years = [int(year) for year in years]

        # fig, axis = plt.subplots()
        # axis.plot(years, life)
        # axis.xaxis.set_major_locator(MaxNLocator(integer=True))
        # axis.set_xlabel("Year")
        # axis.set_ylabel("Life expectancy")
        # axis.set_title("Life expectancy over the years")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.title(f"Life expectancy of {country} over the years")
        plt.plot(years, life)
        plt.show()
    except Exception:
        print("Dataset is modified")
        return


if __name__ == "__main__":
    main()
