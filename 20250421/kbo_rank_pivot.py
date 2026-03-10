import pandas as pd

ulr = 'https://sports.news.naver.com/kbaseball/record/index?category=kbo&year='
years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
df = pd.DataFrame()

for y in years:
    kbo_df = pd.read_html(ulr + str(y))[0]
    kbo_df['year'] = y
    df = pd.concat([df, kbo_df])
#print(df)
df = df.replace({'SK':'SSG'})
#print(df)
rank_df = df.pivot(values='순위', index = 'year', columns = '팀')
#print(rank_df)
rank_df = rank_df.fillna(0)
#print(rank_df)
rank_df = rank_df.fillna(0).astype('Int8')
print(rank_df)
