class Solution:
    def maxValue_backpack(self, weights, values, capacity):
        """
        :type weights: List[]
        :type values: List[]
        :type capacity: int
        :rtype: int
        """
        # 在n个重量、价值分别为w_i，v_i的物品中选出总重量不超过capacity的物品，使其总价值最大
        n = len(weights)

        # dp定义
        # dp[i][j] 为从 前i个物品中选取总重量不超过j时 可能得到的最大价值
        # dp[i][j] 表示选i个物品，剩下容量为j时，能得到的最大值
        # i,j 从1开始有意义

        # dp 初始化
        dp = [[0 for j in range(capacity + 1)] for i in range(n+1)]
        # 不要求恰好装满，全部初始化为0即可

        # dp递推/边界条件
        for i in range(1, n+1):
            for j in range(0, capacity + 1):
                    if weights[i-1] > j:#当物品i重量超过j，不能放入，只能选取前面i-1件
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = max(dp[i-1][j],#第i件不选取
                            dp[i-1][j-weights[i-1]] + values[i-1])#第i件选取，可用空间缩减weights[i],价值增加values[i]
        return dp[n][capacity]

# 优化为1维数组
# class Solution:
    def maxValue_backpack_01(self, weights, values, capacity):
        n = len(weights)
        # dp定义：总重量不超过j时的最大价值
        dp = [0 for j in range(capacity + 1)]

        for i in range(n):
            for j in range(capacity, weights[i] - 1, -1): # 递推方向发生变化
                dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

        return dp[capacity]

if __name__ == '__main__':
    print(Solution().maxValue_backpack_01([2, 3, 4, 5, 9], [3, 4, 5, 8, 10], 20))