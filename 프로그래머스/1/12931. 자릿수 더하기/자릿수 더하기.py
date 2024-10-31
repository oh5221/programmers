# while n 을 해서
# n이 0이 될 때까지 n % 10 한 값을 answer에 더하면
def solution(n):
    answer = 0
    
    while n:
        answer += n % 10
        n = n // 10

    return answer