def find_middle(list1, list2):
    # nlog(n)解法
    n = len(list1)
    m = len(list2)
    for i in range(m):
        list1.append(list2[i])
    list1.sort()
    return list1[(m+n) // 2]

def find_middle(list1, list2):
    # n解法
    n = len(list1)
    m = len(list2)
    i = 0
    j = 0
    count = 0
    middle = (m+n)//2
    while(i < n and j < m):
        if list1[i] < list2[j]:
            i += 1
            if (i + j == middle):
                return list1[i]
        else:
            j += 1
            if (i + j == middle):
                return list2[j]
    if (i == n-1):
        while(i + j < middle):
            j += 1
        return list2[j]
    if (j == m - 1):
        while (i + j < middle):
            i += 1
        return list1[i]


def find_middle(list1, list2):
    # log(n)解法
    n = len(list1)
    m = len(list2)
    if n == 0 and m == 0:
        return None
    if n == 1:
        if m == 1:
            return list1[0] if list1[0] < list2[0] else list2[0]
        else:
            # if m % 2 == 0:
            if list1[0] < list2[m // 2 - 1]:
                return list2[m//2 - 1]
            elif list1[0] > list2[m // 2]:
                return list2[m//2]
            else:
                return list1[0]
            # else:
            #     if list1[0] < list2[m //2 - 1]:
            #         return list2[m//2 - 1]
            #     elif list1[0] > list2[m //2 ]:
            #         return list2[m//2]
            #     else:
            #         return list1[0]
    if m == 1:
        if list2[0] < list1[n // 2 - 1]: 
            return list1[n // 2 - 1]
        elif list2[0] > list2[n // 2]:
            return list1[n // 2]
        else:
            return list2[0]
    
    middle1 = list1[n//2]
    middle2 = list2[m//2]
    if middle1 < middle2:
        find_middle(list1[n//2:n], list2[0:m//2])
    else:
        find_middle(list1[0:n//2], list2[m//2:m])

def minDistance(word1, word2):
    n = len(word1)
    m = len(word2)
    # dp定义
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    # dp初始化
    for j in range(m+1):
        dp[0][j] = j
    for i in range(1, n+1):
        dp[i][0] = i
    # 递推
    for i in range(1, n+1):
        for j in range(1, m+1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + 1

    return dp[n][m]

# dp优化
def minDistance(word1, word2):
    n = len(word1)
    m = len(word2)
    # dp定义
    # dp[i]是word1[:i]转换为word2[:j]的操作次数
    dp = [0 for _ in range(n+1)]
    # dp初始化
    # j = 0
    for i in range(n+1):
        dp[i] = i
    # 递推
    for j in range(1, m+1):
        pre = dp[0]
        # 初始化dp[0]
        dp[0] = j

        for i in range(1, n+1):
            tmp = dp[i]
            if word1[i] == word2[j]:
                dp[i] = pre 
            else:
                dp[i] = min(pre, dp[i], dp[i-1]) + 1
            pre = tmp

    return dp[n]