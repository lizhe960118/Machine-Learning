# import sys

# def subsets(nums, D):
#     # 从空集开始搜索，每次将nums的节点加入空集中
#     result = []
#     tmp = []
    
#     if nums is None:
#         return None
    
#     nums.sort()
    
#     startIndex = 0    
#     dfsHelper(nums, startIndex, tmp, result, D)
    
#     return result
    
# def dfsHelper(nums, startIndex, tmp, result, D):
#     # 3.出口
    
#     tmp_copy = tmp.copy()
#     if len(tmp_copy) == 3 and (tmp_copy[-1] - tmp[0]) <= D: 
#         result.append(tmp_copy)
    
#     if startIndex == len(nums):
#         return
    
#     for i in range(startIndex, len(nums)):
#         tmp.append(nums[i])
#         dfsHelper(nums, i + 1, tmp, result, D)
#         tmp.pop()
#     return

# if __name__ == "__main__":
#     # 读取第一行的n
#     line1 = sys.stdin.readline().strip().split()
#     # print(line1)
#     N = int(line1[0])
#     D = int(line1[1])
#     line2 = sys.stdin.readline().strip().split()
#     arr_N = [int(a) for a in line2]
#     result = subsets(arr_N, D)
#     print(len(result))

import sys

def dp_subsets(nums, D):
    # 从空集开始搜索，每次将nums的节点加入空集中
    N = len(nums)
    dp = [0 for i in range(N)]
    start_index = 0

    for i in range(2, N):
        # 找到最开始的大于D的位置
        while (nums[i] - nums[start_index]) > D :
            start_index += 1
        length = i - (start_index)
        if length >= 2:
            dp[i] = dp[i-1] + (length) * (length - 1) // 2
        else:
            dp[i] = dp[i-1]
    return dp[N-1]

if __name__ == "__main__":
    # 读取第一行的n
    line1 = sys.stdin.readline().strip().split()
    # print(line1)
    N = int(line1[0])
    D = int(line1[1])
    line2 = sys.stdin.readline().strip().split()
    arr_N = [int(a) for a in line2]
    result = dp_subsets(arr_N, D)
    print(result % 99997867)