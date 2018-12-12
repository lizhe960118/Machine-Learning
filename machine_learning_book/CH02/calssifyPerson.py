import KNN
from numpy import *

resultList = ['not at all', 'in small doses', 'in large doses']
percentTats = float(input("percentage of time spent playing video games?"))
ffMiles = float(input("frequent flier miles earned per year?"))
iceCream = float(input("liters of ice cream consumed every year?"))
datingDataMat, datingLabels = KNN.file2matrix('datingTestSet2.txt')
normMat, ranges, minValue = KNN.autoNorm(datingDataMat)
inArr = array([ffMiles, percentTats, iceCream])
classifierResult = KNN.classify0(inArr, datingDataMat, datingLabels, 3)
print("You will probably like this person ", resultList[classifierResult - 1])
