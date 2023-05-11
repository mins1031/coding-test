n, k, m = map(int, input().split())
k = k - 1
list = [i for i in range(1, n + 1)]

result = []
remove_count = 0
current_index = k
minus_turn = False

while len(list) != 0:
    remove_target = list[current_index]
    list.remove(current_index)
    result.append(remove_target)

    remove_count += 1
    if remove_count == 4 and minus_turn is False:
        remove_count = 0
        minus_turn = True
    elif remove_count == 4 and minus_turn is True:
        remove_count = 0
        minus_turn = False

    if minus_turn is False:
        if (current_index + k) >= len(list):
            current_index = (current_index + k) - len(list)
        else:
            current_index += k
    else:
        if (current_index - k) < 0:
            current_index = len(list) - (current_index - k)
        else:
            current_index -= k

for i in result:
    print(i)
