n = int(input())

score_n = [int(a) for a in input().split()]

q = int(input())
input_q = []
for i in range(q):
    input_q.append(int(input())) # 表示查询的成绩

count = [0 for i in range(151)]
for i in range(n):
    count[score_n[i]] += 1

for i in range(151):
    count[i] = count[i] + count[i-1]

for i in range(q):
    x = input_q[i]
    c = count[score_n[x-1]]
    res = (c - 1) / n * 100
    print('%.6f' % res)
