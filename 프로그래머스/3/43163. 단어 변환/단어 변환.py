def count_alpha(word, begin):
    cnt = 0
    for i in range(len(word)):
        if word[i] == begin[i]:
            cnt += 1
    return cnt
def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    #
    for word in words:
        # 한 가지 알파벳만 다르다면
        if count_alpha(word, begin) == len(word) - 1:
            begin = word
            answer += 1 
        
        if count_alpha(begin, target) == len(word)-1:
            answer += 1
            return answer