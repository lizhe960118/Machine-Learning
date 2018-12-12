import KNN
from numpy import *

hoRatio = 0.10
datingDataMat, datingLabels = KNN.file2matrix('datingTestSet2.txt')
normMat, ranges, minValue = KNN.autoNorm(datingDataMat)
m = normMat.shape[0]
numTestVecs = int(m * hoRatio) # 得到测试数据的个数
errorCount = 0.0
for i in range(numTestVecs):
    classifierResult = KNN.classify0(normMat[i, :], normMat[numTestVecs:m, ], datingLabels[numTestVecs:m], 3) # normMat[numTestVecs:m, ]用作训练
    print("the classifier come back with :%d ,the real answer is :%d " % (classifierResult, datingLabels[i]))
    if classifierResult != datingLabels[i]:
        errorCount += 1.0
print("the total error rate is : %f" % (errorCount / numTestVecs))

