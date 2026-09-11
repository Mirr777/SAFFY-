# for i in range(1,4):
#     for j in range(1,4):
#         print(i, j)

def recursive(n):
    m = 1
    if n == 4: return
    else:
        print(n, m)
        print(n, m+1)
        print(n, m+2)
        return recursive(n+1)

recursive(1)