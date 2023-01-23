test_case = int(input())
same_candy_max_count = list()

for _ in range(test_case):
    key_input = input()
    password = list()
    point = 0
    for i in range(len(key_input)):
        if key_input[i].isalpha() or key_input[i].isdigit():
            if point != i:
                password.insert(point, key_input[i])
                point += 1
                continue
            password.append(key_input[i])
            point += 1
        elif key_input[i] == "<":
            if point == 0:
                continue
            point -= 1
        elif key_input[i] == ">":
            if point == len(key_input) - 1:
                continue
            point += 1
        elif key_input[i] == "-":
            password.pop()
            point -= 1

    same_candy_max_count.append(password)

for i in same_candy_max_count:
    print(''.join(i))


