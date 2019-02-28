class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # prefix sum 前置一个0，方便迭代
        # sum(i, j) = prefix_sum[j + 1] - prefix_sum[i]
        
        if nums is None or len(nums) < k or k == 0:
            return []
        
        prefix_sum = [0 for i in range(len(nums) + 1)]
        
        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
            
        result = []
        for i in range(k, len(nums)+1):
            result.append(prefix_sum[i] - prefix_sum[i-k])
        
        return result
