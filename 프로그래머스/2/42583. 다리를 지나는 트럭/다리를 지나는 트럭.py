from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    
    time = 0
    bridge_weight = 0
    while bridge:
        time += 1
        bridge_weight -= bridge.popleft()
        
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                bridge_weight += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
        if not truck_weights and bridge_weight == 0:
            break
    return time