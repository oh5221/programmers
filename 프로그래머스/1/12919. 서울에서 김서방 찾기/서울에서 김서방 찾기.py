def solution(seoul):
    for idx, kim in enumerate(seoul):
        if kim == "Kim":
            return ("김서방은 " + str(idx) + "에 있다")