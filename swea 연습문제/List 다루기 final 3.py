arr = [2, 5, 1, 6, 4, 3]
answer = 0
max_val = float("-inf")
min_val = float("inf")
for i in arr:
    answer += i
for j in arr:
    if max_val < j:
        max_val = j
    if min_val > j:
        min_val = j
print(answer)
print(max_val - min_val)