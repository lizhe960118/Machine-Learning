class Solution:
    # 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。
    # 如果不存在符合条件的连续子数组，返回 0。
    def minSubArrayLen(self, nums, target):
        n = len(nums)

        # fast = 0
        slow = 0

        min_len = len(nums)
        tmp = 0
        ans = []

        for fast in range(n):
            tmp += nums[fast]
            if tmp < target:
                continue
            else:
                # 满足条件的子数组
                while tmp - nums[slow] >= target and slow < fast:
                    tmp -= nums[slow]
                    slow += 1
                if fast - slow + 1 < min_len:
                    min_len = fast - slow + 1
                    ans = nums[slow:slow+min_len]

        return ans

if __name__ == '__main__':
    print(Solution().minSubArrayLen([2,3,1,2,4,3], 7))


