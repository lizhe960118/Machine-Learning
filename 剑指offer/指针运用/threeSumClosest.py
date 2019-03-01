class Solution:
    def threeSumClosest(self, nums, target):
        # 先排序,固定一个数然后移动之后两个指针，每次记录最近目标值的数组，接下来要解决重复情况
        result = []
        if nums is None or len(nums) <=2:
            return result
        
        nums.sort()

        min_diff = float("inf")

        for i in range(len(nums) - 2):
            # 给第一个数去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l_left = i + 1
            l_right = n - 1
            
            while l_left < l_right:
                cur_sum = nums[i] + nums[l_left] + nums[l_right]
                cur_diff = abs(target - cur_sum)

                if cur_diff < min_diff:
                    min_diff = cur_diff
                    result = []
                    result.append([nums[i], nums[l_left], nums[l_right]])

                if cur_sum < target:
                    l_left += 1
                else:
                    l_right -= 1

        return cur_diff