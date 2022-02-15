from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    clear_trucks = list()
    total = len(truck_weights)

    present_weight = 0
    cnt = 0
    bridge = deque()
    while len(clear_trucks) != total:
        if len(truck_weights) != 0:
            if (present_weight + truck_weights[0]) <= weight:
                present_weight += truck_weights[0]
                bridge.append([truck_weights.pop(0), cnt])

        if (cnt - bridge[0][1]) == bridge_length-1:
            present_weight -= bridge[0][0]
            clear_trucks.append(bridge.popleft())

        cnt += 1
    answer = cnt + 1
    return answer

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))