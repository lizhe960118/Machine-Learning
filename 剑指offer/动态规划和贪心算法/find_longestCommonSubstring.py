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

        res = 0
        # 3. dp 递推
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    # 当前字符相等时，在dp[i-1][j-1]的基础上加1
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # 当前字符串不相等，即最后一位不相等，不构成公共字串
                    dp[i][j] = 0
                res = max(res, dp[i][j])

        return res

    # 4. dp 优化: 一维dp, 空间复杂度 O(n)
    def find_LongestCommonSequence_1(self, s1, s2):
        """
        type:s1:string
        type:s2:string
        rtype: int
        """
        n = len(s1)
        m = len(s2)

        # 保证m不小于n
        if m < n:
            s1, s2 = s2, s1
            m, n = n, m

        # 1. dp 定义
        # dp[j] 是字符串前缀s1[:i]与字符串s2[:j]得到的最长公共子串长度，只是这里我们遍历i

        # 2. dp 初始化
        dp = [0 for j in range(m)]

        res = 0
        # 3. dp 递推
        for i in range(n):
            for j in range(m, -1， -1):
                # 由于dp[j] 有dp[j-1]递推得到，所以反向遍历
                if s1[i] == s2[j]:
                    if i == 0 or j == 0:
                        dp[j] = 1
                    else:
                        # 当前字符相等时，在dp[i-1][j-1]的基础上加1
                        dp[j] = dp[j-1] + 1
                else:
                    # 当前字符串不相等，即最后一位不相等，不构成公共字串
                    dp[j] = 0
                res = max(res, dp[j])
        return res

    # 4. dp 优化: 斜向遍历, 空间复杂度 O(1)
    def find_LongestCommonSequence_2(self, s1, s2):
        """
        type:s1:string
        type:s2:string
        rtype: int
        """
        n = len(s1)
        m = len(s2)

        res = 0

        # for col in range(m-1, -1, -1):
        #     dp = 0
        #     i = 0
        #     j = col
        #     while(i < n and j < m):
        #         if s1[i] == s2[j]:
        #             dp += 1
        #         else:
        #             dp = 0
        #         i += 1
        #         j += 1
        #     res = max(res, dp)

        # for row in range(1, n):
        #     dp = 0
        #     i = row
        #     j = 0
        #     while(i < n and j < m):
        #         if s1[i] == s2[j]:
        #             dp += 1
        #         else:
        #             dp = 0
        #         i += 1
        #         j += 1
        #     res = max(res, dp)

        row = 0
        col = m - 1

        while(row < n):
            
            dp = 0
            i = row
            j = col

            while(i < n and j < m):
                if s1[i] == s2[j]:
                    dp += 1
                else:
                    dp = 0
                i += 1
                j += 1

            res = max(res, dp)

            if col > 0:
                col -= 1
            else:
                row += 1

        return res