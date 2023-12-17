from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

df = pd.read_csv('test_data.csv', encoding='utf-8')
df = df.drop(['PLAYER', 'POSITION', 'TEAM', 'AB/HR', 'BB/K'], axis=1)

y = df['RANK']
x = df.drop(['RANK'], axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=101)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

rf_model = RandomForestClassifier()
rf_model.fit(x_train, y_train)