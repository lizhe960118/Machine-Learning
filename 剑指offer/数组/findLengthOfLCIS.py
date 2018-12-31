class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        ans = 0
        i = 0
        while(i < n):
            j = i
            while j < n - 1 and nums[j] < nums[j+1]:
                j += 1
            # print(i, j)
            ans = max((j - i + 1), ans)
            i = j + 1
        return ans