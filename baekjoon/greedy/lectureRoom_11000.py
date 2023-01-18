import sys
import heapq

n = int(input())
lecture_times = []

for i in range(n) :
    start, end = sys.stdin.readline().split(" ")
    lecture_times.append([int(start), int(end)])

lecture_times.sort()

end_time_list = []
heapq.heappush(end_time_list, lecture_times[0][1])

for i in range(1, n) :
    min_end_time = end_time_list[0]
    if lecture_times[i][0] < min_end_time :
        heapq.heappush(end_time_list, lecture_times[i][1])
    else:
        heapq.heappop(end_time_list)
        heapq.heappush(end_time_list, lecture_times[i][1])

print(len(end_time_list))
# 종료시간이 리스트에서 유지된다는건 그만큼의 강의실 숫자가 유지된다는 의미이다.
