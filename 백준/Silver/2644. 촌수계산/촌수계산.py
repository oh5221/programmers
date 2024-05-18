from collections import deque

ppl = int(input())  # 사람 수
check = list(map(int, input().split()))  # 계산해야 하는 사람
n = int(input())  # 관계 수

fam = {i: [] for i in range(1, ppl + 1)}  # 가족 관계면 추가하기

for i in range(n):
    p, c = map(int, input().split())  # 부모, 자식 입력받기
    fam[p].append(c)
    fam[c].append(p)

# print(fam)

def solution(start, end, fam):
    visited = set()  # 중복 방지를 위해 set으로
    queue = deque([(start, [start])])  # dict의 key값(=연결된 노드 체크용) & 루트 체크

    while queue:
        curr, path = queue.popleft()
        if curr == end:
            return (len(path) - 1)

        visited.add(curr)
        for neighbor in fam[curr]:
            # curr을 key로 갖는 value들 중에
            if neighbor not in visited: # 첫 방문이면 (= 최단 루트면)
                visited.add(neighbor)
                # 방문한 적 없으면
                queue.append([neighbor, path + [neighbor]]) # queue에 추가

            # 방문한 적 있으면 그냥 무시하고 다음으로 넘어감 -> queue에는 첫 방문인 노드만 남음
    return -1

print(solution(check[0], check[1], fam))