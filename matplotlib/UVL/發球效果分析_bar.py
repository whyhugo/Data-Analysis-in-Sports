from matplotlib import pyplot as plt
from collections import Counter

results1 = []
results = []
for i in range(1, 4):
    oneset = []
    filename = 'UVL108-EX2-Champion-Set'+str(i)+'.txt'
    with open(filename) as f:
        data = f.readlines()
    for row in data:
        hits = row.split()
        results1.append(hits[0])
        if hits[0][0] == hits[-1][0] and row.count(hits[0][0])==2:
            results.append(hits[0])

sc_cnt = Counter(results)
players = []
serves = []
colors = []
for e in sc_cnt.most_common():
    print('球員', e[0], '發球得分', e[1], '次')
    players.append(e[0])
    serves.append(e[1])
    if e[0][0] == 'A':
        colors.append('#00B2FF')
    else:
        colors.append('#FFCA16')

cnt = Counter(results1)
players1 = []
serves1 = []
colors1 = []
for e in cnt.most_common():
    print('球員', e[0], '發球', e[1], '次')
    players1.append(e[0])
    serves1.append(e[1])
    if e[0][0] == 'A':
        colors1.append('blue')
    else:
        colors1.append('orange')

players_ = []
serves_ = []
colors_ = []
for i in players1:
  if i in players:
    for j in range(len(serves)):
      if players[j] == i:
        serves_.append(serves[j])
        colors_.append(colors[j])
        break
  else:
    serves_.append(0)
    colors_.append('white')

for i in range(len(serves_)):
  serves1[i] -= serves_[i]
print(serves_)

plt.bar(players1, serves1, color=colors1)
plt.bar(players1, serves_, color=colors_, bottom=serves1)

plt.show()