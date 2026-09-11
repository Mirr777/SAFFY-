def get_find(text):
    answer = []
    for i in text:
        a = i.find("[")
        b = i.find("]")
        if a != -1 or b != -1:
            answer.append(i[a+1:b])    
    return answer


text = ["ABCQ", "B[4]R", "CCDA", "BT[15]"]
print(*get_find(text))