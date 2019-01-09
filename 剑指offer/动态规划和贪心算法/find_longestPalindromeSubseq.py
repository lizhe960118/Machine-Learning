class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 最长回文子序列
        # bbbab 返回4

        # 1. dp定义
        # 定义dp[i][j]为子串s[i:j]中包含的最长回文子串的长度
        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n)]

        # 2.dp初始化 
        # dp[i][i] = 1
        for i in range(n):
            dp[i][i] = 1

        # 3.dp递推
        for j in range(1, n):
            for i in range(j-1, -1, -1): #注意递推顺序
                if s[i] == s[j]:
                    # 此时结果为子串s[i+1:j-1]中包含的最长回文子串的长度加2
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][n-1]