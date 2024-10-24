# 45 -> 1200
# 45 // 3 -> 15 and 45 % 3 -> 0
# 15 // 3 -> 5 and 15 % 3 -> 0
# 5 // 3 -> 1 and 5 % 3 -> 2
# 1 // 3 -> 0 and 1 % 3 -> 1
def solution(n):
    answer = 0
    num = []
    reverse_num = []
    
    while n:
        num.append(n % 3)
        n = n // 3
    
    reverse_num = num[::-1]
    for idx in range(len(reverse_num)):
        answer += reverse_num[idx] * (3 ** idx)
    
    return answer