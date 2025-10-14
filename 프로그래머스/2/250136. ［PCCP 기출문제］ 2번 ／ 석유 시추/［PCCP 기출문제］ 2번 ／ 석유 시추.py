# bfs로. 각 열마다 시추 가능한 석유 찾기
from collections import deque
dh, dw = [0, -1, 0, 1], [-1, 0, 1, 0] # 좌 상 우 하
def bfs(i, j, land):
    q = deque([(i, j)])
    land[i][j] = now
    visited[i][j] = True
    cnt = 1 # land[i][j]에 일단 석유가 있다는 거니까 -> 1부터 시작
    
    while q:
        cx, cy = q.popleft()
        
        for i in range(4):
            x, y = cx + dh[i], cy + dw[i]
            if 0 <= x < n and 0 <= y < m and visited[x][y] == False and land[x][y] != 0:
                land[x][y] = now # 몇번 땅인지 체크
                visited[x][y] = True # 방문했다고 체크
                cnt += 1 # 석유 양 +1
                q.append([x, y])
    oils[now] = cnt # 전체 석유 양
    
def solution(land):
    global now, oils, visited, n, m
    now = 1 # 몇 번 땅인지 계산하는 용도
    oils = {} # 몇 번 땅에 석유가 얼마나 있는지 {땅번호:석유의 양}
    totals = [] # 각 열에서 석유를 얼마나 가져올 수 있는지
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    # print(visited)
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == False:
                bfs(i, j, land)
                now += 1
                
    for i in range(m):
        s = set()
        total = 0
        for j in range(n):
            if land[j][i] != 0:
                s.add(land[j][i])
                
        for t in s:
            total += oils[t]
        totals.append(total)
        
    return max(totals)