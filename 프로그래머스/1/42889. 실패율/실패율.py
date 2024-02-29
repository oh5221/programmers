def solution(N, stages):
    # 사용자가 도전 중인 스테이지 count
    # 몇 stage의 실패율인지 알아야 하니까 dict
    failCount = {}
    # 도전자 수
    player = len(stages)
    
    for i in range(1, N+1):
        if player == 0:
            failCount[i] = 0
        
        else:
            # 스테이지 못 깬 사람 수
            fail = stages.count(i)
            # 실패율
            failCount[i] = fail / player
            player -= fail
            
    # dictionary 정렬법
    # https://codechacha.com/ko/python-sorting-dict/ 참고
    answer = sorted(failCount, key = lambda x: failCount[x], reverse = True)
    
    return answer