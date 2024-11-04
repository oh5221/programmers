# R/T C/F J/M A/N
# 0~6까지 점수 있고 
# 0, 6은 3점 / 1, 5은 2점 / 2, 4는 1점 / 3은 0점
# 선택한 게 있으면 -> 점수 높은 걸로
# 선택한 게 없으면 -> 사전순으로 빠른 거
def solution(survey, choices):
    answer = ''
    mbti = {alpha:0 for alpha in ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']}
     
    for i in range(len(survey)):
        if choices[i] < 4: # 1, 2, 3
            mbti[survey[i][0]] += (4 - choices[i])
        if choices[i] > 4: # 5, 6, 7
            mbti[survey[i][1]] += (choices[i] - 4)
    
    if mbti['R'] >= mbti['T']:
        answer += 'R'
    elif mbti['T'] > mbti['R']:
        answer += 'T'
    
    if mbti['C'] >= mbti['F']:
        answer += 'C'
    elif mbti['F'] > mbti['C']:
        answer += 'F'
        
    if mbti['J'] >= mbti['M']:
        answer += 'J'
    elif mbti['M'] > mbti['J']:
        answer += 'M'
    
    if mbti['A'] >= mbti['N']:
        answer += 'A'
    elif mbti['N'] > mbti['A']:
        answer += 'N'
            
    return answer