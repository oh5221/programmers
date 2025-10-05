# t초간 x만큼의 체력 -> t초 연속 성공하면 y만큼 추가 회복
# max(체력회복량+원래체력, 최대체력). return은 남은체력 or -1 (죽음)
# 공격당하면 -> 연속성공 0, 체력감소
# bandage = [시전시간, 초당회복량, 추가회복량]
# health = 최대체력 / attacks = [공격시간, 피해량]
# attacks[-1][0]까지 for문 돌리면서?
def solution(bandage, health, attacks):
    answer = 0
    max_health = 0
    max_health = health
    time = attacks[-1][0] + 1
    stack = 0 # 연속성공스택
    
    for i in range(time):
        if i == attacks[0][0]:
            stack = 0
            health -= attacks[0][1]
            attacks.pop(0)
            # print(f"공격당함. 현재 체력: {health} 남은 공격 {attacks}")
            if health <= 0:
                # print("사망")
                return -1
            continue
        if health < max_health:
            stack += 1
            health += bandage[1]
            health = min(health, max_health)
            # print(f"회복 시전. 현재 체력: {health} 현재 스택: {stack}")
        if stack == bandage[0]:
            health += bandage[2]
            health = min(health, max_health)
            stack = 0
            # print(f"회복 스택 max. 추가 회복. 현재 체력: {health}")
    
    return health