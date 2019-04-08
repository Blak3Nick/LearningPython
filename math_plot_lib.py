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

fig = plt.figure(figsize=(12,5))

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()

fig = plt.figure(figsize=(12,12))
forty_eight = fig.add_subplot(5,1,1)
forty_eight.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
forty_nine = fig.add_subplot(5,1,2)
forty_nine.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
fifty = fig.add_subplot(5,1,3)
fifty.plot(unrate[24:36]['DATE'], unrate[24:36]['VALUE'])
fifty_one = fig.add_subplot(5,1,4)
fifty_one.plot(unrate[36:48]['DATE'], unrate[36:48]['VALUE'])
fifty_two = fig.add_subplot(5,1,5)
fifty_two.plot(unrate[48:60]['DATE'], unrate[48:60]['VALUE'])
plt.show()

unrate.describe()

unrate['MONTH'] = unrate['DATE'].dt.month

fig = plt.figure(figsize=(10,6))

plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c='red', label='1948')
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'], c='blue', label='1949')
plt.plot(unrate[24:36]['MONTH'], unrate[24:36]['VALUE'], c='green', label='1950')
plt.plot(unrate[36:48]['MONTH'], unrate[36:48]['VALUE'], c='orange', label='1951')
plt.plot(unrate[48:60]['MONTH'], unrate[48:60]['VALUE'], c='black', label='1952')
plt.legend(loc='upper left')
plt.show()

year = 1947
year_string = str(year)
print(year_string)

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
year = 1947
for i in range(5):
    year += 1
    year_string = str(year)
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=year_string)
plt.legend(loc='upper left')
plt.title("Monthly Unemployment Trends, 1948-1952")
plt.xlabel('Month, Integer')
plt.ylabel('Unemployment Rate, Percent')
plt.show()