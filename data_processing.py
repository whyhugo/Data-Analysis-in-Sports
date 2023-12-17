import pandas as pd

mlb_rank = pd.read_csv('mlb_stats/MLB_rank.csv', encoding='utf-8', index_col=0)
urls = pd.read_csv('mlb_stats_urls.csv', encoding='utf-8')

data_list = []
for year in range(2013, 2024):
    for team_name in urls['link']:
        file = f'mlb_stats/{year}/{team_name[26:-1]}_{year}.csv'
        time.sleep()
        df = pd.read_csv(file, encoding='utf-8')
        rank = mlb_rank.loc[df.loc[0, 'TEAM'], str(year)]
        df = df.drop(['PLAYER', 'POSITION', 'TEAM'], axis=1)
        try:
            df = df.replace('--', 0, inplace=True)
            df = df.replace('-.--', 0, inplace=True)
            df = df.replace('.---', 0, inplace=True)
        except:
            continue
        column_means = df.mean()
        data_list.append(column_means.append(int(rank)))

data = pd.DataFrame(data_list)
data.to_csv('data.csv', index=False, encoding='utf-8')