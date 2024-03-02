def solution(s):
    # 1. s를 공백 기준으로 나누기
    s = s.split(" ")
    sample = []
    
    # 2. 짝수번째는 대문자, 홀수번째는 소문자
    for i in s:
        string = ""
        for j in range(len(i)):
            if j % 2 == 0:
                string += i[j].upper()
            else:
                string += i[j].lower()
        # print(string)
        sample.append(string)
    
    # print(sample)
    return ' '.join(sample)