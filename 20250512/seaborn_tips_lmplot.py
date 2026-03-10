import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="darkgrid")
tips = sns.load_dataset("tips")

#print(sns.get_dataset_names()) #제공하는 라이브러리 보는 법

sns.lmplot(data=tips, x = "total_bill", y="tip",  hue = "smoker")
fig = plt.gcf()
plt.savefig("Implot_ex.png")
