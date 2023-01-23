n = int(input())
inputs = list()
stack = [0] * n

for i in range(n):
    inputs.append(int(input()))

same_candy_max_count = list()
push_cnt = 1
for i in range(n):
    standard = inputs[i]
    if stack[-1] < standard:
        for j in range(push_cnt, standard + 1):
            same_candy_max_count.append("+")
            stack.append(j)
        stack.pop()
        same_candy_max_count.append("-")
        push_cnt = inputs[i]
    elif stack[-1] == standard:
        stack.pop()
        same_candy_max_count.append("-")
    else:
        print("NO")
        exit(0)

for i in same_candy_max_count:
    print(i)

