# 한명은 왼쪽부터 한명은 오른쪽부터
# 중앙에 물 있고 물 먼저 먹는 놈이 이김
# 칼로리 낮은 것부터 / 음식 종류랑 양 같아야 함
# food는 idx의 수
def solution(food):
    answer = ""
    for i in range(len(food)):
        answer += str(i) * (food[i]//2)
    
    return answer + "0" + answer[::-1]