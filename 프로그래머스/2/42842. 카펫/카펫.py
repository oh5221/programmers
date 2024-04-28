def solution(brown, yellow):
    # row_b * col_b == (row_y + 2) * (col_y + 2)
    # brown: 2(a + b) - 4
    # yellow: 2((a-2) + (b-2)) - 4 == 2a + 2b - 12
    
    # answer = [a, b]
    answer = []
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            row_y = yellow // i
            col_y = i
            if 2 * (row_y + col_y) + 4 == brown:
                return [row_y + 2, col_y + 2]
    