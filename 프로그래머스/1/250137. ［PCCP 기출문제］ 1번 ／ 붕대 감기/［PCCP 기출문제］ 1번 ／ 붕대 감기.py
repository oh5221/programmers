# 붕대감기: 1초에 x만큼 체력 회복(최대 t초) / t초 연속으로 붕대 감으면 +y
# 공격당하면 기술 취소, 체력 회복 x / 다시 스킬쓰면 t == 0
# bandage=[시전시간(t), 1초당회복량(x), 추가회복량(y)]
# health = 최대체력
# attacks = 몬스터공격시간, 피해량
def solution(bandage, health, attacks):
    answer = health # 남은 체력
    t = 0 # 연속 붕대
    times = attacks[-1][0] # 공격 시간
    
    
    for i in range(1, times + 1):
        print(i, "초")
        
        if i == attacks[0][0]: # 몬스터가 공격할 시간이면
            answer -= attacks[0][1]
            attacks.pop(0) # 공격 끝난 시점 제거
            print("몬스터 공격 후 체력", answer)
            t = 0 # 연속 붕대 리셋
            print("붕대 리셋", t)
            if answer <= 0: # 만약 남은 체력이 0 이하면
                return -1
        elif answer < health: # 남은 체력이 전체 체력 미만이면
            answer += bandage[1] # 체력 추가
            print("붕대 감기 후 체력", answer)
            t += 1 # 연속 붕대 카운트
            print("연속 성공", t)
            if t == bandage[0]: # 시전 시간을 다 채웠으면
                answer += bandage[2] # 체력 추가
                print("붕대 전부 감음", answer)
                t = 0 # 다 감았으니까 리셋
            if answer <= 0: # 만약 남은 체력이 0 이하면
                return -1
        if answer > health:
            answer = health
                
                
    return answer