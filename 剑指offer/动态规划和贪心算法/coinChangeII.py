class Solution:
    def coinChange(self, coins, target):
        """
        type:coins: list[int]]
        type:target: int
        rtype: int
        """
        # n = len(coins)
        # 1. dp 定义
        # dp[i] 为得到 target== i 时所用的硬币组合数

        # 2. dp 初始化
        dp = [0 for i in range(target + 1)]
        dp[0] = 1 
        #如果刚好有硬币使得 i - k == 0,组合数加1  

        # 3. dp 递推
        for k in coins:
            for i in range(k, target):
                # 每当使用一枚值为k的硬币，可以增加的组合数为dp[i-k]
                dp[i] += dp[i - k]
        # 4. dp 优化

        return dp[target]