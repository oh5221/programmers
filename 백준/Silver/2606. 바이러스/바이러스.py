n = int(input()) # 컴퓨터의 수
con = int(input()) # 연결되어 있는 수
connection = {i: [] for i in range(1, n+1)}

# dict로 연결해서 a는 key로 b는 value로
for i in range(con):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)

# print(connection)

# 계속 타고 가려면 역시 function을...
def connect(node):
    visit[node] = 1
    for k in connection[node]:
        if not visit[k]:
            connect(k) # 재귀로 마지막까지

# 컴퓨터 방문했는지 체크할 배열
visit = [0 for i in range(n + 1)]
connect(1)

print(visit.count(1) - 1)
