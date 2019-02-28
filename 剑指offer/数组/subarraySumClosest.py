class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        if nums is None or len(nums) == 0:
            return nums
            
        result = []
        
        prefix_sum = [0 for i in range(len(nums) + 1)]
        #sum(i, j) = prefix_sum[j + 1] - prefix_sum[i]
        
        d = {prefix_sum[0]:0} # 保存位置

        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
            if nums[i] == 0:
                result = [i, i]
            if prefix_sum[i+1] in d:
                prev_index = d[prefix_sum[i + 1]]
                result = [prev_index, i]
            d[prefix_sum[i+1]] = i+1        
        
        # print(prefix_sum)
        # 前缀和排序
        prefix_sum.sort()
        
        diff = float('inf')
        # print(prefix_sum)
        # print(d)
        if len(result) == 0:
            for i in range(1, len(prefix_sum)):
                now_diff = prefix_sum[i] - prefix_sum[i - 1]
                if now_diff < diff:
                    diff = now_diff
                    first_index = d[prefix_sum[i]]
                    last_index = d[prefix_sum[i - 1]]
                    if first_index > last_index:
                        first_index -= 1 
                    else:
                        last_index -= 1
                    result = [first_index, last_index]
            result.sort()        
        return result

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        if nums is None or len(nums) == 0:
            return nums
            
        result = []
        
        prefix_sum = [[0,0] for i in range(len(nums) + 1)]
        #sum(i, j) = prefix_sum[j + 1] - prefix_sum[i]

        for i in range(len(nums)):
            prefix_sum[i + 1][0] = prefix_sum[i][0] + nums[i]
            prefix_sum[i+1][1] = i+1        
        

        # 前缀和排序
        prefix_sum = sorted(prefix_sum, key = lambda x:x[0])

        diff = float('inf')

        for i in range(1, len(prefix_sum)):
            now_diff = prefix_sum[i][0] - prefix_sum[i - 1][0]
            if now_diff < diff:
                diff = now_diff
                first_index = prefix_sum[i][1]
                last_index = prefix_sum[i - 1][1]
                if first_index > last_index:
                    first_index -= 1 
                else:
                    last_index -= 1
                result = [first_index, last_index]
                
                
        result.sort()        
        return result