n = int(input())

up = True
down = False
front_val = 1
back_val = 1
count = 1
while True:
    if n == 1 or count == n :
        break

    if up:
        if front_val == 1:
            up = False
            down = True
            back_val += 1
        else:
            front_val -= 1
            back_val += 1

    elif down:
        if back_val == 1:
            up = True
            down = False
            front_val += 1
        else:
            front_val += 1
            back_val -= 1

    count += 1

print(str(front_val) + "/" + str(back_val))