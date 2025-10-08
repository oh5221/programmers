# 일주일동안 설정한 출근 시간에 안 늦으면 상품
# 출근희망시각+10분까지 ㄱㄴ, 주말은 이벤트해당x
# 시간: timelogs//100 분: timelogs%100
# startday = 
def solution(schedules, timelogs, startday):
    answer = 0
    # 희망시각 1150일 때 -> 11 * 60 + 50 = 710
    # 1200까지 오키 -> 12 * 60 = 720
    # 1210 도착했다면 -> 12 * 60 + 10 = 730
    
    for i, timelog in enumerate(timelogs):
        count = 0
        active_time = schedules[i] // 100 * 60 + schedules[i] % 100 + 10
        for idx, time in enumerate(timelog):
            time = time // 100 * 60 + time % 100
            if startday == 7:
                startday = 1
                continue
            if startday < 6 and time <= active_time:
                count += 1
            
            startday += 1
        if count == 5:
            answer += 1
    return answer