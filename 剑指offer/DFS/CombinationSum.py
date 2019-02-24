class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        if candidates is None:
            return None
        
        # candidates去重
        candidates = self.deDuplicate(candidates)
        
        result = []
        tmp = []
        startIndex = 0
        
        self.dfsHelper(candidates, target, startIndex, tmp, result)
        
        return result
    
    def dfsHelper(self, candidates, target, startIndex, tmp, result):
        # 递归的出口
        if  target == 0:
            result.append(tmp.copy())
            tmp = []
            return
        
        # 递归
        for i in range(startIndex, len(candidates)):
            if candidates[i] > target:
                return
            self.dfsHelper(candidates, target - candidates[i], i, tmp + [candidates[i]], result)
            
        return
    
    def deDuplicate(self, nums):
        nums = list(set(nums))
        nums.sort()
        return nums
        