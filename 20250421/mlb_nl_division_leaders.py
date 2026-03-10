import pandas as pd

ulr = 'https://sports.news.naver.com/wbaseball/record/index?category=mlb&league=NL&year=2024'
df = pd.DataFrame()

nl_tb = pd.read_html(ulr)

df = nl_tb[0]
d1 = df.loc[0]
d1 = d1.rename(index={'동부지구.1':'1위팀'})
d1.drop(index='동부지구', inplace=True)
df = nl_tb[1]
d2 = df.loc[0]
d2 = d2.rename(index={'중부지구.1':'1위팀'})
d2.drop(index='중부지구', inplace=True)
df = nl_tb[2]
d3 = df.loc[0]
d3 = d3.rename(index={'서부지구.1':'1위팀'})
d3.drop(index='서부지구', inplace=True)

df = pd.concat([d1, d2, d3], axis = 1)
df.columns = ['동부', '중부', '서부']
print(df)
