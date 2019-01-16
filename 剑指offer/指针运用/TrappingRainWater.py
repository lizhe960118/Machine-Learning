class Solution:
    def trappingRainWater(self, height):
        n = len(height)

        if n <= 1:
            return 0

        left = 0
        right = n - 1

        maxleft = 0
        maxright = 0

        ret = 0

        while left < right:
            if height[left] < height[right]:
                # 在满足左边比右边小的情况下，蓄水是在左边最大值得基础上减去当前值
                if height[left] > maxleft:
                    maxleft = height[left]
                else:
                    ret += maxleft - height[left]

                left += 1

            else:
                if height[right] > maxright:
                    maxright = height[right]
                else:
                    ret += maxright - height[right]
                right -= 1

        return ret

if __name__ == '__main__':
    print(Solution().trappingRainWater([0,1,0,2,1,0,1,3,2,1,2,1]))