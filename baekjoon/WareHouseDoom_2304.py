
def calculate_pillar_hei(half_point_leng):
    global result, point
    exist_pillar_point = 0
    exist_pillar_hei = 0

    for i in range(half_point_leng + 1):
        input_pillar_point = point[i][0]
        input_pillar_hei = point[i][1]
        pillar_len_sub = abs(input_pillar_point - exist_pillar_point) - 1

        if i == half_point_leng:
            result += pillar_len_sub * input_pillar_hei

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

    for i in range(half_point_leng + 1):
        input_pillar_point = point[i][0]
        input_pillar_hei = point[i][1]
        pillar_len_sub = abs(input_pillar_point - exist_pillar_point)

        if i == half_point_leng:
            result += pillar_len_sub * input_pillar_hei

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
half_point_leng = len(point) // 2

half_point_leng_rest = len(point) % 2
exist_pillar_point = 0
exist_pillar_hei = 0

result = 0

calculate_pillar_hei(half_point_leng)

point.sort(reverse=True)

calculate_pillar_hei_reverse(half_point_leng)

if half_point_leng_rest == 1:
    result += point[half_point_leng][1]

print(result)