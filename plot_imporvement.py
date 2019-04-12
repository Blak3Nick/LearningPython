import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

women_degrees = pd.read_csv('women_degrees.csv')
fig, ax = plt.subplots()
x_values = women_degrees['Year']
men_degrees = 100 - women_degrees['Biology']
y_values = women_degrees['Biology']

ax.plot(x_values, y_values, color='blue', label="Women")
ax.plot(x_values, men_degrees, color='green', label='Men')
plt.title("Percentage of Biology Degrees Awarded By Gender")
ax.tick_params(bottom=False, top=False, left=False, right=False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
plt.legend(loc=1)
plt.show()


cb_dark_blue = (0/255, 107/255, 164/255)
cb_orange = (255/255, 128/255, 14/255)
major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
fig = plt.figure(figsize=(12, 12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.tick_params(bottom=False, top=False, left=False, right=False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    plt.title(major_cats[sp])
plt.legend(loc='upper right')

plt.show()

stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']
fig = plt.figure(figsize=(18, 3))
for sp in range(0,6):
    ax = fig.add_subplot(1,6,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    if sp == 0:
        ax.text(2005, 87, "Men")
        ax.text(2002, 8, "Women")
    if sp == 5:
        ax.text(2005, 62, "Men")
        ax.text(2001, 35, "Women")
#plt.legend(loc='upper right')
plt.show()
