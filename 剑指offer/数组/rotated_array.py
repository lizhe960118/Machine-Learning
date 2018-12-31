class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 二分法，但是是用到两次二分
        left = 0
        right = len(nums) - 1
        while(left < right):
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        p = left
        l1 = self.binary_search(nums[:p], target)
        l2 = self.binary_search(nums[p:], target)
        if l1 >= 0:
            return l1
        if l2 >= 0:
            return p + l2
        return -1
    
    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1