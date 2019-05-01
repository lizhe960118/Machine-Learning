import sys 

def check_right(arr):
    a = arr.copy()
    a.sort()

    for x in set(a):
        if a.count(x) > 4:#某张牌的数量超过了4，是不正确的。
            return False

    #是否有对子检查
    double=[]
    for x in set(a):
        if a.count(x)>=2:
            double.append(x)

    if len(double)==0:
        return False
    
    #常规和牌检测
    for x in double:
        a1 = a.copy()
        a1.remove(x)
        a1.remove(x)
        for i in range(int(len(a1)/3)):
            if a1.count(a1[0])==3:
                a1=a1[3:]
            elif (a1[0]) in a1 and (a1[0]+1) in a1 and (a1[0]+2) in a1:
                #这里注意，11,2222,33，和牌结果22,123,123，则连续的3个可能不是相邻的。
                a1.remove(a1[0]+2)
                a1.remove(a1[0]+1)
                a1.remove(a1[0])
        if len(a1) == 0:
            return True
    return False

if __name__ == "__main__":
    line = sys.stdin.readline().strip().split()
    arr_N = [int(a) for a in line]
    result = []
    for i in range(1, 10):
        arr_N.append(i)
        if check_right(arr_N):
            result.append(i)
        arr_N.pop()
    if len(result) != 0:
        for i in range(len(result)):
            print(result[i])
    else:
        print(0)