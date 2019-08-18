line1 = [int(a) for a in input().split()]
n, q = line1[0], line1[1]

raw_nums = [-int(a) for a in input().split()]
input_q = []
for i in range(q):
    input_q.append(-int(input()))

# print(n, q, raw_nums, input_q)

#python 默认小顶堆
import heapq
h = []#建立一个常见的堆
for i in range(len(raw_nums)):
    heapq.heappush(h, raw_nums[i])

for i in range(q):
    cur_num = input_q[i]
    # count = 0 
    tmp = []
    # -4 > -5
    while(h and cur_num >= h[0]):
        tmp.append(heapq.heappop(h) + 1)
    input_q[i] = len(tmp)
    for i in range(input_q[i]):
        heapq.heappush(h, tmp[i])

print(input_q)
