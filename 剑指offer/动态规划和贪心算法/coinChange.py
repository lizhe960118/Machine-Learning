class Solution:
    def coinChange(self, coins, target):
        """
        type:coins: list[int]]
        type:target: int
        rtype: int
        """
        # n = len(coins)
        # 1. dp 定义
        # dp[i] 为得到 target== i 时所用的最小硬币个数

        # 2. dp 初始化
        dp = [float(inf) for i in range(target + 1)]
        dp[0] = 0
        #其他i, dp[i] = float(inf)

        # 3. dp 递推
        for k in coins:
            for i in range(k, target):
                # 每当使用一枚值为k的硬币，数量上只增加1
                dp[i] = min(dp[i], dp[i - k] + 1)
        # 4. dp 优化

        return dp[target] if dp[target] != float(inf) else 'No'