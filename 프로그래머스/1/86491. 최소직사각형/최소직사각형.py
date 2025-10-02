# 가로를 무조건 더 큰 숫자가 오도록
# 작은것중에 큰숫자 * 큰것중에 큰숫자 
def solution(sizes):
    answer = 0
    max_garo, max_sero = 0,0
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
    
    for size in sizes:
        if size[0] > max_garo:
            max_garo = size[0]
        if size[1] > max_sero:
            max_sero = size[1]
    return max_garo * max_sero