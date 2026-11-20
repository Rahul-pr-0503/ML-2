from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from wittgenstein import RIPPER
iris = load_iris()
X = iris.data
y = (iris.target == 2).astype(int)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
model = RIPPER(random_state=42)
model.fit(X_train, y_train, pos_class=1)
print("Generated Rules:\n", model.ruleset_)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))