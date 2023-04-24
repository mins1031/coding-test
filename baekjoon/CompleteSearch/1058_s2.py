n = int(input())
maps = []
friends = dict()

# 입력 값을 받아 maps에 저장하고 i를 사람 식별자로 지정한 딕셔너리(=각 사람의 친구목록) 생성.
for i in range(n):
    temp = list(input())
    maps.append(temp)
    friends[i] = []

# 입력받은 값을 돌며 Y값이 나오면 x,y 좌표(x,y 사람)를 각각의 친구목록에 저장해줌
for i in range(n):
    for j in range(n):
        if maps[i][j] == "Y":
            friends[i].append(j)
            friends[j].append(i)

# 친구목록 중복값 제거
for key, value in friends.items():
    key = set(value)

max = 0
# 사람과 그 사람의 친구목록, 목록에 있는 친구의 친구까지 합친다 =temp
# 합친 목록중 중복제거 및 자기 자신을 제외한게 해당 키값 사람의 친구 수이다.
for key, value in friends.items():
    temp = []
    temp.extend(value)
    for i in value:
        temp.extend(friends[i])
    temp_set = list(set(temp))
    if key in temp_set:
        temp_set.remove(key)

    temp_max = len(temp_set)
    if temp_max > max:
        max = temp_max

print(max)

