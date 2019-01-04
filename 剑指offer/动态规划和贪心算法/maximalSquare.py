class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #动态规划
        #if matrix[i][j] == 1:
        #   dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        #if matrix[i][j] == 0:
        #   dp[i][j] = 0
        n = len(matrix)
        result = 0
        if n <= 0:
            return result
        m = len(matrix[0])
        if m <= 0:
            return result
        dp = [[0 for j in range(m)] for i in range(n)]
        print(dp)
        for j in range(m):
            if matrix[0][j] == "1":
                dp[0][j] = 1
                result = max(dp[0][j], result)
            else:
                dp[0][j] = 0
        for i in range(1,n):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                result = max(dp[i][0], result)
            else:
                dp[i][0] = 0
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    result = max(dp[i][j], result)
                    print(result)
                else:
                    dp[i][j] = 0
        return result * result