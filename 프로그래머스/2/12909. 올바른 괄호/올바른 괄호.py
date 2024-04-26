def solution(s):
    answer = True
    
    if s[0] == ')' or s[-1] == '(': # 맨 처음이 )이거나 맨 끝이 (면 무조건 false
        answer = False
    else:
        if s.count('(') != s.count(')'): # (와 )의 개수가 맞지 않아도 false
            answer = False
    
    # 반례 ())((()))(()
    # 개수는 맞는데 중간에 )(가 끼어 있는 경우
    
    # 앞에서부터 돌면서 (를 stack 배열에 넣기
    # )를 만나면 stack에서 pop하기
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                answer = False
                break
            else: stack.pop()
            

    return answer
