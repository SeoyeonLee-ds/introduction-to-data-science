import pandas as pd

# read csv
df = pd.read_csv('Mall_Customers.csv')
print(df)

#feature scaling
from sklearn.preprocessing import MinMaxScaler
data = df[['Annual Income (k$)', 'Spending Score (1-100)']]
scaler = MinMaxScaler()
data_scale = scaler.fit_transform(data)

#kmeans clustering (k=3, 4, 5, 6)
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
ks = [3,4,5,6]
plt.figure(figsize=(10,10))
for k in ks:
    model = KMeans(n_clusters=k, random_state = 10)
    model.fit(data_scale)
    df['cluster'] = model.fit_predict(data_scale)

    plt.subplot(2,2, k-2)
    for i in range(k):
        plt.scatter(df.loc[df['cluster']==i, 'Annual Income (k$)'], df.loc[df['cluster']==i, 'Spending Score (1-100)'], label = 'cluster' + str(i))

    plt.legend()
    plt.title('K = %d result' %k)
    plt.xlabel('Annual Income')
    plt.ylabel('Spending Score')
plt.savefig('clustering_ex.png')
#scatter plot
