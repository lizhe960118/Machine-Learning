import heapq

class Solution:
    def smallestRange(self, nums):
        #有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
        pq = [(rows[0], i, 0) for i, rows in enumerate(nums)]
        heapq.heapify(pq)

        ans = [-1e5, 1e5]

        right = max(rows[0] for rows in nums)

        while pq:
            # left = nums[i][j]
            left, i, j = heapq.heappop(pq) #记录下最小值

            if right - left < ans[1] - ans[0]:
                ans = [left, right]

            if j == len(nums[i]) - 1:
                # 某一数组结束
                break
                
            right = max(right, nums[i][j + 1])

            heapq.heappush(pq, (nums[i][j+1], i, j+1))

        return ans

if __name__ == '__main__':
    print(Solution().smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))