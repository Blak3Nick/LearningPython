import pandas as pd

laptops = pd.read_csv("laptops.csv", encoding="Latin-1")


def clean_c(string):
    string = string.strip()
    string = string.replace("Operating System", "os")
    string = string.replace("(", "")
    string = string.replace(")", "")
    string = string.lower()
    string = string.replace(" ", "_")
    return string
new_columns = []
for c in laptops.columns:
    new_name = clean_c(c)
    new_columns.append(new_name)
laptops.columns = new_columns

ram = laptops["ram"]
laptops.rename({"ram": "ram_gb"}, axis=1, inplace=True)
laptops["ram_gb"] = laptops["ram_gb"].str.replace("GB", "")
laptops["ram_gb"] = laptops["ram_gb"].astype(int)
dtypes = laptops.dtypes
weight = laptops["weight"]
laptops["weight"] = laptops["weight"].str.replace("kg", "")
laptops["weight"] = laptops["weight"].str.replace("s", "")
unique = laptops["weight"].unique()
laptops["weight"] = laptops["weight"].astype(float)
laptops.rename({"weight": "weight_kg"}, axis=1, inplace=True)
laptops["price_euros"] = laptops["price_euros"].str.replace(",", ".")
laptops["price_euros"] = laptops["price_euros"].astype(float)

weight_describe = laptops["weight_kg"].describe()
price_describe = laptops["price_euros"].describe()
laptops["cpu_manufacturer"] = (laptops["cpu"].str.split(n=1, expand=True).iloc[:, 0])

