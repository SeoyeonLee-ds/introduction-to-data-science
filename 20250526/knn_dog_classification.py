#dachshund data
dachshund_length = [77, 78, 85, 83, 73, 77, 73, 80]
dachshund_height = [25, 28, 19, 30, 21, 22, 17, 35]
dachshund = list(zip(dachshund_length, dachshund_height))
X1 = [list(x) for x in dachshund]
y1 = [0] * len(X1)
#samoyed data
samoyed_length = [75, 77, 86, 86, 79, 83, 83, 88]
samoyed_height = [56, 57, 50, 53, 60, 53, 49, 61]
samoyed = list(zip(samoyed_length, samoyed_height))
X2 = [list(x) for x in samoyed]
y2 = [1] * len(X2)
#maltese data
maltese_length = [34, 38, 38, 41, 30, 37, 41, 35]
maltese_height = [22, 25, 19, 30, 21, 24, 28, 18]
maltese = list(zip(maltese_length, maltese_height))
X3 = [list(x) for x in maltese]
y3 = [2] * len(X3)

dogs = X1 + X2 + X3
labels = y1 + y2 + y3
dog_classes = {0:'닥스훈트', 1: '사모예드', 2:'말티즈'} 

from sklearn.neighbors import KNeighborsClassifier
#knn
def classify_dog(data, label):
    for n in range(1, 6):
         knn = KNeighborsClassifier(n_neighbors = n)
         knn.fit(dogs, labels)
         y_pred = knn.predict(data)
         print(label,":n_neighbor가 ", n, "일때 :", dog_classes[y_pred[0]])

A = [[56, 44]]
classify_dog(A, 'A')
B = [[74, 29]]
classify_dog(B, 'B')
C = [[59, 30]]
classify_dog(C, 'C')
D = [[70, 43]]
classify_dog(D, 'D')
E = [[75, 35]]
classify_dog(E, 'E')

#scatter
import matplotlib.pyplot as plt
plt.scatter(dachshund_length, dachshund_height, c = 'red', label='dachshund')
plt.scatter(samoyed_length, samoyed_height, c = 'blue', label='dachshund')
plt.scatter(maltese_length, maltese_height, c = 'green', label='dachshund')
plt.scatter(56,44,s=300, c='magenta', label='A')
plt.scatter(74,29,s=300, c='gray', label='B')
plt.scatter(59,30,s=300, c='cyan', label='C')
plt.scatter(70,43,s=300, c='yellow', label='D')
plt.scatter(75,35,s=300, c='pink', label='E')
plt.xlabel('length')
plt.ylabel('Height')
plt.title('Dog size')
plt.legend()
plt.savefig('dog_size.png', dpi=300, bbox_inches='tight')