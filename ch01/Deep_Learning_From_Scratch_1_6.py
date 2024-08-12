import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

x = np.arange(0, 6, 0.1) # 0에서 6까지 0.1 간격으로 생성
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle='--', label="cos") # cos 함수는 점선으로 그리기
plt.xlabel("x") # x축 이름
plt.ylabel("y") # y축 이름
plt.title('sin & cos') # 제목
plt.legend()
plt.show()

img = imread('C:/Users/user/Desktop/coding/Deep_Learning_From_Scratch/고양이.jpg')

plt.imshow(img)
plt.show()