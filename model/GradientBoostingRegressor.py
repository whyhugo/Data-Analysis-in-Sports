import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from scipy import stats

data = pd.read_csv(r'D:\programing\swiftx\NTNU\Data Analysis in Sports\mlb_stats\data_filter.csv')

X = data.drop('RANK', axis=1)
y = data['RANK']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=50)

gb_regressor = GradientBoostingRegressor(random_state=50)

param_grid = {
    'n_estimators': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],
    'learning_rate': [0.05, 0.1, 0.2, 0.3, 0.4, 0.5],
    'max_depth': [2, 3, 4, 5, 6]
}

grid_search = GridSearchCV(estimator=gb_regressor, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)

grid_search.fit(X_train, y_train)

##
cv_results = pd.DataFrame(grid_search.cv_results_)
plt.figure(figsize=(12, 6))

for learning_rate in param_grid['learning_rate']:
    mask = (cv_results['param_learning_rate'] == learning_rate)
    plt.plot(cv_results['param_n_estimators'][mask], -cv_results['mean_test_score'][mask], label=f'learning_rate={learning_rate}')

plt.xlabel('Number of Estimators')
plt.ylabel('Negative Mean Squared Error')
plt.legend(title='Learning Rate')
plt.title('Grid Search Results')
plt.show()
##

best_params = grid_search.best_params_
print(f'Best Parameters: {best_params}')

best_model = grid_search.best_estimator_
best_model.fit(X_train, y_train)

y_pred = best_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'Mean Absolute Error: {mae}')
print(f'R-squared: {r2}')

plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.title('Scatter Plot of True vs Predicted Values')
plt.xlabel('True Values')
plt.ylabel('Predicted Values')
plt.show()

residuals = y_test - y_pred
plt.figure(figsize=(10, 6))
sns.residplot(x=y_test, y=residuals, lowess=True, color='g')
plt.title('Residual Plot')
plt.xlabel('True Values')
plt.ylabel('Residuals')
plt.show()

plt.figure(figsize=(10, 6))
stats.probplot(residuals, dist="norm", plot=plt)
plt.title('Q-Q Plot of Residuals')
plt.show()

# 若要進一步調整模型參數，可以使用 GridSearchCV 進行交叉驗證和參數搜索
# from sklearn.model_selection import GridSearchCV
# param_grid = {'n_estimators': [50, 100, 150], 'learning_rate': [0.05, 0.1, 0.2], 'max_depth': [3, 4, 5]}
# grid_search = GridSearchCV(GradientBoostingRegressor(random_state=42), param_grid, cv=5)
# grid_search.fit(X_train, y_train)
# best_params = grid_search.best_params_
# best_model = grid_search.best_estimator_
# 在最佳參數下重新訓練模型並進行預測