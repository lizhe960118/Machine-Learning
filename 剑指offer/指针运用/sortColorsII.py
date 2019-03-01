class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # 每次以 k // 2 为分界点进行快排 nlog(k)
        return self.quickSelect(colors, 0, len(colors)- 1, 1, k)
    
    def quickSelect(self, nums, start, end, k_start, k_end):
        if start >= end or k_start == k_end:
            return 
        
        left = start 
        right = end
        
        pivot = (k_start + k_end) // 2 
        # 左边都小于等于 pivot 
        while left <= right:
            
            while left <= right and nums[left] <= pivot:
                left += 1 
            while left <= right and nums[right] > pivot:
                right -= 1 
                
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
        # ..., right, left, ..

        self.quickSelect(nums, start, right, k_start, pivot)
        self.quickSelect(nums, left, end, pivot + 1, k_end)
