import pandas as pd

weather = pd.read_csv('weather.csv', index_col = 0, encoding = 'utf8')

#1
print(weather.head(3))
print(weather.tail(3))

#2
print(weather.loc['2015-06-06'])

#3
print(weather['평균기온'].max())

#4
print(weather[weather['평균기온'] == weather['평균기온'].max()])

#5
print(weather[weather['평균기온'] >= 30])