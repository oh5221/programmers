# 최소 필요 피로도 / 소모 피로도
# 탐험할 수 있는 최대 던전 수

# 1. k와 최소 필요 피로도가 동일하다면 -> 이걸 먼저
# 2. 이후에는 (최소 필요 피로도 - 소모 피로도) 큰 순서로?
# 3. 같다면 최소 필요 피로도가 높은 순서로
# 76, [[72, 29], [44, 28], [72, 4], [59, 22]] -> 3
answer = 0
N = 0
visited = []
def dfs(k, cnt, dungeons):
    global answer
    
    # 최대 던전 수
    if cnt > answer:
        answer = cnt
        
    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k-dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0
    
def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer