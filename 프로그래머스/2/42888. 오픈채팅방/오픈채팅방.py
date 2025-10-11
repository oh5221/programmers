# 중복닉 허용. 한사람이 들어왔다가 나갔다가 다시 들어오면서 닉변하면 이전것도 다 바뀜
# record에 uid로 사람 구분
# Enter / Leave / Change
def solution(record):
    answer = []
    record_dict = {}
    records = []
    
    for r in record:
        if r[0] == "L":
            command, uid = r.split()
        else:
            command, uid, nickname = r.split()
            record_dict[uid] = nickname
        records.append([uid, command])
    
    for r in records:
        uid, command = r[0], r[1]
        if command == "Enter":
            a = record_dict[uid] + "님이 들어왔습니다."
            answer.append(a)
        elif command == "Leave":
            a = record_dict[uid] + "님이 나갔습니다."
            answer.append(a)
    
    return answer