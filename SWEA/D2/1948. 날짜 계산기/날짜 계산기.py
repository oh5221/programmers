# SWEA 1948 날짜 계산기 https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PnnU6AOsDFAUq&categoryId=AV5PnnU6AOsDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

calendar = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 각 월별 날짜
T = int(input())
for test_case in range(1, T+1):
    dates = list(map(int, input().split()))
    first_date = sum(calendar[:dates[0]], dates[1]) # 3/1이면 2월까지 전부 sum + 주어진날짜
    second_date = sum(calendar[:dates[2]], dates[3])

    print(f"#{test_case} {second_date - first_date + 1}") # 날짜 뺄셈이라 +1