n = int(input())
lec_times = []

end_times = []
lec_counts = [1]

for _ in range(n):
    lec_num, start, end = map(int, input().split())
    lec_times.append((start, end))

lec_times.sort()

end_times.append(lec_times[0][1])

for i in range(1, n):
    temp_start_time = lec_times[i][0]
    temp_end_time = lec_times[i][1]

    if end_times[0] <= temp_start_time:
        end_lec_count = 0
        for val in end_times:
            if val > temp_start_time:
                break
            end_lec_count += 1

        for j in range(end_lec_count):
            end_times.pop(0)

    end_times.append(temp_end_time)
    lec_counts.append(len(end_times))
    end_times.sort()

print(max(lec_counts))


