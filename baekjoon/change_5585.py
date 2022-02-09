payment = 1000
coins = [500, 100, 50, 10, 5, 1]

change = int(input())
temp_change = payment - change
result = 0
for i in coins:
    result += temp_change // i
    temp_change %= i

print(result)
