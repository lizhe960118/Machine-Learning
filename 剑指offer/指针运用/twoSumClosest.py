# 找到两数之和最接近target的数组对

# [1, 2, 3, 4]  target = 6
# return [2, 4]
# [1, 2, 40]  target = 6
# return [1, 2]
class Solution:
    def twoSumClosest(self, nums, target):
        result = []

        if nums is None or len(nums) <= 1:
            return result

        # 相向双指针
        left = 0
        right = len(nums) - 1

        min_diff = float("inf")

        while left < right:
            diff_now = abs(nums[left] + nums[right] - traget)
            if diff_now < min_diff:
                min_diff = diff_now # 记得更新diff
                result = [] 
                result.append(nums[left], nums[right])
            if nums[left] + nums[right] < traget:
                left += 1
            else:
                right -= 1

        return result