class Solution:
    def powerEggs(self, N, M):
        """
        :type N: int (nums of eggs)
        :type M: int (levels of buliding) 
        : E :鸡蛋的硬度
        :rtype: int(in most terrible stuation, the min times using N eggs to decide in E in M levels bulidng)
        """
        # 1.dp 定义
        # dp[i][j] 为使用i个鸡蛋从M层楼往下扔时的最坏操作次数(E >= M)
        dp = [[0 for j in range(M + 1)] for i in range(N+1)]
        # 有意义值为N * M 的矩阵

        # 2.dp初始化
        for i in range(1, N + 1):
            dp[i][1] = 1 #只有一层楼的情况
        for j in range(1, M + 1):
            dp[1][j] = j #只用一个鸡蛋的情况

        # 3.dp递推
        for i in range(2, N +1):
            for j in range(2, M + 1):
                for k in range(1, j + 1):
                # 从某一层k往下扔
                # 鸡蛋碎了，剩下鸡蛋N-1，剩下楼层k-1
                # 鸡蛋好的，剩下鸡蛋N，剩下楼层 j - k
                    dp[i][j] = min(max(dp[i-1][k-1] + 1, dp[i][j-k] + 1), dp[i][j])
        return dp[N][M]

    # dp 优化 空间复杂度O(M)
    def powerEggs_1(self, N, M):
        dp_pre = [0 for j in range(M + 1)]
        dp = [0 for j in range(M + 1)]

        for j in range(M+1):
            dp[j] = j

        for i in range(2, N+1):
       # 当前备忘录拷贝给上一次备忘录，并重新初始化当前备忘录
            dp_pre = dp
            for j in range(M + 1):
                dp[j] = j

            for j in range(2, M + 1):
                for k in range(1, j + 1):
                    # 扔鸡蛋的楼层从1到m枚举一遍，如果当前算出的尝试次数小于上一次算出的尝试次数，则取代上一次的尝试次数。
                    # 这里可以打印k的值，从而知道第一个鸡蛋是从第几次扔的。
                    dp[j] = min(max(dp_pre[k-1] + 1, dp[j - k] + 1), dp[j])
   return dp[M]

   def powerEggs_2(self, N, M):
    """
    :type N: int (nums of eggs)
    :type M: int (levels of buliding) 
    最坏情况也就是鸡蛋摔碎的临界值E > M 
    :rtype: int(min times using N eggs to decide in M levels bulidng)
    """
    # 1.dp 定义
    # dp[i][j] 为使用i个鸡蛋扔j次可以确定的最大层楼，最大扔32次
    dp = [[0 for j in range(32 + 1)] for i in range(N+1)]
    # 有意义值为N * 32 的矩阵

    # 2.dp初始化
    for i in range(1, N + 1):
        dp[i][1] = 1 #只有扔一次的情况
    for j in range(1, 32 + 1):
        dp[1][j] = j #只用一个鸡蛋的情况

    # 3.dp递推
    for i in range(2, N +1):
        for j in range(2, 32 + 1):
            # 从某一层j往下扔
            # 鸡蛋碎了，剩下鸡蛋i-1，剩下次数j - 1, 可能确定的最大层数dp[i-1][j-1]
            # 鸡蛋好的，剩下鸡蛋i，剩下次数j - 1，可能确定的最大层数dp[i][j-1]
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1] + 1

    res = 0
    # 找到层数刚好超过的为M的最小次数j
    for j in range(1, 32 + 1):
        if dp[N][j] >= M:
            res = j
            break

    return res