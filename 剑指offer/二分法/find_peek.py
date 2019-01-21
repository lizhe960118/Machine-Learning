class Solution:
    def findPeek(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if nums is None or n == 0:
            return -1
        
        start = 0
        end = n - 1
        
        # 关键是找到缩小数组为一半的条件
        while(start + 1 < end):
            mid = start + (end - start) // 2
            if nums[mid] < nums[mid - 1]:
                end = mid
            elif nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid
        
        if nums[start] < nums[end]:
            return start
        else:
            return end