n = int(input()) # 회의 수

meeting = []

for i in range(n):
    meeting.append(list(map(int, input().split())))


# meeting을 종료 시간, 시작 시간 기준으로 정렬
meeting = sorted(meeting, key=lambda x:(x[1], x[0]))
def max_meetings(meeting):
    end_time = 0
    count = 0
    selected = []

    for m in meeting:
        start, end = m # 시작, 종료시간 설정
        if start >= end_time:
            selected.append(m)
            end_time = end
            count += 1

    return count

print(max_meetings(meeting))