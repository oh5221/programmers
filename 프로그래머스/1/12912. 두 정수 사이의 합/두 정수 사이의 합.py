# a = 1 b = 4
# 작은 수부터 큰 수까지 for문 돌려 가면서? answer에 더하기
def solution(a, b):
    answer = 0
    if a < b:
        for i in range(a, b+1):
            answer += i    
        return answer
    elif b < a:
        for i in range(b, a+1):
            answer += i    
        return answer
    else:
        return b        
