import pandas as pd

fitness_file = pd.read_excel("E:\DocumentsForLongTermStorage\SquadronReadiness\Fitness.xls", sheet_name=0, header=11,  parse_dates=True,  skipfooter=9, index_col=0)

name = fitness_file[["Last Name", "First Name"]]

first_name = name["First Name"]
last_name = name["Last Name"]
all_names = pd.concat([last_name, first_name], axis=1)