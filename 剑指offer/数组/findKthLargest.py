class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        start = 0
        end = n - 1
        ans = -1
        while(ans != n - k):
            ans = self.quick_sort(nums, start, end)
            if ans < n - k:
                start = ans + 1
            elif ans > n - k:
                end = ans - 1
        return nums[ans]
    
    def quick_sort(self, nums, start, end):
        # 取最后一位作为分解符
        q = nums[end]
        # 小技巧i从-1开始，判断j，则可以定位i+1为第一个大于q，j为第一个小于q
        i = start - 1
        for j in range(start, end):
            if nums[j] < q:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[end] = nums[end], nums[i + 1]
        return i + 1
        