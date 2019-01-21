class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if nums is None or n == 0:
            return -1
        
        start = 0
        end = n - 1
        
        # half half模型：使用增加判断条件的方法缩小区间
        while(start + 1 < end):
            mid = start + (end - start) // 2
            
            if nums[mid] == target:
                return mid
            if nums[start] < nums[mid]:
                # 说明 start 到 mid 是上升区间， mid 到 end 是先降再升
                if (nums[start] <= target and target <= nums[mid]):
                    end = mid # 缩小区间
                else:
                    start = mid
            else:
                # 说明 mid 到end是上升，start 到mid 是先升后降
                if (nums[mid] <= target and target <= nums[end]):
                    start = mid
                else:
                    end = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1
        