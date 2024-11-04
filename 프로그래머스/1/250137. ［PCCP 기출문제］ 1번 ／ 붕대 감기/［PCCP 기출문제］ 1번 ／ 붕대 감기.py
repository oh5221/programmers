def solution(bandage, health, attacks):
    t, x, y = bandage  # 시전 시간, 초당 회복량, 추가 회복량
    current_health = health  # 현재 체력
    consecutive_success = 0  # 연속 성공 시간
    time = 0  # 현재 시간 인덱스
    attack_index = 0  # 공격 리스트 인덱스
    
    while attack_index < len(attacks):
        attack_time, damage = attacks[attack_index]
        
        # 몬스터 공격 전까지 붕대 감기 시전
        while time < attack_time:
            # 체력이 0 이하면 사망
            if current_health <= 0:
                return -1
            
            # 붕대 감기 시전 중
            current_health += x  # 초당 회복량만큼 체력 회복
            current_health = min(current_health, health)  # 최대 체력 초과 방지
            consecutive_success += 1
            
            # 시전 시간만큼 붕대 감기에 성공한 경우 추가 회복
            if consecutive_success == t:
                current_health += y
                current_health = min(current_health, health)  # 최대 체력 초과 방지
                consecutive_success = 0  # 연속 성공 초기화
            
            time += 1  # 시간 증가
        
        # 몬스터 공격을 받는 경우
        if time == attack_time:
            current_health -= damage  # 피해량만큼 체력 감소
            consecutive_success = 0  # 공격을 받으면 연속 성공 초기화
            attack_index += 1  # 다음 공격으로 넘어감
            time += 1  # 시간 증가
            
    # 공격이 모두 끝난 후 체력을 반환
    return current_health if current_health > 0 else -1
