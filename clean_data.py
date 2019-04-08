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
ghz = laptops["cpu"]
ghz_string = ghz.str.rsplit(n=1, expand=True)
ghz_string.loc[:,1] = ghz_string.loc[:,1].str.replace("GHz", "")
print(ghz_string.loc[:,1].unique())
laptops["cpu_speed_ghz"] = ghz_string.loc[:,1].astype(float)

mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}
laptops["os"] = laptops["os"].map(mapping_dict)
laptops_no_null_rows = laptops.dropna()
laptops_no_null_cols = laptops.dropna(axis=1)
laptops.loc[laptops["os"] == "No OS", "os_version"] = "Version Unknown"

version_unknown = laptops.loc[laptops["os_version"] == "No OS"]

print(laptops.loc[laptops["os_version"].isnull(), "os"].value_counts())


laptops["storage_1_capacity_gb"] = laptops["storage"].str.split(n=1)
second_half = laptops["storage_1_capacity_gb"].values

for i in range(len(second_half)):
    second_half[i] = second_half.item(i)[1]
laptops.rename({"storage_1_capacity_gb": "storage_1_type"}, axis=1, inplace=True)
first_half = laptops["storage"].str.split(expand=True)

first_storage = first_half.loc[:,0]
first_type = first_half.loc[:,1]

laptops["storage_1_type"] = first_type
laptops["storage_1_capacity_gb"] = first_storage

laptops["storage_1_capacity_gb"] = laptops["storage_1_capacity_gb"].str.replace("GB", "")
laptops.loc[laptops["storage_1_capacity_gb"] == "1TB", "storage_1_capacity_gb"] = "1000"
laptops.loc[laptops["storage_1_capacity_gb"] == "2TB", "storage_1_capacity_gb"] = "2000"
laptops["storage_1_capacity_gb"] = laptops["storage_1_capacity_gb"].astype(float)
laptops["storage_2_capacity_gb"] = first_half[3]
first_half[4].unique()
laptops.loc[laptops["storage_2_capacity_gb"] == "+", "storage_2_capacity_gb" ] = "1TB"
laptops["storage_2_capacity_gb"] = laptops["storage_2_capacity_gb"].str.replace("GB", "")
laptops["storage_2_capacity_gb"] = laptops["storage_2_capacity_gb"].str.replace("1TB", "1000")
laptops["storage_2_capacity_gb"] = laptops["storage_2_capacity_gb"].str.replace("2TB", "2000")
print(laptops["storage_2_capacity_gb"].unique())
laptops["storage_2_capacity_gb"] = laptops["storage_2_capacity_gb"].astype(float)
# first_half.loc[first_half.loc[:,5] == "HDD", first_half.loc[4]] = "HDD"

first_half[4, 447] = "HDD"
laptops["storage_2_type"] = first_half[4]

laptops["storage_2_type"] = laptops["storage_2_type"].str.replace("1TB", "HDD")