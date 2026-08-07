from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque(0 for _ in range(bridge_length))
    bridge_weight = 0
    
    while truck_weights or bridge_weight > 0:
        time += 1
        
        bridge_weight -= bridge.popleft()
        
        if truck_weights and bridge_weight + truck_weights[0] <= weight:
            bridge_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
        
    return time