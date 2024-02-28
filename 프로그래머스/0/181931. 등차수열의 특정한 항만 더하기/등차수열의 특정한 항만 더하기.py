def solution(a, d, included):
    answer = 0
    for idx, i in enumerate(included):
        if i == True:
            answer += (a + d * idx)
    return answer