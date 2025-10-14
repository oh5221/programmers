import re
def solution(s):
    answer = len(s)
    strings = []
    
    for unit in range(1, len(s) // 2 + 1):
        compressed = "" # 압축된
        prev = s[0:unit] # 이전 문자열
        count = 1
        
        for i in range(unit, len(s), unit):
            curr = s[i:i+unit]
            # print("현재", curr, "이전", prev)
            if curr == prev:
                count += 1
            else:
                compressed += str(count) + prev if count > 1 else prev
                count = 1
                prev = curr
        compressed += str(count) + prev if count > 1 else prev # 다 끝나고 남아있는 curr 추가
        # print(compressed)
        
        if len(compressed) < answer:
            answer = len(compressed)
        
    return answer