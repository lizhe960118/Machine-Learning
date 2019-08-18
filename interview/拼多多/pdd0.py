A = input().split()
A = [int(a) for a in A]

B = input().split()
B = [int(b) for b in B]


dict_num = {}

for i in range(len(A) - 1):
    if A[i] > A[i + 1]:
        index = i
        min_target = A[i - 1] if i > 0 else -float("inf")
        max_target = A[i + 1]
        if (min_target < max_target):
            dict_num[index] = (min_target, max_target)

        index = i + 1
        min_target = A[i]
        max_target = A[i + 2] if (i < len(A) - 1) else float("inf")
        dict_num[index] = (min_target, max_target)
        break
   
result = {}
for key_index, target in dict_num.items():
    min_target, max_target = target 
    for i in range(len(B)):
        if (B[i] > min_target) and (B[i] < max_target):
            result[key_index] = max(B[i], result[key_index]) if (key_index in result) else B[i]

if result:
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)[0]
    A[result[0]] = result[1]
    print(A)
else:
    print("No")
