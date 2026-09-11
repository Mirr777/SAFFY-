arr_ground = [[4, 5, 7, 6], [1, 5, 5, 4], [1, 1, 1, 1]]
arr_person = [[5, 6, 4], [1, 5, 3]]

dat = [[0] * 3 for _ in range(2)]

for i in range(2):
    for j in range(3):
        for k in arr_ground:
            for l in k:
                if l == arr_person[i][j]:
                    dat[i][j] +=1
for _ in range(2):
    print(*dat[_])
