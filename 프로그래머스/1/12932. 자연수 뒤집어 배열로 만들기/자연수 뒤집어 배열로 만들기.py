def solution(n):
    # 자연수를 list로 만들기?
    # 뒤에서부터 list에 집어넣기 
    # stack 형태로
    answer = []
    n = list(map(int, str(n)))
    
    # print(n) # list화 체크용
    
    for i in reversed(n):
        answer.append(i)
    
    # print(answer)
    
    return answer   