class Solution:
    def findMinValueIndex(self, nums):
        n = len(nums)
        if (nums is None or n == 0):
            return -1

        start = 0
        end = n - 1

        while(start + 1 < end):
            # 相邻就退出
            mid = start + (end - start) // 2
            if nums[mid] <= nums[n - 1]:
                # 这个条件使得数组为[XXXXOOO]
                end = mid
            else:
                start = mid

        if nums[start] < nums[end]:
            return start
        else:
            return end