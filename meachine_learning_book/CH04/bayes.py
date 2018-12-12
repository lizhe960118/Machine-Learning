# bayes.py
from numpy import *


def loadDataSet():
    postringList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                    ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                    ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                    ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                    ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                    ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]
    return postringList, classVec


def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
        # 对于所有的document求并集
    return list(vocabSet)


def setOfWord2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:  # 如果词在词典中，将该位置置为1
            returnVec[vocabList.index(word)] = 1
        else:
            print('the word:%s is not in my Vocabulary' % word)
    return returnVec


def trainNB0(trainMatrix, trainCategory):
    # 输入为文档矩阵trainMatrix，每篇文档类别标签所构成的向量trainCategory
    numTrainDocs = len(trainMatrix)  # 有多少篇文档
    numWords = len(trainMatrix[0])  # 有多少个词
    pAbusive = sum(trainCategory) / float(numTrainDocs)  # 标签和除以总的文档数，即侮辱性文档的个数
    # p0Num = zeros(numWords)#初始化分子为0【0,0，。。。0】，词数目个0
    # p1Num = zeros(numWords)
    # p0Denom = 0.0
    # p1Denom = 0.0
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):  # 对于每篇文档
        if trainCategory[i] == 1:  # 如果为侮辱性文档
            p1Num += trainMatrix[i]  # 分子为第i篇文档向量相加
            p1Denom += sum(trainMatrix[i])  # 分母为第i篇文档的含词数相加
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    # p1Vect = p1Num/p1Denom
    # p0Vect = p0Num/p0Denom
    p1Vect = log(p1Num / p1Denom)
    p0Vect = log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vect, p1Vect, pClass1):
    p1 = sum(vec2Classify * p1Vect) + log(pClass1)
    p0 = sum(vec2Classify * p0Vect) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():
    list0Posts, listClasses = loadDataSet()
    myVocabList = createVocabList(list0Posts)
    trainMat = []
    for postinDoc in list0Posts:
        trainMat.append(setOfWord2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWord2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as:', classifyNB(thisDoc, p0V, p1V, pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWord2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as:', classifyNB(thisDoc, p0V, p1V, pAb))


def bagOfWord2VecMN(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:  # 如果词在词典中，将该位置加1
            returnVec[vocabList.index(word)] += 1
        else:
            print('the word:%s is not in my Vocabulary' % word)
    return returnVec


def textParse(bigString):
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(listOfTokens) > 0]


def spamText():
    docList = []
    classList = []
    fullText = []
    for i in range(1, 26):
        wordList = textParse(str(open('C://Users/lizhe/Desktop/CH04/email/spam/%d.txt' % i).read))
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(str(open('email/ham/%d.txt' % i).read))
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    trainingSet = list(range(50))
    testSet = []
    for i in range(10):  # 取总数据集的数据构成测试集
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWord2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = setOfWord2Vec(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V,
                      pSpam) != classList[docIndex]:
            errorCount += 1
    print('the error rate is:', float(errorCount) / len(testSet))
