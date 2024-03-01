def solution(x):
    list_x = list(map(int, str(x)))
    answer = False
    if x % sum(list_x) == 0:
        answer = True
    return answer