# 귤 크기별로 수확해서 서로 다른 종류의 수를 최소화함
# [1, 2, 2, 3, 3, 4, 5, 5] -> 2개씩 있는 거 (2, 3, 5) * 2
def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    set_t = set(tangerine)
    dictionary = {s:0 for s in set_t}
    for t in tangerine:
        dictionary[t] += 1
    # print(dictionary)
    
    tan_cnt = sorted(dictionary.items(), key=lambda x:x[1], reverse=True)
    # print(tan_cnt)
    
    for tc in tan_cnt:
        size, cnt = tc[0], tc[1]
        if k <= 0:
            break
        k -= cnt
        answer += 1
    
#     while k > 0:
#         t = tan_cnt[0]
#         k -= t[1]
#         answer += 1
    
    return answer