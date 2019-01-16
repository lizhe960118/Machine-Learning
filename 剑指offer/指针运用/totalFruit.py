class Solution:
    def totalFruit(self, nums):
        # 寻找一个最大的子区间，该子区间中只包含两种元素（无顺序要求）
        n = len(nums)
        if n <= 2:
            return nums

        res = 0
        left = 0

        q = [] # 队列长度为2，放两种相邻的元素
        d = {} # 记录每种元素出现的最后位置

        for right in range(n):
            # 右指针向后移动
            d[nums[right]] = right

            if len(q) < 2 and nums[right] not in q: # q未满
                q.append(nums[right])
            elif nums[right] in q and nums[right] == q[-1]: # 在q里面，且为第二个元素
                pass
            elif nums[right] in q and nums[right] == q[0]: # 为第一个元素,但是后进来就把它放在后面
                q.pop(0)
                q.append(nums[right])
            elif len(q) >= 2 and nums[right] not in q: # q已满，新来的元素不在q里，将q[0]出队，用字典d返回q[0]最后出现的位置
                # left = d[q[0]] + 1
                # q.pop(0)
                left = d[q.pop(0)] + 1 # 更新左指针位置
                q.append(nums[right])

            res = max(res, right - left + 1)

        return res

if __name__ == '__main__':
    print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))

