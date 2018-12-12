from numpy import *
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    # .shape[0]表示dataSet有多少行，.shape[1]表示dataSet有多少列
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet  # '''行重复dataSet次，列为一列'''
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)  # '''axis=1表示按行相加，axis=2表示按列相加'''
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()  # '''返回数组值从小到大的索引值'''
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(
            voteIlabel, 0) + 1  # '''字典中查找voteIlabel,当不存在时返回默认值0'''
    sortedClassCount = sorted(
        classCount.items(),
        key=operator.itemgetter(1),
        reverse=True)  # '''从大到小排序'''
    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numbersOfLines = len(arrayOLines)  # 得到文件行数
    returnMat = zeros((numbersOfLines, 3))  # 1000行3列的0矩阵
    classLabelVector = []  # 分类矩阵
    index = 0
    for line in arrayOLines:
        line = line.strip()  # 截取掉所有的回车符
        listFromLine = line.split('\t')  # 将整行数据分割成元素表
        returnMat[index, :] = listFromLine[0:3]  # 获取每行数据的前3列，返回到矩阵的第一行
        classLabelVector.append(int(listFromLine[-1]))  # 获取每行数据的最后的一列，返回到分类矩阵
        index += 1  # 计算下一行
    return returnMat, classLabelVector


def autoNorm(dataSet):
    minValue = dataSet.min(0)
    maxValue = dataSet.max(0)
    ranges = maxValue - minValue
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]  # 获得dataSet的行数
    normDataSet = dataSet - tile(minValue, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minValue

def img2vector(filename):
    returnVect = zeros((1, 1024))#一行1024列的向量
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
           returnVect[0, 32 * i + j] = int(lineStr[j])
            # returnVect[1, 32 * i + j] = int(lineStr[j])
    return returnVect
