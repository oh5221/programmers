# 선물 주고받은 기록 바탕으로 다음 달의 max(선물받음) 구하기
# a와 b 사이에 선물 주고받은 기록 있을 때 -> 더 많이 준 사람이 다음달에 받음
# 주고받은 기록 없거나 같다면 -> 선물지수 큰 사람이 받음
# 선물지수 = 자기가 준 선물 - 받은 선물
# 선물지수도 같으면 주고받지 않음
"""
["muzi frodo",
 "muzi frodo", 
 "ryan muzi",
 "ryan muzi", 
 "ryan muzi", 
 "frodo muzi",
 "frodo ryan", 
 "neo muzi"]
    give:
 	{'muzi': {'ryan': 0, 'frodo': 2, 'neo': 0},
    'ryan': {'muzi': 3, 'frodo': 0, 'neo': 0},
    'frodo': {'muzi': 1, 'ryan': 1, 'neo': 0},
    'neo': {'muzi': 1, 'ryan': 0, 'frodo': 0}}
    
    take:
    {'muzi': {'ryan': 3, 'frodo': 1, 'neo': 1},
    'ryan': {'muzi': 0, 'frodo': 1, 'neo': 0},
    'frodo': {'muzi': 2, 'ryan': 0, 'neo': 0},
    'neo': {'muzi': 0, 'ryan': 0, 'frodo': 0}}
    
    무지: 프로도한테 받음
    라이언: 무지한테 받음
    프로도: 라이언한테 받음
    네오: 무지한테 받음, 프로도한테 받음
    
    선물 지수:
    {'muzi': -3, 'ryan': 2, 'frodo': 0, 'neo': 1}
"""
def solution(friends, gifts):
    give = {name: {other_name: 0 for other_name in friends 
                   if other_name != name} for name in friends}
    take = {name: {other_name: 0 for other_name in friends 
                   if other_name != name} for name in friends}
    present = {name:0 for name in friends}
    for gift in gifts:
        # 공백을 기준으로 나누었을 때
        g = gift.split(" ")
        giver, taker = g[0], g[1]
        give[giver][taker] += 1
        take[taker][giver] += 1
        
    # 선물 지수
    for name in friends:
        present[name] = sum(give[name].values()) - sum(take[name].values())
        
    next_month = {name:0 for name in friends}
    
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            a, b = friends[i], friends[j]
            a_to_b = give[a][b]
            b_to_a = give[b][a]
            
            # a가 준 게 더 많다면 a가 받음
            if a_to_b > b_to_a:
                next_month[a] += 1
            # b가 준 게 더 많다면 b가 받음
            elif b_to_a > a_to_b:
                next_month[b] += 1
            # 동일하다면
            else:
                # a의 선물 지수가 더 높으면 a가 받음
                if present[a] > present[b]:
                    next_month[a] += 1
                # b가 더 높으면 b가 받음
                elif present[b] > present[a]:
                    next_month[b] += 1
    return max(next_month.values())
    
    