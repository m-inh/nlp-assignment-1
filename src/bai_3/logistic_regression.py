from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from src.load_data import load_data

X, y = load_data()
X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LogisticRegression(solver="lbfgs").fit(X_train, y_train)

training_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print("training set score: %f" % training_score)
print("test set score: %f" % test_score)

"""
training set score: 0.846784
test set score: 0.708772
"""