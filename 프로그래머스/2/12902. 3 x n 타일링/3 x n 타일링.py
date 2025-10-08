# 가로 2고 세로 1인 직사각형으로
# 세로 3이고 가로 n인 바닥 가득 채우기
# 경우의 수를 1_000_000_007으로 나눈 나머지 return

# n = 2: 3
# n = 4: f(2) * 3 + 2 = 11
# n = 6: f(4) * 3 + f(2) * 2 + 2 = 33 + 6 + 2 = 41
# n = 8: f(6) * 3 + f(4) * 2 + f(2) * 2 + 2 = 123 + 22 + 6 + 2 = 123 + 30 = 153
def solution(n):
    answer = [0, 3, 11]
    if n % 2 == 1:
        return 0
    for i in range(6, n+1, 2):
        answer.append(answer[-1] * 3 + sum(answer[:-1]) * 2 + 2)
    return answer[-1] % 1_000_000_007