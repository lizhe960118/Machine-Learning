# O(n)解法
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        tmp = nums[0]
        result = nums[0]
        for i in range(1, n):
            if tmp < 0:
                tmp = 0
            tmp +=  nums[i]
            result = max(result, tmp)
        return result

# 分治解法
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 0:
            return None
        return self.helper(nums, 0, n)
    
    def helper(self, nums, left, right):
        if right - left == 1:
            return nums[left]
        
        center = (left + right) // 2
        maxleft = self.helper(nums, left, center)
        maxright = self.helper(nums, center, right)
        
        lefttmp = 0
        leftcount = nums[center-1]
        for i in range(center-1, left-1, -1):
            lefttmp += nums[i]
            if lefttmp > leftcount:
                leftcount = lefttmp
                
        righttmp = 0
        rightcount = nums[center]
        for i in range(center, right):
            righttmp += nums[i]
            if righttmp > rightcount:
                rightcount = righttmp
                
        return max(maxleft, maxright, leftcount+rightcount)