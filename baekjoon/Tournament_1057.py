import sys

n , jimin, hansu = map(int, sys.stdin.readline().rstrip().split())
res = 1

while True:
    if max(jimin, hansu) % 2 == 0 and abs(jimin - hansu) == 1:
        break

    res += 1

    if jimin % 2 == 0:
        jimin = jimin // 2
    elif jimin % 2 == 1:
        jimin = (jimin // 2) + 1

    if hansu % 2 == 0:
        hansu = hansu // 2
    elif hansu % 2 == 1:
        hansu = (hansu // 2) + 1

print(res)
