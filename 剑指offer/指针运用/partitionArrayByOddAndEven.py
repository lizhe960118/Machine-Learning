class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # 反向双指针
        if nums is None or len(nums) <= 1:
            return nums
            
        left = 0 
        right = len(nums) - 1 
        
        while left <= right:
            while left <= right and nums[left] % 2 != 0:
                left += 1 
                # 定位到第一个偶数
            while left <= right and nums[right] % 2 == 0:
                right -= 1 
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
        
        return nums
            
