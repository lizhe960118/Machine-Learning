n, k = input().split()
n = int(n)
k = int(k)

nums = input().split()
nums = [int(a) for a in nums]

# nums.sort()

# index_smallest = 0

for i in range(k)：
    if count == n:
        print(0)
    else:
        b = []
        for i in range(n):
            if i 


for i in range(k):
    if len(nums) == 0:
        print(0)
    else:
        # smallest = nums[index_smallest]
        # print(smallest)
        print(nums[0])

        nums = [a - nums[0] for a in nums]

        count_0 = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                count_0 += 1
            else:
                break
        nums = nums[count_0:]

移动， 可以直接找到最小
然后交换

n, k = input().split()
n = int(n)
k = int(k)

nums = input().split()
nums = [int(a) for a in nums]

import heapq

h = []
tmp_smallest = 0 

for i in range(n):
    heapq.heappush(h, nums[i])

for i in range(k):
    if len(h) == 0:
        print(0)
    else:
        cur_smallest = heapq.heappop(h)
        print(cur_smallest - tmp_smallest)
        while h:
            if h[0] == cur_smallest:
                cur_smallest = heapq.heappop(h)
            else:
                break
        tmp_smallest = cur_smallest
