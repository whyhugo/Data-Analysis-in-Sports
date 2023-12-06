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

metric = 'AST'
data = []
for tname in team_data:
    data.append([tname, mean(team_data[tname][metric])])

data.sort(key = lambda x: x[1], reverse = (metric not in ['TOV', 'PF']))

for e in data:
    print(e)

tnames = [e[0] for e in data]
values = [e[1] for e in data]

colors = []
for i in range(len(tnames)):
    if tnames[i] == 'WAS':
        colors.append('#15A782')
    else:
        colors.append('#89D12D')

plt.figure(figsize=(15, 5))
plt.bar(tnames, values, color=colors)
plt.title(f'NBA 2021-2022 例行賽: 平均 {metric}', fontsize=16)
plt.savefig(f'NBA 2021-2022 例行賽 - 平均 {metric}.png')
plt.show()
