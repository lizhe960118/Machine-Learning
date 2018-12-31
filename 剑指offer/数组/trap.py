class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        count = 0
        n = len(height)
        if n <= 1:
            return 0
        max_right_list = [0 for _ in range(n)]
        h_now = height[n-1]
        for i in range(n-2, -1, -1):
            max_right_list[i] = h_now
            h_now = max(height[i], h_now)
        
        max_left = 0
        for i in range(0, n-1):
            max_left = max(max_left, height[i])
            max_right = max_right_list[i]
            tmp = min(max_left, max_right)
            count += tmp - height[i] if tmp > height[i] else 0
        return count
            