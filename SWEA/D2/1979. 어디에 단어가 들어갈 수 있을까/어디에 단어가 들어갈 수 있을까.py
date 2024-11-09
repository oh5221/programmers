# SWEA 1979 어디에 단어가 들어갈 수 있을까 https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PuPq6AaQDFAUq&categoryId=AV5PuPq6AaQDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1
# 10,000번째 참여자~ ><
# n * n 크기의 단어 퍼즐에서 특정 k 길이 단어가 들어갈 수 있느 자리 수는?
# 들어갈 수 있는 거 - 1 없는 거 - 0

T = int(input()) # 테스트 케이스 수
for test_case in range(1, T+1):
    n, k = map(int, input().split())
    arr = []
    for i in range(n):
        row = list(map(str, input().split()))
        row = "".join(row)
        arr.append(row)
    # print(arr)

    chk = "1" * k # 체크리스트
    # print(chk)
    row_cnt = 0 # 가로줄
    col_cnt = 0 # 세로줄

    # 가로줄로 계산할 때
    for row in arr:
        row_list = row.split("0")
        for rl in row_list:
            if chk == rl:
                row_cnt += 1
    # print(row_cnt)

    # 세로줄로 볼 때
    zip_arr = ["".join(col) for col in zip(*arr)]
    for col in zip_arr:
        col_list = col.split("0")
        for cl in col_list:
            if chk == cl:
                col_cnt += 1

    print(f"#{test_case} {col_cnt + row_cnt}")