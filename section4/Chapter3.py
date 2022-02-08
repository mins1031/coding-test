import sys

sys.stdin = open("in_out/chapter3/in1.txt", "rt")

n, m = map(int, input().split())
songs = list(map(int, input().split()))

largest = sum(songs)
lt = 1
rt = largest
res=0
while lt <= rt:
    mid = (rt + lt) // 2
    dvd_amount = 0
    temp = 0
    for i in songs:
        if temp > mid:
            dvd_amount += 1
            temp = i
        else:
            temp += i

    if dvd_amount <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid - 1

print(res)