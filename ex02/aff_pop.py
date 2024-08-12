import matplotlib.pyplot as plt
from load_csv import load


def is_int(var):
    """checks if var is int"""
    try:
        int(var)
        return True
    except Exception:
        return False


def my_convert(var):
    """converts var to float in millions"""
    opt = 0
    if (var[-1] == "M"):
        opt = 1
    elif var[-1] == "k":
        opt = 2
    elif var[-1] == "B":
        opt = 3
    var = var[:-1]
    out = float(var)
    if opt == 2:
        out /= 1000.0
    elif opt == 3:
        out *= 1000.0
    return out


def main() -> None:
    """main function"""
    country1 = "France"
    country2 = "Germany"

    df = load("../population_total.csv")
    if df is None:
        return
    try:
        germany = df[df['country'] == country1]
        france = df[df['country'] == country2]
        years = germany.columns[1:]
        germany_pop = [my_convert(germany[year].values[0])
                       for year in years if int(year) <= 2050]
        france_pop = [my_convert(france[year].values[0])
                      for year in years if int(year) <= 2050]
        years = [int(year) for year in years if int(year) <= 2050]

        plt.xlabel("year")
        plt.ylabel("population")
        plt.title(f"population comparison of {country1} and {country2}")
        plt.plot(years, germany_pop)
        plt.plot(years, france_pop)
        plt.legend([country1, country2], loc='upper left')
        plt.show()

    except Exception:
        print("Something is wrong with data")
        return


if __name__ == "__main__":
    main()
