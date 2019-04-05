import pandas as pd
import numpy as np
from pandas import DataFrame as df
f500 = pd.read_csv("C:\\Users\\Cyr1lfiggus1\\Downloads\\f500.csv", index_col=0)
f500.index.name = None
f500_type = type(f500)
f500_shape = f500.shape
f500.head(7)
f500.info(3)

industries = f500.loc[:, "industry"]
previous = f500.loc[:,["rank", "previous_rank", "years_on_global_500_list"]]
financial_data = f500.loc[:, "revenues":"profit_change"]
countries = f500.country
revenues_years = f500[["revenues", "years_on_global_500_list"]]
ceo_to_sector = f500.loc[:, "ceo": "sector"]


ceos = f500["ceo"]
walmart = ceos["Walmart"]
apple_to_samsung = ceos["Apple":"Samsung Electronics"]
oil_companies = ceos[["Exxon Mobil", "BP", "Chevron"] ]
chevron = ceos["BP"]
drink_companies = f500.loc[["Anheuser-Busch InBev", "Coca-Cola", "Heineken Holding"]]
big_movers = f500.loc[["Aviva", "HP", "JD.com", "BHP Billiton"]]
big_movers = big_movers[["rank", "previous_rank"]]
middle_companies = f500.loc["Tata Motors":"Nationwide"]
middle_companies = middle_companies.loc[:, "rank":"country"]
my_series = f500.loc[:, "profits"]
profits_desc = my_series.describe()
profits_desc = f500.loc[:, "profits"].describe()
revenue_and_employees_desc = f500.loc[:, ["revenues", "employees"]].describe()
top_3countries = f500["country"].value_counts().head(3)
top3_previous_rank = f500["previous_rank"].value_counts().head(3)

max_f500 = f500.select_dtypes(include='number').max()
f500["revenues_b"] = f500["revenues"] / 1000
f500.loc["Dow Chemical", "ceo"] = "Jim Fitterling"
kr_bool = f500["country"] == "South Korea"
top_5_kr = f500.loc[kr_bool].head()
nan_bool = f500["previous_rank"] == 0
f500.loc[nan_bool, "previous_rank"] = np.nan
prev_rank_after = f500["previous_rank"].value_counts().head()

cities_usa = f500["hq_location"].value_counts().head(5)
sector_china_bool = f500["country"] == "China"
sector_china = f500.loc[sector_china_bool, "sector"].value_counts().head(3)

mean_employees_japan_bool = f500["country"] == "Japan"
mean_employees_japan = f500.loc[mean_employees_japan_bool, "employees"].mean()

fifth_row = f500.iloc[4]
first_three_rows = f500.iloc[0:3]
first_seventh_row_slice = f500.iloc[[1, 7], 0:5]
