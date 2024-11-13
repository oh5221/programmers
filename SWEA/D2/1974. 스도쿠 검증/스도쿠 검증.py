# SWEA 1974 스도쿠 검증 https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq&categoryId=AV5Psz16AYEDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

T = int(input())
for test_case in range(1, T+1):
    sudoku = []
    flag = 0

    for i in range(9):
        sudoku.append(list(map(int, input().split())))

    for i in range(9):
        col_check = [0] * 9
        row_check = [0] * 9
        for j in range(9): # 세로줄 검증
            col_check[sudoku[j][i] - 1] += 1
            row_check[sudoku[i][j] - 1] += 1
        for t in range(9):
            if col_check[t] != 1 or row_check[t] != 1:
                flag = 1
                break

    if flag == 0:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square_check = [0] * 9
                for x in range(3):
                    for y in range(3):
                        square_check[sudoku[i+x][j+y] - 1] += 1
                for t in range(9):
                    if square_check[t] != 1:
                        flag = 1
                        break
            if flag == 1:
                break

    if flag == 1:
        print(f"#{test_case} 0")
    else:
        print(f"#{test_case} 1")