def solution(wallpaper):
    # files 배열에 wallpaper의 파일 위치를 저장
    # [".#...", "..#..", "...#."]면 [1, 2, 3] 이런 식으로
    
    files_row = set() # 파일이 있는 행 저장
    files_col = [] # 각 행에서 파일이 있는 위치 저장
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                files_row.add(i)
                files_col.append(j)
    print(files_row)
    print(files_col)
    answer = []
    answer.append(min(files_row))
    answer.append(min(files_col))
    answer.append(max(files_row) + 1) # 마지막 파일을 포함하려면 파일 위치 +1씩 해줘야
    answer.append(max(files_col) + 1)
    return answer