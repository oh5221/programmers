def solution(s):
    count = 0
    decimal = 0
    while(s != "1"):
        count += 1
        # s에서 제거된 0의 개수 count
        decimal += s.count("0")
        # 1의 개수를 count 후 2진변환
        s = format(s.count("1"), 'b')
        
    
    
    return [count, decimal]