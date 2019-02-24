class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        if nums is None:
            return None
            
        result = []
        tmp = []
        
        nums.sort()
        
        self.dfsHelper(nums, tmp, result)
        
        return result
    
    def dfsHelper(self, nums, tmp, result):
        if len(nums) == 0:
            result.append(tmp.copy())
            return
        
        # 递归
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            tmp.append(nums[i])
            self.dfsHelper(nums[:i] + nums[i+1:], tmp, result)
            tmp.pop()
        
        return