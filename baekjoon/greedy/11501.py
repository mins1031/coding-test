test = int(input())

for _ in range(test):
    days = int(input())
    price = list(map(int, input().split()))
    max_value = max(price)
    sells = []
    result = 0

    for i in range(days):
        if price[i] == max_value:
            for j in sells:
                result += abs(price[i] - j)
            sells = []
        else:
            if i + 1 == days:

            sells.append(price[i])

    print(result)

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