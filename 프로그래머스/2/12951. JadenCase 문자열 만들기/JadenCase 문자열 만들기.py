def solution(s):
    answer = ''
    for i in s.lower().split(' '):
        if answer == '':
            answer += i.capitalize()
        else:
            answer += ' '+i.capitalize()
    return answer