def solution(id_list, report, k): 
    report_set = set(report) # 똑같은 신고 제거하기 위해 set에
    report_dict = {user: 0 for user in id_list} # 신고당한 횟수
    
    # 신고당한 사람은 +1 해줌
    for r in report_set:
        r = r.split(' ')
        report_dict[r[1]] += 1
    # print(report_dict)
    
    suspended = []
    for user, count in report_dict.items():
        # dictionary를 key, value 순으로 돌리면서
        if count >= k:
            # count가 k를 넘으면 정지 유저에 포함시킴
            suspended.append(user)
    # print("정지유저", suspended)
    
    mailed = {user: 0 for user in id_list} # 메일 받은 횟수
    for rep in report_set:
        rep = rep.split(' ')
        # 신고당한 사람이 정지 유저에 포함되면
        if rep[1] in suspended:
            # 신고한 사람을 key로 갖는 value에 +1 해줌
            mailed[rep[0]] += 1
    # print(mailed)
    
    answer = []
    for user in id_list:
        # mailed dictionary의 value를 list에 추가
        answer.append(mailed[user])
    
    return answer
    
    """
    reported = [0] * len(id_list) # 신고 당한 횟수 count
    emailed = [0] * len(id_list)
    r = []
    s = [] # 신고자, 신고당한자 체크용
    
    for r in report:
        # 신고자 / 신고당한자 공백 기준 나눔
        r = r.split(' ')
        s.append([r[0], r[1]])
        for i in range(len(id_list)):
            # 신고당한 자가 id_list에 있는 사람과 같으면
            if r[1] == id_list[i]:
                reported[i] += 1
    print(reported)
    print(s)
    
    for i in range(len(id_list)):
        if reported[i] >= k: # 신고당한 횟수가 k 이상이면
            for j in range(len(id_list)):
                if s[i][0] == id_list[j]:
                    emailed[j] += 1
                    
    print(emailed)
    """