import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
unrate = pd.read_csv('unrate.csv')

unrate["DATE"] = pd.to_datetime(unrate['DATE'])
print(unrate.head(12))


x_values = unrate['DATE'].head(12)
y_values = unrate['VALUE'].head(12)

plt.plot(x_values, y_values)
plt.xticks(rotation=90)
plt.xlabel('Month')
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show()