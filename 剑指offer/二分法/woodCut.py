class Solution:
    def findFirstBadVersion(self, nums):
        n = len(nums)
        if (nums is None or n == 0):
            return -1

        start = 0
        end = n - 1

        while(start + 1 < end):
            # 相邻就退出
            mid = start + (end - start) // 2
            if nums[mid] == False:
                end = mid
            else:
                start = mid

        if nums[start] == False:
            return start

        if nums[end] == False:
            return end

        return -1