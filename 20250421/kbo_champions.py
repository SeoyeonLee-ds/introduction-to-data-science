import pandas as pd

ulr = 'https://sports.news.naver.com/kbaseball/record/index?category=kbo&year='
years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
df = pd.DataFrame()

for y in years:
    kbo_df = pd.read_html(ulr + str(y))[0]
    kbo_df['year'] = y
    df = pd.concat([df, kbo_df])

df = df.replace({'SK':'SSG'})
df = df.replace({'넥센':'키움'})

df = df[df['순위'] == 1]
print(df)