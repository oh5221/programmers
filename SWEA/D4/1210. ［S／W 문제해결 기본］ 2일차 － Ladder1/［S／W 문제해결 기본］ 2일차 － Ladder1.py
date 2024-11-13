# SWEA 1210 Ladder1 https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh&categoryId=AV14ABYKADACFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 사다리게임. 좌우로 이동 가능하면 좌/우로 이동 (0, -1), (0, 1)
# 방향 전환하면 아래로만
# 사다리는 1 도착점은 2

# ladder[0][i]가 1이면 그걸 시작점으로 잡음
# start = [0, 4, 6, 9] 이렇게 저장해 두기?
# 그러고 0부터 length까지 돌리면서 [s][i+1] 혹은 [s][i-1]이 1이면 s += 1
# 아니면 i += 1하는 식으로? 그래서 s가 length - 1이랑 같은데 2이면 답이고 아니면 답 아님
def check(sx, sy, dir):
    if sx == length - 1: # sx가 마지막에 다다랐는데
        if ladder[sx][sy] == 2: # 값이 2면
            return 1
        else: # 아니면
            return -1

    if dir == 0: # 아래로 내려가는 중이면
        if sy + 1 < length and ladder[sx][sy + 1] == 1: # 오른쪽에 길이 있으면
            return check(sx, sy + 1, 1) # direction을 1로 설정
        elif 0 <= sy - 1 < length and ladder[sx][sy - 1] == 1: # 왼쪽에 길이 있으면
            return check(sx, sy - 1, -1) # direction -1로 설정
        else:
            return check(sx + 1, sy, 0)
    elif dir == 1: # 오른쪽으로 가는 중이면 -> 왼쪽 고려하지 않음
        if sy + 1 < length and ladder[sx][sy + 1] == 1:  # 오른쪽에 길이 있으면
            return check(sx, sy + 1, 1)  # direction을 1로 설정
        else:
            return check(sx + 1, sy, 0)
    elif dir == -1: # 왼쪽으로 가는 중이면 -> 오른쪽 고려하지 않음
        if 0 <= sy - 1 < length and ladder[sx][sy - 1] == 1: # 왼쪽에 길이 있으면
            return check(sx, sy - 1, -1) # direction -1로 설정
        else:
            return check(sx + 1, sy, 0)
for test_case in range(1, 11):
    _ = int(input()) # 테케 입력 무시
    ladder = []
    start = []
    answer = []

    lad = list(map(int, input().split()))
    ladder.append(lad)

    length = len(lad)

    for i in range(length - 1):
        ladder.append(list(map(int, input().split())))
    # print(ladder)

    for i in range(length):
        if ladder[0][i] == 1:
            start.append(i)

    for s in start:
        chk = check(0, s, 0)
        if chk == 1:
            print(f"#{test_case} {s}")
