# 단품 조합 -> 코스요리
# 이전에 손님들이 같이 주문했던 것으로.
# 2명 이상의 손님이 같이 주문한 최소 2개 이상 메뉴로 코스요리
# 주문한 조합을 2~len(메뉴수) 해서 dictionary 만들기
# course에 해당하는 단품메뉴들 return. (course가 [2, 3, 4]라면 메뉴2개, 메뉴3개, 메뉴4개로)
# solution 알파벳도 오름차순으로 정렬돼야함
from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    order_comb = {c:defaultdict(int) for c in course}
    # order_set = set() # order_set 만들지 말고 order로 combination 만들면서 바로 체크?
    
    for order in orders:
        order = sorted(order)
        for c in course:
            if len(order) >= c:
                for o in combinations(order, c):
                    order_comb[c]["".join(o)] += 1
    
    for c in course:
        if not order_comb[c]:
            continue
        max_cnt = max(order_comb[c].values())
        for order, value in order_comb[c].items():
            if max_cnt >= 2 and value == max_cnt:
                answer.append(order)
    
    return sorted(answer)