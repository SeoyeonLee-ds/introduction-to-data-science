import pandas as pd
import matplotlib.pyplot as plt
#학생들의 키를 모은 데이터
df = pd.DataFrame({'학생키': [170, 160, 164, 185, 180, 169, \
                           167, 172, 175, 165, 199]})
print(df)

plt.boxplot(df)
#plt.show()

Q1 = df['학생키'].quantile(0.25)
Q3 = df['학생키'].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df['학생키'] < Q1-1.5*IQR) | (df['학생키'] >Q3+1.5*IQR)]

print(outliers)
df = df.drop(outliers.index)
print(df)

plt.clf()
plt.boxplot(df)
plt.show()