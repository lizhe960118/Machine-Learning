import KNN
from numpy import *

datingDataMat, datingLabels = KNN.file2matrix('datingTestSet2.txt')
normMat, ranges, minValue = KNN.autoNorm(datingDataMat)
print(normMat)
print(ranges)
print(minValue)