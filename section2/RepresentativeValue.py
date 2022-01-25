import sys

sys.stdin = open("in_out/section2/chapter4/in1.txt", "rt")

# 파이썬에서 반올림을 하고 싶을 때눈 round() 함수를 사용한다!
# 파이썬에서 절댓값을 구하고 싶을 때눈 abs() 함수를 사용한다!

# def sol(n, n_list):
#     avg = 0
#     avg = round(sum(n_list) / n)
#
#     avg_list = tuple()
#     shortness = abs(n_list[0] - avg)
#     for i in range(1, n):
#         if abs(n_list[i] - avg) < shortness:
#             shortness = abs(n_list[i] - avg)
#
#     near_index = 0
#     near_value = 0
#     for index, value in enumerate(n_list):
#         if abs(value - avg) != shortness:
#             continue
#         # 근사치값이 같은경우
#
#         if near_value > value:
#             continue
#         elif near_value == value:
#             if near_index < index:
#                 continue
#
#         near_index = index
#         near_value = value
#
#     return avg, near_index+1

n = int(input())
n_list = list(map(int, input().split()))
# result = sol(n, n_list)
# print("%d %d" %(result[0], result[1]))

avg = round(sum(n_list) / n)
min = 2147000000
for idx, x in enumerate(n_list):
    tmp=abs(x-avg)
    if tmp<min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if score < x:
            score = x
            res = idx+1
print(avg, res)