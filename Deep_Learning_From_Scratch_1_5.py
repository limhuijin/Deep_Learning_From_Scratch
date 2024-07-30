import numpy as np

x = np.array([1.0, 2.0, 3.0]) # 넘파이 배열 생성
print(x)                      # 배열 출력
type(x) 

x = np.array([1.0, 2.0, 3.0]) 
y = np.array([2.0, 4.0, 6.0]) 
print(x + y)
print(x - y)
print(x * y)
print(x / y)

A = np.array([[1, 2], [3, 4]])
print(A)
print(A.shape)

A = np.array([[1, 2], [3, 4]])
B = np.array([[3, 0], [0, 6]])
print(A + B)

A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
print(A * B)

X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
print(X[0])
print(X[0][1])

X = X.flatten()         # 1차원 배열로 변환
print(X)

print(X[np.array([0, 2, 4])])  # X 배열의 0, 2, 4 인덱스의 원소 얻기
print(X [X > 15])       # 15이상인 값만 출력하기
