import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

flights = sns.load_dataset("flights")

flights_wide = flights.pivot(index='year', columns='month', values='passengers')

#print(flights_wide)

#sns.relplot(data = flights_wide, kind = "line")
sns.relplot(data=flights_wide.transpose(), kind = 'line')

fig = plt.gcf()
#plt.savefig("relplot.png")
plt.savefig("relplot_ex.png")