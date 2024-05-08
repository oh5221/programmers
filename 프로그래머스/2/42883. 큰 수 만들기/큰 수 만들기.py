def solution(number, k):
    stack = []
    for num in number:
        # num이 stack에 가장 최근 들어간 수보다 더 크다면
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        
        # stack에 num 넣음
        stack.append(num)
        # print(stack)
    
    # 제거해야 할 자릿수가 남았다면
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)