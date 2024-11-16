# SWEA 1228 암호문 1 https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AV14w-rKAHACFAYD&categoryId=AV14w-rKAHACFAYD&categoryType=CODE&problemTitle=%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 0~ 999,999 사이의 수를 나열
# x, y, s. 앞에서부터 x의 위치 바로 다음에 y개의 숫자 s를 삽입한다.
# 수정된 결과의 처음 10개 숫자를 출력한다.
import copy
for test_case in range(1, 11):
    length = int(input()) # 암호문의 길이
    crypto = list(input().split())  # 원본 암호문

    n = int(input()) # 명령어 개수
    command = list(input().split()) # 명령어 받음
    commands = [] # 명령어 정리
    # print(command)
    x, y = 0, 0
    for i in range(len(command)):
        if command[i] == 'I':
            x = command[i + 1]
            y = command[i + 2]
            s = command[i + 3 : i + 3 + int(y)]
            commands.append([int(x), int(y), s])
    # print(commands)

    for c in commands:
        x = c.pop(0)
        y = c.pop(0)
        s = c.pop(0)
        # print(s)

        start, end = crypto[:x], crypto[x:]
        # print(start, end)
        for nums in s:
            start.append(nums)
        for nums in end:
            start.append(nums)
        crypto = copy.deepcopy(start)
        # print(crypto)

    print(f"#{test_case}", end=" ")
    for i in range(10):
        print(crypto[i], end=" ")
    print()