def tree(lev):
    if lev == 3:
        return
    for i in range(2):
        tree(lev+1)
    print(lev)

tree(0)