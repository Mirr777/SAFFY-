# for i in range(1,4):
#     for j in range(1,4):
#         for k in range(1,4):
#             for l in range(1,4):
#                 print(i, j, k, l)

def recursive_loop(i, j, k, l):
    if i >= 4:
        return
    if l < 4:
        print(i, j, k, l)
        recursive_loop(i, j, k, l + 1)
    elif k < 3:
        recursive_loop(i,j,k+1,1)
    elif j < 3:
        recursive_loop(i,j+1,1,1)
    else:
        recursive_loop(i+1,1,1,1)

recursive_loop(1,1,1,1)