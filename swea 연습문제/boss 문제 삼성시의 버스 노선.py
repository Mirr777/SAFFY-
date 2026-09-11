def bus_stop(A1,B1,C1,N,P):
    bus_number = [0] * 5001
    answer = []
    for i in range(N):
        a = A1[i]
        b = B1[i]
        for j in range(a,b+1):
            bus_number[j] +=1
    for k in range(P):
        answer.append(bus_number[C1[k]])
    return answer




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    A1 = []
    B1 = []
    for n in range(N):
        a1, b1 = map(int,input().split())
        A1.append(a1)
        B1.append(b1)
    P = int(input())
    C1 = []
    for i in range(P):
        C1.append(int(input()))
    print("#", end = "")
    print(tc, end =" ")
    print(*bus_stop(A1,B1,C1,N,P))