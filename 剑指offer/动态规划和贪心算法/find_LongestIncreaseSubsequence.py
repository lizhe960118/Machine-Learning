class Solution:
    def find_LongestIncreaseSequence(self, nums):
        """
        type:nums：list
        rtype: int
        """
        n = len(nums)

        # 1. dp 定义
        # dp[i] 为nums[i]对应能得到的最长递增子序列

        # 2. dp 初始化
        dp = [1 for i in range(n)]

        res = 0
        # 3. dp 递推
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    #当前数比nums[j],可构成的最大递增子序列长度对j而言为dp[j]加1，这里我们要取小于nums[i]的最大j
                    # dp[i] 应该等于 max{dp[j]} 对应的那个 dp[j] + 1，且只增加一次， 前提是nums[j] < nums[i]
                    dp[i] = dp[j] + 1

            res = max(res, dp[i])

        return res