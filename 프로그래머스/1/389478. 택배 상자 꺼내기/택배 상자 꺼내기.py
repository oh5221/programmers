# 1~n 택배상자 -> 왼부터 오른쪽으로 택배상자 놓음
# 가로로 w개 놓으면 오->왼으로
def solution(n, w, num):
    answer = 0
    boxes = []
    box = []
    
    for i in range(0, n, w):
        box = list(range(i+1, min(i+w+1, n+1)))
        if len(box) < w:
            box += [0] * (w - len(box))
        if (i//w) % 2 == 1:
            box.reverse()
        boxes.append(box)
            
    
    for row_idx, row in enumerate(boxes):
        if num in row:
            col_idx = row.index(num)
            break

    count = 0
    for i in range(row_idx, len(boxes)):
        if boxes[i][col_idx] != 0:
            count += 1
            
    return count