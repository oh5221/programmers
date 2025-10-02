# 종류별로 1개씩만 입고, 전날이랑 다른의상이거나 추가됐으면 다른방식임
# 조합 몇개할수있는지 체크
# [[의상명, 종류]] 형태의 list임 -> 종류 기준으로 dict화?
from collections import Counter
from itertools import combinations
def solution(clothes):
    answer = 1
    cloth_dict = Counter([cloth[1] for cloth in clothes])
    
    for cnt in cloth_dict.values():
        answer *= (cnt + 1)
        
    answer -= 1
    return answer
