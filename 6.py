import numpy as np
def f(x):
    return x**2
N = 10000
samples = np.random.rand(N)
values = f(samples)
estimate = np.mean(values)
print("Estimated Integral of x^2 from 0 to 1:", estimate)