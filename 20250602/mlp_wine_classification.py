from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

#데이터셋 준비
wine = load_wine()
print(wine)
X = wine.data
y = wine.target

#학습용/테스트용 데이터 분할 (테스트 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

#특징 정규화
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#MLP 분류기 학습
mlp = MLPClassifier(hidden_layer_sizes = (10, ), activation = 'relu', solver= 'adam', max_iter=1000)
mlp.fit(X_train, y_train)

y_pred = mlp.predict(X_test)
print(classification_report(y_test, y_pred, target_names = wine.target_names))
print('정확도: ', mlp.score(X, y))