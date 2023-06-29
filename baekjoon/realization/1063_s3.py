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
    return check_point[0] < 1 or check_point[1] < 1 or check_point[0] > 8 or check_point[1] > 8


def check_overlap_stone_point(temp_target_king_point):
    return temp_target_king_point[0] == present_stone_x_point and temp_target_king_point[1] == present_stone_y_point

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

present_king_x_point = point_value[king_point[0]]
present_king_y_point = int(king_point[1])

present_stone_x_point = point_value[stone_point[0]]
present_stone_y_point = int(stone_point[1])

for i in range(int(k)):
    input_dir = input() ## 1. 방향 받음
    move_x_value = directions[input_dir][0]
    move_y_value = directions[input_dir][1] ## 방향의 x,y 증감값 추출

    temp_target_king_point = calculate_target_point(present_king_x_point, present_king_y_point, move_x_value, move_y_value) ## 2. 목표값 계산
    if check_out_board(temp_target_king_point): # 목표값이 보드 밖으로 나가는지 파악
        continue # 다음 인덱스 수행

    if check_overlap_stone_point(temp_target_king_point): # 목표값 == 현재 돌 위치값 인경지 아닌지
        temp_target_stone_point = calculate_target_point(present_stone_x_point, present_stone_y_point, move_x_value,move_y_value) # 돌의 목표값 계산.
        if check_out_board(temp_target_stone_point): # 이동된 돌의 목표값이 보드 밖으로 나가는지 파악
            continue

        present_king_x_point = temp_target_king_point[0]
        present_king_y_point = temp_target_king_point[1]
        present_stone_x_point = temp_target_stone_point[0]
        present_stone_y_point = temp_target_stone_point[1]
    else:
        present_king_x_point = temp_target_king_point[0]
        present_king_y_point = temp_target_king_point[1]

print(find_key_by_value_in_point_value(present_king_x_point) + str(present_king_y_point))
print(find_key_by_value_in_point_value(present_stone_x_point) + str(present_stone_y_point))
