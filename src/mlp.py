from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

from src.utils.load_data import load_data

X, y = load_data()
X_train, X_test, y_train, y_test = train_test_split(X, y)
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

clf.fit(X_train, y_train)

training_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)

print("training set score: %f" % training_score)
print("test set score: %f" % test_score)

"""
training set score: 0.948538
test set score: 0.684211
"""