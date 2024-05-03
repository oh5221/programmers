def solution(bridge_length, weight, truck_weights):
    bridge_now = [0] * bridge_length # 다리 길이 맞추기
    
    time = 0
    total_weight = 0
    while bridge_now:
        time += 1
        total_weight -= bridge_now.pop(0) # 다리에서 나가는 트럭의 무게를 빼줌
        
        if truck_weights:
            # 다음 트럭이 다리에 올라갈 수 있으면 추가
            if total_weight + truck_weights[0] <= weight:
                bridge_now.append(truck_weights.pop(0))
                total_weight += bridge_now[-1]
            else:
                # 올라갈 수 없으면 0을 추가하여 대기
                bridge_now.append(0)

    return time
