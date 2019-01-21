class Solution:
    def findFirstIndex(self, nums, target):
        n = len(nums)
        if (nums is None or n == 0):
            return -1

        start = 0
        end = n - 1

        while(start + 1 < end):
            # 相邻就退出
            mid = start + (end - start) // 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        return -1