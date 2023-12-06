from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('cpbl-player-batter-1990-2023.csv', encoding='big5')
plt.rc('font', family='Microsoft JhengHei')

def get_avg_ta(df):
    temp_total, temp_count, year = 0, 0, 1990
    ta_list = []
    for i in range(len(df)):
        if df.loc[i,'YEAR'] == year:
            temp_total += df.loc[i, 'TA']
            temp_count += 1
        else:
            year += 1
            ta_list.append(temp_total/temp_count)
            temp_total, temp_count = 0, 0
    ta_list.append(temp_total/temp_count)
    return ta_list

def get_avg_rbi(df):
    temp_total, temp_count, year = 0, 0, 1990
    rbi_list = []
    for i in range(len(df)):
        if df.loc[i,'YEAR'] == year:
            temp_total += df.loc[i, 'RBI']
            temp_count += 1
        else:
            year += 1
            rbi_list.append(temp_total/temp_count)
            temp_total, temp_count = 0, 0
    rbi_list.append(temp_total/temp_count)
    return rbi_list

def plt_show(rbi_list, ta_list):
    years = list(range(1990, 2024))

    fig, ax1 = plt.subplots(figsize=(15, 6))

    ax1.plot(years, rbi_list, label='平均打點數', marker='o', color='#FDAB02', linewidth=2)
    ax1.set_xlabel('年份')
    ax1.set_ylabel('打點數 (RBI)', color='black')
    ax1.tick_params('y', colors='black')

    ax2 = ax1.twinx()
    ax2.plot(years, ta_list, label='平均攻擊指數', marker='s', color='#00A2FD', linewidth=2)
    ax2.set_ylabel('攻擊指數 (TA)', color='black')
    ax2.tick_params('y', colors='black')

    plt.xticks(years[::3]) 

    plt.title('1990 年至 2023 年聯盟平均攻擊指數與平均打點數')

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    
    plt.grid(True)
    plt.show()

rbi = get_avg_rbi(df)
ta = get_avg_ta(df)
plt_show(rbi, ta)