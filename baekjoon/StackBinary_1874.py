n = int(input())
inputs = list()
stack = [0] * n

for i in range(n):
    inputs.append(int(input()))

result = list()
push_cnt = 1
for i in range(n):
    standard = inputs[i]
    if stack[-1] < standard:
        for j in range(push_cnt, standard + 1):
            result.append("+")
            stack.append(j)
        stack.pop()
        result.append("-")
        push_cnt = inputs[i]
    elif stack[-1] == standard:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)

for i in result:
    print(i)

