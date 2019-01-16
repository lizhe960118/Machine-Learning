class Solution:
    
    def longestMountain(self, nums):
        # 找出一个数组中最长的山形数组的长度。所谓山形数组就是前半段是单调递增的，后半段是单调递减的。
        # 解法：定义两个数组，一个数组记录当前位置左边递增的个数，一个数组记录表右边位置递减的个数
        n = len(nums)

        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                left[i] = left[i - 1] + 1

        for i in range(n-2, -1, -1):
            if nums[i] > nums[i + 1]:
                right[i] = right[i + 1] + 1

        ans = 0
        for i in range(n):
            tmp = left[i] + right[i] + 1
            ans = tmp if tmp > ans else ans

        return ans
    
    def longestMountain_1(self, nums):
        n = len(nums)

        ans = 0
        i = 1

        while i < n:
            left = i - 1
            while i < n and nums[i] > nums[i - 1]:
                i += 1
            if left == i - 1:
                i += 1
                continue

            right = i - 1
            while right < n -1 and nums[right] > nums[right + 1]:
                right += 1
            if right == i - 1:
                i += 1
                continue
            else:
                ans = max(ans, right - left + 1)
                i = right + 1

        return ans

if __name__ == '__main__':
    print(Solution().longestMountain([2,1,4,7,3,2,5]))
    print(Solution().longestMountain_1([7,3,2,5]))
