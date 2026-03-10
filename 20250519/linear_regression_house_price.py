from sklearn import linear_model

regr = linear_model.LinearRegression()

X = [[85, 6], [76, 5], [50, 4], [44, 3], [57, 4], [88, 5], [78, 7], [97, 7], [45, 3], [76, 6]]
y = [8.9, 7.7, 3.1, 1.8, 6.7, 9.5, 8.4, 12.2, 2.3, 8.5]

regr.fit(X, y)

test_X = [[65, 5], [75, 5]]

print("계수:", regr.coef_)
print("절편:", regr.intercept_)
print("점수:", regr.score(X, y))
print("실면적 65 m^2, 접근성 점수 5:", regr.predict([[65, 5]]))
print("실면적 75 m^2, 접근성 점수 5:", regr.predict([[75, 5]]))