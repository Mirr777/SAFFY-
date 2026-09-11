path = []
arr = ["A", "B", "C", "D", "E"]
def combination(lev):
    if lev == 3:
        for i in path:
            print(arr[i], end = " ")
        print()
        return
    else:
        for i in range(5):
            if i > max(path, default = -1):
                path.append(i)
                combination(lev + 1)
                path.pop()

combination(0)