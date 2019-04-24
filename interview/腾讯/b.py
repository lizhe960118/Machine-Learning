N = int(raw_input())

l = [int(i) for i in raw_input().split()]

pay = 0
for i in range(0, n-1):
    pay += abs(l[i])
    l[i+1] += l[i]

print(pay)