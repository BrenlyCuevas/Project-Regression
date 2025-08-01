# import libraries
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression

# Creating Dataset
X, y = make_regression(n_features=4, n_informative=2,
                       random_state=0, shuffle=False)

# Creating and validating model
regr = RandomForestRegressor(max_depth=2, random_state=0)
regr.fit(X, y)
print(regr.predict([[0, 0, 0, 0]]))
