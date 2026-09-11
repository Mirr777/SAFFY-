text = "ABCDEFABCKKKKKABC"
answer = 0
a = 0
while True:
    if a == -1:
        break
    else:
        a = text.find("ABC",a+3)
        answer +=1
print(answer)