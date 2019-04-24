N = int(input()) # 测试用例个数
result = [0 for i in range(N)]

for i in range(N):
    M = int(input()) # 当前用例的帧数
    all_zhen = {}
    bigest = 0

    for j in range(M):
        tmp = [int(a) for a in input().split()] 
        cur_num = tmp[0] # 当前帧的特征运动个数
        
        if cur_num == 0:
            all_zhen = {}
            continue

        for k in range(1, cur_num, 2):
            key = (tmp[k], tmp[k+1])
            if key in all_zhen:
                all_zhen[key] += 1
            else:
                all_zhen[key] = 1
            bigest = max(bigest, all_zhen[key])
        result[i] = bigest

for i in range(N):
    print(result[i])
            
        