payment = 1000
coins = [500, 100, 50, 10, 5, 1]

change = int(input())
temp_change = payment - change
same_candy_max_count = 0
for i in coins:
    same_candy_max_count += temp_change // i
    temp_change %= i

print(same_candy_max_count)
