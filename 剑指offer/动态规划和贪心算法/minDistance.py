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