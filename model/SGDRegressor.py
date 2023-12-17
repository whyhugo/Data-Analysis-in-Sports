import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import explained_variance_score

data = pd.read_csv(r'D:\programing\swiftx\NTNU\Data Analysis in Sports\mlb_stats\data.csv')

X = data.drop('RANK', axis=1)
y = data['RANK']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = SGDRegressor(max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)

predictions = model.predict(X_test_scaled)

mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')
mae = mean_absolute_error(y_test, predictions)
print(f'Mean Absolute Error: {mae}')
r2 = r2_score(y_test, predictions)
print(f'R^2 Score: {r2}')
evs = explained_variance_score(y_test, predictions)
print(f'Explained Variance Score: {evs}')
