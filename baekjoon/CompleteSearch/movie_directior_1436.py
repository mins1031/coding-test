n = int(input())
temp_result = str(666)
stick_count = 1
right = False
left = True
for i in range(n) :
    if right :
        temp_result = temp_result + str(stick_count)
        stick_count += 1

    if left :
        temp_result = str(stick_count) + temp_result
        stick_count += 1

    if stick_count == 5:
        stick_count = 0
        if right :
            left = True
            right = False
        else:
            left = False
            right = True

print(temp_result)