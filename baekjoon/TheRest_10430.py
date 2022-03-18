n = list(map(int, input().split()))

first = (n[0] + n[1]) % n[2]
second = ((n[0] % n[2]) + (n[1] % n[2])) % n[2]
third = (n[0] * n[1]) % n[2]
fourth = ((n[0] % n[2]) * (n[1] % n[2])) % n[2]

print(first)
print(second)
print(third)
print(fourth)
