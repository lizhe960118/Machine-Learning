import math

class Solution:
    # 给定book的页数 pages = [3,2,4], k=2, return 5
    # k 为给定copy book的人数，return 最少需要多少时间来复制完一本书，规定每个人只能复制连续页面的书
    def copyBooks(self, nums, k):
        n = len(nums)
        if (nums is None or n == 0 or k <= 0):
            return 0

        # 确定开始位置和结束位置
        start = max(nums) # 最小需要把最费时的那一页copy完
        end = sum(nums) # 最长在一个人时，需要复制整本书

        while(start + 1 < end):
            # 相邻就退出
            mid = start + (end - start) // 2
            if self.countPersons(nums, mid) == k:
                # 使用countPersons求在当前用时为mid时，需要多少人来复制书
                # mid越大，return的值越小（用时越多，需要的人越少）
                # 求第一个使得人数为k的mid
                # 4 5 6 7 8 9
                # 3 2 2 2 2 1
                end = mid
            elif self.countPersons(nums, mid) < k:
                end = mid
            else:
                start = mid

        if self.countPersons(nums, start) == k:
            return start

        if self.countPersons(nums, end) == k:
            return end

        return 0

    def countPersons(self, pages, t):
        # 在给定时间t内复制book，最少需要多少人
        count = 0
        sum_time = 0
        for page in pages:
            if sum_time + page > t:
                sum_time = page
                count += 1
            else:
                sum_time += page
        return count if sum_time == 0 else count + 1

if __name__ == '__main__':
    print(Solution().copyBooks([3, 2, 4], 2))