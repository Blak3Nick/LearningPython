import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate["DATE"] = pd.to_datetime(unrate['DATE'])
print(unrate.head(12))

x_values = unrate['DATE'].head(12)
y_values = unrate['VALUE'].head(12)
plt.plot(x_values, y_values)
plt.show()