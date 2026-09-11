path = []
answer = 0
def cafe(lev, friend, j):
    global answer
    if lev == j:
        answer += 1
        return
    else:
        for i in range(len(friend)+1):
            if i > max(path,default = 0):
                path.append(i)
                cafe(lev+1, friend, j)
                path.pop()



friend = list(map(str,input().split()))
for j in range(2,len(friend)+1):
    cafe(0,friend,j)
print(answer)