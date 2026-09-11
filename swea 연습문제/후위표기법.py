def back(arr_list):
    stack = []
    n = 0

    while True:
        if n == len(arr_list):
            return "error"

        elif arr_list[n] == ".":
            if len(stack) != 1:
                return "error"
            else:
                return stack[-1]

        elif arr_list[n] == "+":
            if len(stack) < 2:
                return "error"

            a = stack.pop()
            b = stack.pop()
            stack.append(b + a)
            n += 1

        elif arr_list[n] == "-":
            if len(stack) < 2:
                return "error"

            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
            n += 1

        elif arr_list[n] == "/":
            if len(stack) < 2:
                return "error"

            a = stack.pop()
            b = stack.pop()

            if a == 0:
                return "error"

            stack.append(b // a)
            n += 1

        elif arr_list[n] == "*":
            if len(stack) < 2:
                return "error"

            a = stack.pop()
            b = stack.pop()
            stack.append(b * a)
            n += 1

        else:
            stack.append(int(arr_list[n]))
            n += 1


T = int(input())

for tc in range(1, T + 1):
    arr = input().split()
    print(f"#{tc} {back(arr)}")