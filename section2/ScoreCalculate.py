import sys

sys.stdin = open("in_out/section2/chapter10/in5.txt", "rt")


def sol(n, score_list):
    score = 0
    count = 1
    for i in score_list:
        if i == 1:
            score += count
            count += 1
        else:
            count = 1

    return score


n = int(input())
score_list = map(int, input().split())

print(sol(n, score_list))
