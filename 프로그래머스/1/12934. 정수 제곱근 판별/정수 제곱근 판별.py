import math
def solution(n):
    # 양의 정수 n이 정수 x의 제곱인지 아닌지
    # 제곱이면 (x+1)**2 아니면 -1 return
    
    # 단순히 n**(1/2).is_integer()으로 판단하면 제곱근이 아닌 수도 그냥 +1 해서 제곱해버림
    if n**(1/2) % 1 == 0:
        return (n**(1/2) + 1) ** 2
        # math 라이브러리 사용이 안 되는 듯...?
        # return (math.sqrt(n) + 1) ** 2
    else:
        return -1