n, m = map(int, input().split())
package = []
one = []

for i in range(m):
    p, o = map(int, input().split())
    package.append(p)
    one.append(o)

p_min = min(package)
o_min = min(one)

res = 0

if (o_min * 6) > p_min:
    if n >= 6:
        res += (n // 6) * p_min
        tmp = n % 6
        if (o_min * tmp) < p_min:
            res += o_min * tmp
        else:
            res += p_min
    else:
        if (o_min * n) < p_min:
            res = o_min * n
        else:
            res = p_min
else:
    res = o_min * n

print(res)


