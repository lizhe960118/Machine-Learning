class Solution:
    def find_LongestCommonSequence(self, s1, s2):
        """
        type:s1:string
        type:s2:string
        rtype: int
        """
        n = len(s1)
        m = len(s2)

        # 1. dp 定义
        # dp[i][j] 是字符串前缀s1[:i]与字符串s2[:j]得到的最长公共子串长度

        # 2. dp 初始化
        dp = [[0 for j in range(m + 1)] for i in range(n+1)]

        # 3. dp 递推
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    # 当前字符相等时，在dp[i-1][j-1]的基础上加1
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        # 4. dp 优化

        return dp[n][m]