from collections import deque
def solution(priorities, location):
    q = deque(priorities)
    
    answer = 1
    while priorities:
        process = q.popleft()
        # 나머지 프로세스 중에 더 우선순위가 높은 게 있다면
        if q and process < max(q):
            # 다시 집어넣음 
            q.append(process)
            
            if location == 0:
                # 지금 process랑 location이 똑같으면 맨 마지막으로 바뀜
                location = len(q) - 1
            else:
                # 앞으로 한칸 당겨지니까 -1
                location -= 1
        # 지금 프로세스가 가장 우선순위가 높으면
        else:
            if location == 0:
                # 그게 location과 동일하면
                return answer
            else:
                # 하나가 처리된 거니까 +1
                answer += 1
                location -= 1
    
    return answer