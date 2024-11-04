# 한 명 빼고 마라톤 완주함 -> 누군지 return
# 동명이인 있을 수 있음
def solution(participant, completion):
    answer = ''
    part = {name:0 for name in participant}
    complete = {name:0 for name in completion}
    
    for p in participant:
        part[p] += 1
    for c in completion:
        part[c] -= 1
    for name, value in enumerate(part):
        if part[value] > 0:
            return value