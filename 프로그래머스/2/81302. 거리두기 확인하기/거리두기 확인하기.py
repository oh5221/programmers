def solution(places):
    answer = []
    # 맨해튼 거리 2 이하 방향
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), 
                  (1, 1), (1, -1), (-1, 1), (-1, -1),
                  (2, 0), (0, 2), (-2, 0), (0, -2)]

    for place in places:
        grid = [list(row) for row in place]
        ok = 1  # 기본값 1 (거리두기 지킴)
        for i in range(5):
            for j in range(5):
                if grid[i][j] != 'P':
                    continue
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    # 범위 밖 무시
                    if not (0 <= ni < 5 and 0 <= nj < 5):
                        continue

                    # 1칸 거리 → 바로 위반
                    if abs(dx) + abs(dy) == 1:
                        if grid[ni][nj] == 'P':
                            ok = 0
                            break

                    # 2칸 직선 거리
                    elif abs(dx) + abs(dy) == 2 and (dx == 0 or dy == 0):
                        mid_i, mid_j = i + dx // 2, j + dy // 2
                        if grid[ni][nj] == 'P' and grid[mid_i][mid_j] != 'X':
                            ok = 0
                            break

                    # 대각선
                    elif abs(dx) == 1 and abs(dy) == 1:
                        if grid[ni][nj] == 'P' and (grid[i][nj] != 'X' or grid[ni][j] != 'X'):
                            ok = 0
                            break
                if ok == 0:
                    break
            if ok == 0:
                break
        answer.append(ok)
    return answer
