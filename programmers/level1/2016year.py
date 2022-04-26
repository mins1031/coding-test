def solution(a, b):
    monthOfDay = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    dayName = {1: "SAT", 2: "SUN", 3: "MON", 4: "TUE", 5: "WED", 6: "THU", 0: "FRI"}
    tot_days = -1
    for i in range(1, a):
        tot_days += monthOfDay.get(i)
    tot_days += b

    return dayName.get(tot_days % 7)


a = 5
b = 24
print(solution(a, b))
