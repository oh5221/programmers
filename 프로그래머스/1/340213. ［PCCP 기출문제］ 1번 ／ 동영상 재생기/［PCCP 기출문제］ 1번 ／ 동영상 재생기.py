# prev 입력받으면 10초 전으로 이동. 현재 10초 미만이면 0분 0초로
# next 입력받으면 10초 후로 이동. 남은 길이가 10초 미만이면 끝으ㅡ로
# 오프닝 건너뛰기: op_end로 이동
# video_len 동영상 길이 pos 기능 수행 직전 재생위치 commands 입력
def solution(video_len, pos_len, op_start_len, op_end_len, commands):
    answer = ''
    # 계산이 용이하게 전부 '초' 단위로 변경
    video_minute, video_second = video_len.split(":")
    pos_minute, pos_second = pos_len.split(":")
    ops_minute, ops_second = op_start_len.split(":")
    ope_minute, ope_second = op_end_len.split(":")
    
    video = int(video_minute) * 60 + int(video_second) 
    pos = int(pos_minute) * 60 + int(pos_second) # 여기가 기준점
    op_start = int(ops_minute) * 60 + int(ops_second)
    op_end = int(ope_minute) * 60 + int(ope_second)
    
    for command in commands:
        if op_start <= pos <= op_end: # 오프닝 구간이면 스킵
            pos = op_end
            # print("skip openning", pos)
        if command == 'next':
            if pos < video - 10:
                pos += 10
                # print("next", pos)
            else:
                pos = video
                # print("next", pos)
        if command == 'prev':
            if pos > 10:
                pos -= 10
                # print("prev", pos)
            else:
                pos = 0
                # print("prev", pos)
    
    # command 다 적용했는데 오프닝 구간이면 스킵하기
    if op_start <= pos <= op_end: 
        pos = op_end
        # print("skip openning", pos)
    
    minute = str(pos // 60)
    second = str(pos % 60)
    if len(minute) != 2:
        minute = "0" + minute
    if len(second) != 2:
        second = "0" + second
    answer = str(minute) + ":" + str(second)
    return answer