import pandas as pd
df = pd.DataFrame({'name': ['A','B','C', 'D'],
                   'horse power': [120, 220, 120, 200],
                   'weight': [1.9, 2.1, 1.5, 2.9],
                   'efficiency': [18.3, 19.2, 21.1, 17.3]})
df_2 = pd.DataFrame({'name': ['A','B','C','D','E','F','G'],
                     'horse power': [130, 250, 190, 300, 210, 220, 170],
                     'weight': [1.9, 2.6, 2.2, 2.9, 2.4, 2.3, 2.2],
                     'efficiency': [16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2]})
df = df.set_index('name')
df_2 = df_2.set_index('name')
print(df)

df_3 = pd.concat([df, df_2])
print(df_3)

df['com'] = 'P'
df_2['com'] = 'Q'
df_3 = pd.concat([df, df_2])
df_3['hp x mile'] = df_3['horse power'] * df_3['efficiency']
print(df_3)

print(df_3.groupby('com').mean()['hp x mile'])