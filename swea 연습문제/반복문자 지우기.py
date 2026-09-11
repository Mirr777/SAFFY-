def string(arr_list):
    stack = []
    n = 0
    while True:
        if n == len(arr_list):
            return len(stack)
        elif stack == []:
            stack.append(arr_list[n])
            n = n + 1
        elif stack[-1] != arr_list[n]:
            stack.append(arr_list[n])
            n = n+1
        elif stack[-1] == arr_list[n]:
            stack.pop()
            n = n+1

T = int(input())
for tc in range(1,T+1):
    arr = (str(input()))
    print(f"#{tc} {string(arr)}")