import numpy as np
import matplotlib.pylab as plt

def step_function(x): #계단 함수
    # if x > 0:
    #     return 1
    # else:
    #     return 0
    return np.array(x > 0, dtype=np.int64)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()

def sigmoid(x): #시그모이드 함수
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()

def relu(x):
    return np.maximum(0, x)


