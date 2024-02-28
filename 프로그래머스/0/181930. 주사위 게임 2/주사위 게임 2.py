def solution(a, b, c):
    answer = a + b + c
    if a == b and b == c:
        answer *= ((a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3))
    elif a != b and b != c and a != c:
        answer = answer
    else:
        answer *= (a ** 2 + b ** 2 + c ** 2)

    return answer