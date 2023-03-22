a, b = map(str, input().split())
b_length = len(b)
a_length = len(a)

same_count = 0
biggest_same_start_index = 0
biggest_same_end_index = 0
if a_length == b_length :
    result = 0
    for i in range(a_length) :
        if a[i] != b[i]:
            result += 1

    print(result)
else :
    for i in range(b_length - a_length + 1) :
        temp_same_count = 0
        a_index = 0
        for j in range(i, i + a_length) :
            if b[j] == a[a_index] :
                temp_same_count += 1
            a_index += 1

        if temp_same_count >= same_count:
            same_count = temp_same_count
            biggest_same_start_index = i
            biggest_same_end_index = i + a_length

    result = 0
    a_index = 0
    for i in range(biggest_same_start_index, biggest_same_end_index) :
        if a[a_index] != b[i] :
            result += 1
        a_index += 1

    print(result)



