arr_criminal = [[5,7, 9, 55], [30, 10, 6, 8]]
arr_apartment = [[1, 2, 3, 4], [5, 7, 10, 15]]

dat = [0] * 60

for i in range(2):
    for j in range(4):
        for k in range(2):
            for l in range(4):
                if arr_criminal[i][j] == arr_apartment[k][l]:
                    dat[arr_criminal[i][j]] += 1
print(sum(dat), 8-sum(dat))
