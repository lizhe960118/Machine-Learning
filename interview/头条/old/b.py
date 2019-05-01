N = int(input())

delay_time = [[int(a) for a in input().split()] for _ in range(N)]

a, b, k = [int(a) for a in input().split()]

def flayAlgoritm(graph):
    minDistance = [[0 for _ in range(len(graph[0]))] for _ in range(len(graph))]
    N = len(graph)

    for i in range(N):
        for j in range(N):
            minDistance[i][j] = graph[i][j]
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if minDistance[i][j] > minDistance[i][k] + minDistance[k][j]:
                    minDistance[i][j] = minDistance[i][k] + minDistance[k][j]
    
    return minDistance

minDistance = flayAlgoritm(delay_time)

temp = [delay_time[i][j] for i in range(len(delay_time)) for j in range(len(delay_time[0])) if i > j]

min_delay = min(temp)

t = k - min_delay

if t <= 0:
    print(-1)
else:
    for i in range(t):
        print(i)