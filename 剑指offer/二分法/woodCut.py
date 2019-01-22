import math

class Solution:
    # 给定L = [232, 124, 456], k=7, return 114,
    # 给定一组树木,要求切割任意次之后相同长度的树木个数大于等于k,求最长切割后的长度

    def woodCut(self, nums, k):
        n = len(nums)
        if (nums is None or n == 0):
            return -1

        # 确定开始位置和结束位置
        start = 1
        end = max(nums)

        while(start + 1 < end):
            # 相邻就退出
            mid = start + (end - start) // 2
            if self.check_nums(nums, mid) == k:
                # 使用check_nums求在当前每段长度为mid时，可以将数组分成多少段
                # mid越大，return的值越小，找到结果为k的最大的mid（last_index）
                start = mid
            elif self.check_nums(nums, mid) > k:
                start = mid
            else:
                end =  mid

        if self.check_nums(nums, start) == k:
            return start
        if self.check_nums(nums, end) == k:
            return end

        return 0

    def check_nums(self, nums, mid):
        count = 0
        for num in nums:
            count += num // mid
        return count

if __name__ == '__main__':
    print(Solution().woodCut([232, 124, 456], 7))