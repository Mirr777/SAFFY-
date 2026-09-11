List_8 = [0] * 8
for i in range(4):
    List_8[i] = 7
for j in range(4):
    List_8[-j-1] = 15
print(*List_8)