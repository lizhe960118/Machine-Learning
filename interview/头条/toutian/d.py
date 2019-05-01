n, k = [int(i) for i in input().split()]

oks = [int(i) for i in input().split()]

dp = [abs(1 - i) for i in oks]

acc = 0
acc_l = []

for i in range(len(dp)):
    acc += dp[i]
    acc_l.append(acc)

ans = 0
for i, val1 in enumerate(acc_l):
    for j, val2 in enumerate(acc_l):
        if 0 <= val2 - val1 <= k and dp[i] == 0 and dp[j] == 1:
            ans = max(ans, j - i + 1)

print(ans)
