from matplotlib import pyplot as plt
from collections import Counter

results = []
for i in range(1, 4):
    filename = 'UVL108-EX2-Champion-Set'+str(i)+'.txt'
    with open(filename) as f:
        data = f.readlines()
    for row in data:
        hits = row.split()
        results.append(hits[0])

cnt = Counter(results)
players = []
serves = []
colors = []
for e in cnt.most_common():
    print('球員', e[0], '發球', e[1], '次')
    players.append(e[0])
    serves.append(e[1])
    if e[0][0] == 'A':
        colors.append('blue')
    else:
        colors.append('orange')

plt.bar(players, serves, color=colors)
plt.show()
