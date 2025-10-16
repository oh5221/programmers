# 백준 14940 쉬운 최단거리 https://www.acmicpc.net/problem/14940

# 모든 지점에 대해 목표지점(2)까지의 거리를 구한다
# 0은 못가는곳 1은 갈수있는곳임

import sys
from collections import deque
def bfs(graph, visited, start):
    dx, dy = [0, -1, 1, 0], [-1, 0, 0, 1]
    queue = deque([start])
    visited[start[0]][start[1]] = 0

    while queue:
        s = queue.popleft()
        nx, ny = s[0], s[1]

        for i in range(4):
            x, y = nx + dx[i], ny + dy[i]

            if 0 <= x < n and 0 <= y < m:
                if visited[x][y] == -1 and graph[x][y] == 1:
                    visited[x][y] = visited[nx][ny] + 1
                    queue.append((x, y))


n, m = map(int, sys.stdin.readline().split()) # n 세로 m 가로 (둘 다 2 이상 1000 이하)
visited = [[-1] * m for _ in range(n)] # 방문 표시
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start = (i, j)
        elif graph[i][j] == 0:
            visited[i][j] = 0

bfs(graph, visited, start)

for i in range(n):
    for j in range(m):
        print(visited[i][j], end= ' ')
    print()