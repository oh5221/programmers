def solution(n,a,b):    
    answer = 0 
    
    while a != b:
        # 한번 이기면 4번일 때 2번, 7번일 때 4번
        # 홀수면 +1, 짝수면 // 2
        a = a // 2 + 1 if a % 2 != 0 else a // 2
        b = b // 2 + 1 if b % 2 != 0 else b // 2
            
        # 한번 이길 때마다 answer++
        answer += 1
    
    return answer