# 다트 3번 던져서 점수 합으로 실력 겨룸
# S -> 점수**1 / D -> 점수**2 / T -> 점수**3
# 스타상(*) -> 현재 점수와 직전 점수 각각 2배씩. 첫번째에 나오면 현재 점수만 2배
# 아차상(#) -> 현재 점수 마이너스 (전체 합에서 이걸 마이너스 처리?)
# 스타상 2번(**)이면 4배 / 아차상-스타상(#*) 이면 -2배 

# dartResult를 일단 for문을 돌림
# .isnumber() 맞나? 이거랑 .isalpha()로 구분
# 10을 어떻게 십이라고 인식하지?..................
# 1부터 10까지니까 dart가 0이면 score.pop()하고 10을 넣자
# 아니 아니잖아 0부터 10까지잖아 악 
def solution(dartResult):
    n = ''
    score = []
    # 1D2S#10S
    for dart in dartResult:
        if dart.isnumeric():
            n += dart
        elif dart.isalpha():
            int_n = int(n)
            score.append(int_n)
            n = ''
            # S는 원 점수 그대로라서 조건 안 넣음
            if dart == 'D':
                score[-1] = score[-1] ** 2
            elif dart == 'T':
                score[-1] = score[-1] ** 3
        else:
            if dart == '*':
                if len(score) >= 2:
                    score[-1] = score[-1] * 2
                    score[-2] = score[-2] * 2
                else:
                    score[-1] = score[-1] * 2
            elif dart == '#':
                score[-1] = score[-1] * -1
    
    return sum(score)