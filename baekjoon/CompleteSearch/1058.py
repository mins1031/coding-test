n = int(input())
maps = []
dic = dict()

for i in range(n):
    temp = list(input())
    maps.append(temp)
    dic[i] = []

for i in range(n):
    for j in range(n):
        if maps[i][j] == "Y":
            dic[i].append(j)
            dic[j].append(i)

for key, value in dic.items():
    key = set(value)

max = 0
for key, value in dic.items():
    temp = []
    temp.extend(value)
    for i in value:
        temp.extend(dic[i])
    temp_set = list(set(temp))
    if key in temp_set:
        temp_set.remove(key)

    temp_max = len(temp_set)
    if temp_max > max:
        max = temp_max

print(max)

