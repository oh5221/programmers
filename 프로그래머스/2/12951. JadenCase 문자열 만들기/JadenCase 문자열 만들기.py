def solution(s):
    answer = list(s)
    # print(answer)
    
    for idx, word in enumerate(answer):
        if word.isalpha():
            # idx가 0이거나 answer[idx-1]이 공백이면 .upper()
            if idx == 0 or answer[idx-1].isspace():
                answer[idx] = word.upper()
            
            # answer[idx-1]이 공백이 아니면 .lower()
            elif answer[idx-1].isspace() == False:
                answer[idx] = word.lower()
    
    # print(answer)    
    
    answer = "".join(answer)
    # print(answer)
    
    return answer