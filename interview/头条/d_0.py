n = int(input())
c = []
for i in range(n):
    c.append([int(a) for a in input().split()])

path_length=[]
path_vertexs=[]  

def find_path(j, n, c, path_length, path_vertexs):
    path_vertexs.append(j)     
    row = c[j]  
    copy_row = [value for value in row]
    walked_vertex = []
    for i in path_vertexs:
        walked_vertex.append(copy_row[i])
    for vertex in walked_vertex:
        copy_row.remove(vertex)

    if len(path_vertexs) < n:
        min_e=min(copy_row)
        j=row.index(min_e)
        path_length.append(min_e)
        find_path(j, n, c, path_length, path_vertexs)
    else:
        min_e=c[j][0]
        path_length.append(min_e)
        path_vertexs.append(0)
    return path_vertexs,path_length

path_vertexs,path_length = find_path(0, n, c, path_length, path_vertexs)
print(sum(path_length))

# if __name__ == "__main__":
#     # c=[[0,2,6,5],
#     # [2,0,4,4],
#     # [6,0,4,2],
#     # [5,4,2,0]]