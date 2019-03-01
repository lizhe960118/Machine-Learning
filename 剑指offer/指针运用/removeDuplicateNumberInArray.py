class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None or len(nums) <= 0:
            return 0
        
        # 保证left左边的数不同
        left = 0
        right = 0
        
        while right < len(nums):
            if nums[right] != nums[left]:
                left += 1 
                # nums[right], nums[left] = nums[left], nums[right]
                nums[left] = nums[right]
            right += 1
        return len(nums[:left+1])