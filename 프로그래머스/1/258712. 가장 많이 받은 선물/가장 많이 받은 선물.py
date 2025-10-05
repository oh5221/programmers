# 선물 주고받은 기록이 있어야 -> 더 많은 선물 준 사람이 다음 달에 선물 받음
# 주고받은 기록 없거나 같다면 -> 선물 지수 더 큰 사람이 작은 사람한테 받음
# 선물 지수 = 모든 친구들에게 준 선물 수 - 받은 선물 수
# 선물 지수까지도 같다면 주고받지 않음
# 한 사람이 받는 선물 중 가장 많이 받는 선물 수는?
def solution(friends, gifts):
    answer = 0
    gift_score = {name:0 for name in friends} # 선물 지수
    take_gifts = {name:0 for name in friends} # 받을 선물 수
    gnt = {name:[] for name in friends} # give and take
    
    for gift in gifts:
        g = gift.split()
        # 선물 지수 계산
        gift_score[g[0]] += 1
        gift_score[g[1]] -= 1
        # key가 준 사람, value가 받은 사람
        gnt[g[0]].append(g[1])
        
    # print(gift_score)
    # print(gnt)
    
    # 선물을 주고받은 기록이 있다면 == gnt에 기록돼있다면
    # muzi, frodo일 때. gnt[muzi] 안에 frodo 수 랑 gnt[frodo] 안에 muzi 수 비교
    # 더 크면 -> key값이 하나 더 받음 (take_gifts[muzi] += 1)
    # 같으면 -> 선물 지수 비교 (gift_score[muzi], gift_score[frodo]) -> take_gifts[muzi] += 1
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if friends[i] == friends[j]:
                continue
            # print(take_gifts)
    
            if gnt[friends[j]].count(friends[i]) > gnt[friends[i]].count(friends[j]):
                take_gifts[friends[j]] += 1
            elif gnt[friends[j]].count(friends[i]) < gnt[friends[i]].count(friends[j]):
                take_gifts[friends[i]] += 1
            else:
                if gift_score[friends[i]] > gift_score[friends[j]]:
                    take_gifts[friends[i]] += 1
                elif gift_score[friends[i]] < gift_score[friends[j]]:
                    take_gifts[friends[j]] += 1
            
    
    # print(take_gifts)
    return max(take_gifts.values())