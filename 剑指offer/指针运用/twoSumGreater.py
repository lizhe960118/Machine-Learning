# 找到两数之和大于target的对数
# [1, 2, 3, 4] target = 3 
#  1 + 3 > 3
#  1 + 4 > 3
#  2 + 3 > 3
#  2 + 4 > 3
#  3 + 4 > 3
#  return 5

# 如果 1 + 4 > 3 那么1~4之间的数和4相加也大于3
# left,  ..., right - 1都可以和right配对，
# count += (right - 1) - left + 1 = right - left

class Solution:
    def twoSumGreater(self, nums, target):
        if nums is None or len(nums) <= 0:
            return 0

        left = 0
        right = len(nums) - 1 
        count = 0

        while left < right:
            if nums[left] + nums[right] > target:
                count += right - left
                right -= 1 
            else:
                left += 1
        return count

if __name__ == '__main__':
    print(Solution().twoSumGreater([1, 1, 2, 2, 3, 4], 3))