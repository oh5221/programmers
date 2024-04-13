def solution(sizes):
    # sizes[]의 max를 비교 -> 큰 값을 arr[0]에, 작은 값을 arr[1]에
    # 각 max값 곱하기
    cols = len(sizes[0])
    rows = len(sizes)
    arr = [[0 for j in range(cols)] for i in range(rows)]
    
    # [작은값, 큰값] 순으로 정렬하기
    for i in range(rows):
        if sizes[i][0] > sizes[i][1]:
            arr[i][0] = sizes[i][1]
            arr[i][1] = sizes[i][0]
        else:
            arr[i][0] = sizes[i][0]
            arr[i][1] = sizes[i][1]
    
    #print(arr)
    
    # arr[][0]의 max1, arr[][1]의 max2
    max1 = 0
    max2 = 0
    for i in range(rows):
        if max1 < arr[i][0]:
            max1 = arr[i][0]
            
        if max2 < arr[i][1]:
            max2 = arr[i][1]
    
    return max1 * max2