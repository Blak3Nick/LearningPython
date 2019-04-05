import pandas as pd
import numpy as np
f500 = pd.read_csv("C:\\Users\\Cyr1lfiggus1\\Downloads\\f500.csv")
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan
sorted_emp = f500.sort_values("employees",ascending=False)
top5_emp = sorted_emp.iloc[0:5]
previously_ranked = f500[f500["previous_rank"].notnull()]
rank_change = previously_ranked["previous_rank"] - previously_ranked["rank"]
