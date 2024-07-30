def Default_AND(x1, x2):    #일반 AND 게이트
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
    
print(Default_AND(0, 0))
print(Default_AND(1, 0))
print(Default_AND(0, 1))
print(Default_AND(1, 1))

import numpy as np  #Numpy를 사용한 AND 게이트

x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7
print(w*x)
print(np.sum(w*x))
print(np.sum(w*x) + b)

def AND(x1, x2):    #가중치와 편향을 도입한 AND 게이트
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def NAND(x1, x2):   #가중치와 편향을 도입한 NAND 게이트
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def OR(x1, x2):     #가중치와 편향을 도입한 OR 게이트
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

XOR(0, 0)
XOR(1, 0)
XOR(0, 1)
XOR(1, 1)