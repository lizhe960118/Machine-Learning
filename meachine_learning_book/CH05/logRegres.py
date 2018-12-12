from numpy import *


def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        # 前两行值为X1，X2，并将X0设为1.0
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat


def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))


def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)  # 2维numpy数组，每行表示训练样本，每列表示不同特征
    labelMat = mat(classLabels).transpose()  # 将1*100行向量转置为100*1的列向量
    m, n = shape(dataMatrix)  # 得到矩阵大小 m= 100，n= 3
    alpha = 0.001
    maxCycles = 500
    weights = ones((n, 1))  # 返回Array
    for k in range(maxCycles):  # 进行500次循环
        h = sigmoid(dataMatrix * weights)  # h为列向量 100*1
        error = (labelMat - h)
        weights += alpha * dataMatrix.transpose() * error  # 3*100 * 100*1
    return weights


def plotBestFit(wei):
    import matplotlib.pyplot as plt
    #weights = wei.getA()
    weights = wei
    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


def stocGradAscent0(dataMartix, classLabels):
    m, n = shape(dataMartix)  # 100*3
    alpha = 0.01
    weights = ones(n)
    for i in range(m):  # 0到100
        h = sigmoid(sum(dataMartix[i] * weights))  # 1*3 3*1
        error = classLabels[i] - h  # 1
        weights += alpha * error * dataMartix[i]  # 1*1 1*3
    return weights


def stocGradAscent1(dataMartix, classLabels, numIter=150):
    m, n = shape(dataMartix)
    weights = ones(n)
    for j in range(numIter):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4 / (1.0 + j + i) + 0.01
            randIndex = int(random.uniform(0, len(dataIndex)))
            h = sigmoid(sum(dataMartix[randIndex] * weights))
            error = classLabels[randIndex] - h
            weights += alpha * error * dataMartix[randIndex]  # 1*1 1*3
            del(dataIndex[randIndex])
    return weights
