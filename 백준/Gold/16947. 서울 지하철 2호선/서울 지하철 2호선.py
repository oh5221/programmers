# 백준 16947번 "서울 지하철 2호선" https://www.acmicpc.net/problem/16947

# 지하철 51개의 역, 연결하는 구관 51개
# 지선 2개, 순환선 1개임
# 각 역과 순환선 사이의 거리는?
import sys
from collections import deque, defaultdict
n = int(sys.stdin.readline().strip())
edges = []
graph = defaultdict(list)

for _ in range(n):
    edges.append(list(map(int, sys.stdin.readline().split())))

for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

# ----- 1) 잎부터 제거해서 순환선 정점 찾기 -----
deg = [0] * (n + 1)
for v in range(1, n + 1):
    deg[v] = len(graph[v])

q = deque()
in_cycle = [True] * (n + 1)  # 일단 전부 순환이라고 가정하고 잎부터 제거
for v in range(1, n + 1):
    if deg[v] == 1:
        q.append(v)
        in_cycle[v] = False  # 잎은 순환에 포함X

while q:
    v = q.popleft()
    for nx in graph[v]:
        if in_cycle[nx]:
            deg[nx] -= 1
            if deg[nx] == 1:
                in_cycle[nx] = False
                q.append(nx)

# 이제 in_cycle[v] == True 인 정점들이 '순환선' 정점들
cycle_nodes = [v for v in range(1, n + 1) if in_cycle[v]]
# print(cycle_nodes)

# 2) 순환선 정점을 시작으로 BFS하여 거리 계산
dist = [-1] * (n + 1)
dq = deque()

for v in cycle_nodes:
    dist[v] = 0
    dq.append(v)

while dq:
    cur = dq.popleft()
    for nx in graph[cur]:
        if dist[nx] == -1:
            dist[nx] = dist[cur] + 1
            dq.append(nx)

print(*dist[1:])