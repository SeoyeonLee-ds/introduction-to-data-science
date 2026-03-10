import csv
import matplotlib.pyplot as plt

#open and read csv file
f = open('weather.csv', encoding='utf8')
data = csv.reader(f)
header = next(data)

# define and initialize 1) list for wind, 2) list for days
# monthly_wind = [0,0,0,0,0,0,0,0,0,0,0,0]
monthly_wind = [0 for x in range(12)]
days_counted = [0 for x in range(12)]

# iterate for each row
# get month and wind
# update lists
for row in data:
    month = int(row[0][5:7])
    if row[3] != '':
        wind = float(row[3])
        monthly_wind[month-1] += wind
        days_counted[month-1] += 1


#compute monthly_wind
for i in range(12):
    monthly_wind[i] /= days_counted[i]
#plot and save
plt.plot(monthly_wind,'blue')
plt.savefig('weather_graph.png')
f.close()
