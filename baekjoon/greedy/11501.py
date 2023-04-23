test = int(input())

for _ in range(test):
    days = int(input())
    price = list(map(int, input().split()))
    max = price[-1]
    result = 0

    for i in range(days - 2, -1, -1):
        if price[i] > max:
            max = price[i]
        else:
            result += max - price[i]

    print(result)

# 시간초과
# f
# or _ in range(test):
#     days = int(input())
#     price = list(map(int, input().split()))
#     max_value = max(price)
#     max_index = price.index(max_value)
#     sells = []
#     result = 0
#
#     for i in range(days):
#         if price[i] == max_value:
#             for j in sells:
#                 result += abs(price[i] - j)
#             sells = []
#             if i != days - 1:
#                 max_value = max(price[i+1:])
#         else:
#             sells.append(price[i])
#
#     print(result)

# 3
# 3
# 10 7 6
# 3
# 3 5 9
# 5
# 1 1 3 1 2

# 1
# 5
# 1 2 3 2 4
