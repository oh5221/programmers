def solution(a, d, included):
    i_included = []
    answer = 0
    for i in range(len(included)):
        i_included.append(a + d * i)
        
    for idx, i in enumerate(included):
        if i == True:
            answer += i_included[idx]
    return answer