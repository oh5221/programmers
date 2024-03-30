def solution(s):
    # answer = s.split() # 단어 별로 구분하기 위함
    answer = list(s)
    # print(answer)
    
    '''
    for words in answer:
        word = words[0].upper() + words[1:].lower()
        # print(word)
        JadenCase.append(word)
    '''
    
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
    print(answer)
    
    return answer