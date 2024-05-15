from collections import deque
n, m = input().split()
n, m = int(n), int(m)
# print(n, m)

maze = []
for i in range(n):
    maze.append(list(input()))
# print(maze)
for mz in maze:
    for i in range(len(mz)):
        mz[i] = int(mz[i])
# print(maze)
# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 여부를 체크하는 배열. 0이면 방문 x
visited = [[0 for _ in range(m)] for _ in range(n)]
queue = deque([(0, 0)])

while queue:
    x, y = queue.popleft() # 0, 0에서 시작
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # nx, ny가 배열 범위 안이고
        if 0 <= nx < n and 0 <= ny < m:
            # 방문한 적 없고 지나갈 수 있으면
            if visited[nx][ny] == 0 and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

print(maze[n-1][m-1])
