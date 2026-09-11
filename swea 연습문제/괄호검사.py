def test(arr_list):
    stack = []
    n = 0
    while True:
        if n == len(arr_list):
            break
        elif arr_list[n] == "(" or arr_list[n] == ")" or arr_list[n] == "{" or arr_list[n] == "}":
            if stack == [] and (arr_list[n] == "}" or arr_list[n] == ")"):
                return 0
            elif stack == []:
                stack.append(arr_list[n])
                n = n + 1
            elif stack[-1] == "(" and arr_list[n] == ")":
                stack.pop()
                n = n+1
            elif stack[-1] == "{" and arr_list[n] == "}":
                stack.pop()
                n = n+1
            else:
                stack.append(arr_list[n])
                n = n+1
        else:
            n = n+1
    if stack == []:
        return 1
    else:
        return 0
T = int(input())
for tc in range(1,T+1):
    arr = str(input())
    print(f"#{tc} {test(arr)}")