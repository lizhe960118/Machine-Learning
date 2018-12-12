import KNN
from numpy import *
import os

hwLabels = []
trainingFileList = os.listdir("trainingDigits")
m = len(trainingFileList)
trainingMat = zeros((m, 1024))
for i in range(m):
    fileNameStr = trainingFileList[i]
    fileStr = fileNameStr.split('.')[0]
    classNumStr = int(fileStr.split('_')[0]) #找出分类的数字
    hwLabels.append(classNumStr)
    trainingMat[i:] = KNN.img2vector('trainingDigits/%s' % fileNameStr)#第i行

testFileList = os.listdir("testDigits")
errorCount = 0.0
mTest = len(testFileList)
for i in range(mTest):
    fileNameStr = testFileList[i]
    fileStr = fileNameStr.split('.')[0]
    classNumStr = int(fileStr.split('_')[0]) #找出分类的数字
    vectorUnderTest = KNN.img2vector('testDigits/%s' % fileNameStr) #打开文件注意
    classifierResult = KNN.classify0(vectorUnderTest, trainingMat, hwLabels, 3)
    if classifierResult != classNumStr:
        errorCount += 1.0

print("the total classify error num is %d" % errorCount)
print("the total classify error rate is %f" % (errorCount / float(mTest)))
