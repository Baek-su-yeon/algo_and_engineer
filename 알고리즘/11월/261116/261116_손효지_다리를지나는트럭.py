from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)  # 다리 길이를 0(빈 공간)으로 채워 큐 생성
    truck_weights = deque(truck_weights)
    
    current_weight = 0  # 현재 다리 위의 총 무게
    time = 0            # 총 소요 시간
    
    while truck_weights:
        time += 1
        
        # 1초가 지났으므로 다리를 건넌 트럭이 있다면 다리에서 제외
        out = bridge.popleft()
        current_weight -= out
        
        # 다음 대기 트럭이 다리 무게를 견딜 수 있는지 확인
        if current_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            # 무게를 견딜 수 없으면 빈 공간(0)을 추가하여 시간 경과 반영
            bridge.append(0)
            
    # 마지막 트럭이 다리에 올라간 후, 완전히 건너는 데 걸리는 시간(bridge_length) 추가
    time += bridge_length
    
    return time