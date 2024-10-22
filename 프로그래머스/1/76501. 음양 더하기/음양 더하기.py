def solution(absolutes, signs):
    answer = 0
    for idx, num in enumerate(absolutes):
        if signs[idx] is not True:
            answer -= num
        else:
            answer += num
    return answer