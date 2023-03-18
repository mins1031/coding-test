n, s = map(int, input().split())

numbers = list(map(int, input().split()))
numbers_size = len(numbers)

result = 0

for i in range(numbers_size) :
    temp_sum_list = [numbers[i]]
    for j in range(i+1, numbers_size) :
        temp_sum_list.append(numbers[j])
        if sum(temp_sum_list) == s:
            result += 1

print(result)

