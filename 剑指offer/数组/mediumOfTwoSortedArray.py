class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        a_len = len(A)
        b_len = len(B)

        new_nums = []
        for i in range(a_len):
            new_nums.append(A[i])
        for i in range(b_len):
            new_nums.append(B[i])
        print(new_nums)
        
        result = 0
        total_len = a_len + b_len
        
        if (total_len) % 2 == 0:
            result = float(self.findKthLargeNum(new_nums, total_len // 2 + 1) + self.findKthLargeNum(new_nums, total_len // 2))
            result /= 2
   
        else:
            result = self.findKthLargeNum(new_nums, total_len // 2 + 1)
        return result
    
    def findKthLargeNum(self, nums, k):
        return self.quickSelect(nums, 0, len(nums) - 1, k)
        
    # 从数组中选择第k大的数
    def quickSelect(self, nums,start, end, k):
        # 出口
        if start == end:
            return nums[start]
        
        left = start 
        right = end 
        mid = start + (end - start) // 2
        pivot = nums[mid]
        
        while(left <= right):
            while nums[left] > pivot and left <= right:
                left += 1 
            while nums[right] < pivot and left <= right:
                right -= 1 
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
        
        # left > right
        # 5, 4,.. right, left, 3 2 1
        # start, 1,.. left, ...
        # 1, 2, .. ,k,...
        if start + k - 1 <= right:
            return self.quickSelect(nums, start, right, k)
        if start + k - 1 >= left:
            return self.quickSelect(nums, left, end, k - (left - start))
        return nums[start + k - 1]