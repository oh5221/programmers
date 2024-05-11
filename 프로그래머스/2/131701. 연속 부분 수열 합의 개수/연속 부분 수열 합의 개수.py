from itertools import combinations
def solution(elements):
    # 숫자 하나씩 돌아가면서 세기
    answer = set()
    for i in range(len(elements)):
        combi_sum = 0
        for j in range(len(elements)):
            combi_sum += elements[(i+j)%len(elements)]
            # print(combi_sum)
            answer.add(combi_sum)
    return len(answer)
            
    
    # ▽ 연속되는 수만 참고한 게 아니라 모든 수로 순열 만듦
    # combinations로 1부터 len(elements)까지 조합 뽑아서 list화
    # 부분순열의 합을 set로 하는 게 나을 거 같기도?
    
    # answer = set()
    # for i in range(1, len(elements)+1):
    #     for sub in combinations(elements, i):
    #         answer.add(sum(sub))
    # print(answer)
    # return len(answer)
