def solution(numbers, target):
    answer = 0
    result = [0]
    
    
    for num in numbers:
        arr = []
        for res in result:
            arr.append(res + num)
            arr.append(res - num)
        result = arr
    
    for res in result:
        if res == target:
            answer += 1
    
    return answer