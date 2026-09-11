icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 1, '*': 2, '/': 2, '+': 3, '-': 3}

stack = [''] * 100  # 0 대신 '' 로 초기화
top = -1

fx = '(6+5*(2-8)/2)'
susik = ''

for x in fx:
    if x not in '(+-*/)':  # 피연산자인 경우 출력
        susik += x
    elif x == ')':  # 여는 괄호까지 pop
        while stack[top] != '(':
            susik += stack[top]  # top + 1 대신 top 사용
            top -= 1
        top -= 1
    else:  # 연산자인 경우
        if top == -1 or icp[x] > isp[stack[top]]:
            top += 1
            stack[top] = x
        else:
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top]  # top + 1 대신 top 사용
                top -= 1
            top += 1
            stack[top] = x
print(susik)
