# 1등 - 6개 / 2등 - 5개 / 3등 - 4개 / 4등 - 3개 / 5등 - 2개 / 6등 - 그 외
# 낙서된 번호 - 0
# 
def solution(lottos, win_nums):
    answer = []
    count, zero_cnt = 0, 0
    for num in lottos:
        if num in win_nums:
            count += 1
        if num == 0:
            zero_cnt += 1
            
    answer.append(min(6, 6 - (count + zero_cnt) + 1))
    answer.append(min(6, 6 - count + 1))
    return answer