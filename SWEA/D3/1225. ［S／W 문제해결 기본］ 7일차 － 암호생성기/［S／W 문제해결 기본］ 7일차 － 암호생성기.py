# SWEA 1225 암호생성기 https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AV14uWl6AF0CFAYD&categoryId=AV14uWl6AF0CFAYD&categoryType=CODE&problemTitle=%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

# 8개의 숫자 입력받고 -> .popleft() 하고 -1 하고 append하고
# 다음 숫자는 .popleft() -2 append
# 그 다음은 3... 이렇게 5까지 감소
# 숫자가 0보다 작아지면 0으로 유지, 이 때의 값이 암호가 됨

for test_case in range(1, 11):
    _ = int(input()) # 테스트 케이스 번호. 입력 무시
    numbers = list(map(int, input().split()))
    minus = 1

    while True:
        num = numbers.pop(0)

        if minus > 5:
            minus = 1

        if num - minus <= 0:
            numbers.append(0)
            break

        numbers.append(num - minus)
        minus += 1
    answer = ""
    for i in range(len(numbers)):
        answer += str(numbers[i]) + " "
    print(f"#{test_case} {answer}")