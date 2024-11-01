# n * n 크기 격자
# 위에는 크레인, 오른쪽은 바구니
# 인형이 없으면 빈칸, 격자 아래부터 차곡차곡
# 크레인은 가장 위에 있는 것만 (dequeue?)
# 집어올리면 바구니에 쌓음 -> 같은 거 2개가 쌓이면 터져서 사라짐
# 터뜨려서 사라진 인형의 개수를 구해라
"""
[[0,0,0,0,0],
 [0,0,1,0,3],
 [0,2,5,0,1],
 [4,2,4,4,2],
 [3,5,1,3,1]]
 
 [[0,0,0,0,0],
 [0,0,0,0,0],
 [0,0,5,0,0],
 [0,2,4,0,2],
 [0,5,1,3,1]]
 
basket = [4, 3, 1, 1, 3, 2, 4]
"""
def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        for i in range(len(board)):
            # move에 해당하는 칸의 맨 위의 숫자를
            if board[i][move - 1] > 0:
                num = board[i][move-1]
                
                # board에서 제외한다
                board[i][move - 1] = 0
                
                # basket에 전에 들어가 있던 숫자와 다르다면
                if len(basket) == 0 or num != basket[-1]:
                    # 바로 넣고
                    basket.append(num)
                # 마지막 숫자와 num이 같다면
                elif len(basket) > 0 and num == basket[-1]:
                    answer += 2 # answer에 두 개를 더하고
                    basket.pop() # 맨 뒤에 걸 빼고
                break
                
    return answer