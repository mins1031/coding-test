n = int(input())

current_bird = n
fly_bird_count = 1
result = 0

while True:
    if current_bird == 0:
        break

    if current_bird >= fly_bird_count:
        current_bird -= fly_bird_count
        fly_bird_count += 1
        result += 1
    else:
        current_bird -= 1
        fly_bird_count = 2
        result += 1

print(result)
