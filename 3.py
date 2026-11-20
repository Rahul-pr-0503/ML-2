from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
wine = load_wine()
X, y = wine.data, wine.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=50,
    random_state=42,
)
bagging.fit(X_train, y_train)
bag_pred = bagging.predict(X_test)
boosting = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(max_depth=1),
    n_estimators=50,
    random_state=42,
)
boosting.fit(X_train, y_train)
boost_pred = boosting.predict(X_test)
print("Bagging Accuracy:", accuracy_score(y_test, bag_pred))
print("Boosting Accuracy:", accuracy_score(y_test, boost_pred))