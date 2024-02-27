def solution(number, n, m):
    if number <= 10 or number >=100: return 0
    if n < 2 or n > 10: return 0
    if m < 2 or m > 10: return 0

    if number % n == 0 and number % m == 0:
        return 1
    
    return 0