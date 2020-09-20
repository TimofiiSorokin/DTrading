import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dg_year_2016.csv")

df = df[['АЕС', 'ТЕЦ', 'Генерація з ВДЕ', 'ТЕС', 'ГЕС']].sum()

labels = ('АЕС', 'ТЕЦ', 'Генерація з ВДЕ', 'ТЕС', 'ГЕС')
sizes = [df[0], df[1], df[2], df[3], df[4]]
colors = ['blue', 'yellowgreen', 'magenta', 'yellow', 'red']
explode = (0.1, 0, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
