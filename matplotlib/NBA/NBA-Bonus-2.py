import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_excel('NBA Boxscores 2019-22.xlsx', sheet_name='2021-2022例行賽')

team_list = []
for team in df1['TEAM'].unique():
    team_list.append(team)

# POR 對戰各隊

w_list = []
l_list = []

for team in team_list:
    w_temp = 0
    l_temp = 0
    for i in range(len(df1)):
        if df1.loc[i, 'TEAM'] == 'POR' and df1.loc[i, 'MATCHUP'][-3:] == team:
            if df1.loc[i, 'W/L'] == 'W':
                w_temp += 1
            else:
                l_temp += 1
        elif df1.loc[i, 'TEAM'] == team and df1.loc[i, 'MATCHUP'][-3:] == 'POR':
            if df1.loc[i, 'W/L'] == 'W':
                l_temp += 1
            else:
                w_temp += 1
    w_list.append(w_temp)
    l_list.append(l_temp)

plt.rc('font', family='Microsoft JhengHei')
fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(team_list, w_list, label='勝', color='#5BC49F')
ax.bar(team_list, l_list, bottom=w_list, label='負', color='#FEB64D')

ax.set_title('NBA 2021-2022 POR 對戰它隊勝負結果')
ax.legend()

plt.show()