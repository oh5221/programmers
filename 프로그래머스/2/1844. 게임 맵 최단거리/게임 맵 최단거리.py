from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    
    # 상하좌우 이동
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 방문 여부와 이동 거리를 저장하는 배열
    visited = [[0 for _ in range(col)] for _ in range(row)]
    
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        
        for i in range(4):
            # 상하좌우로 이동
            nx = x + dx[i]
            ny = y + dy[i]
            
            # nx, ny가 배열 범위 안이고
            if 0 <= nx < row and 0 <= ny < col:
                # maps가 1이고, 방문한 적이 없을(-1) 때
                if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny)) # 지금 방문한 곳에서 
        
    if visited[row-1][col-1]:
        return maps[row-1][col-1]
    else:
        return -1
    return answer