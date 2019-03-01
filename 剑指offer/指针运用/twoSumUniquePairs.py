# [1, 1, 2, 3, 3] target=4, return 1
# [1, 1, 2, 3, 3] target=5, return 1
# [1, 1, 2, 45, 46, 46], target=47, return 2 (1, 46) （2，45）
# 返回和为target的对数
class Solution:
    def twoSumUniquePairs(self, nums, target):
        if nums is None or len(nums) <= 0:
            return 0
        
        # for i in range(len(nums)):
        # 总是取第一个出现的值

        left = 0
        right = len(nums) - 1

        count = 0
        while left < right: # 相等就退出
            if nums[left] + nums[right] == target:
                count += 1
                left += 1
                right -= 1
                # 这里去重
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return count

if __name__ == '__main__':
    print(Solution().twoSumUniquePairs([1, 1, 2, 45, 46, 46], 47))


