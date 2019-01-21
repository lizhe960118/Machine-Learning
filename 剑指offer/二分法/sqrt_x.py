class Solution:
    def sqrt_x(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
            return 0

        nums = [i for i in range(x)]
        # 10 [0 1 2 3 4 5 6 7 8 9]
        
        start = 0
        end = x - 1
        
        # 关键是找到缩小数组为一半的条件
        while(start + 1 < end):
            mid = start + (end - start) // 2
            if nums[mid] * nums[mid] == x:
                return mid
            elif nums[mid] * nums[mid] < x:
                start = mid
            else:
                end = mid
        
        if nums[end] * nums[end] < x:
            return end
        
        if nums[start] * nums[start] < x:
            return start

        return 0

if __name__ == '__main__':
    print(Solution().sqrt_x(10))