def solution(s):
    count = 0
    i = 0
    length = len(s)
    
    while i < length:
        x = s[i]
        count_x = 0
        count_not_x = 0
        
        while i < length:
            if s[i] == x:
                count_x += 1
            else:
                count_not_x += 1
            i += 1
            if count_x == count_not_x:
                break
        
        count += 1
    
    return count