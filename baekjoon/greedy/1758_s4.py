n = int(input())
consumers = []

for _ in range(n):
    tip = int(input())
    consumers.append(tip)

consumers.sort(reverse=True)

result = 0

for i in range(n):
    tip = consumers[i] - i
    if tip < 0:
        break

    result += tip

print(result)