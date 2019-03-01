class Solution:
    def twoSum(self, arr, target):
        #给定一个整数数组，找出这个数组中有多少对的和是小于或等于目标值。返回对数。
        count = 0

        arr_length = len(arr)
        if arr_length <= 1:
            return count

        l_left = 0
        l_right = arr_length - 1

        while(l_left < l_right):
            if arr[l_left] + arr[l_right] <= target:
                count += l_right - l_left
                # 特别注意这里nums[l_left+1:l_right+1]之间的数和nums[l_left]相加都是<=target
                l_left += 1

            else:
                l_right -= 1

        return count