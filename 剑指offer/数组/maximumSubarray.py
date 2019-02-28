class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        if nums is None:
            return nums
            
        prefix_sum = 0
        max_sum = -float("inf")
        min_sum = 0
        
        # sum(i,j) = prefix_sum[j] - prefix_sum[i]
        for i in range(len(nums)):
            prefix_sum += nums[i]
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)
            
        return max_sum
        
