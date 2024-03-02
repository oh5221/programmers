def solution(n, lost, reserve):
    # 전체 학생 수 n
    # 체육복 도난당한 lost 
    # 여벌 체육복 reverse
    
    lost.sort()
    reserve.sort()
    
    # 중복값까지 한 for문에서 제거하니까 오류가 나나? 싶어서 따로 분류
    for r in reserve[:]:
        if r in lost:
            lost.remove(r)
            reserve.remove(r)
    
    
    # 반복문 진행하는 list와 remove하는 list 구분
    for r in reserve:
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)
    
    answer = n - len(lost)
    return answer
    
    '''
    처음 풀이. 이렇게 푸니까 한번 remove한 이후 반복문을 진행하지 못함
    
    for l in lost:
        print(l)
        # 도난당한 학생이 가져왔을 경우
        if l in reserve:
            lost.remove(l)
        
        # 도난당한 학생이 다른 학생에게 빌릴 수 있을 경우
        elif l - 1 in reserve:
            lost.remove(l)
        
        elif l + 1 in reserve:
            lost.remove(l)
    '''
