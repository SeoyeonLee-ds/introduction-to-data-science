import numpy as np

X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([0, 0, 0, 1])

class Perceptron:
    def __init__(self, input_size, lr, epochs):
        self.weight = np.zeros(input_size) #[0,0]
        self.bias = 0
        self.lr = lr
        self.epochs = epochs
    
    def activation(self, x):
        return 1 if x >= 0 else 0
    
    def train(self, X, y):
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                pred = self.predict(xi)
                error = target - pred
                self.weight += self.lr * error * xi
                self.bias += self.lr * error
    
    def predict(self, x):
        return self.activation(np.dot(x, self.weight) + self.bias)
    
#퍼셉트론 학습
p  = Perceptron(2, lr=0.1, epochs = 10)
p.train(X, y)
#추론
print('예측 결과:')
for xi in X:
    print(f"{xi} => {p.predict(xi)}")
print('weight = ', p.weight)
print('bias = ', p.bias)