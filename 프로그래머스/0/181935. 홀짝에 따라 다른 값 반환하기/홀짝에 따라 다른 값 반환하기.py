def solution(n):
    answer = 0
    
    if n < 0 and n > 100: return 0

    if n % 2 == 1:
        for i in range(1, n + 1, 2):
            answer = answer + i
    else:
        for i in range(2, n + 1, 2):
            answer = answer + i*i
            
    return answer