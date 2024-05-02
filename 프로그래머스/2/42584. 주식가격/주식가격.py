def solution(prices):
    answer = []
    for i in range(len(prices)):
        time = 0 # 마지막 가격은 0초간 안 떨어진 거니까 기본값 0으로 설정
        for j in range(i+1, len(prices)):
            time += 1 # 일단 한번 가격이 설정되면 1초간 유지된 거니까 1
            if prices[i] > prices[j]:
                break
        answer.append(time)
    return answer