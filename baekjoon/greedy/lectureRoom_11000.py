n = int(input())
lecture_times = []

for i in range(n) :
    start, end = input().split(" ")
    lecture_times.append((int(start), int(end)))

lecture_times.sort(key= lambda x: (x[0], x[1]))
print(lecture_times)
is_first = True

end_time_list = []
result = 0

for lecture_time in lecture_times :
    if is_first :
        end_time_list.append(lecture_time[1])
        result += 1
        is_first = False
        continue

    if lecture_time[0] in end_time_list:
        end_time_list.append(lecture_time[1])
        continue
    else:
        end_time_list.append(lecture_time[1])
        result += 1
        continue

print(result)