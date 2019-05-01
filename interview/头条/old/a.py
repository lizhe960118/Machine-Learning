import sys

def isBad(point_i, point_j, zero_h):
    i, h_i = point_i[0], point_i[1]
    j, h_j = point_j[0], point_j[1]
    _, h = zero_h

    if h_i <= h:
        right_x = (h * i) / (h - h_i)    
        if h_j >= (h * (right_x - j)) / right_x:
            return True
    else:
        left_x = (h * i) / (h - h_j)
        if h_j >= (h * (left_x + j)) / left_x:
            return True

if __name__ == "__main__":
    # 读取第一行的n
    line1 = sys.stdin.readline().strip().split()
    # print(line1)
    n = int(line1[0])
    h = int(line1[1])
    line2 = sys.stdin.readline().strip().split()
    arr_h = [int(a) for a in line2]
    # print(n, h, arr_h)
    zero_h = (0, h)
    points = []
    points.append([0, h])
    for i in range(n):
        points.append([i+1, arr_h[i]])

    result = [0 for i in range(n + 1)]
    for i in range(2, n+1):
        tmp = i - 1
        while tmp != 0:
            if isBad(points[i], points[tmp], zero_h):
                result[i] = tmp
                break
            else:
                tmp = result[tmp] 
    
    for i in range(1, n+1):
        print(result[i])