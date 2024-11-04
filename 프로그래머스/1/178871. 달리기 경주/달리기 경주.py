# 추월한 선수의 이름을 부름
def solution(players, callings):
    answer = []
    rank = {name:idx for idx, name in enumerate(players)}
    
    for call in callings:
        idx = rank[call] # 현재 등수
        rank[call] -= 1
        rank[players[idx - 1]] += 1
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
    return players