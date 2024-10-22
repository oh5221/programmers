# 0 : 9 list
# for l in list 
# l not in numbers -> answer += l 더하는 식으로
def solution(numbers):
    answer = 0
    chk_list = [i for i in range(10)]
    
    for l in chk_list:
        if l not in numbers:
            answer += l
    
    return answer