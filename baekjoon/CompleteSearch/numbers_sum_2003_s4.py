n, m = map(int, input().split())

numbers = list(map(int, input().split()))

numbers_size = len(numbers)
result = 0

for i in range(numbers_size) :
    temp_sum = numbers[i]
    if temp_sum == m:
        result += 1
        continue

    for j in range(i+1, numbers_size) :
        temp_sum += numbers[j]
        if temp_sum == m:
            result += 1
            break

        if temp_sum > m:
            break

print(result)