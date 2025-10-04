import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, v, visited):
    global order
    visited[v] = order     # 방문 순서 기록
    for nxt in graph[v]:
        if visited[nxt] == 0:
            order += 1
            dfs(graph, nxt, visited)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
order = 1

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

dfs(graph, R, visited)

for i in range(1, N+1):
    print(visited[i])