test_case = int(input())
for _ in range(test_case):
    friends = int(input())
    dic = dict()
    for i in range(friends):
        name1, name2 = map(str, input().split())

        if name1 not in dic.keys():
            dic[name1] = name2
        else:
            dic[name1] += name2

        # if name2 not in dic.keys():
        #     dic[name2] = 1
        # else:
        #     dic[name2] += 1

        print(dic[name1] + dic[name2])

