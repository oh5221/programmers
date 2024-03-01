def solution(arr, divisor):
    # arr 중 divisor로 나누어 떨어지는 값을 오름차순 정렬
    # 나누어 떨어지는 값이 없으면 -1
    
    answer = []
    check = False
    
    # 1. arr을 하나씩 체크하며 나누어 떨어지면 answer에 추가
    for i in arr:
        if i % divisor == 0:
            check = True
            answer.append(i)
    
    # 2. 나누어 떨어지는 element가 하나도 없으면 -1 추가
    if check == False:
        answer.append(-1)
    
    # 3. 정렬
    return sorted(answer)
    