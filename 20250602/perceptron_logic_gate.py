from sklearn.linear_model import Perceptron

# 학습 데이터
X = [[0, 0], [0, 1], [1, 0], [1, 1]]

# AND 게이트
y_and = [0, 0, 0, 1]
y_or = [0, 1, 1, 1]
y_xor = [0, 1, 1, 0]
p = Perceptron(max_iter=1000, tol=1e-3)
#p.fit(X, y_and)
#p.fit(X, y_or)
p.fit(X, y_xor)


print('weight = ', p.coef_)
print('bias = ', p.intercept_)

print("예측 결과:")
for input_data in X:
    pred = p.predict([input_data])
    print(input_data, "=>", pred)