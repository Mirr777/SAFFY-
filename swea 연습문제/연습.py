N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

# Please write your code here.
milk_set = set()
people_set = set()
answer = 0
max_answer = float("-inf")
for i in range(D):
    for j in range(S):
        if sick_t[j]-1 >= t[i] and sick_p[j] == p[i]:
            milk_set.add(m[i])
for l in list(milk_set):
    people_set = set()
    for k in range(D):
        if m[k] == l:
            people_set.add(p[k])
            print(people_set)
    answer = len(people_set)
    max_answer = max(answer, max_answer)
print(max_answer)
