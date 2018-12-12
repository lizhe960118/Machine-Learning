from numpy import *
import numpy as np

def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open("testSet.txt")
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append([float(lineArr[2])])
    return dataMat, labelMat


def selectJrand(i, m):
    j = i
    while j == i:
        j = int(random.uniform(0, m))  # 直到j 不等于 i
    return j


def clipAlpha(aj, H, L):  # 调整大于H或者小于L的alpha值
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj


def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels)
    b = 0
    m, n = shape(dataMatrix)
    alphas = np.asmatrix(zeros([m, 1]))
	#alphas = mat(alphas)
    iter = 0
    while iter < maxIter:
        alphaPairsChanged = 0
        for i in range(m):
            fXi = float(multiply(alphas, labelMat).T *
                        (dataMatrix * dataMatrix[i, :].T)) + b
            Ei = fXi - float(labelMat[i])
            if ((labelMat[i] * Ei < -toler) and (alphas[i] < C)
                ) or ((labelMat[i] * Ei > toler) and (alphas[i] > 0)):
                j = selectJrand(i, m)
                fXj = float(multiply(alphas, labelMat).T *
                            (dataMatrix * dataMatrix[j, :].T)) + b
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                if labelMat[i] != labelMat[j]:
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L == H:
                    print("L == H")
                    continue
                eta = float(2.0 * dataMatrix[i,
                                       :] * dataMatrix[j,
                                                       :].T - dataMatrix[i,
                                                                         :] * dataMatrix[i,
                                                                                         :].T - dataMatrix[j,
                                                                                                           :] * dataMatrix[j,
                                                                                                                           :].T)
                if eta >= 0:
                    print("eta >= 0")
                    continue
                alphas[j] -= labelMat[j] * (Ei - Ej) / eta
                alphas[j] = clipAlpha(alphas[j], H, L)
                if abs(alphas[j] - alphaJold) < 0.00001:
                    print("j not moving enough")
                    continue
                alphas[i] += labelMat[j] * labelMat[i] * (alphaJold - alphas[j])
                b1 = b - Ei - labelMat[i] * (alphas[i] - alphaIold) * dataMatrix[i,
                                                                                 :] * dataMatrix[i,
                                                                                                 :].T - labelMat[j] * (alphas[j] - alphaJold) * dataMatrix[i,
                                                                                                                                                           :] * dataMatrix[j,
                                                                                                                                                                           :].T
                b2 = b - Ej - labelMat[i] * (alphas[i] - alphaIold) * dataMatrix[i,
                                                                                 :] * dataMatrix[i,
                                                                                                 :].T - labelMat[j] * (alphas[j] - alphaJold) * dataMatrix[i,
                                                                                                                                                           :] * dataMatrix[j,
                                                                                                                                                                           :].T
                if(0 < alphas[i]) and (C > alphas[i]):
                    b = b1
                elif(0 < alphas[j]) and (C > alphas[j]):
                    b = b2
                else:
                    b = (b1 + b2) / 2.0
                alphaPairsChanged += 1
                print(
                "iter: %d i:%d,pairs changed %d" %
                (iter, i, alphaPairsChanged))
            if alphaPairsChanged == 0:
                iter += 1
            else:
                iter = 0
            print("iteration number : %d" % iter)
    return b, alphas

if __name__ == "__main__":
    dataArr, labelArr = loadDataSet()
    print(dataArr)
    print(shape(dataArr))
    print(labelArr)
    print(shape(labelArr))
    b, alphas = smoSimple(dataArr, labelArr, 0.6, 0.001, 40)
    print(b)
    print(alphas[alphas > 0])
    print(shape(alphas[alphas > 0]))