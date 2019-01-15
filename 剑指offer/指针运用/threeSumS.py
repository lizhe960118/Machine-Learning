class Solution:
    def threeSumS(self, nums, target):
        # 给定一个n个整数的数组和一个目标整数target，
        # 找到下标为i、j、k的数组元素0 <= i < j < k < n，满足条件nums[i] + nums[j] + nums[k] <= target.
        # 先排序,固定一个数然后移动之后两个指针
        n = len(nums)
        if n <= 2:
            return 0
        
        nums.sort()

        count = 0
        
        for i in range(n - 2):

            l_left = i + 1
            l_right = n - 1

            while l_left < l_right:
                s = nums[i] + nums[l_left] + nums[l_right]
                if s <= target:
                    count += l_right - l_left
                    l_left += 1
                else:
                    l_right -= 1

        return count