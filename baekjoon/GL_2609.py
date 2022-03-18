n, m = map(int, input().split(' '))

for i in range(min(n,m), 0, -1):
    if n%i==0 and m%i == 0:
        print(i)
        break

k = 1
while True:
    tmp = max(n, m) * k
    if tmp % min(n,m) == 0:
        print(tmp)
        break
    else:
        k += 1
