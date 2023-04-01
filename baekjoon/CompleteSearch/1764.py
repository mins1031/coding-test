n, m = map(int, input().split())
dud_bo = []

for i in range(n + m):
    dud_bo_word = input()
    dud_bo.append(dud_bo_word)

current_word = ""
repeat_count = 0
result = set()
dud_bo.sort()
for i in dud_bo:
    if i == current_word:
        result.add(i)

    current_word = i

result = list(result)
print(len(result))
for i in result:
    print(i)




