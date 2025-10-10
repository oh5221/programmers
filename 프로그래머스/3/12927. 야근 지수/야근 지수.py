# 야근 피로도 = 남은작업량^2
# n시간 = 퇴근까지 남은 시간
# 퇴근 시간까지 일하고 남은 작업량을 각각 제곱해서 더한 게 야근 피로도임

# works에서 가장 큰 수, 두번째로 작은 수를 뽑음
# jangyo에서 (가장 큰 수 - 두번쨰로 작은 수)만큼 n에서 뺌
# 다 같은 수라면 -> 앞에서부터 n // len(works)만큼 뺌
# 각 값을 제곱해서 더함
from heapq import heappush, heappop, heapify
def solution(n, works):
    answer = 0
    jangyo = sum(works) - n # 남은 일
    
    if jangyo <= 0: # 남은 시간 안에 작업 끝낼 수 있다면
        return 0
    
    heap_works = [-work for work in works] # 최댓값 찾아야하니까 -로 넣기
    heapify(heap_works)
    
    while n:
        max_num = heappop(heap_works)
        heappush(heap_works, max_num + 1)
        n -= 1

    for work in heap_works:
        answer += work ** 2
    return answer