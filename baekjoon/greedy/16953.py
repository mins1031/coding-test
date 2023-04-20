start, goal = map(int, input().split())
temp_goal = goal
result = 1
while True:
    if temp_goal == start:
        break

    if temp_goal == 1:
        result = -1
        break

    if temp_goal % 10 == 1:
        temp_goal = temp_goal // 10
    elif temp_goal % 2 == 0:
        temp_goal = temp_goal // 2
    else:
        result = -1
        break

    result += 1

print(result)

