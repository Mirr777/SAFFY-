def bomb(arr_list,m,n,l):
    dx = [0, 1, 0, -1, 0]
    dy = [0, 0, 1, 0, -1]
    bomb_list = []
    str_list = ""
    for i in range(m):
        for j in range(n):
            if arr_list[i][j] == "@":
                bomb_list.append([i,j])
    for a in range(len(bomb_list)):
        for c in range(5):
            for b in range(l+1):
                if 0 <= bomb_list[a][0] + dx[c]*b <= m-1 and 0 <= bomb_list[a][1] + dy[c]*b <= n-1:
                    if arr_list[bomb_list[a][0] + (dx[c]*b)][bomb_list[a][1] + (dy[c]*b)] == "#":
                        break
                    else:
                        arr_list[bomb_list[a][0] + (dx[c]*b)][bomb_list[a][1] + (dy[c]*b)] = "%"
    for k in range(m):
        for l in range(n):
            str_list += arr_list[k][l]
        str_list += "\n"
    return str_list



a, b = map(int,input().split())
c = int(input())
arr = []
for i in range(a):
    arr.append(list(map(str,input())))
print(bomb(arr,a,b,c))
