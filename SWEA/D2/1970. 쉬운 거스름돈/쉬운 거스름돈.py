# SWEA 1970 쉬운 거스름돈 https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PsIl6AXIDFAUq&categoryId=AV5PsIl6AXIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for test_case in range(1, T+1):
    n = int(input())
    print(f"#{test_case}")
    for m in money:
        print(n // m, end=" ")
        n = n % m
    print()