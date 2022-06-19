# 필수 테스트 - 승점구하기

def calculate_point(games):
    win_point = 0
    for score in games:
        left_score = int(score[0])
        right_score = int(score[2])

        if left_score > right_score:
            win_point += 3
        elif left_score == right_score:
            win_point += 1

    return win_point

results = ["3:4","1:4","4:1","3:3","2:1","2:2","2:3","3:0","0:0","1:0"]

print(calculate_point(results))
