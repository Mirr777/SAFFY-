S = str(input())
answer = 0
for i in range(len(S)):
    if S[i] == "[":
        b = S.find("]",i)
        if b == -1:
            break
        else:
            answer += int(S[i+1:b])
    elif S[i] == "{":
        b = S.find("}",i)
        if b == -1:
            break
        else:
            answer *= int(S[i+1:b])
print(answer)