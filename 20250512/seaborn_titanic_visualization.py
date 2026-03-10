import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")
#print(titanic) #1

#sns.countplot(data=titanic, x ="class", hue="who")
#fig = plt.gcf()
#plt.savefig("titanic.png") #2

# sns.relplot(data = titanic, x = "age", y = "fare", col = "survived")
# fig = plt.gcf()
# plt.savefig("titanic_fare.png") #3

titanic2 = titanic.pivot_table(index = "sex", columns = "class", values = 'survived',  aggfunc='sum')
sns.heatmap(titanic2, annot = True, cmap ='Blues')
fig = plt.gcf()
plt.savefig("titanic_heatmap.png") #4