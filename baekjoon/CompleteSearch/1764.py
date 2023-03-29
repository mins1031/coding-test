n, m = map(int, input().split())
dud = []
bo = []

for i in range(n):
    dud_word = input()
    dud.append(dud_word)

for i in range(m):
    bo_word = input()
    bo.append(bo_word)

dud.extend(bo)
x = []
result = []

for i in range(len(dud)):
    if i == 0:
        x.append(dud[i])

    if dud[i] in x :
        result.append(dud[i])
    else:
        x.append(dud[i])

result = list(set(result))
print(len(result))
result.sort()
for i in result:
    print(i)

