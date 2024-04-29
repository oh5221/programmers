def solution(progresses, speeds):
    answer = []
    
    # 각 기능 완료까지 걸리는 시간
    days = []
    for i in range(len(progresses)):
        # 기능 완료까지 걸리는 시간
        day = (100 - progresses[i]) // speeds[i]
        
        # 나누어 떨어지지 않으면 day +1
        if (100 - progresses[i]) % speeds[i] != 0:
            day += 1
        
        days.append(day)
        
    print(days) # [7, 3, 9] / [5, 10, 1, 1, 20, 1]
    copy_days = days
    
    index = 0
    
    for i in range(len(days)):
        # 현재 값보다 나중에 개발이 완료되는 기능이 있다면
        if days[index] < days[i]:
            # 더 나중에 완료되는 값의 위치 - 현재 위치를 answer에 추가함
            answer.append(i - index)
            index = i
    
    # 마지막으로 배포되어야 하는 기능들을 한번에 추가
    answer.append(len(days) - index)
    return answer