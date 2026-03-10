import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv('weather.csv', index_col = 0, encoding='utf8')
weather['평균풍속'].plot(kind='hist', bins=33)
plt.show()