def solution(friends, gifts):
    # 각 친구가 다른 친구에게 준 선물의 개수를 저장할 딕셔너리
    gifted = {friend: {} for friend in friends}
    # 각 친구의 선물 지수를 저장할 딕셔너리
    gift_idx = {friend: 0 for friend in friends}
    
    # 선물 기록을 분석하여 gifted와 gift_idx 업데이트
    for gift in gifts:
        giver, receiver = gift.split()
        if receiver in gifted[giver]:
            gifted[giver][receiver] += 1
        else:
            gifted[giver][receiver] = 1
        gift_idx[giver] += 1
        gift_idx[receiver] -= 1
    
    # 각 친구가 다음 달에 받을 선물의 수를 저장할 리스트
    will_get = [0 for _ in friends]
    
    # 모든 친구 쌍에 대해 선물을 주고받은 결과에 따라 will_get 업데이트
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            curr = friends[i]
            another = friends[j]
            
            gifts_curr_to_another = gifted[curr].get(another, 0)
            gifts_another_to_curr = gifted[another].get(curr, 0)
            
            if gifts_curr_to_another > gifts_another_to_curr:
                will_get[i] += 1
            elif gifts_curr_to_another < gifts_another_to_curr:
                will_get[j] += 1
            else:
                if gift_idx[curr] > gift_idx[another]:
                    will_get[i] += 1
                elif gift_idx[curr] < gift_idx[another]:
                    will_get[j] += 1

    # 가장 많이 선물을 받는 친구의 선물 수를 반환
    return max(will_get)

# def solution(friends, gifts):
#     # 선물을 가장 많이 받을 친구가 받을 선물의 수는?
    
#     # 2차원 배열 실패 -> dict로 저장
#     gift_map = {f: {t: 0 for t in friends if t != f} for f in friends}
    
#     # 선물 데이터를 기반으로 각 친구 간의 선물 수를 카운트
#     for gift in gifts:
#         giver, receiver = gift.split()
#         gift_map[giver][receiver] += 1
    
#     # 각 친구의 선물 지수 계산 (준 선물 수 - 받은 선물 수)
#     gift_scores = {f: 0 for f in friends}
#     for giver in gift_map:
#         for receiver in gift_map[giver]:
#             gift_scores[giver] += gift_map[giver][receiver]
#             gift_scores[receiver] -= gift_map[giver][receiver]

#     # 다음 달에 선물을 받게 될 수를 카운트
#     gifts_received = {f: 0 for f in friends}
#     for giver in gift_map:
#         for receiver in gift_map[giver]:
#             if gift_map[giver][receiver] > gift_map[receiver][giver]:  # giver가 더 많이 준 경우
#                 gifts_received[receiver] += 1
#             elif gift_map[giver][receiver] < gift_map[receiver][giver]:  # receiver가 더 많이 준 경우
#                 gifts_received[giver] += 1
#             elif gift_map[giver][receiver] == gift_map[receiver][giver]:  # 똑같이 주고 받은 경우
#                 if gift_scores[giver] > gift_scores[receiver]:  # 선물 지수 비교
#                     gifts_received[giver] += 1
#                 elif gift_scores[receiver] > gift_scores[giver]:
#                     gifts_received[receiver] += 1
    
#     # 가장 많이 선물을 받는 친구의 수를 반환
#     return max(gifts_received.values())

    
#     # 1. friends 배열을 이름 기준으로 dictionary화? 아니면 2차원 배열?
#     # count_friends = [] 
    
# #     # 2. gifts 배열을 2차원 배열로 ex. "muzi frodo" -> ["muzi", "frodo"]
# #     real_gifts = []
# #     for gift in gifts:
# #         real_gifts.append(gift.split(' '))
    
# #     print(real_gifts)
# #     # 3. [0]이면 해당 이름에 +1, [1]이면 해당 이름에 -1
# #     score = [0] * len(friends) # 선물 지수
# #     for gift in real_gifts:
# #         for idx, name in enumerate(friends):
# #             if gift[0] == name:
# #                 score[idx] += 1
# #             if gift[1] == name:
# #                 score[idx] -= 1
# #     print(score)
# #     answer = max(score)
# #     return answer