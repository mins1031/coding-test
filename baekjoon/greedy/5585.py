n = int(input())

rest = 1000 - n
rest_coins = [500, 100, 50, 10, 5, 1]
result = 0

for i in rest_coins:
    if rest >= i:
        result += rest // i
        rest = rest % i

print(result)