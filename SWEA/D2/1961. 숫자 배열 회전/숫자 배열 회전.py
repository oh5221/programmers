# SWEA 1961 숫자 배열 회전 https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# n * n 행렬의 오른쪽으로 90도, 180도, 270도 회전한 모양은?
# 3 <= n <= 7
import copy
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = []
    answer = [[""] for _ in range(n)]# 정답 저장
    for i in range(n):
        arr.append(list(input().split()))

    # 90도
    # arr[0][0] arr[1][0] arr[2][0]
    # arr[1][0] arr[1][1] arr[2][1]
    # arr[2][0] arr[2][1] arr[2][2]
    rotate = [[0 for _ in range(n)] for _ in range(n)]
    rotate = copy.deepcopy(arr)
    for _ in range(3): # 90도 180도 270도 3번
        arr = copy.deepcopy(rotate)
        # print("arr", arr)
        for i in range(n):
            row = ""
            for j in range(n-1, -1, -1):
                row += arr[j][i]
                rotate[i][n - j - 1] = arr[j][i]
        # print(rotate)
            answer[i].append(row)
        # print(answer)

    print(f"#{test_case}")
    for i in range(n):
        for j in range(1, 4):
            print(answer[i][j], end=" ")
        print()