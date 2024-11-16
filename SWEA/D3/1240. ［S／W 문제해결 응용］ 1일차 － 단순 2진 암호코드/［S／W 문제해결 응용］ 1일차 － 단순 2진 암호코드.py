# SWEA 1240 단순 2진 암호코드 https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AV15FZuqAL4CFAYD&categoryId=AV15FZuqAL4CFAYD&categoryType=CODE&problemTitle=%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 암호코드는 8개 숫자, 7개의 비트 -> 가로 길이 56
# 암호코드 = (홀수 자리 합 * 3) + (짝수 자리 합) % 10 == 0

# 암호코드의 0 ~ 9까지를 저장
codes = ["0001101", "0011001", "0010011", "0111101", "0100011",
        "0110001", "0101111", "0111011", "0110111", "0001011"]
# 암호코드의 맨 앞자리는 0, 맨 뒷자리는 1로 통일되어 있음
# 각 행을 뒤에서부터 읽어서 1이 있는 자리부터 7글자를 저장
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    maze = []

    for i in range(N):
        maze.append(list(input()))
    str = []
    numbers = [] # 암호의 정보를 넣을 거임
    for i in range(N):
        idx = 0
        for j in range(M-1, -1, -1): #뒤에서부터 거꾸로 읽기
            if maze[i][j] == "1": # 1이 인식되면 암호의 마지막 부분이라는 뜻
                str = maze[i][j-55:j+1] # 56글자를 긁음
                break
        if str:
            break
    # 다 같은 암호가 반복되는 듯. 바깥에서 for문
    for i in range(0, 56, 7):
        s = "".join(str[i:i+7]) # 7글자씩 묶음
        for code in codes:
            if s == code: # str이 codes랑 동일하다면
                numbers.append(codes.index(code)) # numbers에 인덱스를 저장
                break
    # print(numbers)

    odd, even = 0, 0 # 홀수, 짝수
    for idx, num in enumerate(numbers):
        if idx % 2 == 0: # 홀수 번째면
            odd += num
        else:
            even += num

    if ((odd * 3) + even) % 10 == 0: # 홀수 * 3 + 짝수 가 10의 배수이면
        print(f"#{test_case} {odd + even}")
    else:
        print(f"#{test_case} 0")
