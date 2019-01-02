class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #贪心算法
        n = len(prices)
        if n == 0:
            return 0
        minbuy = prices[0]
        result = 0
        n = len(prices)
        for i in range(1, n):
            minbuy = min(minbuy, prices[i])
            result = max(result, prices[i] - minbuy)
        return result