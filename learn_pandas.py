import pandas as pd
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