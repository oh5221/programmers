def solution(numbers, hand):
    '''
    phone = [[1, 2, 3], 
             [4, 5, 6], 
             [7, 8, 9], 
             ['*', 0, '#']]
    '''
    
    # phone 배열의 인덱스를 전부 dict에 입력하기 (거리 계산용)
    phone = {
        1:(0, 0), 2:(0, 1), 3:(0, 2),
        4:(1, 0), 5:(1, 1), 6:(1, 2),
        7:(2, 0), 8:(2, 1), 9:(2, 2),
        '*':(3, 0), 0:(3, 1), '#':(3, 2)
    }
    
    # 왼손, 오른손 엄지가 직전에 누른 숫자를 저장한다
    left = '*'
    right = '#'
    
    answer = ''
    
    
    for num in numbers:
        if num in [1, 4, 7]:
            left = num
            answer += 'L'
        elif num in [3, 6, 9]:
            right = num
            answer += 'R'
        else:
            # 각 손가락의 키패드 위치와 숫자 간의 거리 비교
            Ldistance = abs(phone[left][0] - phone[num][0]) + abs(phone[left][1] - phone[num][1])
            Rdistance = abs(phone[right][0] - phone[num][0]) + abs(phone[right][1] - phone[num][1])
            
            if Ldistance > Rdistance:
                right = num
                answer += 'R'
            elif Rdistance > Ldistance:
                left = num
                answer += 'L'
            else:
                if hand == 'left':
                    left = num
                    answer += 'L'
                else:
                    right = num
                    answer += 'R'
    return answer