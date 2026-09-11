path = []

def KFC(lev, n):
    if lev == n:
        if len(path) == len(set(path)):
            print(*path)
        return

    for i in range(1,7):
        path.append(i)
        KFC(lev + 1, n)
        path.pop()
N = int(input())
KFC(0, N)

# def KFC(lev):  순열 기본 코드
#     if lev == 2:
#         print(*path)
#         return
#
#     for i in range(3):
#         if used[i] == 1: continue       continue 처리 잘하기
#         used[i] = 1    # dat 배열 사용하기
#         path.append(i)
#         KFC(lev + 1)
#         path.pop()
#         used[i] = 0    # dat 배열 초기화화# path = []
# used = [0] * 4
# KFC(0)
