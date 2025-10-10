# 특정 멜로디는 음악 맨끝+음악 처음 일수도있음
# 네오가 기억한 멜로디가 있다고 해서 무조건 그 노래가 아닐 수도 있음 
# -> 해당되는 노래 중에 재생시간 가장 긴 음악 반환
# -> 시간도 같으면 먼저 입력된 음악 반환. 아예 없으면 "(None)" 반환
# 음은 1분에 1개씩 재생되고, 음악은 재생 시간만큼 반복됨 (음악길이>재생시간) 이면 0:재생시간 까지
import re
def solution(m, musicinfos):
    # musicinfo는 문자열. "시간시간,종료시각,음악제목,악보정보" -> 쉼표로 split
    musics = []
    idx = 0 # 순서 표기용
    m_lst = []
    m = list(m)
    while m:
        if len(m) > 1:
            if m[1] == '#':
                m_lst.append(''.join(m[0:2]))
                del m[0:2]
            else:
                m_lst.append(m[0])
                del m[0]
        else:
            m_lst.append(m[0])
            del m[0]
    # print(f"찾을 음계: {m_lst}")
    
    for musicinfo in musicinfos:
        info = musicinfo.split(',')
        # print(info)
        start_time, end_time = info[0].split(':'), info[1].split(':')
        time = (int(end_time[0]) * 60 + int(end_time[1])) - (int(start_time[0]) * 60 + int(start_time[1]))
        # print(time)
        
        music = list(info[3])
        music_lst = []
        i = 0
        while music:
            if len(music) > 1:
                if music[i+1] == '#':
                    music_lst.append(''.join(music[i:i+2]))
                    del music[i:i+2]
                else:
                    music_lst.append(music[i])
                    del music[i]
            else:
                music_lst.append(music[i])
                del music[i]
        # print(music_lst)
        
        full_music = music_lst * (time // len(music_lst))
        full_music += music_lst[:(time % len(music_lst))]
        # print(full_music)
        
        for i in range(0, len(full_music) - len(m_lst) + 1):
            if m_lst == full_music[i:i+len(m_lst)]:
                musics.append([time, info[2], idx])
                break
        idx += 1
    musics.sort(key=lambda x:(-x[0], x[2]))
    # print(musics)
    return musics[0][1] if musics else "(None)"