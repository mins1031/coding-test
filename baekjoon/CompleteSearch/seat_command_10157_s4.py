def handle_input_direction(start_x, start_y, repeat_count, direction) :
    if direction == "up":
        input_up_direction(start_x, start_y, repeat_count)
    elif direction == "down" :
        input_down_direction(start_x, start_y, repeat_count)
    elif direction == "right" :
        input_right_direction(start_x, start_y, repeat_count)
    elif direction == "left" :
        input_left_direction(start_x, start_y,repeat_count)

def change_xy(temp_x, temp_y) :
    global real_start_x, real_start_y
    real_start_x = temp_x
    real_start_y = temp_y

def input_up_direction(start_x, start_y, repeat_count) :
    global list, count
    temp_x = start_x
    temp_y = start_y
    for _ in range(repeat_count) :
        list[temp_x][temp_y] = count
        temp_x -= 1
        count += 1
    change_xy(temp_x, temp_y)

def input_down_direction(start_x, start_y, repeat_count) :
    global list, count
    temp_x = start_x
    temp_y = start_y
    for _ in range(repeat_count) :
        list[temp_x][temp_y] = count
        temp_x += 1
        count += 1
    change_xy(temp_x, temp_y)

def input_left_direction(start_x, start_y, repeat_count) :
    global list, count
    temp_x = start_x
    temp_y = start_y
    for _ in range(repeat_count) :
        list[temp_x][temp_y] = count
        temp_y -= 1
        count += 1
    change_xy(temp_x, temp_y)

def input_right_direction(start_x, start_y, repeat_count) :
    global list, count
    temp_x = start_x
    temp_y = start_y
    for _ in range(repeat_count) :
        list[temp_x][temp_y] = count
        temp_y += 1
        count += 1
    change_xy(temp_x, temp_y)

c, r = map(int, input().split())
target = int(input())
list = [[0 for _ in range(c)] for i in range(r)]

count = 1
temp_c_count = c
temp_r_count = r

direction = ["up", "right", "down", "left"]

real_start_x = r - 1
real_start_y = 0

while True:
    if count == (c*r) :
        break

    stand_direction = direction.pop(0)

    handle_input_direction(real_start_x, real_start_y, temp_r_count, stand_direction)
    if stand_direction == "up" or stand_direction == "down":
        temp_r_count -= 1
    else:
        temp_c_count -= 1

    direction.append(stand_direction)
    count += 1


for i in range(r) :
    for j in range(c) :
        if list[i][j] == target:
            print(list[i][j])
            break;





