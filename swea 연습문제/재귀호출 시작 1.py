# 중복 순열
# 재귀호출 + stack
# 재귀호출 + path 배열 (흔적 배열)

path = []


def KFC(lev):
    if lev == 3:
        print(*path)
        return

    for i in range(1, 7):  # branch 3, 카드 종류가 3개이므로
        path.append(i)
        KFC(lev + 1)
        path.pop()


KFC(0)