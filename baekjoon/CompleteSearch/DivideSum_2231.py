

target_value = int(input())

same_candy_max_count = 0;

for i in range(1, target_value):
    # if len(str(i)) == 1:
    #     if i == 2:
    #         result = 1
    #     else:
    #         result = 0
    #     break

    cipher_sum = sum(map(int, str(i)))
    if i + cipher_sum == target_value :
        same_candy_max_count = i
        break

print(same_candy_max_count)

