import sys

# sys.stdin = open("in_out/chapter9/in5.txt", "rt")

first = input()
second = input()
first_dic = dict()
second_dic = dict()
for i in first:
    if i not in first_dic:
        first_dic[i] = 1
    else:
        first_dic[i] +=1

for i in second:
    if i not in second_dic:
        second_dic[i] = 1
    else:
        second_dic[i] +=1

for key, val in first_dic.items():
    if key not in second_dic.keys():
        print("NO")
        break
    else:
        if second_dic[key] != val:
            print("NO")
            break
else:
    print("YES")


