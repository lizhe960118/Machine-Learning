class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        if nums is None:
            return None
            
        result = []
        tmp = []
        
        self.dfsHelper(nums, tmp, result)
        
        return result
    
    def dfsHelper(self, nums, tmp, result):
        if len(nums) == 0:
            result.append(tmp.copy())
            return
        
        # 递归
        for i in range(len(nums)):
            tmp.append(nums[i])
            self.dfsHelper(nums[:i] + nums[i+1:], tmp, result)
            tmp.pop()
        
        return