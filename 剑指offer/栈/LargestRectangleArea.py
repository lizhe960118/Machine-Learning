class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # 此题目目的是找到当前元素左边的能取得长度，和右边能取到的长度
        # 左右两边要不小于当前元素的值

        # 维护一个单调递增栈，当入栈元素小于栈顶元素时，取出栈顶元素
        # 因为，对于栈顶元素，此时找到了左右两边比他小的元素
        # 计算最大面积，入栈的是元素在height中的坐标
        if height is None or len(height) == 0:
            return 0
        
        stack = []
        
        max_area = 0
        
        for i in range(len(height) + 1):
            cur_height = height[i] if i < len(height) else -1
            # 当前入栈元素比栈顶元素小
            while(stack and cur_height < height[stack[-1]]):
                # 取出栈顶元素
                h = height[stack.pop()]
                # stack保存最近一个小于入栈元素的位置，stack空的时候保存的是数组中的最小值
                w = i if len(stack) == 0 else i - stack[-1] - 1 
                max_area = max(max_area, h * w)
            stack.append(i)
            
        return max_area
