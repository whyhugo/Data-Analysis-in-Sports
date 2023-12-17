import pandas as pd
import time

mlb_rank = pd.read_csv('mlb_stats/MLB_rank.csv', encoding='utf-8', index_col=0)
urls = pd.read_csv('mlb_stats_urls/mlb_stats_urls.csv', encoding='utf-8')

data_list = []
for year in range(2013, 2014):
    for team_name in urls['link']:
        print(team_name[26:-1])
        file = f'mlb_stats/{year}/{team_name[26:-1]}_{year}.csv'
        #time.sleep(1)
        df = pd.read_csv(file, encoding='utf-8')
        rank = mlb_rank.loc[df.loc[0, 'TEAM'], str(year)]
        df = df.drop(['PLAYER', 'POSITION', 'TEAM'], axis=1)
        try:
            df = df.replace('--', 0, regex=True)
            df = df.replace('-.--', 0, regex=True)
            df = df.replace('.---', 0, regex=True)
            df = df.applymap(lambda x: f'0.{str(x)[1:]}' if str(x).startswith('.') else x)
        except:
            continue
        df = df.astype(float)
        column_means = list(df.mean())
        column_means.append(int(rank))
        data_list.append(column_means)

column_name = df.columns.tolist()
column_name.append('RANK')
data = pd.DataFrame(data_list, columns=column_name)
data.to_csv('data.csv', index=False, encoding='utf-8')