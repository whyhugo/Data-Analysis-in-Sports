import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_excel('NBA Boxscores 2019-22.xlsx', sheet_name='2021-2022例行賽')

team_list = []
for team in df1['TEAM'].unique():
    team_list.append(team)

#-------------------------------------好像應該用 fuction QAQ

count = 0
total = 0
temp_list = []
for i in team_list:
    avg_pts = []
    for j in range(len(df1)):
        if df1.iloc[j, 1] == i:
            total += df1.iloc[j, 6]
            count += 1
    avg_pts.append(i)
    avg_pts.append(total/count)
    temp_list.append(avg_pts)
df_pts = pd.DataFrame(temp_list, columns=['TEAM', 'PTS'])
df_pts['PTS'] = df_pts['PTS'].astype(float)
df_pts = df_pts.sort_values(by='PTS', ascending=False, ignore_index=True)
rank = [1]
for i in range(1, len(df_pts)):
    if df_pts.iloc[i, 1] < df_pts.iloc[i-1, 1]:
        rank.append(i+1)
    else:
        rank.append(rank[i-1])

df_pts['排名'] = rank

#-------------------------------------

count = 0
total = 0
temp_list = []
for i in team_list:
    avg_reb = []
    for j in range(len(df1)):
        if df1.iloc[j, 1] == i:
            total += df1.loc[j, 'REB']
            count += 1
    avg_reb.append(i)
    avg_reb.append(total/count)
    temp_list.append(avg_reb)
df_reb = pd.DataFrame(temp_list, columns=['TEAM', 'reb'])
df_reb['reb'] = df_reb['reb'].astype(float)
df_reb = df_reb.sort_values(by='reb', ascending=False, ignore_index=True)
rank = [1]
for i in range(1, len(df_reb)):
    if df_reb.iloc[i, 1] < df_reb.iloc[i-1, 1]:
        rank.append(i+1)
    else:
        rank.append(rank[i-1])

df_reb['排名'] = rank

#-------------------------------------

count = 0
total = 0
temp_list = []
for i in team_list:
    avg_ast = []
    for j in range(len(df1)):
        if df1.iloc[j, 1] == i:
            total += df1.loc[j, 'AST']
            count += 1
    avg_ast.append(i)
    avg_ast.append(total/count)
    temp_list.append(avg_ast)
df_ast = pd.DataFrame(temp_list, columns=['TEAM', 'ast'])
df_ast['ast'] = df_ast['ast'].astype(float)
df_ast = df_ast.sort_values(by='ast', ascending=False, ignore_index=True)
rank = [1]
for i in range(1, len(df_ast)):
    if df_ast.iloc[i, 1] < df_ast.iloc[i-1, 1]:
        rank.append(i+1)
    else:
        rank.append(rank[i-1])

df_ast['排名'] = rank

#-------------------------------------

count = 0
total = 0
temp_list = []
for i in team_list:
    avg_blk = []
    for j in range(len(df1)):
        if df1.iloc[j, 1] == i:
            total += df1.loc[j, 'BLK']
            count += 1
    avg_blk.append(i)
    avg_blk.append(total/count)
    temp_list.append(avg_blk)
df_blk = pd.DataFrame(temp_list, columns=['TEAM', 'blk'])
df_blk['blk'] = df_blk['blk'].astype(float)
df_blk = df_blk.sort_values(by='blk', ascending=False, ignore_index=True)
rank = [1]
for i in range(1, len(df_blk)):
    if df_blk.iloc[i, 1] < df_blk.iloc[i-1, 1]:
        rank.append(i+1)
    else:
        rank.append(rank[i-1])

df_blk['排名'] = rank

#-------------------------------------

count = 0
total = 0
temp_list = []
for i in team_list:
    avg_stl = []
    for j in range(len(df1)):
        if df1.iloc[j, 1] == i:
            total += df1.loc[j, 'STL']
            count += 1
    avg_stl.append(i)
    avg_stl.append(total/count)
    temp_list.append(avg_stl)
df_stl = pd.DataFrame(temp_list, columns=['TEAM', 'stl'])
df_stl['stl'] = df_stl['stl'].astype(float)
df_stl = df_stl.sort_values(by='stl', ascending=False, ignore_index=True)
rank = [1]
for i in range(1, len(df_stl)):
    if df_stl.iloc[i, 1] < df_stl.iloc[i-1, 1]:
        rank.append(i+1)
    else:
        rank.append(rank[i-1])

df_stl['排名'] = rank

#-------------------------------------

rank_list = []
datatype = []
data = []

for i in range(len(df_pts)):
    if df_pts.loc[i, 'TEAM'] == 'POR':
        rank_list.append(df_pts.loc[i, '排名'])
        datatype.append('PTS')
        data.append(df_pts.loc[i, 'PTS']/df_pts['PTS'].mean()*100)
    elif df_reb.loc[i, 'TEAM'] == 'POR':
        rank_list.append(df_reb.loc[i, '排名'])
        datatype.append('REB')
        data.append(df_reb.loc[i, 'reb']/df_reb['reb'].mean()*100)
    elif df_ast.loc[i, 'TEAM'] == 'POR':
        rank_list.append(df_ast.loc[i, '排名'])
        datatype.append('AST')
        data.append(df_ast.loc[i, 'ast']/df_ast['ast'].mean()*100)
    elif df_blk.loc[i, 'TEAM'] == 'POR':
        rank_list.append(df_blk.loc[i, '排名'])
        datatype.append('BLK')
        data.append(df_blk.loc[i, 'blk']/df_blk['blk'].mean()*100)
    elif df_stl.loc[i, 'TEAM'] == 'POR':
        rank_list.append(df_stl.loc[i, '排名'])
        datatype.append('STL')
        data.append(df_stl.loc[i, 'stl']/df_stl['stl'].mean()*100)

#-------------------------------------

plt.rc('font', family='Microsoft JhengHei')
fig, ax = plt.subplots(figsize=(8, 6.5))

ax.bar(datatype, data)
ax.set_ylabel('相對聯盟平均值 %')
ax.set_title('NBA 2021-2022 POR 數據 vs. 聯盟平均')
for i, (value, r) in enumerate(zip(data, rank_list)):
    ax.text(i, value + -0.1, str(r), ha='center', va='bottom')
plt.show()