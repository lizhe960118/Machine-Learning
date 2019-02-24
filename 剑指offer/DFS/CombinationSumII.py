class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum2(self, candidates, target):
        if candidates is None:
            return None
        
        # candidates排序
        candidates.sort()
        
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
            # 去重, 第一个大循环中依次进数时，判断第二个数进入的数和第一个数不同
            if (i != startIndex) and (candidates[i] == candidates[i - 1]):
                continue
            if candidates[i] > target:
                return
            self.dfsHelper(candidates, target - candidates[i], i + 1, tmp + [candidates[i]], result)
            
        return