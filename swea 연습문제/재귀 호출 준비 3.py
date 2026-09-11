def tree(n):
    if n == 6:
        return
    print(n, end = " ")
    tree(n+1)
    print(n, end = " ")
tree(0)