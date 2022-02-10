n, c = map(int, input().split())
houses = list()
for i in range(n):
    houses.append(int(input()))

houses.sort()

lt = 1
rt = houses[-1]
res = 0
while lt<=rt:
    mid = (rt+lt) // 2

    cnt = 1
    end_point = houses[0]
    for i in range(1, n):
        if (houses[i]-end_point) >= mid:
            end_point = houses[i]
            cnt += 1

    if cnt >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)