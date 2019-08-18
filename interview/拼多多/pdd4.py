N = int(input())

length_nums = [int(a) for a in input().split()]
# print(length_nums)
weight_nums = [int(a) for a in input().split()]
# print(weight_nums)
max_weight = 1000

# 存储物品编号的字典
codedict = [[length_nums[i], weight_nums[i]] for i in range(N)]
# print(codedict)
# 按长度开始排序
codedict = sorted(codedict, key=lambda x: x[0], reverse=True)
print(codedict)

result = []
result.append(codedict[0]) # 将最长的积木加入
weight_left = [float("inf") for i in range(N)]
weight_left[0] = codedict[0][1] * 7
# dp = [[0 for i in range(max_weight * 7)] for n in range(N)]
print(weight_left)

for i in range(1, N):
    # 当前加入的小于总质量
    if codedict[i][1] <= min(weight_left):
        result.append(codedict[i])
        weight_left = [weight - codedict[i][1] for weight in weight_left]
        weight_left[i] = codedict[i][1] * 7

print(len(result))