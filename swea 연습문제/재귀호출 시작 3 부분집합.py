# mem = ["Luffy", "Zoro", "Sanji"]
# path = []
# answer = []
# def part(lev):
#     if lev == 3:
#         answer = []
#         for i in range(3):
#             if path[i] == 0:
#                 answer.append(mem[i])
#         print(*answer)
#         return
#     else:
#         for i in range(0, 2):
#             path.append(i)
#             part(lev+1)
#             path.pop()
# part(0)

# 부분집합
arr = ["Luffy", "Zoro", "Sanji"]
n = len(arr)

def get_sub(i):
    for j in range(n):
        if i & (1 << j):
            print(arr[j], end = " ")
for tar in range(1 << n):
    get_sub(tar)
    print()