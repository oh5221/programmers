# 2차원 격자
# 위, 아래, 왼, 오 중 같은 색의 칸은?
[["blue", "red", "orange", "red"], 
 ["red", "red", "blue", "orange"], 
 ["blue", "orange", "red", "red"], 
 ["orange", "orange", "red", "blue"]]
def solution(board, h, w):
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    answer = 0
    
    for i in range(4):
        if 0 <= h + dh[i] < len(board) and 0 <= w + dw[i] < len(board):
            if board[h][w] == board[h+dh[i]][w+dw[i]]:
                answer += 1
            
    
    return answer