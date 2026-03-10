from sklearn.neural_network import MLPClassifier

X = [[0,0], [0,1], [1,0], [1,1]]
y = [0, 1, 1, 0]

mlp = MLPClassifier(hidden_layer_sizes=(4,), activation = 'logistic', solver = 'lbfgs', max_iter = 1000)
mlp.fit(X, y)

print('XOR 문제 예측 결과:')
for x in X:
    pred = mlp.predict([x])
    print(x, "=>", pred[0])
print('정확도: ', mlp.score(X, y))