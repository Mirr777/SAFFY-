path = []
answer = 0
def card(lev,N):
    global answer
    if lev == 4:
        answer += 1
        return answer
    else:
        for i in N:
            if path == [] or i-3 <= path[-1] <= i+3:
                path.append(i)
                card(lev+1,N)
                path.pop()





N = list(map(int,input()))
card(0,N)
print(answer)
