class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        if numbers is None or len(numbers) <= 0:
            return None
        
        num_index = []
        for index, num in enumerate(numbers):
            num_index.append([num, index])
        
        num_index = sorted(num_index, key = lambda x:x[0])
        
        # print(num_index)
        # pionter from start to end 
        left = 0
        right = len(num_index) - 1 
        
        while left < right:
            if num_index[left][0] + num_index[right][0] == target:
                result = [num_index[left][1], num_index[right][1]]
                result.sort()
                return result
            elif  num_index[left][0] + num_index[right][0] < target:
                left += 1 
            else:
                right -= 1 
        
        return None