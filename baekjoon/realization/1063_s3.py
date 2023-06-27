'''
R : 한 칸 오른쪽으로
L : 한 칸 왼쪽으로
B : 한 칸 아래로
T : 한 칸 위로
RT : 오른쪽 위 대각선으로
LT : 왼쪽 위 대각선으로
RB : 오른쪽 아래 대각선으로
LB : 왼쪽 아래 대각선으로

a - 1
b - 2
c - 3
d - 4
e - 5
f - 6
g - 7
h - 8

A1 A2 5
B
L
LB
RB
LT
'''


def calculate_target_point(king_x_point, king_y_point, input_x, input_y):
    return int(king_x_point) + int(input_x), int(king_y_point) + int(input_y)


def check_out_board(check_point):
    return check_point[0] < 1 or check_point[1] < 1


def check_overlap_stone_point(temp_target_king_point):
    return temp_target_king_point[0] == point_value[stone_point[0]] and temp_target_king_point[1] == int(stone_point[1])

def find_key_by_value_in_point_value(x_point):
    for key, value in point_value.items():
        if value == x_point:
            return key


point_value = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8
}

directions = {
    "R": (1, 0),
    "L": (-1, 0),
    "B": (0, -1),
    "T": (0, 1),
    "RT": (1, 1),
    "LT": (-1, 1),
    "RB": (1, -1),
    "LB": (-1, -1)
}

king_point, stone_point, k = input().split()

for i in range(int(k)):
    input_dir = input()
    move_x_value = directions[input_dir][0]
    move_y_value = directions[input_dir][1]

    temp_target_king_point = calculate_target_point(point_value[king_point[0]], king_point[1], move_x_value, move_y_value)
    if check_out_board(temp_target_king_point):
        king_point = find_key_by_value_in_point_value(point_value[king_point[0]]) + str(king_point[1])
        stone_point = find_key_by_value_in_point_value(point_value[stone_point[0]]) + str(stone_point[1])
        continue

    if check_overlap_stone_point(temp_target_king_point):
        temp_target_stone_point = calculate_target_point(point_value[stone_point[0]], stone_point[1], move_x_value,
                                                         move_y_value)
        if check_out_board(temp_target_stone_point):
            continue
        king_point = find_key_by_value_in_point_value(point_value[temp_target_king_point[0]]) + str(temp_target_king_point[1])
        stone_point = find_key_by_value_in_point_value(point_value[temp_target_stone_point[0]]) + str(temp_target_stone_point[1])
    else:
        king_point = find_key_by_value_in_point_value(point_value[temp_target_king_point[0]]) + str(temp_target_king_point[1])
        stone_point = find_key_by_value_in_point_value(point_value[stone_point[0]]) + str(stone_point[1])

print(king_point)
print(stone_point)
