n = int(input())

arr = [[1, 5, 10, 15], [15, 15, 20, 30]]
dat = [0]*31
for i in arr:
    for j in i:
        dat[j] += 1

print(dat[n])