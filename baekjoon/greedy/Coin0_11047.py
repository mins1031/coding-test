n , k = input().split(" ")
n = int(n)
k = int(k)

coins = []

for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
temp_k = k
result = 0
for coin in coins :
    if coin > k :
        continue

    temp_value = temp_k // coin
    temp_k = temp_k - (coin * temp_value)
    result += temp_value

print(result)



