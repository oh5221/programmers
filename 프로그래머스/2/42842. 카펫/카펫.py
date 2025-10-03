# 중앙 노란색 / 테두리 1줄 갈색
# brown + yellow = garo * sero
# 제곱근부터 1까지 역순으로 돌면서 약수 저장 -> brown의 약수, yellow의 약수 저장
# brown, yellow의 약수들을 보면서 -> 가로 * 2 + (세로 - 2) * 2가 brown이랑 동일한 약수 추출
def solution(brown, yellow):
    # brown = 4992
    # yellow = 2493
    answer = []
    
    divisor = []
    # 약수
    for i in range(int((brown+yellow)**1/2), 0, -1):
        if (brown+yellow) % i == 0:
            if i >= int((brown+yellow)/i):
                lst = []
                lst.append(i)
                lst.append(int((brown+yellow)/i))
                divisor.append(lst)
    
#     print(f"약수: {divisor}")
    for div in divisor:
        if div[0] * 2 + (div[1] - 2) * 2 == brown:
            return div