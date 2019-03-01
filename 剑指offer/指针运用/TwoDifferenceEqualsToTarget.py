# 给定个数组，返回两数之差和target最接近的两个数

# [2,7,11,17,25] target = 5
# return [2, 7]

class Solution:
    def differenceEqualsToTarget(self, nums, target):
        result = []

        if nums is None or len(nums) <= 1:
            return result

        # 同向双指针
        nums.sort() 

        min_diff = float("inf")

        for i in range(len(nums) - 1):
            left = i
            right = i + 1

            while left < right:
                now_diff = abs((nums[right] - nums[left]) - target)
                if now_diff < min_diff:
                    min_diff = now_diff
                    result = []
                    result.append(nums[left], nums[right])

                if nums[right] - nums[left] < target or abs(nums[right] - nums[left] - target) == min_diff:
                    right += 1 
                else:
                    break

        # while left < len(nums) - 1:
        #     if left == right:
        #         right = left + 1

        #     now_diff = abs((nums[right] - nums[left]) - target)
        #     if now_diff < min_diff:
        #         min_diff = now_diff
        #         result = []
        #         result.append(nums[left], nums[right])

        #     if nums[right] - nums[left] < target or abs(nums[right] - nums[left] - target) == min_diff:
        #         right += 1 
        #     else:
        #         left += 1

        return result
