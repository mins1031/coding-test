
def calculate_pillar_hei(max_hei):
    global result, point
    exist_pillar_point = 0
    exist_pillar_hei = 0

    for i in range(max_hei + 1):
        input_pillar_point = point[i][0]
        input_pillar_hei = point[i][1]
        pillar_len_sub = abs(input_pillar_point - exist_pillar_point) - 1

        if i == 0:
            result += input_pillar_hei
            exist_pillar_point = input_pillar_point
            exist_pillar_hei = input_pillar_hei
            continue

        if exist_pillar_hei >= input_pillar_hei:
            result += (pillar_len_sub * exist_pillar_hei) + exist_pillar_hei
            exist_pillar_point = input_pillar_point
        elif exist_pillar_hei < input_pillar_hei:
            result += (pillar_len_sub * exist_pillar_hei) + input_pillar_hei
            exist_pillar_point = input_pillar_point
            exist_pillar_hei = input_pillar_hei

def calculate_pillar_hei_reverse(half_point_leng):
    global result, point
    exist_pillar_point = 0
    exist_pillar_hei = 0

    for i in range(len(point) - 1, half_point_leng, -1):
        input_pillar_point = point[i][0]
        input_pillar_hei = point[i][1]
        pillar_len_sub = abs(input_pillar_point - exist_pillar_point) - 1

        if i == half_point_leng:
            result += pillar_len_sub * exist_pillar_hei
            break

        if i == 0:
            result += input_pillar_hei
            exist_pillar_point = input_pillar_point
            exist_pillar_hei = input_pillar_hei
            continue

        if exist_pillar_hei >= input_pillar_hei:
            result += (pillar_len_sub * exist_pillar_hei) + exist_pillar_hei
            exist_pillar_point = input_pillar_point
        elif exist_pillar_hei < input_pillar_hei:
            result += (pillar_len_sub * exist_pillar_hei) + input_pillar_hei
            exist_pillar_point = input_pillar_point
            exist_pillar_hei = input_pillar_hei

n = int(input())

point = []

for i in range(n):
    x, y = map(int, input().split())
    point.append((x, y))

point.sort()
point_leng = len(point)
max_hei_idx = point.index(max(point, key=lambda x:x[1]))

result = 0


if max_hei_idx != 0:
    calculate_pillar_hei(max_hei_idx)

if len(point) - 1 != max_hei_idx :
    calculate_pillar_hei_reverse(max_hei_idx)

print(result)
# 8
# 1 10
# 2 50
# 3 40
# 4 30
# 5 40
# 6 30
# 7 50
# 8 100
# 410