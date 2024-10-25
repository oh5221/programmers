# 2중for문으로 곱한거 전부 배열에 -> set으로 
def solution(numbers):
    answer = set()
    if len(numbers) > 1:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                answer.add(numbers[i] + numbers[j])
        answer = list(answer)
        answer.sort()
        return answer
    else:
        return 0