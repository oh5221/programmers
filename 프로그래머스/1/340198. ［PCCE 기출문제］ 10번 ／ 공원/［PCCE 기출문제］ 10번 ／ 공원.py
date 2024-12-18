# # mats -> 돗자리 한 변 길이 / park -> 현재 공원 자리 배치도
# # 깔 수 있는 가장 큰 돗자리 return . 없으면 -1 return
# """
# -1이 비어 있는 공간.
# -1일 때, park[i:i+mat][j:j+mat]의 길이가 mat라면?
# 저 조건에 해당되면 mat는 가능한 것. 가능 리스트에 옮김
# 이건 문제에 나온 테케만 해당되는 것. 중간에 알파벳이 끼어 있으면 안 됨
# return(max(가능리스트))
# """

# def solution(mats, park):
#     # park = [["A", "A", "-1", "B", "B", "B", "B", "-1"],
#     #     ["A", "A", "-1", "B", "B", "B", "B", "-1"],
#     #     ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
#     #     ["D", "D", "G", "-1", "-1", "-1", "E", "-1"],
#     #     ["D", "D", "-1", "-1", "H", "-1", "-1", "F"],
#     #     ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]] # 결과: 2
#     answer = 0
#     st = ""
#     available = [-1] # 아무것도 append되지 않으면 -1
    
#     rows = len(park)
#     cols = len(park[0])
    
#     for mat in mats:
#         # print(mat)
#         for i in range(rows - mat + 1):
#             for j in range(cols - mat + 1):
#                 if not any(park[x][y].isalpha() for x in range(i, i+mat) for y in range(j, j+mat)):
#                     available.append(mat)
#                     break

    
#     return max(available)

def solution(mats, park):
    rows = len(park)
    cols = len(park[0])

    # 큰 돗자리부터 검사할 수 있도록 mats 내림차순 정렬
    mats.sort(reverse=True)
    
    for mat in mats:
        # park 내에 mat x mat 크기의 빈 공간이 존재하는지 확인
        for i in range(rows - mat + 1):
            for j in range(cols - mat + 1):
                # 해당 mat x mat 영역에 알파벳이 하나라도 있으면 즉시 중단
                if all(not park[x][y].isalpha() for x in range(i, i + mat) for y in range(j, j + mat)):
                    return mat  # 가장 큰 돗자리 크기를 찾으면 즉시 반환
    return -1  # 적합한 돗자리를 찾지 못한 경우 -1 반환
