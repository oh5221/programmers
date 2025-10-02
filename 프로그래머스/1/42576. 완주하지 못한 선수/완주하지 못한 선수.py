# 참여: part  / 완주: complete 
# 완주하지 못한 선수의 이름은?
# participant를 dictionary로 만들어서 -> 이름이 key, count가 value
# completion에 해당하면 -1 하기
from collections import Counter
def solution(participant, completion):
    counts = Counter(participant)
    
    for name in completion:
        if name in counts:
            counts[name] -= 1
    
    for name in counts:
        if counts[name] != 0:
            return name