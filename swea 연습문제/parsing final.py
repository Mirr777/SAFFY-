text = ["GOLDABCGOLD", "HELLOWORLD", "WHITEGOLD"]
a = 0
b = 0
answer = 0
for i in text:
    a = 0
    while True:
        a = i.find("GOLD", b)
        b = a+4
        answer +=1
        if a == -1:
            answer -= 1
            break    
print(answer)