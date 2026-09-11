N = int(input())
if N % 2 ==0:
    for i in range(6):
        print(N+ i*2, end = " ")

elif N % 2 == 1:
    for j in range(11):
        print(N + j*3, end = " ")