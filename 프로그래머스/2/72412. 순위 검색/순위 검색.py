from itertools import combinations
from collections import defaultdict
import bisect

def solution(info, query):
    info_dict = defaultdict(list)

    # info 정규화해서 조합 만들기
    for i in info:
        i = i.split()
        conditions = i[:-1]
        score = int(i[-1])

        # 4개 중 어떤 자리에 '-'를 넣을지 조합
        for n in range(5):  # 0~4
            for comb in combinations(range(4), n):
                temp = conditions.copy()
                for idx in comb:
                    temp[idx] = "-"
                key = " ".join(temp)
                info_dict[key].append(score)

    # 점수 정렬
    for key in info_dict:
        info_dict[key].sort()

    # 쿼리 처리
    answer = []
    for q in query:
        q = q.replace("and", "").split()
        score = int(q[-1])
        key = " ".join(q[:-1])
        scores = info_dict.get(key, [])

        # 이진 탐색으로 score 이상인 개수 구하기
        idx = bisect.bisect_left(scores, score)
        answer.append(len(scores) - idx)

    return answer
