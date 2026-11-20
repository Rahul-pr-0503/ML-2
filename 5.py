from minisom import MiniSom
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
iris = load_iris()
X = MinMaxScaler().fit_transform(iris.data)
som = MiniSom(
    x=7,
    y=7,
    input_len=4,
    sigma=1.0,
    learning_rate=0.5,
    random_seed=42,
)
som.random_weights_init(X)
som.train_random(X, 100)
plt.figure(figsize=(7, 7))
for i, x in enumerate(X):
    w = som.winner(x)
    plt.text(
        w[0],
        w[1],
        str(iris.target[i]),
        color=plt.cm.rainbow(iris.target[i] / 2),
        fontdict={"weight": "bold", "size": 11},
    )
plt.show()