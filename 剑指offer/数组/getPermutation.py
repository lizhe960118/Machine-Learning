class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factor = 1
        for i in range(1, n):
            factor *= i
        arr = [i+1 for i in range(n)]
        ans = []
        # 这里将k减1，不放入循环
        k -= 1
        for i in range(n-1, 0, -1):
            index = k // factor
            ans.append(str(arr[index]))
            arr = arr[:index] + arr[index+1:]
            k = k % factor
            factor = factor / i
        ans.append(str(arr[0]))
        return ("").join(ans)