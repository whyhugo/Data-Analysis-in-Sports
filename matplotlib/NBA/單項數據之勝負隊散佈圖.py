import pandas as pd
from matplotlib import pyplot as plt

def ReadDataFromFile(filename, sheetname):
    data = pd.read_excel(filename, sheet_name = sheetname).to_dict('records')
    return list(data[0].keys()), data
#-----------------------------------------------------------------------
def GetTeamRecord(fields, game_data):
    team_data = {}
    for g in game_data:
        team = g['TEAM']
        if team not in team_data:
            team_data[team] = {}
            for field in fields[2:]:
                team_data[team][field] = []
        for field in fields[2:]:
            team_data[team][field].append(g[field])
    #原始資料的順序是由新到舊，所以我們把數據順序反過來
    for t in team_data:
        for f in team_data[t]:
            team_data[t][f] = team_data[t][f][::-1]
    return team_data

def mean(vals):
    if len(vals)>0:
        return sum(vals)/len(vals)
    else:
        return 0

plt.rc('font', family='Microsoft JhengHei')

fields, game_data = ReadDataFromFile('NBA Boxscores 2019-22.xlsx', '2021-2022例行賽')
team_data = GetTeamRecord(fields, game_data)

N = len(game_data)//2
metric = 'AST'
win = [0]*N
lose = [0]*N

for row in game_data:
    i = row['場次'] #第幾場比賽
    if row['W/L'] == 'W':
        win[i-1] = row[metric]
    else:
        lose[i-1] = row[metric]

plt.figure(figsize=(6, 6))
plt.plot([10, 40], [10, 40], color='gray') #畫對角線
plt.plot(win, lose, 'o') #以勝隊數值為 x 值，敗隊數值為 y 值
plt.xlabel('勝隊數值')
plt.ylabel('敗隊數值')
plt.title('NBA 2021-2022 勝負隊 ' + metric + ' 數據')
plt.savefig(f'NBA 2021-2022 勝負隊 {metric} 數據.png')
plt.show()