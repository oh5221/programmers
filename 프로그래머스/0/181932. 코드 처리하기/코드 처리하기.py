def solution(code):
    mode = False
    ret = ''
    for idx, i in enumerate(code):
        if i == "1":
            mode = not mode
        
        elif idx % 2 == 0 and mode == False:
            ret += i
        
        elif idx % 2 == 1 and mode == True:
            ret += i
        
    if ret == '':
        return "EMPTY"
    else:
        return ret
        