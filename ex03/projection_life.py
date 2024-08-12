import matplotlib.pyplot as plt
from load_csv import load


def main():
    """main function"""
    year = "1900"
    df_exp = load("../life_expectancy_years.csv")
    df_inc = load("../income_per_person_gdppercap"
                  "ita_ppp_inflation_adjusted.csv")
    if df_exp is None or df_inc is None:
        return
    try:
        life_exp = df_exp[year]
        income = df_inc[year]
        plt.xlabel("Cross domestic product")
        plt.ylabel("Life Expectancy")
        plt.title(year)
        plt.xscale("log")
        plt.scatter(income, life_exp)
        plt.show()
    except Exception:
        print("smth is wrong with data")
        return


if __name__ == "__main__":
    main()
