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