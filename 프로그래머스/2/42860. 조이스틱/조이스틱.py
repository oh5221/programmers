# 1A 2B 3C 4D 5E
# 6F 7G 8H 9I 10J
# 11K 12L 13M 14N 15O 
# 16P 17Q 18R 19S 20T 
# 21U 22V 23W 24X 25Y 26Z
def solution(name):
    answer = 0
    n = len(name)
    for ch in name:
        answer += min(ord(ch) - ord('A'), 26 - (ord(ch) - ord('A')))
    
    move = n - 1
    for i in range(n):
        next_i = i+1
        
        # 모든 문자열이 'A'이기 때문에 name 대상이 A연속이라면
        # 피해서 돌아가는 게 빠름
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        
        move = min(move, 2*i + n-next_i, i + 2*(n-next_i))
        
    return answer+move