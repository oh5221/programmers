# SWEA 1954 달팽이 숫자 2차 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    snail = [[_ for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    # snail[x][y]가
    # 아니면 visited[i][j]가 True면 방향을 바꿈
    dx = [0, 1, 0, -1] # 오른쪽 아래 왼쪽 위
    dy = [1, 0, -1, 0] # 오른쪽 아래 왼쪽 위
    x, y = 0, 0
    dir = 0 # 오른쪽부터 시작

    for num in range(1, n*n+1):
        snail[x][y] = num
        visited[x][y] = True

        nx, ny = x + dx[dir], y + dy[dir]

        # nx, ny가 n**2 배열 안에 있을 때 다음 방향이 방문한 적 없는 거면
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
            x, y = nx, ny
        else: # 방문한 적 있거나 배열 범위 밖이면
            dir = (dir + 1) % 4 # 다음 방향으로 넘어감
            x, y = x + dx[dir], y + dy[dir] # x, y도 바꿈

    print(f"#{test_case}")
    for i in range(n):
        for j in range(n):
            print(snail[i][j], end=" ")
        print()