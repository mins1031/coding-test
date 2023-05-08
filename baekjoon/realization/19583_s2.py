from datetime import datetime
import sys

start_time, end_time, end_streaming_time = map(str, input().split())

real_start_time = datetime.strptime(start_time, "%H:%M")
real_end_time = datetime.strptime(end_time, "%H:%M")
real_end_streaming_time = datetime.strptime(end_streaming_time, "%H:%M")

start_attends = []
end_attends = []

for line in sys.stdin:
    time, name = line.rstrip().split()
    temp_time = datetime.strptime(time, "%H:%M")
    if temp_time <= real_start_time:
        start_attends.append(name)
    elif real_end_time <= temp_time <= real_end_streaming_time:
        end_attends.append(name)

# while True:
#     try:
#         time, name = input().split()
#         temp_time = datetime.strptime(time, "%H:%M")
#         if temp_time <= real_start_time:
#             start_attends.append(name)
#         elif real_end_time <= temp_time <= real_end_streaming_time:
#             end_attends.append(name)
#
#     except:
#         break

result = set(start_attends.extend(end_attends))
print(len(result))




