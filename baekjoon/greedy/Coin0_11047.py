n , k = input().split(" ")
n = int(n)
k = int(k)

coins = []

for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
temp_k = k
same_candy_max_count = 0
for coin in coins :
    if coin > k :
        continue

    temp_value = temp_k // coin
    temp_k = temp_k - (coin * temp_value)
    same_candy_max_count += temp_value

print(same_candy_max_count)



