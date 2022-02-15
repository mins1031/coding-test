def solution(priorities, location):
    answer = 0
    priorities = [(i, idx) for idx, i in enumerate(priorities)]
    while len(priorities) > 0:
        if priorities[0] == max(priorities, key=lambda x: x[0]):
            if priorities[0][1] == location:
                answer += 1
                break
            answer += 1
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))

    return answer


priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))
