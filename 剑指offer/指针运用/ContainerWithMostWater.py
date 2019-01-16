class Solution:
    def containerWithMostWater(self, container):
        """
        :type container:List
        :rtype: int
        """
        n = len(container)

        if n <= 1:
            return 0

        left = 0
        right = n - 1

        ans = min(container[left], container[right]) * (right - left) # 不能初始化为0

        while left < right:
            if container[left] < container[right]:
                tmp = container[left] * (right - left)
                left += 1
            else:
                tmp = container[right] * (right - left)
                right -= 1
            ans = max(ans, tmp)

        return ans

if __name__ == '__main__':
    print(Solution().containerWithMostWater([1,8,6,2,5,4,8,3,7]))