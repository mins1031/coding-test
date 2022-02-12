n = int(input())
temp = list()
stack = list()

for i in range(n):
    temp.append(int(input()))

plus_cnt = 0
for i in range(n):
    standard = temp[i]
    if plus_cnt < standard:
        for j in range(plus_cnt+1, standard + 1):
            print("+")
            stack.append(j)
        stack.pop()
        print("-")
        plus_cnt = temp[i]
    else:
        if stack[-1] == standard:
            stack.pop()
            continue
        print("NO")
        break
