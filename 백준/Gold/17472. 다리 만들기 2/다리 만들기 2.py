import sys
from collections import deque

input = sys.stdin.readline

def label_islands():
    label = 1
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                label += 1
                q = deque([(i, j)])
                land[i][j] = label
                while q:
                    x, y = q.popleft()
                    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1:
                            land[nx][ny] = label
                            q.append((nx, ny))
    return label - 1  # 총 섬 개수

def find_bridges():
    edges = []
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    for x in range(n):
        for y in range(m):
            if land[x][y] > 1:
                from_island = land[x][y]
                for dx, dy in directions:
                    length = 0
                    nx, ny = x+dx, y+dy
                    while 0 <= nx < n and 0 <= ny < m:
                        if land[nx][ny] == from_island:
                            break
                        elif land[nx][ny] == 0:
                            length += 1
                            nx += dx
                            ny += dy
                        else:
                            if length >= 2:
                                to_island = land[nx][ny]
                                edges.append((length, from_island, to_island))
                            break
    return compress_edges(edges)

def compress_edges(edges):
    edge_dict = {}
    for length, a, b in edges:
        if a > b:
            a, b = b, a
        if (a, b) not in edge_dict or edge_dict[(a, b)] > length:
            edge_dict[(a, b)] = length
    return [(l, a, b) for (a, b), l in edge_dict.items()]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x

def kruskal(edges, island_count):
    edges.sort()  # 다리 길이 기준 오름차순
    total = 0
    used = 0
    for length, a, b in edges:
        if find(a) != find(b):
            union(a, b)
            total += length
            used += 1
    # 모든 섬이 하나로 연결되었는지 확인
    roots = set(find(i) for i in range(2, island_count+2))
    if len(roots) == 1:
        return total
    else:
        return -1

if __name__ == "__main__":
    n, m = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(n)]

    island_count = label_islands()

    edges = find_bridges()

    parent = [i for i in range(island_count+3)]  # 섬 번호가 2부터 시작하므로 여유있게

    answer = kruskal(edges, island_count)
    print(answer)
