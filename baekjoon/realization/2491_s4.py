n = int(input())
numbers = list(map(int, input().split()))

num_length_list = []
long_num_length = 1

for i in range(n - 1):
    if numbers[i] < numbers[i+1] :
        long_num_length += 1
        for j in range(i+1, n -1) :
            if numbers[j] > numbers[j+1]:
                break
            long_num_length += 1
        num_length_list.append(long_num_length)
        long_num_length = 1
    elif numbers[i] > numbers[i+1] :
        long_num_length += 1
        for j in range(i + 1, n - 1):
            if numbers[j] < numbers[j + 1]:
                break
            long_num_length += 1
        num_length_list.append(long_num_length)
        long_num_length = 1
    elif numbers[i] == numbers[i+1] :
        long_num_length += 1
        continue

if len(numbers) == 1 :
    print(1)
else:
    print(max(num_length_list))
