class Solution:
    def search(self, nums, target):
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
        
        # 首先要找到分界点-> 找旋转数组里的最小值->以小于等于旋转数组的最后一位数为条件
        while(start + 1 < end):
            mid = start + (end - start) // 2
            if nums[mid] <= nums[n-1]:
                end = mid
            else:
                start = mid
        
        mid_find = 0
        if nums[start] < nums[end]:
            mid_find = start
        else:
            mid_find = end
        
        result1 = self.binarySearch(nums[:mid_find], target)
        result2 = self.binarySearch(nums[mid_find:], target)
        
        if result1 != -1:
            return result1
        
        if result2 != -1:
            return mid_find + result2
        
        return -1
        
        # 分别在两个数组里面用二分法
    def binarySearch(self, nums, target):
        n = len(nums)
        if nums is None or n == 0:
            return -1
        start = 0
        end = n - 1
        while(start + 1 < end):
            mid = start + (end - start) // 2
            if nums[mid] == target:
                start = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1