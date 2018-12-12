# import matplotlib
import matplotlib.pyplot as plt
import KNN
from numpy import *

datingDataMat, datingLabels = KNN.file2matrix('datingTestSet2.txt')
# print(datingDataMat[0:100])
# print(datingLabels[0:20])

fig = plt.figure()
ax = fig.add_subplot(111)
'''
这些是编码为单个整数的子图网格参数。
例如，“111”表示“1×1 grid，first subplot”，“234”表示“2×3 grid，4th subplot”。
add_subplot(111)的替代形式是add_subplot(1, 1, 1)
'''
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 *
           array(datingLabels), 15.0 * array(datingLabels))  # 使用标签来决定所画图像的颜色和大小
plt.show()
