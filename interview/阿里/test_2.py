def helper(N, M, K):
    if K < 2:
        return 0
    if K == 2:
        return 1
    if K == 3:
        if N = 1 and M = 1:
            return 1
    else:
        return N * M 


if __name__ == '__main__':
    N, M, K = raw_input().split()
    N = int(N)
    M = int(M)
    K = int(K)
    result = helper(N, M, K)
    result = result % 10000
    print result