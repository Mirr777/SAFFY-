a,b,c = map(str,input().split())

text = "ABCDE"
answer = []
dat = [0] * 100
alpha_list = [a,b,c]
for i in range(5):
    dat[ord(text[i])] +=1

for j in alpha_list:
    if dat[ord(j)] == 1:
        answer.append("O")
    else:
        answer.append("X")
print(*answer)
