# 소수 특징: 2~n-1까지 나누어 떨어지는 수가 없다.
# 약수 구하는 것처럼 n ** (1/2) or n//2
# 조합 라이브러리 -> 이름이 기억x라서 도움받음
from itertools import combinations
def solution(nums):
    
    combi_nums = list(combinations(nums, 3))
    sum_combi = []
    # print(combi_nums)
    
    # (1,2,3) 이걸 더해서 넣을거임
    for num in combi_nums:
        sum_combi.append(sum(num))
    # print(sum_combi)
    
    answer = len(sum_combi)
    
    # 소수 특징 구하기
    for num in sum_combi:
        for i in range(2, num):
            if num % i == 0:
                answer -= 1
                break
    return answer