# 위/아래/왼/오 중 같은 색으로 칠해진 칸의 개수
# board[h][w]와 이웃한 칸에서 같은 색인 칸의 개수
def solution(board, h, w):
    n = len(board)
    count = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h][w] == board[h_check][w_check]:
                count += 1
    
    return count