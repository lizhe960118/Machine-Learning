class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        # prefix_sum
        
        if nums is None:
            return None
            
        prefix_sum = [0 for i in range(len(nums) + 1)]
        
        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        
        result = []
        d = {}
        for i in range(len(nums) + 1):
            if prefix_sum[i] in d:
                j = d[prefix_sum[i]]
                result.append(j)
                result.append(i - 1)
                break
            else:
                d[prefix_sum[i]] = i
                    
        return result