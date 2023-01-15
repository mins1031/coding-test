n = int(input())
reservations = []

for i in range(n) :
    start, end = input().split(" ")
    reservations.append((int(start), int(end)))

reservations.sort(key= lambda x: (x[1], x[0]))
print(reservations)
is_first = True

present_end_time = 0
result = 0
for reservation in reservations :
    if is_first :
        present_end_time = reservation[1]
        result += 1
        is_first = False
        continue

    if reservation[0] >= present_end_time:
        present_end_time = reservation[1]
        result += 1
        continue

print(result)

#5
#1 100
#100 300
#99 101
#199 300
#199 201