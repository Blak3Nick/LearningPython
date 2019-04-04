import pandas as pd

fitness_file = pd.read_excel("E:\DocumentsForLongTermStorage\SquadronReadiness\Fitness.xls", sheet_name=0, header=11,  parse_dates=True, index_col="Last Name")
nichoslon = fitness_file.loc["NICHOLSON"]
