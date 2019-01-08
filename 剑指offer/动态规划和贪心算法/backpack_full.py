class Solution:
    def maxValue_backpack_full(self, weights, values, capacity):
        """
        :type weights: List[]
        :type values: List[]
        :type capacity: int
        :rtype: int
        """
        # 在价值分别为w_i，v_i的物品，每个物品可以取任意件，
        # 选出总重量恰好为capacity的物品，使其总价值最大
        n = len(weights)

        # dp定义
        # dp[i][j] 为从 前i个物品中选取总重量为j时 可能得到的最大价值

        # dp 初始化
        dp = [[float(inf) for j in range(capacity + 1)] for i in range(n+1)]
        # 要求恰好装满，初始化为inf即可
        for i in range(n+1):
            dp[i][0] = 0
        # 满足总重量为0，可以得到的最大价值也为0

        # for j in range(1, capacity + 1):
        #     dp[0][j] = 0
        # 没有取物品时，不能取到总重量为j的物品

        # dp递推/边界条件
        for i in range(1, n+1):
            for j in range(0, capacity + 1):
                for k in range(j // weights[i-1]):
                    dp[i][j] = max(dp[i-1][j - k * weights[i-1]] + k * values[i-1])#第i件选取，可用空间缩减weights[i],价值增加values[i]
        
        return dp[n][capacity]

    def maxValue_backpack_full(self, weights, values, capacity):
        n = len(weights)
        dp = [[float(inf) for j in range(capacity + 1)] for i in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0

        for i in range(1, n): 
            for j in range(0, capacity + 1):
                if weights[i - 1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j - weights[i-1]] + values[i-1]) 
                    # dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i-1]] + values[i-1]) 01背包问题

        return dp[n][capacity] if dp[n][capacity] != float(inf) else 'No'