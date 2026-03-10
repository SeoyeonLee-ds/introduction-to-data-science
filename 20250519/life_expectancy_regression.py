from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

life = pd.read_csv("life_expectancy.csv")
print('life.shape = ', life.shape)

life.dropna(inplace = True)
print('life.shape = ', life.shape)

X = life[['Alcohol', 'Percentage expenditure', 'Polio', 'BMI', 'GDP', 'Thinness 1-19 years']]
print('X.shape = ', X.shape)
y = life['Life expectancy']

#split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
#training
regr = LinearRegression()
regr.fit(X_train, y_train)
#prediction
y_pred = regr.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print('mse = ', mse)
print('rmse = ', rmse)

# plt.scatter(y_pred, y_test)
# x = np.linspace(0, 330, 100)
# plt.plot(x, x)
# plt.show()