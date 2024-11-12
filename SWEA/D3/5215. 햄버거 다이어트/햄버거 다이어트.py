# SWEA 5215 햄버거 다이어트 https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

def dfs(depth, cal, score):
    global best
    if cal > limit:
        return

    # 최댓값 갱신
    best = max(best, score)

    for i in range(depth, n):
        dfs(i+1, cal+score_calory[i][1], score+score_calory[i][0])

T = int(input())
for test_case in range(1, T+1):
    n, limit = map(int, input().split()) # 재료의 수, 제한 칼로리
    score_calory = [list(map(int, input().split())) for _ in range (n)] # [맛에 대한 점수, 칼로리]
    # [[100, 200], [300, 500], [250, 300], [500, 1000], [400, 400]]

    best = 0 # 가장 점수 높은 햄버거
    dfs(0, 0, 0)
    print(f"#{test_case} {best}")
