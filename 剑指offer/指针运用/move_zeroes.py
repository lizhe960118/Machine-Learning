class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        if nums is None or len(nums) <= 1:
            return nums
        
        # 保证left左边都不为0    
        left = 0
        right = 0 
        end = len(nums) - 1
        
        # while right <= end and left <= end:
        #     while right <= end and left <= end and nums[left] != 0:
        #         left += 1 
        #         right = left + 1
        #     while right <= end and left <= end and nums[right] == 0:
        #         right += 1
        #     if right <= end and left <= end:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left += 1 
        #         right += 1 
        
        while right <= end:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
            right += 1 
        return nums