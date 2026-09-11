def capcha(sample, passcode, a, b):
    start_point = 0  # sample index
    pass_point = 0  # passcode index

    while True:
        if start_point == a and pass_point != b: # sample의 index가 먼저 끝난다면
            return 0
        elif pass_point == b:
            return 1 
        elif sample[start_point] == passcode[pass_point]: # sample passcode 둘 다 맞다면
            start_point += 1 # 둘 다 index 한칸씩 이동
            pass_point +=1
        elif sample[start_point] != passcode[pass_point]: # sample passcode 가 다르면, sample index만 한칸 옮기기
            start_point += 1




K = int(input())
for i in range(K):
    n, m = map(int,input().split())
    sample_list = list(map(int,input().split()))
    passcode_list = list(map(int,input().split()))
    print(f"#{i+1} {capcha(sample_list,passcode_list,n,m)}")